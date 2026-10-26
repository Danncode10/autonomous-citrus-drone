// Shared slide chrome. Each slide sets data-num, data-part and data-eyebrow on <body>;
// this script adds the top bar (eyebrow + storyline progress) and the footer, then
// renders the Lucide icons and flags the page as ready for build.py to capture.
const PARTS = [
  ['problem', 'Problem'],
  ['solution', 'Solution'],
  ['method', 'Method'],
  ['build', 'System'],
  ['plan', 'Plan'],
];

const SHORT_TITLE = 'Computer Vision and Autonomous Drone Inspection for Hydroponic Towers';

(function () {
  const body = document.body;
  const slide = document.querySelector('.slide');

  if (body.dataset.frame !== 'none') {
    const current = PARTS.findIndex(([key]) => key === body.dataset.part);
    const steps = PARTS.map(([, name], i) => {
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

  if (window.lucide) lucide.createIcons({ attrs: { 'stroke-width': 1.75 } });

  document.fonts.ready.then(() => { window.slideReady = true; });
})();
