/**
 * GeometorInteractive / EuclidInteractive
 * Shared interactive SVG inlining and graphic-scoped Geometor highlighting engine
 * for both folio_review and Sphinx foundation book pages.
 */
(function (window, document) {
  'use strict';

  const EuclidInteractive = {
    activeHighlights: new Set(),
    svgRefMap: new Map(), // key ("<folio>.<gid>:<canonical_geometor_id>") -> Set of SVG elements
    stepState: null,

    getDefaultFolioId() {
      if (typeof window.FOLIO_ID === 'string' && window.FOLIO_ID) {
        return window.FOLIO_ID;
      }
      const milestone = document.querySelector('[data-folio]');
      if (milestone) {
        return milestone.getAttribute('data-folio') || '0000';
      }
      return '0000';
    },

    getRootContainer() {
      return (
        document.getElementById('mdView-rendered') ||
        document.querySelector('.folio-book-page') ||
        document.querySelector('article .content') ||
        document.querySelector('main') ||
        document.body
      );
    },

    renderMath() {
      const container = this.getRootContainer();
      if (!container || typeof window.renderMathInElement !== 'function') return;
      try {
        window.renderMathInElement(container, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true },
          ],
          throwOnError: false,
        });
      } catch (err) {
        console.warn('KaTeX auto-render error:', err);
      }
    },

    init() {
      this.renderMath();
      this.inlineFiguresInTranscription();
      this.buildSvgIndex();
      this.bindTextElements();
      this.bindAssertionElements();
      this.bindSvgElements();
      this.initStepPlayer();
    },

    // Normalize graphic ID to "<folio>.<gid>" (e.g. "g1" -> "0255.g1")
    normalizeGraphicId(gid) {
      const raw = (gid || '').trim();
      const folioId = this.getDefaultFolioId();
      if (!raw) return `${folioId}.g1`;
      if (raw.includes('.')) return raw;
      return `${folioId}.${raw}`;
    },

    // Format a number cleanly for SVG path data
    fmtNum(v) {
      if (Math.abs(v - Math.round(v)) < 1e-6) return String(Math.round(v));
      return Number(v.toFixed(2)).toString();
    },

    // Convert a closed wedge path "M vx vy L x1 y1 A rx ry rot laf sf x2 y2 Z"
    // into an open 3-vertex arc path "M x1 y1 A r r 0 0 sf mx my A r r 0 0 sf x2 y2"
    // whose interior vertex (mx, my) is at the exact angular midpoint of the arc.
    wedgeToMidArcPath(d) {
      const m = (d || '')
        .trim()
        .match(
          /^M\s*([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)\s*L\s*([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)\s*A\s*([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)\s+([+-]?\d+(?:\.\d+)?)\s+([01])\s*[,\s]\s*([01])\s+([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)\s*[Zz]$/
        );
      if (!m) return null;
      const vx = parseFloat(m[1]);
      const vy = parseFloat(m[2]);
      const x1 = parseFloat(m[3]);
      const y1 = parseFloat(m[4]);
      const rx = parseFloat(m[5]);
      const sf = parseInt(m[9], 10);
      const x2 = parseFloat(m[10]);
      const y2 = parseFloat(m[11]);

      const theta1 = Math.atan2(y1 - vy, x1 - vx);
      const theta2 = Math.atan2(y2 - vy, x2 - vx);
      const twoPi = 2 * Math.PI;
      let dtheta;
      if (sf === 1) {
        dtheta = ((theta2 - theta1) % twoPi + twoPi) % twoPi;
      } else {
        dtheta = -(((theta1 - theta2) % twoPi + twoPi) % twoPi);
      }
      const thetaMid = theta1 + dtheta / 2;
      const r =
        rx > 0
          ? rx
          : (Math.hypot(x1 - vx, y1 - vy) + Math.hypot(x2 - vx, y2 - vy)) / 2;
      const mx = vx + r * Math.cos(thetaMid);
      const my = vy + r * Math.sin(thetaMid);

      const rStr = this.fmtNum(r);
      return `M ${this.fmtNum(x1)} ${this.fmtNum(y1)} A ${rStr} ${rStr} 0 0 ${sf} ${this.fmtNum(mx)} ${this.fmtNum(my)} A ${rStr} ${rStr} 0 0 ${sf} ${this.fmtNum(x2)} ${this.fmtNum(y2)}`;
    },

    // Ensure <defs> tick markers (#geom-tick-1/2/3), 3-vertex segment paths, and
    // 3-vertex angle arc paths (.geom-ang-arc) exist in an SVG element.
    ensureSvgTickInfrastructure(svg) {
      const svgNs = 'http://www.w3.org/2000/svg';

      // 1. Ensure <defs> with #geom-tick-1, #geom-tick-2, #geom-tick-3
      let defs = svg.querySelector('defs');
      if (!defs) {
        defs = document.createElementNS(svgNs, 'defs');
        const styleEl = svg.querySelector('style');
        if (styleEl && styleEl.nextSibling) {
          svg.insertBefore(defs, styleEl.nextSibling);
        } else {
          svg.insertBefore(defs, svg.firstChild);
        }
      }
      if (!defs.querySelector('#geom-tick-1')) {
        const markerSpecs = [
          { id: 'geom-tick-1', xs: [0] },
          { id: 'geom-tick-2', xs: [-1.8, 1.8] },
          { id: 'geom-tick-3', xs: [-3.2, 0, 3.2] },
        ];
        markerSpecs.forEach((spec) => {
          const marker = document.createElementNS(svgNs, 'marker');
          marker.setAttribute('id', spec.id);
          marker.setAttribute('viewBox', '-6 -6 12 12');
          marker.setAttribute('refX', '0');
          marker.setAttribute('refY', '0');
          marker.setAttribute('markerWidth', '12');
          marker.setAttribute('markerHeight', '12');
          marker.setAttribute('markerUnits', 'userSpaceOnUse');
          marker.setAttribute('orient', 'auto');
          spec.xs.forEach((xVal) => {
            const line = document.createElementNS(svgNs, 'line');
            line.setAttribute('x1', String(xVal));
            line.setAttribute('y1', '-4.5');
            line.setAttribute('x2', String(xVal));
            line.setAttribute('y2', '4.5');
            line.setAttribute('class', 'geom-tick-mark');
            marker.appendChild(line);
          });
          defs.appendChild(marker);
        });
      }

      // 2. Convert any <line> elements outside <defs> into 3-vertex <path> elements
      // so marker-mid renders at their exact midpoint.
      const lines = Array.from(svg.querySelectorAll('line'));
      lines.forEach((lineEl) => {
        if (lineEl.closest('defs')) return;
        const x1 = parseFloat(lineEl.getAttribute('x1') || '0');
        const y1 = parseFloat(lineEl.getAttribute('y1') || '0');
        const x2 = parseFloat(lineEl.getAttribute('x2') || '0');
        const y2 = parseFloat(lineEl.getAttribute('y2') || '0');
        const mx = (x1 + x2) / 2;
        const my = (y1 + y2) / 2;

        const pathEl = document.createElementNS(svgNs, 'path');
        Array.from(lineEl.attributes).forEach((attr) => {
          if (!['x1', 'y1', 'x2', 'y2'].includes(attr.name)) {
            pathEl.setAttribute(attr.name, attr.value);
          }
        });
        pathEl.setAttribute(
          'd',
          `M ${this.fmtNum(x1)} ${this.fmtNum(y1)} L ${this.fmtNum(mx)} ${this.fmtNum(my)} L ${this.fmtNum(x2)} ${this.fmtNum(y2)}`
        );
        lineEl.replaceWith(pathEl);
      });

      // 3. Ensure 2-vertex straight <path d="M x1 y1 L x2 y2"> elements have a midpoint vertex
      const straightPaths = Array.from(svg.querySelectorAll('path'));
      straightPaths.forEach((pEl) => {
        if (pEl.closest('defs')) return;
        const d = (pEl.getAttribute('d') || '').trim();
        const m = d.match(
          /^M\s*([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)\s*L\s*([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)$/
        );
        if (m) {
          const x1 = parseFloat(m[1]);
          const y1 = parseFloat(m[2]);
          const x2 = parseFloat(m[3]);
          const y2 = parseFloat(m[4]);
          const mx = (x1 + x2) / 2;
          const my = (y1 + y2) / 2;
          pEl.setAttribute(
            'd',
            `M ${this.fmtNum(x1)} ${this.fmtNum(y1)} L ${this.fmtNum(mx)} ${this.fmtNum(my)} L ${this.fmtNum(x2)} ${this.fmtNum(y2)}`
          );
        }
      });

      // 4. Ensure each angle wedge (.wedge.angle) has a companion .geom-ang-arc path
      let highlightsGroup = svg.querySelector('#highlights');
      if (!highlightsGroup) {
        highlightsGroup = svg.querySelector('#graphics') || svg;
      }
      const existingArcRefs = new Set(
        Array.from(svg.querySelectorAll('path.geom-ang-arc')).map((el) =>
          (el.getAttribute('data-ref') || '').trim()
        )
      );
      const wedges = Array.from(svg.querySelectorAll('path.wedge, path.angle'));
      wedges.forEach((wEl) => {
        const ref = (wEl.getAttribute('data-ref') || '').trim();
        if (!ref || existingArcRefs.has(ref)) return;
        const arcD = this.wedgeToMidArcPath(wEl.getAttribute('d') || '');
        if (!arcD) return;
        const arcEl = document.createElementNS(svgNs, 'path');
        const wId = wEl.getAttribute('id') || '';
        if (wId) {
          arcEl.setAttribute('id', wId.replace(/^(el|hl)-ang-/, 'hl-arc-'));
        }
        arcEl.setAttribute('data-ref', ref);
        const aliases = wEl.getAttribute('data-aliases');
        if (aliases) arcEl.setAttribute('data-aliases', aliases);
        arcEl.setAttribute('d', arcD);
        arcEl.setAttribute('class', 'geom-ang-arc geom-overlay');
        highlightsGroup.appendChild(arcEl);
        existingArcRefs.add(ref);
      });
    },

    // Parse a Geometor typed expression (with optional "<gid>:" prefix) into:
    // { graphicId, type, points, keys: [scopedKey, ...], pointKeys: [scopedPtKey, ...] }
    parseGeometorRef(rawStr, defaultGraphicId) {
      let str = (rawStr || '').trim();
      if (!str) return null;

      let graphicId = this.normalizeGraphicId(defaultGraphicId);
      const colonIdx = str.indexOf(':');
      if (colonIdx !== -1) {
        const prefix = str.slice(0, colonIdx).trim();
        str = str.slice(colonIdx + 1).trim();
        if (prefix) graphicId = this.normalizeGraphicId(prefix);
      }

      if (!str) return null;

      const extractPts = (inner) => {
        const tokens = inner.trim().split(/[\s,]+/).filter(Boolean);
        if (tokens.length === 1 && /^[A-Z]{2,}$/.test(tokens[0])) {
          return tokens[0].split('');
        }
        return tokens;
      };

      const makeScoped = (expr) => `${graphicId}:${expr}`;
      const keys = new Set();
      let points = [];
      let type = 'unknown';

      // 1. Wedge / Angle with circle prefix: ( A B )< B A C >
      const fullWedgeMatch = str.match(/^\(([^)]+)\)\s*<([^>]+)>$/);
      // 2. Wedge / Angle / Arc shorthand: < B A C )
      const shortWedgeMatch = !fullWedgeMatch && str.match(/^<([^)]+)\)$/);
      // 3. Line: [ A B ]
      const lineMatch = str.match(/^\[([^\]]+)\]$/);
      // 4. Segment / Section: / A B / or } A C B {
      const segMatch = str.match(/^\/([^/]+)\/$/) || str.match(/^\}([^{]+)\{$/);
      // 5. Circle: ( A B ) or ( B C D )
      const circleMatch = !fullWedgeMatch && str.match(/^\(([^)]+)\)$/);
      // 6. Polygon: < A B C >
      const polyMatch = !fullWedgeMatch && !shortWedgeMatch && str.match(/^<([^>]+)>$/);

      if (fullWedgeMatch) {
        type = 'wedge';
        const cPts = extractPts(fullWedgeMatch[1]);
        const aPts = extractPts(fullWedgeMatch[2]);
        points = Array.from(new Set([...cPts, ...aPts]));
        const cPart = `( ${cPts.join(' ')} )`;
        keys.add(makeScoped(`${cPart}< ${aPts.join(' ')} >`));
        keys.add(makeScoped(`< ${aPts.join(' ')} )`));
        if (aPts.length === 3) {
          const revA = [aPts[2], aPts[1], aPts[0]];
          keys.add(makeScoped(`${cPart}< ${revA.join(' ')} >`));
          keys.add(makeScoped(`< ${revA.join(' ')} )`));
        }
      } else if (shortWedgeMatch) {
        type = 'wedge';
        points = extractPts(shortWedgeMatch[1]);
        keys.add(makeScoped(`< ${points.join(' ')} )`));
        if (points.length === 3) {
          const rev = [points[2], points[1], points[0]];
          keys.add(makeScoped(`< ${rev.join(' ')} )`));
        } else if (points.length === 2) {
          keys.add(makeScoped(`< ${[points[1], points[0]].join(' ')} )`));
        }
      } else if (lineMatch) {
        type = 'line';
        points = extractPts(lineMatch[1]);
        keys.add(makeScoped(`[ ${points.join(' ')} ]`));
        keys.add(makeScoped(`[ ${[...points].reverse().join(' ')} ]`));
      } else if (segMatch) {
        points = extractPts(segMatch[1]);
        type = points.length >= 3 ? 'section' : 'segment';
        keys.add(makeScoped(`/ ${points.join(' ')} /`));
        keys.add(makeScoped(`/ ${[...points].reverse().join(' ')} /`));
      } else if (circleMatch) {
        type = 'circle';
        points = extractPts(circleMatch[1]);
        if (points.length === 2) {
          keys.add(makeScoped(`( ${points.join(' ')} )`));
        } else if (points.length === 3) {
          const [a, b, c] = points;
          [
            [a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]
          ].forEach((p) => keys.add(makeScoped(`( ${p.join(' ')} )`)));
        } else {
          keys.add(makeScoped(`( ${points.join(' ')} )`));
          keys.add(makeScoped(`( ${[...points].reverse().join(' ')} )`));
        }
      } else if (polyMatch) {
        type = 'polygon';
        points = extractPts(polyMatch[1]);
        if (points.length === 3) {
          const [a, b, c] = points;
          [
            [a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]
          ].forEach((p) => keys.add(makeScoped(`< ${p.join(' ')} >`)));
        } else if (points.length > 3) {
          const n = points.length;
          for (let i = 0; i < n; i++) {
            const rot = [...points.slice(i), ...points.slice(0, i)];
            keys.add(makeScoped(`< ${rot.join(' ')} >`));
            const rev = [...rot].reverse();
            keys.add(makeScoped(`< ${rev.join(' ')} >`));
          }
        } else {
          keys.add(makeScoped(`< ${points.join(' ')} >`));
          keys.add(makeScoped(`< ${[...points].reverse().join(' ')} >`));
        }
      } else {
        const clean = str.replace(/[^A-Za-z0-9]/g, '').trim();
        if (!clean) return null;
        if (clean.length === 1 || /^[A-Z]\d+$/.test(clean)) {
          type = 'point';
          points = [clean];
          keys.add(makeScoped(clean));
        } else if (clean.length === 2) {
          type = 'legacy2';
          points = [clean[0], clean[1]];
          keys.add(makeScoped(clean));
          keys.add(makeScoped(clean[1] + clean[0]));
          keys.add(makeScoped(`/ ${clean[0]} ${clean[1]} /`));
          keys.add(makeScoped(`/ ${clean[1]} ${clean[0]} /`));
        } else if (clean.length === 3) {
          type = 'legacy3';
          points = clean.split('');
          const [a, b, c] = points;
          [a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a].forEach((p) =>
            keys.add(makeScoped(p))
          );
        } else {
          type = 'legacyN';
          points = clean.split('');
          keys.add(makeScoped(clean));
        }
      }

      const pointKeys = points.map((pt) => makeScoped(pt));
      return {
        graphicId,
        type,
        points,
        keys: Array.from(keys),
        pointKeys,
      };
    },

    // Inlines Vector SVGs in transcription / book page container
    inlineFiguresInTranscription() {
      const container = this.getRootContainer();
      const folioGraphics = window.FOLIO_GRAPHICS;
      if (!container || !Array.isArray(folioGraphics) || folioGraphics.length === 0) return;

      const imgs = Array.from(container.querySelectorAll('img:not(.woodcut-img)'));

      folioGraphics.forEach((g) => {
        if (!g.svg_exists || !g.svg_content) return;

        let targetImg = imgs.find((img) => {
          const src = img.getAttribute('src') || '';
          return src.includes(g.file) || (g.svg_file && src.includes(g.svg_file)) || src.includes(g.id);
        });

        if (!targetImg && imgs.length === 1 && folioGraphics.length === 1) {
          targetImg = imgs[0];
        }

        if (targetImg) {
          const fullGid = this.normalizeGraphicId(g.id);
          const parentBlock = targetImg.closest('figure.photon-picture, figure, p');
          const figureDiv = document.createElement('div');
          figureDiv.className = 'euclid-figure-container';
          figureDiv.setAttribute('data-graphic-id', g.id);
          figureDiv.setAttribute('data-full-graphic-id', fullGid);
          figureDiv.innerHTML = `
            <div class="figure-svg-wrapper" id="fig-view-svg-${g.id}">
              ${g.svg_content}
            </div>
            ${g.caption ? `<div class="figure-caption">${g.caption}</div>` : ''}
          `;

          const svgEl = figureDiv.querySelector('svg');
          if (svgEl) {
            svgEl.classList.add('euclid-graphic');
            svgEl.setAttribute('data-graphic-id', fullGid);
            svgEl.setAttribute('data-short-gid', g.id);
          }

          if (parentBlock && parentBlock.querySelectorAll('img').length === 1) {
            parentBlock.replaceWith(figureDiv);
          } else {
            targetImg.replaceWith(figureDiv);
          }
        }
      });
    },

    // Indexes all SVG elements by their graphic-scoped Geometor ID and aliases
    buildSvgIndex() {
      this.svgRefMap.clear();
      const svgs = document.querySelectorAll('svg.euclid-graphic, figure.photon-svg svg');

      svgs.forEach((svg) => {
        svg.classList.add('euclid-graphic');
        const fullGid = this.normalizeGraphicId(
          svg.getAttribute('data-graphic-id') ||
            svg.closest('.euclid-figure-container')?.getAttribute('data-full-graphic-id') ||
            'g1'
        );
        svg.setAttribute('data-graphic-id', fullGid);

        this.ensureSvgTickInfrastructure(svg);

        const candidates = svg.querySelectorAll('[data-ref], [id]');
        candidates.forEach((el) => {
          if (el.tagName.toLowerCase() === 'g' && !el.hasAttribute('data-ref')) return;
          if (el.tagName.toLowerCase() === 'defs' || el.closest('defs')) return;

          const rawRef = (el.getAttribute('data-ref') || el.getAttribute('id') || '').trim();
          if (!rawRef) return;
          if (
            [
              'elements',
              'graphics',
              'highlights',
              'points',
              'labels',
              'construction',
              'geometry',
            ].includes(rawRef)
          ) {
            return;
          }

          const refsToIndex = [rawRef];
          const aliases = (el.getAttribute('data-aliases') || '').trim();
          if (aliases) {
            aliases
              .split(/[|;]/)
              .map((s) => s.trim())
              .filter(Boolean)
              .forEach((a) => refsToIndex.push(a));
          }

          refsToIndex.forEach((r) => {
            const parsed = this.parseGeometorRef(r, fullGid);
            if (parsed) {
              parsed.keys.forEach((k) => this.registerRef(k, el));
            }
          });
        });
      });
    },

    registerRef(key, element) {
      if (!this.svgRefMap.has(key)) {
        this.svgRefMap.set(key, new Set());
      }
      this.svgRefMap.get(key).add(element);
    },

    // Find matching SVG elements for a graphic-scoped Geometor reference
    getSvgElementsForRef(rawRef, defaultGraphicId) {
      const parsed = this.parseGeometorRef(rawRef, defaultGraphicId);
      if (!parsed) return { primary: [], secondary: [], parsed: null };

      const rawMatches = [];
      parsed.keys.forEach((k) => {
        if (this.svgRefMap.has(k)) {
          this.svgRefMap.get(k).forEach((el) => rawMatches.push(el));
        }
      });

      const hasVisiblePrimary = rawMatches.some(
        (el) => !el.closest('#highlights') && !el.classList.contains('geom-overlay')
      );
      const matches = new Set();
      rawMatches.forEach((el) => {
        if (
          hasVisiblePrimary &&
          (el.closest('#highlights') || el.classList.contains('geom-overlay'))
        ) {
          const tag = el.tagName.toLowerCase();
          const isRegionOrWedge =
            tag === 'polygon' ||
            el.classList.contains('wedge') ||
            el.classList.contains('angle') ||
            el.classList.contains('geom-ang-arc') ||
            el.classList.contains('geom-polygon');
          if (!isRegionOrWedge) return;
        }
        matches.add(el);
      });

      // Secondary highlight for constituent points/labels within the same graphic
      const secondary = new Set();
      if (parsed.type !== 'point' && parsed.pointKeys.length > 0) {
        parsed.pointKeys.forEach((pk) => {
          if (this.svgRefMap.has(pk)) {
            this.svgRefMap.get(pk).forEach((el) => {
              if (!matches.has(el) && !el.closest('#highlights')) secondary.add(el);
            });
          }
        });
      }

      return {
        primary: Array.from(matches),
        secondary: Array.from(secondary),
        parsed,
      };
    },

    // Infer target graphic ID and Geometor type for untagged KaTeX math from surrounding context
    inferContextualRef(kel, token) {
      const folioId = this.getDefaultFolioId();
      const explicitScope = kel.closest('[data-graphic]')?.getAttribute('data-graphic');
      const targetGid = explicitScope ? this.normalizeGraphicId(explicitScope) : `${folioId}.g1`;

      let prevText = '';
      let node = kel.previousSibling;
      while (node && prevText.length < 60) {
        prevText = (node.textContent || '') + ' ' + prevText;
        node = node.previousSibling;
      }
      prevText = prevText.toLowerCase();

      const pts = token.split('').join(' ');
      const candidates = [];

      if (token.length === 1) {
        candidates.push(`${targetGid}:${token}`);
      } else if (token.length === 2) {
        if (/\b(produced)\b/.test(prevText)) {
          candidates.push(`${targetGid}:[ ${pts} ]`);
        }
        candidates.push(`${targetGid}:/ ${pts} /`);
        candidates.push(`${targetGid}:${token}`);
      } else if (token.length === 3) {
        if (/\b(angle|angles)\b/.test(prevText)) {
          candidates.push(`${targetGid}:< ${pts} )`);
        } else if (/\b(circle|circles|semicircle)\b/.test(prevText)) {
          candidates.push(`${targetGid}:( ${pts} )`);
        } else if (/\b(circumference|arc)\b/.test(prevText)) {
          candidates.push(`${targetGid}:< ${pts} )`);
          candidates.push(`${targetGid}:( ${pts} )`);
        } else if (/\b(triangle|triangles)\b/.test(prevText)) {
          candidates.push(`${targetGid}:< ${pts} >`);
        }
        candidates.push(`${targetGid}:< ${pts} >`);
        candidates.push(`${targetGid}:( ${pts} )`);
        candidates.push(`${targetGid}:< ${pts} )`);
        candidates.push(`${targetGid}:/ ${pts} /`);
        candidates.push(`${targetGid}:${token}`);
      } else if (token.length >= 4) {
        candidates.push(`${targetGid}:< ${pts} >`);
        candidates.push(`${targetGid}:( ${pts} )`);
        candidates.push(`${targetGid}:${token}`);
      }

      for (const cand of candidates) {
        const { primary } = this.getSvgElementsForRef(cand, targetGid);
        if (primary.length > 0) return cand;
      }
      return null;
    },

    // Binds explicit <span data-ref="..."> elements and contextual KaTeX fallback
    bindTextElements() {
      const container = this.getRootContainer();
      if (!container) return;

      const folioId = this.getDefaultFolioId();

      // 1. Bind explicit <span data-ref="<folio>.<gid>:<geometor_id>"> wrappers
      const explicitSpans = container.querySelectorAll('[data-ref]');
      explicitSpans.forEach((span) => {
        if (span.closest('svg') || span.closest('.euclid-figure-container')) return;

        const rawRefAttr = (span.getAttribute('data-ref') || '').trim();
        if (!rawRefAttr) return;

        const defaultGid =
          span.closest('[data-graphic]')?.getAttribute('data-graphic') || `${folioId}.g1`;
        const refList = rawRefAttr
          .split(';')
          .map((s) => s.trim())
          .filter(Boolean);

        const allCanonicalKeys = [];
        refList.forEach((r) => {
          const parsed = this.parseGeometorRef(r, defaultGid);
          if (parsed) {
            parsed.keys.forEach((k) => allCanonicalKeys.push(k));
          }
        });

        span.classList.add('geom-interactive-ref');
        span.setAttribute('data-geom-keys', allCanonicalKeys.join('||'));
        if (!span.hasAttribute('title')) {
          const shortIds = refList
            .map((r) => (r.includes(':') ? r.split(':').slice(1).join(':').trim() : r))
            .filter(Boolean);
          if (shortIds.length > 0) {
            span.setAttribute('title', shortIds.join('; '));
          }
        }

        span.addEventListener('mouseenter', () => {
          this.highlightFromText(refList, span, defaultGid);
        });

        span.addEventListener('mouseleave', (e) => {
          this.clearHighlights();
          const parentBlock = span.closest('.geom-assert-block');
          if (
            parentBlock &&
            parentBlock._assertGroups &&
            e.relatedTarget &&
            parentBlock.contains(e.relatedTarget) &&
            !e.relatedTarget.closest?.('.geom-interactive-ref, a')
          ) {
            this.highlightAssertion(
              parentBlock._assertGroups,
              parentBlock,
              parentBlock._assertDefaultGid
            );
          } else {
            this.restoreStepHighlight();
          }
        });
      });

      // 2. Contextual fallback for untagged KaTeX math elements
      const katexEls = container.querySelectorAll('.katex');
      katexEls.forEach((kel) => {
        if (kel.closest('[data-ref]') || kel.closest('.euclid-figure-container')) return;

        const annot = kel.querySelector('annotation');
        const rawTex = annot ? annot.textContent.trim() : kel.innerText.trim();
        const tokens = rawTex
          .split(/[,;\s]+/)
          .map((t) => t.replace(/[^A-Za-z0-9]/g, ''))
          .filter(Boolean);

        const resolvedRefs = tokens.map((t) => this.inferContextualRef(kel, t)).filter(Boolean);
        if (resolvedRefs.length > 0) {
          const allCanonicalKeys = [];
          resolvedRefs.forEach((r) => {
            const parsed = this.parseGeometorRef(r, `${folioId}.g1`);
            if (parsed) parsed.keys.forEach((k) => allCanonicalKeys.push(k));
          });

          kel.classList.add('geom-interactive-ref');
          kel.setAttribute('data-geom-keys', allCanonicalKeys.join('||'));
          if (!kel.hasAttribute('title')) {
            const shortIds = resolvedRefs
              .map((r) => (r.includes(':') ? r.split(':').slice(1).join(':').trim() : r))
              .filter(Boolean);
            if (shortIds.length > 0) {
              kel.setAttribute('title', shortIds.join('; '));
            }
          }

          kel.addEventListener('mouseenter', () => {
            this.highlightFromText(resolvedRefs, kel, `${folioId}.g1`);
          });

          kel.addEventListener('mouseleave', () => {
            this.clearHighlights();
            this.restoreStepHighlight();
          });
        }
      });
    },

    // Classify a Geometor ref as 'seg', 'wedge', 'poly', 'circle', or 'point'
    getRefGeometryKind(ref, defaultGid) {
      const { primary, parsed } = this.getSvgElementsForRef(ref, defaultGid);
      if (!parsed) return 'other';
      if (['segment', 'section', 'line', 'legacy2'].includes(parsed.type)) return 'seg';
      if (parsed.type === 'wedge') return 'wedge';
      if (['polygon', 'legacy3'].includes(parsed.type)) return 'poly';
      if (parsed.type === 'circle') return 'circle';
      if (
        primary.some(
          (el) =>
            el.classList.contains('geom-line') || el.getAttribute('data-type') === 'segment'
        )
      ) {
        return 'seg';
      }
      return parsed.type;
    },

    // Parse explicit equality/coincidence groups from data-assert-equal="ref1 = ref2; ref3 ≡ ref4"
    parseEqualitySpec(specStr) {
      const explicitAttr = (specStr || '').trim();
      if (!explicitAttr || explicitAttr.toLowerCase() === 'none') return [];
      return explicitAttr
        .split(';')
        .map((grp) =>
          grp
            .split(/[=,≡]/)
            .map((s) => s.trim())
            .filter(Boolean)
        )
        .filter((grp) => grp.length >= 2);
    },

    // Bind green assertion equality highlighting on inline :eq: / :coincide: spans (.geom-eq-ref)
    bindAssertionElements() {
      const container = this.getRootContainer();
      if (!container) return;

      const folioId = this.getDefaultFolioId();

      // 1. Bind inline .geom-eq-ref[data-assert-equal] spans wrapping "equal" or "coincide"
      const eqRefs = container.querySelectorAll('.geom-eq-ref[data-assert-equal]');
      eqRefs.forEach((eqSpan) => {
        const defaultGid =
          eqSpan.closest('[data-graphic]')?.getAttribute('data-graphic') || `${folioId}.g1`;
        const groups = this.parseEqualitySpec(eqSpan.getAttribute('data-assert-equal'));
        if (!groups || groups.length === 0) return;

        eqSpan.addEventListener('mouseenter', () => {
          this.highlightAssertion(groups, eqSpan, defaultGid);
        });

        eqSpan.addEventListener('mouseleave', () => {
          this.clearHighlights();
          this.restoreStepHighlight();
        });
      });

      // 2. Support legacy hidden .geom-eq-marker or explicit block-level [data-assert-equal] if present
      const eqMarkers = container.querySelectorAll('.geom-eq-marker[data-assert-equal]');
      eqMarkers.forEach((marker) => {
        const spec = (marker.getAttribute('data-assert-equal') || '').trim();
        const host = marker.closest('.assertion, .sub-clause, .geom-step, p, li');
        if (host && spec) {
          const existing = (host.getAttribute('data-assert-equal') || '').trim();
          host.setAttribute('data-assert-equal', existing ? `${existing}; ${spec}` : spec);
          if (marker.hasAttribute('data-assert-coincide')) {
            host.setAttribute('data-assert-coincide', spec);
          }
        }
      });

      const explicitBlocks = container.querySelectorAll(
        '[data-assert-equal]:not(.geom-eq-ref):not(.geom-eq-marker)'
      );
      explicitBlocks.forEach((blockEl) => {
        const defaultGid =
          blockEl.closest('[data-graphic]')?.getAttribute('data-graphic') || `${folioId}.g1`;
        const groups = this.parseEqualitySpec(blockEl.getAttribute('data-assert-equal'));
        if (!groups || groups.length === 0) return;

        blockEl.classList.add('geom-assert-block');
        blockEl._assertGroups = groups;
        blockEl._assertDefaultGid = defaultGid;

        blockEl.addEventListener('mouseover', (e) => {
          if (e.target.closest('.geom-interactive-ref, .geom-eq-ref, a')) return;
          if (e.target.closest('.geom-assert-block') !== blockEl) return;
          this.highlightAssertion(groups, blockEl, defaultGid);
        });

        blockEl.addEventListener('mouseleave', () => {
          this.clearHighlights();
          this.restoreStepHighlight();
        });
      });
    },

    // Spawn a clean solid coincidence ring around a point circle element
    addCoincideRing(ptCircle) {
      if (!ptCircle || !ptCircle.ownerSVGElement) return;
      const svg = ptCircle.ownerSVGElement;
      const cx = ptCircle.getAttribute('cx');
      const cy = ptCircle.getAttribute('cy');
      if (cx === null || cy === null) return;
      const baseR = parseFloat(ptCircle.getAttribute('r') || '3.5');
      const svgNs = 'http://www.w3.org/2000/svg';
      const parent = svg.querySelector('#highlights') || svg.querySelector('#graphics') || svg;

      const ring = document.createElementNS(svgNs, 'circle');
      ring.setAttribute('cx', cx);
      ring.setAttribute('cy', cy);
      ring.setAttribute('r', String(baseR + 4.0));
      ring.setAttribute('class', 'geom-coincide-ring geom-coincide-ring-inner');
      parent.appendChild(ring);
    },

    // Highlight an equality or coincidence assertion with SVG center tick markers (|, ||, |||)
    highlightAssertion(groups, triggerEl, defaultGraphicId) {
      this.clearHighlights();

      const isCoincide =
        triggerEl.classList.contains('geom-coincide-ref') ||
        triggerEl.hasAttribute('data-assert-coincide') ||
        Boolean(triggerEl.querySelector?.('.geom-coincide-ref'));

      if (triggerEl.classList.contains('geom-eq-ref')) {
        triggerEl.classList.add('geom-assert-text');
        if (isCoincide) triggerEl.classList.add('geom-coincide-text');
      } else {
        triggerEl.classList.add('geom-assert-block-active');
        if (isCoincide) triggerEl.classList.add('geom-coincide-block-active');
      }
      this.activeHighlights.add(triggerEl);

      const allTargetKeys = new Set();
      const ringedPoints = new Set();
      let segTickCounter = 0;
      let angTickCounter = 0;

      groups.forEach((grp) => {
        // Determine whether this equality group is segments or angles for tick numbering
        let groupKind = 'other';
        for (const ref of grp) {
          const kind = this.getRefGeometryKind(ref, defaultGraphicId);
          if (kind === 'seg') {
            groupKind = 'seg';
            break;
          }
          if (kind === 'wedge') {
            groupKind = 'ang';
            break;
          }
        }

        let tickClass = null;
        if (groupKind === 'seg') {
          segTickCounter = Math.min(3, segTickCounter + 1);
          tickClass = `geom-tick-${segTickCounter}`;
        } else if (groupKind === 'ang') {
          angTickCounter = Math.min(3, angTickCounter + 1);
          tickClass = `geom-tick-${angTickCounter}`;
        }

        grp.forEach((ref) => {
          const { primary, secondary, parsed } = this.getSvgElementsForRef(ref, defaultGraphicId);
          if (parsed) {
            parsed.keys.forEach((k) => allTargetKeys.add(k));
          }

          let tickTarget = null;
          primary.forEach((svgEl) => {
            if (!svgEl.classList.contains('geom-ang-arc')) {
              svgEl.classList.add('geom-assert-active');
              if (isCoincide) svgEl.classList.add('geom-coincide-active');
              this.activeHighlights.add(svgEl);
            }
            if (
              isCoincide &&
              svgEl.tagName.toLowerCase() === 'circle' &&
              (svgEl.classList.contains('geom-point') || svgEl.classList.contains('point')) &&
              !ringedPoints.has(svgEl)
            ) {
              ringedPoints.add(svgEl);
              this.addCoincideRing(svgEl);
            }
            if (tickClass) {
              if (groupKind === 'ang' && svgEl.classList.contains('geom-ang-arc')) {
                tickTarget = svgEl;
              } else if (
                groupKind === 'seg' &&
                svgEl.tagName.toLowerCase() === 'path' &&
                !svgEl.classList.contains('wedge') &&
                !svgEl.classList.contains('geom-polygon')
              ) {
                tickTarget = svgEl;
              }
            }
          });

          if (tickTarget && tickClass) {
            tickTarget.classList.add('geom-assert-active', tickClass);
            if (isCoincide) tickTarget.classList.add('geom-coincide-active');
            this.activeHighlights.add(tickTarget);
          }

          secondary.forEach((svgEl) => {
            svgEl.classList.add('geom-assert-secondary');
            if (isCoincide) {
              svgEl.classList.add('geom-coincide-secondary');
              if (
                svgEl.tagName.toLowerCase() === 'circle' &&
                (svgEl.classList.contains('geom-point') || svgEl.classList.contains('point')) &&
                !ringedPoints.has(svgEl)
              ) {
                ringedPoints.add(svgEl);
                this.addCoincideRing(svgEl);
              }
            }
            this.activeHighlights.add(svgEl);
          });
        });
      });

      // Highlight matching inline :g: spans within the surrounding clause/paragraph in green/cyan
      const contextRoot =
        triggerEl.closest('.sub-clause, .assertion, .geom-step, p, li') ||
        this.getRootContainer() ||
        document.body;
      const childRefs = contextRoot.querySelectorAll('.geom-interactive-ref');
      childRefs.forEach((txtEl) => {
        const elKeys = (txtEl.getAttribute('data-geom-keys') || '').split('||').filter(Boolean);
        if (elKeys.some((k) => allTargetKeys.has(k))) {
          txtEl.classList.add('geom-assert-text');
          if (isCoincide) txtEl.classList.add('geom-coincide-text');
          this.activeHighlights.add(txtEl);
        }
      });
    },

    // Binds hover events on SVG elements (bidirectional: SVG -> Text)
    bindSvgElements() {
      const svgs = document.querySelectorAll('svg.euclid-graphic');
      svgs.forEach((svg) => {
        const fullGid = this.normalizeGraphicId(svg.getAttribute('data-graphic-id') || 'g1');
        const refElements = svg.querySelectorAll('[data-ref], [id]');
        refElements.forEach((el) => {
          if (el.tagName.toLowerCase() === 'g' && !el.hasAttribute('data-ref')) return;
          if (el.tagName.toLowerCase() === 'defs' || el.closest('defs')) return;
          if (el.classList.contains('geom-ang-arc')) return;

          const rawRef = (el.getAttribute('data-ref') || el.getAttribute('id') || '').trim();
          if (
            !rawRef ||
            [
              'elements',
              'graphics',
              'highlights',
              'points',
              'labels',
              'construction',
              'geometry',
            ].includes(rawRef)
          ) {
            return;
          }

          el.style.cursor = 'pointer';

          el.addEventListener('mouseenter', () => {
            this.highlightFromSvg(rawRef, el, fullGid);
          });

          el.addEventListener('mouseleave', () => {
            this.clearHighlights();
            this.restoreStepHighlight();
          });
        });
      });
    },

    // Highlight trigger from Text hover (warm gold single-element highlight)
    highlightFromText(refs, textElement, defaultGraphicId) {
      this.clearHighlights();

      if (textElement && !textElement.classList.contains('geom-step')) {
        textElement.classList.add('geom-highlight-text');
        this.activeHighlights.add(textElement);
      }

      refs.forEach((ref) => {
        const { primary, secondary } = this.getSvgElementsForRef(ref, defaultGraphicId);

        primary.forEach((svgEl) => {
          if (svgEl.classList.contains('geom-ang-arc')) return;
          svgEl.classList.add('geom-highlight-active');
          this.activeHighlights.add(svgEl);
        });

        secondary.forEach((svgEl) => {
          svgEl.classList.add('geom-highlight-secondary');
          this.activeHighlights.add(svgEl);
        });
      });
    },

    // Highlight trigger from SVG hover (strictly scoped to the hovered SVG's graphicId)
    highlightFromSvg(rawRef, svgElement, fullGid) {
      this.clearHighlights();

      svgElement.classList.add('geom-highlight-active');
      this.activeHighlights.add(svgElement);

      const { primary, secondary } = this.getSvgElementsForRef(rawRef, fullGid);
      primary.forEach((svgEl) => {
        if (svgEl.classList.contains('geom-ang-arc')) return;
        svgEl.classList.add('geom-highlight-active');
        this.activeHighlights.add(svgEl);
      });
      secondary.forEach((svgEl) => {
        svgEl.classList.add('geom-highlight-secondary');
        this.activeHighlights.add(svgEl);
      });

      const targetKeys = new Set();
      const parsed = this.parseGeometorRef(rawRef, fullGid);
      if (parsed) parsed.keys.forEach((k) => targetKeys.add(k));

      const aliases = (svgElement.getAttribute('data-aliases') || '').trim();
      if (aliases) {
        aliases
          .split(/[|;]/)
          .map((s) => s.trim())
          .filter(Boolean)
          .forEach((a) => {
            const pa = this.parseGeometorRef(a, fullGid);
            if (pa) pa.keys.forEach((k) => targetKeys.add(k));
          });
      }

      const container = this.getRootContainer();
      if (!container) return;

      const interactiveTexts = container.querySelectorAll('.geom-interactive-ref');
      interactiveTexts.forEach((txtEl) => {
        const elKeys = (txtEl.getAttribute('data-geom-keys') || '').split('||').filter(Boolean);
        const matches = elKeys.some((k) => targetKeys.has(k));

        if (matches) {
          txtEl.classList.add('geom-highlight-text');
          this.activeHighlights.add(txtEl);
        }
      });
    },

    // Clear all active highlights
    clearHighlights() {
      this.activeHighlights.forEach((el) => {
        el.classList.remove(
          'geom-highlight-text',
          'geom-highlight-active',
          'geom-highlight-secondary',
          'geom-assert-block-active',
          'geom-assert-text',
          'geom-assert-active',
          'geom-assert-secondary',
          'geom-coincide-block-active',
          'geom-coincide-text',
          'geom-coincide-active',
          'geom-coincide-secondary',
          'geom-tick-1',
          'geom-tick-2',
          'geom-tick-3'
        );
      });
      this.activeHighlights.clear();
      document.querySelectorAll('svg.euclid-graphic .geom-coincide-ring').forEach((r) => r.remove());
    },

    // Restore highlight for the currently active step (if in step-by-step mode)
    restoreStepHighlight() {
      if (
        this.stepState &&
        this.stepState.steps.length > 0 &&
        this.stepState.currentStep >= 0 &&
        this.stepState.currentStep < this.stepState.steps.length
      ) {
        this.applyStepHighlight(this.stepState.steps[this.stepState.currentStep]);
      }
    },

    // Apply SVG and inline text highlight for a single step object
    applyStepHighlight(step) {
      this.clearHighlights();
      if (!step) return;

      if (step.eqGroups && step.eqGroups.length > 0) {
        this.highlightAssertion(step.eqGroups, step.el, step.defaultGid);
        step.el.querySelectorAll('.geom-eq-ref').forEach((eqSpan) => {
          eqSpan.classList.add('geom-assert-text');
          if (eqSpan.classList.contains('geom-coincide-ref')) {
            eqSpan.classList.add('geom-coincide-text');
          }
          this.activeHighlights.add(eqSpan);
        });
        if (step.refs && step.refs.length > 0) {
          step.refs.forEach((ref) => {
            const { primary, secondary } = this.getSvgElementsForRef(ref, step.defaultGid);
            primary.forEach((svgEl) => {
              if (
                !svgEl.classList.contains('geom-ang-arc') &&
                !svgEl.classList.contains('geom-assert-active')
              ) {
                svgEl.classList.add('geom-highlight-active');
                this.activeHighlights.add(svgEl);
              }
            });
            secondary.forEach((svgEl) => {
              if (
                !svgEl.classList.contains('geom-assert-active') &&
                !svgEl.classList.contains('geom-assert-secondary')
              ) {
                svgEl.classList.add('geom-highlight-secondary');
                this.activeHighlights.add(svgEl);
              }
            });
          });
        }
      } else if (step.refs && step.refs.length > 0) {
        this.highlightFromText(step.refs, step.el, step.defaultGid);
        step.el.querySelectorAll('.geom-interactive-ref').forEach((refSpan) => {
          refSpan.classList.add('geom-highlight-text');
          this.activeHighlights.add(refSpan);
        });
      }
    },

    // Initialize progressive context step-by-step SVG player
    initStepPlayer() {
      const container = this.getRootContainer();
      if (!container) return;

      const svgs = Array.from(
        container.querySelectorAll('svg.euclid-graphic:not(.euclid-thumbnail)')
      ).filter((svg) => !svg.closest('.collection'));
      if (svgs.length === 0) return;

      const folioId = this.getDefaultFolioId();
      let stepNodes = Array.from(container.querySelectorAll('.geom-step'));
      const isPseudocodeTrack = stepNodes.length > 0;

      if (!isPseudocodeTrack) {
        const candidates = Array.from(
          container.querySelectorAll('.assertion, .sub-clause, .qed, p')
        );
        stepNodes = candidates.filter((el) => {
          if (
            el.closest(
              '.enunciation, .porism, .lemma, .scholium, .collection, .graphviz, #dependency-graph, #required-for, header, footer'
            )
          ) {
            return false;
          }
          if (el.tagName.toLowerCase() === 'p' && el.classList.contains('rubric')) {
            return false;
          }
          return (
            el.hasAttribute('data-assert-equal') ||
            el.querySelector('.geom-interactive-ref, .geom-eq-ref') !== null
          );
        });
      }

      if (stepNodes.length < 2) return;

      // Wrap step sequence in a bounded scrollable viewport (.geom-steps-viewport)
      // directly below the graphic so the graphic and active step stay visible together.
      let viewport = stepNodes[0].closest('.geom-steps-viewport');
      if (!viewport) {
        const firstEl = stepNodes[0];
        const lastEl = stepNodes[stepNodes.length - 1];
        if (firstEl.parentNode && firstEl.parentNode === lastEl.parentNode) {
          const parent = firstEl.parentNode;
          const rangeEls = [];
          let cur = firstEl;
          let canWrapRange = true;
          while (cur) {
            if (
              cur.matches?.('figure, section, .graphviz') ||
              cur.querySelector?.('svg.euclid-graphic, figure.photon-svg')
            ) {
              canWrapRange = false;
              break;
            }
            rangeEls.push(cur);
            if (cur === lastEl) break;
            cur = cur.nextElementSibling;
          }
          if (canWrapRange && rangeEls.length > 0) {
            const nextAfterLast = lastEl.nextElementSibling;
            if (nextAfterLast && nextAfterLast.classList.contains('qed')) {
              rangeEls.push(nextAfterLast);
            }
            viewport = document.createElement('div');
            viewport.className = 'geom-steps-viewport';
            viewport.setAttribute('tabindex', '0');
            viewport.setAttribute('role', 'region');
            viewport.setAttribute('aria-label', 'Construction and proof steps');
            parent.insertBefore(viewport, firstEl);
            rangeEls.forEach((el) => viewport.appendChild(el));
          }
        }
      }

      const steps = stepNodes.map((stepEl, idx) => {
        const defaultGid =
          stepEl.closest('[data-graphic]')?.getAttribute('data-graphic') || `${folioId}.g1`;
        const refs = [];
        stepEl.querySelectorAll('[data-ref]').forEach((span) => {
          const raw = (span.getAttribute('data-ref') || '').trim();
          raw
            .split(';')
            .map((s) => s.trim())
            .filter(Boolean)
            .forEach((r) => {
              if (!refs.includes(r)) refs.push(r);
            });
        });

        const eqGroups = [];
        if (stepEl.hasAttribute('data-assert-equal')) {
          this.parseEqualitySpec(stepEl.getAttribute('data-assert-equal')).forEach((g) =>
            eqGroups.push(g)
          );
        }
        stepEl.querySelectorAll('.geom-eq-ref[data-assert-equal]').forEach((eqSpan) => {
          this.parseEqualitySpec(eqSpan.getAttribute('data-assert-equal')).forEach((g) =>
            eqGroups.push(g)
          );
        });

        const allRefs = [...refs];
        eqGroups.forEach((grp) => {
          grp.forEach((r) => {
            if (!allRefs.includes(r)) allRefs.push(r);
          });
        });

        return {
          el: stepEl,
          index: idx,
          defaultGid,
          refs,
          eqGroups,
          allRefs,
        };
      });

      const directSeenMap = new Map();
      const fallbackSeenMap = new Map();

      steps.forEach((step, idx) => {
        step.allRefs.forEach((ref) => {
          const { primary, secondary, parsed } = this.getSvgElementsForRef(ref, step.defaultGid);
          primary.forEach((svgEl) => {
            if (!directSeenMap.has(svgEl)) {
              directSeenMap.set(svgEl, idx);
            }
          });
          secondary.forEach((svgEl) => {
            if (
              parsed &&
              ['point', 'segment', 'section', 'line', 'legacy2'].includes(parsed.type)
            ) {
              if (!directSeenMap.has(svgEl)) {
                directSeenMap.set(svgEl, idx);
              }
            } else {
              if (!fallbackSeenMap.has(svgEl)) {
                fallbackSeenMap.set(svgEl, idx);
              }
            }
          });
        });
      });

      if (directSeenMap.size === 0 && fallbackSeenMap.size === 0) return;

      const controllableMap = new Map();
      svgs.forEach((svg) => {
        const els = svg.querySelectorAll(
          '#elements > *, #graphics > *, #points > *, #labels > *'
        );
        const candidates =
          els.length > 0
            ? Array.from(els)
            : Array.from(
                svg.querySelectorAll('path, line, circle, ellipse, rect, polygon, polyline, text')
              );

        candidates.forEach((el) => {
          if (el.closest('defs') || el.closest('#highlights') || el.classList.contains('geom-overlay')) {
            return;
          }
          if (directSeenMap.has(el)) {
            controllableMap.set(el, directSeenMap.get(el));
          } else if (fallbackSeenMap.has(el)) {
            controllableMap.set(el, fallbackSeenMap.get(el));
          } else if (el.hasAttribute('data-ref') || el.hasAttribute('id')) {
            controllableMap.set(el, steps.length - 1);
          } else {
            controllableMap.set(el, 0);
          }
        });
      });

      const toolbars = [];
      svgs.forEach((svg) => {
        const fig = svg.closest('figure.photon-svg, .euclid-figure-container');
        if (!fig || fig.querySelector('.geom-step-player')) return;

        const bar = document.createElement('div');
        bar.className = 'geom-step-player';
        bar.setAttribute('role', 'toolbar');
        bar.setAttribute('aria-label', 'Construction step controls');
        bar.innerHTML = `
          <div class="geom-step-controls">
            <button type="button" class="geom-step-btn" data-action="first" title="First step (Given)">|&lt;</button>
            <button type="button" class="geom-step-btn" data-action="prev" title="Previous step (\u2190)">&lt;</button>
            <button type="button" class="geom-step-btn geom-step-play" data-action="play" title="Play / Pause step sequence">&#9654;</button>
            <button type="button" class="geom-step-btn" data-action="next" title="Next step (\u2192)">&gt;</button>
          </div>
          <span class="geom-step-status">All (${steps.length})</span>
          <button type="button" class="geom-step-btn geom-step-all" data-action="all" title="Show complete diagram">All</button>
        `;

        bar.addEventListener('click', (e) => {
          const btn = e.target.closest('button[data-action]');
          if (!btn) return;
          const action = btn.getAttribute('data-action');
          if (action === 'first') {
            this.stopStepPlayback();
            this.setStep(0);
          } else if (action === 'prev') {
            this.stopStepPlayback();
            const cur = this.stepState.currentStep;
            this.setStep(cur > 0 ? cur - 1 : 0);
          } else if (action === 'next') {
            this.stopStepPlayback();
            const cur = this.stepState.currentStep;
            this.setStep(cur < steps.length ? cur + 1 : steps.length);
          } else if (action === 'all') {
            this.stopStepPlayback();
            this.setStep(steps.length);
          } else if (action === 'play') {
            this.toggleStepPlayback();
          }
        });

        fig.appendChild(bar);
        toolbars.push(bar);
      });

      steps.forEach((step, idx) => {
        step.el.setAttribute('data-step-index', String(idx));
        step.el.addEventListener('click', (e) => {
          if (e.target.closest('a')) return;
          this.stopStepPlayback();
          this.setStep(idx);
        });
      });

      this.stepState = {
        steps,
        currentStep: steps.length,
        isPlaying: false,
        timer: null,
        controllableMap,
        toolbars,
        viewport,
        isPseudocodeTrack,
      };

      if (!this._stepKeyHandlerBound) {
        this._stepKeyHandlerBound = true;
        document.addEventListener('keydown', (e) => {
          if (!this.stepState) return;
          if (e.metaKey || e.ctrlKey || e.altKey) return;
          const tag = (e.target?.tagName || '').toLowerCase();
          if (['input', 'textarea', 'select'].includes(tag) || e.target?.isContentEditable) {
            return;
          }
          const { steps: stList, currentStep: cur, viewport: vp } = this.stepState;
          const inPlayerOrVp =
            (vp && vp.contains(e.target)) || Boolean(e.target?.closest?.('.geom-step-player'));
          if (e.key === 'ArrowLeft' || (inPlayerOrVp && e.key === 'ArrowUp')) {
            e.preventDefault();
            this.stopStepPlayback();
            this.setStep(cur > 0 ? cur - 1 : 0);
          } else if (e.key === 'ArrowRight' || (inPlayerOrVp && e.key === 'ArrowDown')) {
            e.preventDefault();
            this.stopStepPlayback();
            this.setStep(cur < stList.length ? cur + 1 : stList.length);
          } else if (inPlayerOrVp && e.key === 'Home') {
            e.preventDefault();
            this.stopStepPlayback();
            this.setStep(0);
          } else if (inPlayerOrVp && e.key === 'End') {
            e.preventDefault();
            this.stopStepPlayback();
            this.setStep(stList.length);
          } else if (inPlayerOrVp && e.key === ' ') {
            e.preventDefault();
            this.toggleStepPlayback();
          }
        });
      }

      // Support ?step=<1..N|all> query param for deep-linking and 1080p stage captures
      const params = new URLSearchParams(window.location.search);
      const stepParam = params.get('step');
      if (stepParam !== null) {
        if (stepParam.toLowerCase() === 'all') {
          this.setStep(steps.length, { smooth: false });
        } else {
          const parsed = parseInt(stepParam, 10);
          if (!Number.isNaN(parsed)) {
            const idx = Math.max(0, Math.min(steps.length, parsed - 1));
            this.setStep(idx, { smooth: false });
          }
        }
      } else if (isPseudocodeTrack) {
        this.setStep(0, { smooth: false });
      } else {
        this.setStep(steps.length, { smooth: false });
      }
    },

    // Smoothly center a step element inside .geom-steps-viewport without scrolling the page window
    scrollStepIntoViewport(stepEl, smooth = true) {
      if (!stepEl || !this.stepState || !this.stepState.viewport) return;
      const vp = this.stepState.viewport;
      if (!vp.contains(stepEl)) return;
      const vpRect = vp.getBoundingClientRect();
      const elRect = stepEl.getBoundingClientRect();
      const offsetInsideVp = elRect.top - vpRect.top + vp.scrollTop;
      const targetScroll = Math.max(
        0,
        offsetInsideVp - vp.clientHeight / 2 + elRect.height / 2
      );
      vp.scrollTo({
        top: targetScroll,
        behavior: smooth ? 'smooth' : 'auto',
      });
    },

    setStep(stepIndex, options = {}) {
      if (!this.stepState) return;
      const { steps, controllableMap, toolbars } = this.stepState;
      const clamped = Math.max(0, Math.min(steps.length, stepIndex));
      this.stepState.currentStep = clamped;

      steps.forEach((step, idx) => {
        step.el.classList.toggle('geom-step-active', idx === clamped);
        step.el.classList.toggle('geom-step-past', clamped < steps.length && idx < clamped);
        step.el.classList.toggle('geom-step-future', clamped < steps.length && idx > clamped);
      });

      controllableMap.forEach((firstSeen, svgEl) => {
        const hidden = clamped < steps.length && firstSeen > clamped;
        svgEl.classList.toggle('geom-step-hidden', hidden);
      });

      if (clamped < steps.length) {
        this.applyStepHighlight(steps[clamped]);
        this.scrollStepIntoViewport(steps[clamped].el, options.smooth !== false);
      } else {
        this.clearHighlights();
      }

      toolbars.forEach((bar) => {
        const statusEl = bar.querySelector('.geom-step-status');
        if (statusEl) {
          statusEl.textContent =
            clamped < steps.length
              ? `Step ${clamped + 1} / ${steps.length}`
              : `All (${steps.length})`;
        }
        const allBtn = bar.querySelector('[data-action="all"]');
        if (allBtn) {
          allBtn.classList.toggle('is-active', clamped === steps.length);
        }
        const playBtn = bar.querySelector('[data-action="play"]');
        if (playBtn) {
          playBtn.innerHTML = this.stepState.isPlaying ? '&#10074;&#10074;' : '&#9654;';
          playBtn.classList.toggle('is-active', this.stepState.isPlaying);
        }
      });
    },

    toggleStepPlayback() {
      if (!this.stepState) return;
      if (this.stepState.isPlaying) {
        this.stopStepPlayback();
        return;
      }
      const { steps } = this.stepState;
      if (this.stepState.currentStep >= steps.length - 1) {
        this.setStep(0);
      }
      this.stepState.isPlaying = true;
      this.setStep(this.stepState.currentStep);

      this.stepState.timer = window.setInterval(() => {
        if (!this.stepState || !this.stepState.isPlaying) return;
        const nextIdx = this.stepState.currentStep + 1;
        if (nextIdx < this.stepState.steps.length) {
          this.setStep(nextIdx);
        } else {
          this.stopStepPlayback();
        }
      }, 1300);
    },

    stopStepPlayback() {
      if (!this.stepState) return;
      if (this.stepState.timer) {
        window.clearInterval(this.stepState.timer);
        this.stepState.timer = null;
      }
      if (this.stepState.isPlaying) {
        this.stepState.isPlaying = false;
        this.setStep(this.stepState.currentStep);
      }
    },
  };

  window.EuclidInteractive = EuclidInteractive;
  window.GeometorInteractive = EuclidInteractive;

  document.addEventListener('DOMContentLoaded', () => {
    if (!document.getElementById('mdView-rendered')) {
      EuclidInteractive.init();
    }
  });
})(window, document);
