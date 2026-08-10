import fs from "node:fs/promises";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const OUT = "/Users/lesterdannlopez/Desktop/Shared_VM_Folder/Advance Robotics/Automated Citrus Drone/Sabatan/GrowKita_Business_Pitch_Template.pptx";
const BUILD = "/Users/lesterdannlopez/Desktop/Shared_VM_Folder/Advance Robotics/Automated Citrus Drone/Sabatan/.growkita-ppt.U84av8";
const W = 1280;
const H = 720;
const C = {
  ink: "#173B2C",
  green: "#0E6B4F",
  green2: "#23835E",
  orange: "#F28C28",
  orangeLight: "#FFF0DB",
  leaf: "#DDEEDC",
  cream: "#FFF9F1",
  paper: "#F7FAF6",
  white: "#FFFFFF",
  gray: "#667085",
  light: "#D5E2DA",
  dark: "#0C2C20",
};

async function writeBlob(path, blob) {
  await fs.writeFile(path, new Uint8Array(await blob.arrayBuffer()));
}

function shape(slide, geometry, position, fill, line = { style: "solid", fill: "none", width: 0 }, name) {
  return slide.shapes.add({ geometry, name, position, fill, line });
}

function text(slide, value, position, style = {}, name) {
  const box = shape(slide, "textbox", position, "none", { style: "solid", fill: "none", width: 0 }, name);
  box.text = value;
  box.text.style = { fontSize: 24, color: C.ink, ...style };
  return box;
}

function rule(slide, x, y, width, color = C.orange, thickness = 5) {
  return shape(slide, "rect", { left: x, top: y, width, height: thickness }, color, { style: "solid", fill: "none", width: 0 });
}

function header(slide, title, kicker, page, ruleY = 140) {
  text(slide, kicker.toUpperCase(), { left: 72, top: 42, width: 540, height: 22 }, { fontSize: 13, bold: true, color: C.green }, "kicker");
  text(slide, title, { left: 72, top: 76, width: 920, height: 52 }, { fontSize: 38, bold: true, color: C.ink }, "title");
  rule(slide, 72, ruleY, 70);
  text(slide, `GROWKITA  |  ${String(page).padStart(2, "0")}`, { left: 1030, top: 45, width: 178, height: 20 }, { fontSize: 11, bold: true, color: C.gray, alignment: "right" }, "page-marker");
}

function imagePlaceholder(slide, x, y, width, height, label, detail = "Paste your real image here") {
  const frame = shape(slide, "rect", { left: x, top: y, width, height }, C.leaf, { style: "solid", fill: C.green2, width: 2 }, "image-placeholder");
  text(slide, label.toUpperCase(), { left: x + 24, top: y + height / 2 - 36, width: width - 48, height: 28 }, { fontSize: 18, bold: true, color: C.green, alignment: "center" });
  text(slide, detail, { left: x + 24, top: y + height / 2 + 2, width: width - 48, height: 24 }, { fontSize: 14, color: C.gray, alignment: "center" });
  return frame;
}

function bulletList(slide, items, x, y, width, fontSize = 22, color = C.ink, gap = 52) {
  items.forEach((item, i) => {
    shape(slide, "ellipse", { left: x, top: y + i * gap + 10, width: 10, height: 10 }, C.orange, { style: "solid", fill: "none", width: 0 });
    text(slide, item, { left: x + 24, top: y + i * gap, width: width - 24, height: 38 }, { fontSize, color });
  });
}

function pill(slide, value, x, y, width, fill = C.orangeLight, color = C.orange) {
  const p = shape(slide, "roundRect", { left: x, top: y, width, height: 36 }, fill, { style: "solid", fill, width: 0 }, "label");
  p.borderRadius = 18;
  p.text = value;
  p.text.style = { fontSize: 13, bold: true, color, alignment: "center" };
}

function footer(slide, note) {
  text(slide, note, { left: 72, top: 675, width: 1050, height: 20 }, { fontSize: 11, color: C.gray });
}

function addNotes(slide, lines) {
  slide.speakerNotes.textFrame.setText(lines);
  slide.speakerNotes.setVisible(true);
}

function addProcessNode(slide, x, label, sub, fill, textColor = C.ink) {
  const node = shape(slide, "roundRect", { left: x, top: 300, width: 226, height: 148 }, fill, { style: "solid", fill: C.green2, width: 1 }, "process-node");
  node.borderRadius = 12;
  text(slide, label, { left: x + 18, top: 332, width: 190, height: 36 }, { fontSize: 21, bold: true, color: textColor, alignment: "center" });
  text(slide, sub, { left: x + 16, top: 378, width: 194, height: 44 }, { fontSize: 14, color: textColor, alignment: "center" });
  return node;
}

function connector(slide, x, y, width) {
  shape(slide, "rightArrow", { left: x, top: y, width, height: 28 }, C.orange, { style: "solid", fill: "none", width: 0 }, "process-arrow");
}

function addDataNode(slide, x, y, title, sub, fill, titleColor = C.ink, subColor = C.gray) {
  const n = shape(slide, "roundRect", { left: x, top: y, width: 198, height: 118 }, fill, { style: "solid", fill: C.green2, width: 1 }, "data-node");
  n.borderRadius = 12;
  text(slide, title, { left: x + 16, top: y + 28, width: 166, height: 28 }, { fontSize: 18, bold: true, color: titleColor, alignment: "center" });
  text(slide, sub, { left: x + 18, top: y + 62, width: 162, height: 34 }, { fontSize: 13, color: subColor, alignment: "center" });
  return n;
}

async function main() {
  const presentation = Presentation.create({ slideSize: { width: W, height: H } });

  // 1. Title
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.dark;
    shape(slide, "rect", { left: 0, top: 0, width: W, height: H }, C.dark);
    imagePlaceholder(slide, 770, 0, 510, 720, "Hero farm photo", "Perante citrus tree or farm landscape");
    shape(slide, "rect", { left: 0, top: 0, width: 810, height: H }, C.dark);
    rule(slide, 72, 150, 88, C.orange, 7);
    text(slide, "GrowKita", { left: 72, top: 186, width: 600, height: 76 }, { fontSize: 64, bold: true, color: C.white }, "brand");
    text(slide, "AI-powered farm intelligence.", { left: 72, top: 280, width: 590, height: 40 }, { fontSize: 28, color: "#DDEEDC" });
    text(slide, "Starting with citrus yield estimation\nfor Nueva Vizcaya farms.", { left: 72, top: 348, width: 600, height: 88 }, { fontSize: 30, bold: true, color: C.white });
    text(slide, "NVSU Business Pitch Competition 2026", { left: 72, top: 620, width: 500, height: 22 }, { fontSize: 15, color: "#B9D5C5" });
    text(slide, "TEAM NAME  |  NUEVA VIZCAYA STATE UNIVERSITY", { left: 72, top: 654, width: 620, height: 20 }, { fontSize: 12, bold: true, color: "#B9D5C5" });
    addNotes(slide, ["Open with the decision, not the drone.", "GrowKita helps farms plan harvest and buyer commitments before the exact fruit volume is known."]);
  }

  // 2. Vision
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.paper;
    header(slide, "Practical AI-powered farm intelligence for Philippine agriculture", "Our vision", 2, 318);
    text(slide, "GrowKita turns field observations into decisions that farms can act on.", { left: 72, top: 184, width: 700, height: 38 }, { fontSize: 24, color: C.gray });
    imagePlaceholder(slide, 824, 170, 384, 390, "Farm landscape or aerial image", "Use a real wide farm photo");
    const steps = [
      ["Observe", "Capture farm conditions\nwith guided monitoring"],
      ["Understand", "Use AI and computer vision\nto analyze what is seen"],
      ["Act", "Deliver clear insights\nfor farm decisions"],
    ];
    steps.forEach(([a, b], i) => {
      const x = 72 + i * 232;
      shape(slide, "ellipse", { left: x, top: 294, width: 74, height: 74 }, i === 0 ? C.orange : C.green, { style: "solid", fill: "none", width: 0 });
      text(slide, String(i + 1), { left: x, top: 313, width: 74, height: 28 }, { fontSize: 21, bold: true, color: C.white, alignment: "center" });
      text(slide, a, { left: x, top: 390, width: 160, height: 28 }, { fontSize: 21, bold: true, color: C.ink });
      text(slide, b, { left: x, top: 426, width: 182, height: 54 }, { fontSize: 16, color: C.gray });
    });
    pill(slide, "FIRST STEP: CITRUS YIELD ESTIMATION", 72, 550, 356, C.orangeLight, C.orange);
    footer(slide, "A platform vision, proven through one focused first product.");
    addNotes(slide, ["Agriculture is entering an AI era, but local farms need practical tools, not technology for its own sake.", "Our first step is citrus yield estimation in Nueva Vizcaya."]);
  }

  // 3. Why citrus
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.cream;
    header(slide, "Start local. Prove value. Then scale.", "Why citrus", 3);
    imagePlaceholder(slide, 72, 180, 430, 360, "Perante oranges on tree", "Paste a clear local citrus photo");
    shape(slide, "rect", { left: 542, top: 180, width: 290, height: 360 }, C.white, { style: "solid", fill: C.light, width: 1 }, "map-placeholder");
    text(slide, "NUEVA VIZCAYA", { left: 570, top: 314, width: 234, height: 24 }, { fontSize: 18, bold: true, color: C.green, alignment: "center" });
    text(slide, "PASTE A SIMPLE\nPROVINCE MAP HERE", { left: 572, top: 358, width: 230, height: 52 }, { fontSize: 16, bold: true, color: C.gray, alignment: "center" });
    text(slide, "Citrus gives GrowKita a focused first market.", { left: 880, top: 194, width: 300, height: 66 }, { fontSize: 26, bold: true, color: C.ink });
    bulletList(slide, ["Build a local, crop-specific AI dataset", "Work with nearby farms and agricultural partners", "Prove farmers will pay for yield insights"], 882, 298, 322, 18, C.ink, 72);
    pill(slide, "LOCAL CROP. LOCAL DATA. LOCAL PROOF.", 72, 578, 408, C.leaf, C.green);
    footer(slide, "First product: citrus yield intelligence.");
    addNotes(slide, ["Nueva Vizcaya's Perante orange focus makes this a practical local entry point.", "[Sources]", "- PROJECT_OVERVIEW.md (local crop focus)"]);
  }

  // 4. Problem
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.paper;
    header(slide, "Before harvest, farms are forced to estimate.", "The problem", 4);
    imagePlaceholder(slide, 750, 170, 458, 400, "Worker inspecting fruit tree", "Paste a real field-inspection photo");
    text(slide, "Farms need earlier answers to three costly questions.", { left: 72, top: 192, width: 600, height: 38 }, { fontSize: 24, color: C.gray });
    const qs = ["How much fruit can we expect?", "How many workers should we prepare?", "What volume can we commit to buyers?"];
    qs.forEach((q, i) => {
      const y = 276 + i * 92;
      shape(slide, "rect", { left: 72, top: y, width: 18, height: 54 }, i === 0 ? C.orange : C.green, { style: "solid", fill: "none", width: 0 });
      text(slide, q, { left: 116, top: y + 7, width: 550, height: 36 }, { fontSize: 24, bold: true, color: C.ink });
    });
    text(slide, "Manual counting is slow, inconsistent, and difficult across many trees.", { left: 72, top: 578, width: 600, height: 48 }, { fontSize: 20, color: C.gray });
    addNotes(slide, ["The issue is not that farmers lack information. They lack timely, consistent information at the scale needed for planning."]);
  }

  // 5. Solution
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.cream;
    header(slide, "A scan becomes a harvest estimate.", "The solution", 5);
    text(slide, "GrowKita sells a decision-ready report, not simply a drone flight.", { left: 72, top: 186, width: 920, height: 32 }, { fontSize: 24, color: C.gray });
    connector(slide, 306, 358, 70);
    connector(slide, 600, 358, 70);
    connector(slide, 894, 358, 70);
    addProcessNode(slide, 72, "Guided scan", "Scan the citrus\nfarm block", C.leaf);
    addProcessNode(slide, 366, "AI detection", "Detect visible\nfruit in images", C.orangeLight);
    addProcessNode(slide, 660, "Farm report", "Yield estimate\nand farm map", C.white);
    addProcessNode(slide, 954, "Better plan", "Harvest, labor,\npacking, and sales", C.green, C.white);
    footer(slide, "The early workflow is operated or supervised by GrowKita to protect data quality.");
    addNotes(slide, ["The product is a useful report and planning insight. The drone is how we collect consistent evidence."]);
  }

  // 6. Report
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.paper;
    header(slide, "A report a farm can act on.", "What the farm receives", 6);
    imagePlaceholder(slide, 72, 184, 610, 388, "Dashboard screenshot", "Paste your actual project dashboard or mockup");
    text(slide, "Clear outputs for a better harvest decision.", { left: 744, top: 194, width: 420, height: 64 }, { fontSize: 28, bold: true, color: C.ink });
    bulletList(slide, ["Estimated visible fruit count", "Map by farm block", "Areas needing a manual check", "Scan history for seasonal comparison"], 746, 294, 420, 20, C.ink, 62);
    pill(slide, "VISIBLE FRUIT-COUNT ESTIMATE", 744, 568, 310, C.orangeLight, C.orange);
    footer(slide, "Be precise: results are a visible fruit-count estimate, not a guaranteed total harvest.");
    addNotes(slide, ["Honesty builds trust: leaves and branches can hide fruit, so we use the phrase visible fruit-count estimate."]);
  }

  // 7. Revenue
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.cream;
    header(slide, "Start with a service. Grow into a platform.", "Business model", 7);
    const cols = [
      ["NOW", "Paid farm scan", "We operate or supervise\nthe scan and report."],
      ["NEXT", "Seasonal monitoring", "Repeat scans, history,\nand comparison reports."],
      ["LATER", "Managed on-site system", "Guided farm-staff scans\nwith software and support."],
    ];
    cols.forEach((c, i) => {
      const x = 72 + i * 378;
      const fill = i === 0 ? C.orangeLight : i === 1 ? C.leaf : C.white;
      shape(slide, "rect", { left: x, top: 206, width: 334, height: 260 }, fill, { style: "solid", fill: i === 0 ? C.orange : C.light, width: 1 }, "revenue-stage");
      text(slide, c[0], { left: x + 24, top: 232, width: 280, height: 20 }, { fontSize: 13, bold: true, color: i === 0 ? C.orange : C.green });
      text(slide, c[1], { left: x + 24, top: 280, width: 282, height: 58 }, { fontSize: 26, bold: true, color: C.ink });
      text(slide, c[2], { left: x + 24, top: 364, width: 282, height: 54 }, { fontSize: 17, color: C.gray });
    });
    text(slide, "Initial price tests", { left: 72, top: 524, width: 260, height: 26 }, { fontSize: 20, bold: true, color: C.ink });
    text(slide, "Pilot: PHP 1,500-3,000     |     Farm/block scan: PHP 5,000-15,000     |     Large/co-op/custom: PHP 20,000+", { left: 72, top: 560, width: 1100, height: 28 }, { fontSize: 18, color: C.gray });
    footer(slide, "Prices are hypotheses to validate against operating cost and customer willingness to pay.");
    addNotes(slide, ["We begin with paid results because that keeps quality under our control.", "Seasonal monitoring is the repeat-revenue goal."]);
  }

  // 8. Advantage
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.paper;
    header(slide, "Our advantage is the system, not the drone.", "Why we can win", 8);
    imagePlaceholder(slide, 72, 190, 330, 346, "Perante citrus or field test photo", "Use a real project or local farm image");
    shape(slide, "ellipse", { left: 692, top: 300, width: 210, height: 210 }, C.green, { style: "solid", fill: "none", width: 0 }, "center");
    text(slide, "LOCAL\nSYSTEM", { left: 720, top: 390, width: 154, height: 48 }, { fontSize: 25, bold: true, color: C.white, alignment: "center" });
    const labels = [
      ["Local data", 480, 224],
      ["AI model", 910, 224],
      ["Field workflow", 480, 528],
      ["Trusted partners", 910, 528],
    ];
    labels.forEach(([label, x, y]) => {
      shape(slide, "roundRect", { left: x, top: y, width: 200, height: 62 }, C.white, { style: "solid", fill: C.light, width: 1 }, "advantage").borderRadius = 10;
      text(slide, label, { left: x + 12, top: y + 19, width: 176, height: 24 }, { fontSize: 18, bold: true, color: C.ink, alignment: "center" });
    });
    text(slide, "Perante orange dataset, farm maps, repeat scan history, and the NVSU agricultural network create a local advantage.", { left: 430, top: 166, width: 750, height: 30 }, { fontSize: 18, color: C.gray, alignment: "center" });
    addNotes(slide, ["Anyone can buy a drone. The defensible asset is local data plus a repeatable workflow that produces useful reports."]);
  }

  // 9. Data flywheel
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.cream;
    header(slide, "Every permissioned scan improves the system.", "Data flywheel", 9);
    text(slide, "Customer trust turns data collection into a compounding product advantage.", { left: 72, top: 184, width: 970, height: 34 }, { fontSize: 24, color: C.gray });
    connector(slide, 264, 344, 66);
    connector(slide, 528, 344, 66);
    connector(slide, 792, 344, 66);
    addDataNode(slide, 72, 300, "More farm scans", "Real-world images\nand scan conditions", C.leaf);
    addDataNode(slide, 336, 300, "Trusted data", "Quality-checked data\nwith clear consent", C.orangeLight);
    addDataNode(slide, 600, 300, "Better citrus AI", "Improved detection\nand evaluation", C.white);
    addDataNode(slide, 864, 300, "Better reports", "More useful insight\nand repeat customers", C.green, C.white, "#DDEEDC");
    text(slide, "Farm-identifiable data stays protected. Any aggregate insight product requires clear consent.", { left: 156, top: 550, width: 968, height: 32 }, { fontSize: 19, color: C.gray, alignment: "center" });
    addNotes(slide, ["We do not build a business by reselling a farm's private records.", "With consent, data improves the AI. Later, aggregated and anonymized insights may serve co-ops, buyers, and agricultural organizations."]);
  }

  // 10. Growth
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.paper;
    header(slide, "Citrus first. Farm intelligence next.", "Growth path", 10);
    const stages = [
      ["1", "Prove paid citrus scans", "Nueva Vizcaya"],
      ["2", "Build seasonal monitoring", "Repeat reports"],
      ["3", "Enable guided farm-staff scans", "Software + support"],
      ["4", "Run paid pilots for the next crop", "Research + controlled environments"],
    ];
    shape(slide, "rect", { left: 140, top: 374, width: 1000, height: 5 }, C.light, { style: "solid", fill: "none", width: 0 });
    stages.forEach((s, i) => {
      const x = 140 + i * 310;
      shape(slide, "ellipse", { left: x, top: 340, width: 72, height: 72 }, i === 0 ? C.orange : C.green, { style: "solid", fill: "none", width: 0 });
      text(slide, s[0], { left: x, top: 360, width: 72, height: 24 }, { fontSize: 20, bold: true, color: C.white, alignment: "center" });
      text(slide, s[1], { left: x - 56, top: 240, width: 184, height: 74 }, { fontSize: 20, bold: true, color: C.ink, alignment: "center" });
      text(slide, s[2], { left: x - 62, top: 434, width: 196, height: 38 }, { fontSize: 15, color: C.gray, alignment: "center" });
    });
    pill(slide, "DO NOT BUILD EVERY CROP SOLUTION AT ONCE", 336, 570, 608, C.orangeLight, C.orange);
    footer(slide, "Expand only after the first use case is paid and repeatable.");
    addNotes(slide, ["The platform is scalable because the workflow repeats, but we expand only after the first market is working."]);
  }

  // 11. Future applications
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.cream;
    header(slide, "One monitoring platform. More farm applications.", "Future applications", 11);
    text(slide, "Citrus is the first product. These are adjacent use cases to validate through paid pilots.", { left: 72, top: 184, width: 990, height: 34 }, { fontSize: 23, color: C.gray });
    const applications = [
      ["HYDROPONICS", "Hydroponic tower image", "Repeat plant observations\nand growth tracking"],
      ["TREES AND CROPS", "Tree or crop-field image", "Inventory, canopy change,\nand targeted field checks"],
      ["ANIMAL FACILITIES", "Poultry or livestock-facility image", "Monitor zones and operations,\nsubject to welfare validation"],
    ];
    applications.forEach((app, i) => {
      const x = 72 + i * 382;
      imagePlaceholder(slide, x, 264, 334, 194, app[1], "Paste a relevant real photo");
      text(slide, app[0], { left: x, top: 492, width: 334, height: 24 }, { fontSize: 17, bold: true, color: i === 0 ? C.orange : C.green, alignment: "center" });
      text(slide, app[2], { left: x + 18, top: 530, width: 298, height: 46 }, { fontSize: 17, color: C.ink, alignment: "center" });
    });
    pill(slide, "FUTURE PILOTS, VALIDATED WITH CUSTOMERS", 380, 622, 520, C.leaf, C.green);
    footer(slide, "The shared workflow: observe, organize data, analyze with AI, and return a useful decision.");
    addNotes(slide, ["These are future applications, not current features.", "Each one must earn its place through a paid pilot and appropriate welfare, safety, and biosecurity validation."]);
  }

  // 12. Ask
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.dark;
    imagePlaceholder(slide, 760, 0, 520, 720, "Team and prototype photo", "Paste a real field-test or team photo");
    shape(slide, "rect", { left: 0, top: 0, width: 800, height: H }, C.dark);
    text(slide, "Our next step: prove value with local farms.", { left: 72, top: 112, width: 590, height: 116 }, { fontSize: 44, bold: true, color: C.white });
    rule(slide, 72, 256, 74, C.orange, 6);
    text(slide, "We are seeking", { left: 72, top: 304, width: 280, height: 26 }, { fontSize: 19, bold: true, color: "#B9D5C5" });
    bulletList(slide, ["Pilot citrus farms or cooperatives", "Agricultural mentors and validation partners", "Support for field testing, data collection, and model improvement"], 72, 350, 596, 20, C.white, 64);
    text(slide, "SUCCESS = A farm uses our report to make a better harvest decision and pays to use it again.", { left: 72, top: 575, width: 590, height: 64 }, { fontSize: 20, bold: true, color: "#F7D6A9" });
    addNotes(slide, ["We are asking for a chance to prove a useful local product with measurable farm value."]);
  }

  // 13. Closing
  {
    const slide = presentation.slides.add();
    slide.background.fill = C.dark;
    shape(slide, "rect", { left: 0, top: 0, width: W, height: H }, C.dark);
    imagePlaceholder(slide, 0, 0, 1280, 720, "Closing background photo", "Paste a real citrus-farm sunrise or team field-test image");
    shape(slide, "rect", { left: 0, top: 0, width: W, height: H }, "#0C2C20/96", { style: "solid", fill: "none", width: 0 });
    rule(slide, 510, 182, 260, C.orange, 6);
    text(slide, "The future of farming\nwill not be guessed.\nIt will be measured.", { left: 250, top: 250, width: 780, height: 210 }, { fontSize: 46, bold: true, color: C.white, alignment: "center" });
    text(slide, "GROWKITA", { left: 450, top: 520, width: 380, height: 24 }, { fontSize: 17, bold: true, color: "#B9D5C5", alignment: "center" });
    text(slide, "AI-powered farm intelligence, starting in Nueva Vizcaya.", { left: 250, top: 560, width: 780, height: 26 }, { fontSize: 18, color: C.white, alignment: "center" });
    addNotes(slide, ["This is an original GrowKita closing statement.", "End on the mission: local data, AI, and practical automation for better farm decisions."]);
  }

  for (const [index, slide] of presentation.slides.items.entries()) {
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    await writeBlob(`${BUILD}/slide-${String(index + 1).padStart(2, "0")}.png`, png);
    const layout = await slide.export({ format: "layout" });
    await fs.writeFile(`${BUILD}/slide-${String(index + 1).padStart(2, "0")}.layout.json`, await layout.text());
  }
  const montage = await presentation.export({ format: "webp", montage: true, scale: 1 });
  await writeBlob(`${BUILD}/deck-montage.webp`, montage);
  const deck = await PresentationFile.exportPptx(presentation);
  await deck.save(OUT);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
