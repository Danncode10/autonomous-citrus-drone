// Small flat illustrations for the literature slides (03a–03d), in the same style as
// tower.js. Each helper returns an SVG string; a slide composes them inside its own
// <svg> and then calls Art.mount() to fill every <svg data-art="name"> on the page.
(function () {
  const LEAF = ['#5fae5a', '#7cc46a', '#9fd67f'];
  const A = {};

  A.lettuce = (x, y, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})">
    <circle cx="-14" cy="4" r="20" fill="${LEAF[0]}"/>
    <circle cx="14" cy="2" r="20" fill="${LEAF[0]}"/>
    <circle cx="0" cy="-12" r="22" fill="${LEAF[1]}"/>
    <circle cx="-6" cy="-2" r="13" fill="${LEAF[2]}"/>
    <path d="M-10 -14q8 6 18 2" stroke="#3e8a46" stroke-width="2" fill="none" stroke-linecap="round"/>
  </g>`;

  // Net pot seen from the front. kind 'L' holds a lettuce; 'E' is empty.
  A.pot = (x, y, s, kind) => `<g transform="translate(${x} ${y}) scale(${s})">
    <path d="M-30 0 L-20 30 H20 L30 0 Z" fill="#e6e8e1" stroke="#c9cdc4" stroke-width="2" stroke-linejoin="round"/>
    <ellipse cx="0" cy="0" rx="30" ry="10" fill="#f3f3ef" stroke="#c9cdc4" stroke-width="2"/>
    <ellipse cx="0" cy="0" rx="22" ry="6" fill="${kind === 'E' ? '#2b2b26' : '#cfd5c8'}"/>
    ${kind === 'L' ? A.lettuce(0, -18, 1) : ''}
  </g>`;

  // ArUco-style marker, same fixed pattern as tower.js.
  A.marker = (x, y, s) => {
    const c = s / 5;
    const bits = [[1, 0, 1], [0, 1, 1], [1, 1, 0]];
    let inner = '';
    bits.forEach((row, r) => row.forEach((b, k) => {
      if (b) inner += `<rect x="${x + c * (k + 1)}" y="${y + c * (r + 1)}" width="${c}" height="${c}" fill="#fff"/>`;
    }));
    return `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#111"/>${inner}`;
  };

  // Small quadcopter seen from the side, centered on (x, y). face = 1 looks right.
  A.drone = (x, y, s = 1, face = 1) => `<g transform="translate(${x} ${y}) scale(${s * face} ${s})">
    <path d="M-44 -10 H44" stroke="#12392b" stroke-width="5" stroke-linecap="round"/>
    <rect x="-46" y="-22" width="4" height="12" fill="#12392b"/>
    <rect x="42" y="-22" width="4" height="12" fill="#12392b"/>
    <ellipse cx="-44" cy="-24" rx="24" ry="4.5" fill="#9fb8ab"/>
    <ellipse cx="44" cy="-24" rx="24" ry="4.5" fill="#9fb8ab"/>
    <rect x="-22" y="-14" width="44" height="18" rx="6" fill="#1d5240"/>
    <rect x="-8" y="-20" width="16" height="7" rx="2" fill="#d9a520"/>
    <circle cx="25" cy="-2" r="6" fill="#16231c" stroke="#9fd6a9" stroke-width="2"/>
  </g>`;

  // Person seen from the side, feet at (x, y), looking up and right.
  A.person = (x, y, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})">
    <rect x="-13" y="-70" width="11" height="70" rx="5" fill="#2f3d35"/>
    <rect x="1" y="-70" width="11" height="70" rx="5" fill="#2f3d35"/>
    <rect x="-22" y="-142" width="44" height="80" rx="16" fill="#2b7a3c"/>
    <path d="M14 -128 L40 -104" stroke="#2b7a3c" stroke-width="11" stroke-linecap="round"/>
    <rect x="30" y="-122" width="26" height="34" rx="3" fill="#fff" stroke="#c9cdc4" stroke-width="2" transform="rotate(-12 43 -105)"/>
    <path d="M36 -112h14M36 -104h14M36 -96h10" stroke="#c9cdc4" stroke-width="2" transform="rotate(-12 43 -105)"/>
    <circle cx="2" cy="-164" r="19" fill="#c98b5e"/>
    <path d="M-17 -166 a19 19 0 0 1 34 -10 q-12 -2 -20 4 q-8 -4 -14 6z" fill="#2a1f17"/>
  </g>`;

  // A tower from tower.js, embedded at (x, y) with the given width.
  A.tower = (x, y, width, pattern, opts) => {
    const m = window.towerMarkup(pattern, opts);
    const height = (width * m.h) / m.w;
    return `<svg x="${x}" y="${y}" width="${width}" height="${height}" viewBox="0 0 ${m.w} ${m.h}">${m.body}</svg>`;
  };
  // Where the tower's ground line lands, as a fraction of its drawn height.
  A.towerGround = (pattern) => {
    const m = window.towerMarkup(pattern);
    return (m.h - 40) / m.h;
  };

  // Red "?" badge for things nobody checks.
  A.ask = (x, y, r = 16) => `<g>
    <circle cx="${x}" cy="${y}" r="${r}" fill="#fff" stroke="#b4452f" stroke-width="3"/>
    <text x="${x}" y="${y + r * 0.45}" text-anchor="middle" font-size="${r * 1.3}" font-weight="800" fill="#b4452f">?</text>
  </g>`;

  A.check = (x, y, r = 14, color = '#2b7a3c') => `<g>
    <circle cx="${x}" cy="${y}" r="${r}" fill="${color}"/>
    <path d="M${x - r * 0.45} ${y} l${r * 0.32} ${r * 0.32} l${r * 0.6} -${r * 0.62}" stroke="#fff" stroke-width="${r * 0.22}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </g>`;

  A.cross = (x, y, r = 14) => `<g>
    <circle cx="${x}" cy="${y}" r="${r}" fill="#b4452f"/>
    <path d="M${x - r * 0.38} ${y - r * 0.38} l${r * 0.76} ${r * 0.76} M${x + r * 0.38} ${y - r * 0.38} l-${r * 0.76} ${r * 0.76}" stroke="#fff" stroke-width="${r * 0.22}" stroke-linecap="round"/>
  </g>`;

  // Fills each <svg data-art="key"> with Art.scenes[key](), keeping its viewBox.
  A.scenes = {};
  A.mount = () => {
    document.querySelectorAll('svg[data-art]').forEach((svg) => {
      svg.innerHTML = A.scenes[svg.dataset.art]();
    });
  };

  window.Art = A;
})();
