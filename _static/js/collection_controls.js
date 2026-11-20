document.addEventListener('DOMContentLoaded', () => {
    const collections = document.querySelectorAll('.collection');

    collections.forEach(collection => {
        // Create controls container
        const controls = document.createElement('div');
        controls.className = 'collection-controls';

        // Define layout options
        const layouts = [
            { name: 'cards', icon: '<svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>' },
            { name: 'banners', icon: '<svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="18" height="7"></rect><rect x="3" y="14" width="18" height="7"></rect></svg>' },
            { name: 'list', icon: '<svg viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>' }
        ];

        // Create buttons
        layouts.forEach(layout => {
            const btn = document.createElement('button');
            btn.innerHTML = layout.icon;
            btn.title = `Switch to ${layout.name} view`;
            btn.className = `layout-btn layout-${layout.name}`;

            btn.addEventListener('click', () => {
                console.log(`Switching to ${layout.name} layout`);
                // Remove active class from all buttons
                controls.querySelectorAll('.layout-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // Remove all layout classes from collection
                layouts.forEach(l => collection.classList.remove(`layout-${l.name}`));
                // Add new layout class
                collection.classList.add(`layout-${layout.name}`);
                console.log(`Added class layout-${layout.name} to collection`);

                // Save preference (optional, implementing simple local storage)
                localStorage.setItem('collection-layout', layout.name);
            });

            controls.appendChild(btn);
        });

        // Set default or saved layout
        const savedLayout = localStorage.getItem('collection-layout') || 'cards';
        const activeBtn = controls.querySelector(`.layout-${savedLayout}`);
        if (activeBtn) {
            activeBtn.click();
        } else {
            // Fallback to first button if saved layout not found
            controls.querySelector('.layout-btn').click();
        }

        // Insert controls before the collection items, but after header if exists
        const header = collection.querySelector('header');
        if (header) {
            header.appendChild(controls);
        } else {
            collection.insertBefore(controls, collection.firstChild);
        }
    });
});
