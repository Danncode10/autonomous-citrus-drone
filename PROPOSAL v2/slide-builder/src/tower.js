// Draws a side view of a hydroponic tower as inline SVG. Used by any slide that puts
// <div class="tower-art" data-pattern="LE LL EL ..."></div> on the page.
// Each space-separated pair is one level, bottom to top: left pot then right pot,
// L = lettuce, E = empty. data-highlight="empty" rings the empty pots in red;
// data-markers="off" hides the ArUco markers.
(function () {
  const LEAF = ['#5fae5a', '#7cc46a', '#9fd67f'];

  function lettuce(x, y) {
    return `<g>
      <circle cx="${x - 14}" cy="${y + 4}" r="20" fill="${LEAF[0]}"/>
      <circle cx="${x + 14}" cy="${y + 2}" r="20" fill="${LEAF[0]}"/>
      <circle cx="${x}" cy="${y - 12}" r="22" fill="${LEAF[1]}"/>
      <circle cx="${x - 6}" cy="${y - 2}" r="13" fill="${LEAF[2]}"/>
      <path d="M${x - 10} ${y - 14}q8 6 18 2" stroke="#3e8a46" stroke-width="2" fill="none" stroke-linecap="round"/>
    </g>`;
  }

  // A cup leaning out from the pipe; side = 1 for right, -1 for left.
  function pot(cx, y, side, kind, ring) {
    const t = `translate(${cx + side * 40} ${y}) scale(${side} 1)`;
    const cup = `<g transform="${t}">
      <path d="M-4 -12 L34 -40 L52 -18 L8 14 Z" fill="#f3f3ef" stroke="#c9cdc4" stroke-width="2" stroke-linejoin="round"/>
      <ellipse cx="43" cy="-29" rx="16" ry="7" transform="rotate(-36 43 -29)" fill="${kind === 'E' ? '#2b2b26' : '#dfe3da'}"/>
      ${kind === 'L' ? lettuce(46, -46) : ''}
      ${kind === 'E' && ring ? '<circle cx="43" cy="-29" r="30" fill="none" stroke="#b4452f" stroke-width="3.5" stroke-dasharray="7 6"/>' : ''}
    </g>`;
    return cup;
  }

  function marker(x, y, s) {
    const c = s / 5;
    // Fixed 3x3 inner pattern so every marker looks like a real ArUco tag.
    const bits = [[1, 0, 1], [0, 1, 1], [1, 1, 0]];
    let inner = '';
    bits.forEach((row, r) => row.forEach((b, k) => {
      if (b) inner += `<rect x="${x + c * (k + 1)}" y="${y + c * (r + 1)}" width="${c}" height="${c}" fill="#fff"/>`;
    }));
    return `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#111"/>${inner}`;
  }

  function draw(el) {
    const levels = (el.dataset.pattern || 'LL LE LL EL LL LE LL').split(' ');
    const ring = el.dataset.highlight === 'empty';
    const markers = el.dataset.markers !== 'off';
    const gap = 92;
    const top = 40;
    const h = levels.length * gap + 40;
    const cx = 220;
    let pots = '';
    let tags = '';
    levels.forEach((lv, i) => {
      const y = top + h - 40 - i * gap - 10;
      pots += pot(cx, y, -1, lv[0], ring) + pot(cx, y, 1, lv[1], ring);
      if (markers && i % 2 === 0) tags += marker(cx - 13, y - 58, 26);
    });
    const base = top + h;
    el.innerHTML = `<svg viewBox="0 0 440 ${base + 70}" fill="none" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="${cx}" cy="${base + 40}" rx="150" ry="16" fill="rgba(0,0,0,0.12)"/>
      <path d="M${cx - 120} ${base} h240 v30 a120 14 0 0 1 -240 0 Z" fill="#2d6a4a"/>
      <ellipse cx="${cx}" cy="${base}" rx="120" ry="14" fill="#3b8059"/>
      <rect x="${cx - 40}" y="${top}" width="80" height="${h}" rx="6" fill="#fbfbf8" stroke="#cfd3ca" stroke-width="2"/>
      <rect x="${cx - 40}" y="${top}" width="22" height="${h}" fill="#e9ebe4"/>
      <ellipse cx="${cx}" cy="${top}" rx="40" ry="8" fill="#eef0ea" stroke="#cfd3ca" stroke-width="2"/>
      ${tags}
      ${pots}
    </svg>`;
  }

  document.querySelectorAll('.tower-art').forEach(draw);
})();
