// Builds the five-part progress rail on a section divider. The current part comes
// from data-part on <body>; load this before frame.js so the icons render.
(function () {
  const PARTS = ['problem', 'solution', 'method', 'build', 'plan'];
  const NAMES = ['The Problem', 'The Solution', 'The Method', 'The System', 'The Plan'];
  const current = PARTS.indexOf(document.body.dataset.part);

  document.querySelector('.rail').innerHTML = NAMES.map((name, i) => {
    const state = i < current ? 'done' : i === current ? 'active' : '';
    return `<li class="${state}"><b>0${i + 1}</b>${name}</li>`;
  }).join('');
})();
