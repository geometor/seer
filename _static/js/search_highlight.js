/**
 * PHOTON Publish — Search Excerpts & In-Page Highlighting Enhancement
 *
 * 1. Appends `?highlight=<terms>` to all search result links on `search.html`.
 * 2. Ensures every search result (including titles and API objects) displays
 *    a clean text excerpt with matched terms highlighted.
 * 3. Preserves `?highlight=<terms>` in the page URL after clicking a search
 *    result link and highlights all matching words inside the article body.
 */
(function () {
  "use strict";

  const initialUrl = new URL(window.location.href);
  const initialUrlHighlight = initialUrl.searchParams.get("highlight") || "";

  /**
   * Append `?highlight=...` to a relative or absolute href before any `#hash`.
   */
  function appendHighlightParam(rawHref, highlightStr) {
    if (!rawHref || !highlightStr) return rawHref;
    const hashIdx = rawHref.indexOf("#");
    const basePath = hashIdx >= 0 ? rawHref.slice(0, hashIdx) : rawHref;
    const hashPart = hashIdx >= 0 ? rawHref.slice(hashIdx) : "";

    // Avoid duplicating if already present
    if (/[?&]highlight=/.test(basePath)) return rawHref;

    const sep = basePath.includes("?") ? "&" : "?";
    const encoded = encodeURIComponent(highlightStr.trim()).replace(/%20/g, "+");
    return `${basePath}${sep}highlight=${encoded}${hashPart}`;
  }

  /**
   * Highlight a list of terms inside a target DOM node using Sphinx's `_highlightText`.
   */
  function highlightTermsInNode(node, terms) {
    if (!node || typeof _highlightText !== "function") return;
    terms.forEach((term) => {
      if (term) {
        _highlightText(node, term.toLowerCase(), "highlighted");
      }
    });
  }

  /**
   * Override SphinxHighlight methods so `?highlight=...` is preserved in the URL
   * and matches are highlighted inside `.content.body` / `[role="main"]`.
   */
  function enhanceSphinxHighlight() {
    if (typeof SphinxHighlight === "undefined") return;

    SphinxHighlight.highlightSearchWords = () => {
      if (
        typeof SPHINX_HIGHLIGHT_ENABLED !== "undefined" &&
        !SPHINX_HIGHLIGHT_ENABLED
      ) {
        return;
      }

      const url = new URL(window.location.href);
      const urlHighlight =
        url.searchParams.get("highlight") || initialUrlHighlight || "";
      const storedHighlight =
        localStorage.getItem("sphinx_highlight_terms") || "";
      const highlight = (urlHighlight || storedHighlight).trim();

      localStorage.removeItem("sphinx_highlight_terms");
      if (!highlight) return;

      // Ensure ?highlight=... is visible in the address bar
      if (!url.searchParams.has("highlight")) {
        url.searchParams.set("highlight", highlight);
        window.history.replaceState({}, "", url);
      }

      const terms = highlight
        .toLowerCase()
        .split(/\s+/)
        .filter((x) => x);
      if (terms.length === 0) return;

      // Populate sidebar search box with the active highlight terms
      document.querySelectorAll('#searchbox input[name="q"]').forEach((el) => {
        if (!el.value) el.value = terms.join(" ");
      });

      const body =
        document.querySelector("div.body") ||
        document.querySelector('[role="main"]') ||
        document.querySelector("main") ||
        document.body;

      window.setTimeout(() => {
        // Avoid double-highlighting if already highlighted
        if (!body.querySelector("span.highlighted")) {
          highlightTermsInNode(body, terms);
        }

        // Scroll first match into view if no specific #anchor was targeted
        if (!window.location.hash) {
          const firstMatch = body.querySelector("span.highlighted");
          if (firstMatch) {
            firstMatch.scrollIntoView({ behavior: "smooth", block: "center" });
          }
        }
      }, 15);

      const searchBox = document.getElementById("searchbox");
      if (searchBox && !searchBox.querySelector(".highlight-link")) {
        const label =
          typeof _ === "function"
            ? _("Hide Search Matches")
            : "Hide Search Matches";
        const p = document.createElement("p");
        p.className = "highlight-link";
        const a = document.createElement("a");
        a.href = "#";
        a.textContent = label;
        a.addEventListener("click", (e) => {
          e.preventDefault();
          SphinxHighlight.hideSearchWords();
        });
        p.appendChild(a);
        searchBox.appendChild(p);
      }
    };

    SphinxHighlight.hideSearchWords = () => {
      document
        .querySelectorAll("#searchbox .highlight-link")
        .forEach((el) => el.remove());
      document.querySelectorAll("span.highlighted").forEach((el) => {
        const parent = el.parentNode;
        if (parent) {
          parent.replaceChild(document.createTextNode(el.textContent), el);
          parent.normalize();
        } else {
          el.classList.remove("highlighted");
        }
      });
      localStorage.removeItem("sphinx_highlight_terms");

      const url = new URL(window.location.href);
      if (url.searchParams.has("highlight")) {
        url.searchParams.delete("highlight");
        window.history.replaceState({}, "", url);
      }
    };
  }

  /**
   * Enhance Sphinx's `Search` object on `search.html`.
   */
  function initSearchPage(indexUrl) {
    if (typeof Search === "undefined") return;

    Search._currentHighlightTerms = [];
    Search._currentSearchTerms = [];

    // Hook _parseQuery to capture current search & highlight terms
    const origParseQuery = Search._parseQuery.bind(Search);
    Search._parseQuery = (query) => {
      const parsed = origParseQuery(query);
      const [, searchTerms, , highlightTerms, objectTerms] = parsed;
      const hl = [...highlightTerms];
      if (hl.length === 0 && objectTerms) {
        hl.push(...objectTerms);
      }
      Search._currentHighlightTerms = hl;
      Search._currentSearchTerms = [...searchTerms];
      return parsed;
    };

    // Robust HTML-to-text extractor that handles dotted IDs and fallback containers
    Search.htmlToText = (htmlString, anchor) => {
      const htmlElement = new DOMParser().parseFromString(
        htmlString,
        "text/html"
      );
      for (const removalQuery of [
        ".headerlink",
        "script",
        "style",
        "noscript",
        ".book-header",
        ".book-footer",
        "nav.breadcrumbs",
        "nav.context",
      ]) {
        htmlElement.querySelectorAll(removalQuery).forEach((el) => el.remove());
      }

      if (anchor && anchor.startsWith("#")) {
        const rawId = decodeURIComponent(anchor.slice(1));
        let anchorNode = htmlElement.getElementById(rawId);
        if (!anchorNode && typeof CSS !== "undefined" && CSS.escape) {
          anchorNode = htmlElement.querySelector(
            `[role="main"] #${CSS.escape(rawId)}`
          );
        }
        if (anchorNode) {
          // If the anchor is on a heading or <dt>, grab its enclosing section/<dl> for context
          if (/^H[1-6]$/.test(anchorNode.tagName) && anchorNode.parentElement) {
            anchorNode = anchorNode.parentElement;
          } else if (
            anchorNode.tagName === "DT" &&
            anchorNode.nextElementSibling &&
            anchorNode.nextElementSibling.tagName === "DD"
          ) {
            return (
              anchorNode.textContent +
              " " +
              anchorNode.nextElementSibling.textContent
            )
              .replace(/\s+/g, " ")
              .trim();
          }
          const text = anchorNode.textContent.replace(/\s+/g, " ").trim();
          if (text) return text;
        }
      }

      const docContent =
        htmlElement.querySelector('[role="main"]') ||
        htmlElement.querySelector(".content") ||
        htmlElement.querySelector("article") ||
        htmlElement.querySelector("main");
      if (docContent) {
        return docContent.textContent.replace(/\s+/g, " ").trim();
      }
      return "";
    };

    // Improved excerpt builder that never produces NaN offsets
    Search.makeSearchSummary = (htmlText, keywords, anchor) => {
      const text = Search.htmlToText(htmlText, anchor);
      if (!text) return null;

      const textLower = text.toLowerCase();
      const candidateTerms = [
        ...(Search._currentHighlightTerms || []),
        ...(keywords ? [...keywords] : []),
      ].filter((k) => k);

      const positions = candidateTerms
        .map((k) => textLower.indexOf(k.toLowerCase()))
        .filter((i) => i > -1);

      const actualStartPosition = positions.length > 0 ? positions[0] : 0;
      const startWithContext = Math.max(actualStartPosition - 100, 0);

      const top = startWithContext === 0 ? "" : "…";
      const excerptLength = 240;
      const tail =
        startWithContext + excerptLength < text.length ? "…" : "";

      const summary = document.createElement("p");
      summary.classList.add("context");
      summary.textContent =
        top + text.substr(startWithContext, excerptLength).trim() + tail;

      return summary;
    };

    // Observe #search-results to enhance result links and excerpts
    const resultsContainer = document.getElementById("search-results");
    if (resultsContainer) {
      const getAllHighlightTerms = () => {
        const combined = new Set([
          ...(Search._currentHighlightTerms || []),
          ...(Search._currentSearchTerms || []).filter((t) => t.length >= 3),
        ]);
        return [...combined];
      };

      const processListItem = (li) => {
        if (li.dataset.photonEnhanced === "true") return;
        li.dataset.photonEnhanced = "true";

        const hlTerms = Search._currentHighlightTerms || [];
        const allTerms = getAllHighlightTerms();
        const highlightParam =
          hlTerms.length > 0 ? hlTerms.join(" ") : allTerms.join(" ");

        const linkEl = li.querySelector("a");
        if (linkEl) {
          const origHref = linkEl.getAttribute("href") || "";
          if (highlightParam) {
            linkEl.setAttribute(
              "href",
              appendHighlightParam(origHref, highlightParam)
            );
          }
          highlightTermsInNode(linkEl, allTerms);

          // If this is an API object result (which has a descr span and no fetched summary),
          // fetch the page to also display an excerpt under the object link.
          const hasDescr = li.querySelector("span") !== null;
          const showSearchSummary =
            typeof DOCUMENTATION_OPTIONS !== "undefined"
              ? DOCUMENTATION_OPTIONS.SHOW_SEARCH_SUMMARY
              : true;
          if (hasDescr && showSearchSummary) {
            const hashIdx = origHref.indexOf("#");
            const baseHref =
              hashIdx >= 0 ? origHref.slice(0, hashIdx) : origHref;
            const anchor = hashIdx >= 0 ? origHref.slice(hashIdx) : "";
            if (baseHref) {
              fetch(baseHref)
                .then((res) => (res.ok ? res.text() : ""))
                .then((html) => {
                  if (!html || li.querySelector("p.context")) return;
                  const summary = Search.makeSearchSummary(
                    html,
                    Search._currentSearchTerms || [],
                    anchor
                  );
                  if (summary) {
                    li.appendChild(summary);
                    highlightTermsInNode(summary, allTerms);
                  }
                })
                .catch(() => {});
            }
          }
        }
      };

      const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType !== Node.ELEMENT_NODE) return;
            if (node.tagName === "LI") {
              processListItem(node);
            } else if (
              node.tagName === "P" &&
              node.classList.contains("context")
            ) {
              highlightTermsInNode(node, getAllHighlightTerms());
            } else {
              node.querySelectorAll?.("li").forEach(processListItem);
            }
          });
        }
      });

      observer.observe(resultsContainer, { childList: true, subtree: true });
    }

    if (indexUrl) {
      Search.loadIndex(indexUrl);
    }
  }

  enhanceSphinxHighlight();

  window.PhotonSearch = {
    initSearchPage,
    appendHighlightParam,
  };
})();
