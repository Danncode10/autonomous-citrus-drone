import fs from "node:fs/promises";
import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const source = "/Users/lesterdannlopez/Desktop/Shared_VM_Folder/Advance Robotics/Automated Citrus Drone/Sabatan/GrowKita_Business_Pitch_Template_RECOVERED_0838.pptx";
const output = "/Users/lesterdannlopez/Desktop/Shared_VM_Folder/Advance Robotics/Automated Citrus Drone/Sabatan/GrowKita_Business_Pitch_Template_RECOVERY_CANDIDATE.pptx";
const build = "/Users/lesterdannlopez/Desktop/Shared_VM_Folder/Advance Robotics/Automated Citrus Drone/Sabatan/.growkita-ppt.U84av8";

async function rewriteText(presentation, slide, changes) {
  const layout = JSON.parse(await (await slide.export({ format: "layout" })).text());
  const matched = new Set();
  for (const element of layout.elements ?? []) {
    if (!Object.hasOwn(changes, element.text)) continue;
    const target = presentation.resolve(element.aid);
    target.text = changes[element.text];
    matched.add(element.text);
  }
  const missing = Object.keys(changes).filter((key) => !matched.has(key));
  if (missing.length) throw new Error(`Could not find expected slide-10 text: ${missing.join(" | ")}`);
}

async function writeBlob(path, blob) {
  await fs.writeFile(path, new Uint8Array(await blob.arrayBuffer()));
}

async function main() {
  const presentation = await PresentationFile.importPptx(await FileBlob.load(source));
  const sourceSlide = presentation.slides.getItem(9);
  const futureSlide = sourceSlide.duplicate();
  futureSlide.moveTo(10);

  await rewriteText(presentation, futureSlide, {
    "GROWTH PATH": "FUTURE APPLICATIONS",
    "Citrus first. Farm intelligence next.": "One monitoring platform. More farm applications.",
    "GROWKITA  |  10": "GROWKITA  |  11",
    "Prove paid citrus scans": "Hydroponic monitoring",
    "Build seasonal monitoring": "Trees and crops",
    "Enable guided farm-staff scans": "Animal facilities",
    "Run paid pilots for the next crop": "Research and controlled systems",
    "Nueva Vizcaya": "Growth tracking",
    "Repeat reports": "Inventory and canopy",
    "Software + support": "Zones and operations",
    "Research + controlled environments": "Repeatable plant data",
    "DO NOT BUILD EVERY CROP SOLUTION AT ONCE": "FUTURE PILOTS, VALIDATED WITH CUSTOMERS",
    "Expand only after the first use case is paid and repeatable.": "Each use case must earn its place through a paid pilot."
  });
  futureSlide.speakerNotes.textFrame.setText([
    "These are future applications, not current features.",
    "The shared workflow is observation, organized data, AI analysis, and a useful decision.",
    "Animal-facility use requires welfare, safety, and biosecurity validation."
  ]);
  futureSlide.speakerNotes.setVisible(true);

  const preview = await presentation.export({ slide: futureSlide, format: "png", scale: 1 });
  await writeBlob(`${build}/recovery-slide-11.png`, preview);
  const layout = await futureSlide.export({ format: "layout" });
  await fs.writeFile(`${build}/recovery-slide-11.layout.json`, await layout.text());
  const montage = await presentation.export({ format: "webp", montage: true, scale: 1 });
  await writeBlob(`${build}/recovery-candidate-montage.webp`, montage);
  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(output);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
