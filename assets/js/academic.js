(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('#main-navigation');
  const closeMenu = (restoreFocus = false) => {
    if (!toggle || !navigation) return;
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
    navigation.classList.remove('is-open');
    if (restoreFocus) toggle.focus();
  };
  if (toggle && navigation) {
    toggle.hidden = false;
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(expanded));
      toggle.setAttribute('aria-label', expanded ? 'Close navigation' : 'Open navigation');
      navigation.classList.toggle('is-open', expanded);
    });
    navigation.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') closeMenu(true);
    });
    window.matchMedia('(max-width: 640px)').addEventListener('change', () => closeMenu());
  }

  const filterGroup = document.querySelector('.project-filters');
  if (filterGroup) {
    const buttons = [...filterGroup.querySelectorAll('[data-filter]')];
    const projects = [...document.querySelectorAll('.archive-project')];
    const counter = document.querySelector('.filter-count');
    const selectFilter = (category, updateHistory) => {
      const selected = buttons.some(b => b.dataset.filter === category) ? category : 'all';
      let count = 0;
      projects.forEach(project => {
        project.hidden = selected !== 'all' && project.dataset.category !== selected;
        if (!project.hidden) count++;
      });
      buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === selected)));
      counter.textContent = `${count} of ${projects.length} projects`;
      if (updateHistory) {
        const url = new URL(window.location.href);
        if (selected === 'all') url.searchParams.delete('category');
        else url.searchParams.set('category', selected);
        window.history.pushState(null, '', url);
      }
    };
    filterGroup.hidden = false;
    filterGroup.addEventListener('click', event => {
      const button = event.target.closest('[data-filter]');
      if (button) selectFilter(button.dataset.filter, true);
    });
    const fromUrl = () => selectFilter(new URL(window.location.href).searchParams.get('category') || 'all', false);
    window.addEventListener('popstate', fromUrl);
    fromUrl();
  }

  const status = document.querySelector('.interaction-status');
  let statusTimer;
  const announce = message => {
    clearTimeout(statusTimer);
    status.textContent = message;
    statusTimer = setTimeout(() => { status.textContent = ''; }, 4500);
  };
  document.querySelectorAll('.copy-citation').forEach(button => {
    if (!navigator.clipboard) return;
    button.hidden = false;
    button.addEventListener('click', async () => {
      try {
        const response = await fetch(button.dataset.citation);
        if (!response.ok) throw new Error('Citation unavailable');
        await navigator.clipboard.writeText(await response.text());
        announce('BibTeX copied.');
      } catch {
        announce('Use the BibTeX link to download the citation.');
      }
    });
  });

  const dialog = document.querySelector('.figure-dialog');
  if (dialog && typeof dialog.showModal === 'function') {
    document.querySelectorAll('.figure-link').forEach(link => {
      link.addEventListener('click', event => {
        event.preventDefault();
        const source = link.querySelector('img');
        const image = dialog.querySelector('img');
        image.src = link.href;
        image.alt = source.alt;
        dialog.querySelector('.figure-dialog__caption').textContent = link.closest('figure').querySelector('figcaption').textContent;
        dialog.showModal();
      });
    });
    dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  }

  document.querySelectorAll('.video-load').forEach(button => {
    button.addEventListener('click', () => {
      const container = button.parentElement.querySelector('.video-container');
      const frame = document.createElement('iframe');
      frame.src = `https://www.youtube-nocookie.com/embed/${button.dataset.video}?autoplay=1`;
      frame.title = 'Neuromatch 2026 project presentation';
      frame.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      frame.allowFullscreen = true;
      container.replaceChildren(frame);
      container.hidden = false;
      button.hidden = true;
      frame.focus();
    }, { once: true });
  });
})();
