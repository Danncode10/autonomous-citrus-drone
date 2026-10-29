// Shared slide chrome. Each slide sets data-num, data-part and data-eyebrow on <body>;
// this script adds the top bar (eyebrow + storyline progress) and the footer, then
// renders the Lucide icons and flags the page as ready for build.py to capture.
// Add class="dark" to <body> for a forest-green content slide.
const PARTS = [
  ['problem', 'Problem'],
  ['solution', 'Solution'],
  ['method', 'Method'],
  ['build', 'System'],
  ['plan', 'Plan'],
];

// Icons Lucide doesn't ship, drawn in the same 24px stroke style.
const CUSTOM_ICONS = {
  drone: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="5" r="3"/><circle cx="19" cy="5" r="3"/><circle cx="5" cy="19" r="3"/><circle cx="19" cy="19" r="3"/><path d="M7.5 7.5 10 10M16.5 7.5 14 10M7.5 16.5 10 14M16.5 16.5 14 14"/><rect x="9.5" y="9.5" width="5" height="5" rx="1"/></svg>',
};

const SHORT_TITLE = 'Computer Vision and Autonomous Drone Inspection for Hydroponic Towers';

(function () {
  const body = document.body;
  const slide = document.querySelector('.slide');

  if (body.dataset.frame !== 'none') {
    const current = PARTS.findIndex(([key]) => key === body.dataset.part);
    const steps = body.dataset.part === 'backup'
      ? '<li class="active">Backup</li>'
      : PARTS.map(([, name], i) => {
          const state = i < current ? 'done' : i === current ? 'active' : '';
          return `<li class="${state}">${name}</li>`;
        }).join('');

    const top = document.createElement('header');
    top.className = 'topbar';
    top.innerHTML = `
      <div class="eyebrow"><span class="num">${body.dataset.num}</span>${body.dataset.eyebrow}</div>
      <ol class="progress">${steps}</ol>`;
    slide.prepend(top);

    const foot = document.createElement('footer');
    foot.className = 'footer';
    foot.innerHTML = `
      <div class="foot-left"><img src="../../figures/nvsu-logo.jpg" alt=""><span>${SHORT_TITLE}</span></div>
      <div class="foot-right">NVSU · CITE · BSCS 4B<span class="page">${body.dataset.num}</span></div>`;
    slide.append(foot);
  }

  document.querySelectorAll('i[data-lucide]').forEach((i) => {
    const svg = CUSTOM_ICONS[i.dataset.lucide];
    if (svg) i.outerHTML = svg;
  });
  if (window.lucide) lucide.createIcons({ attrs: { 'stroke-width': 1.75 } });

  document.fonts.ready.then(() => { window.slideReady = true; });
})();
