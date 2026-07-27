import { DoctorService } from "../services/DoctorService.js";

export function doctor() {

  const report = new DoctorService().run();

  console.log();
  console.log("ATON Doctor");
  console.log("────────────────────────────────");

  console.log();
  console.log("Workspace");
  console.log("────────────────────────────────");

  console.log(`Name       ${report.workspace.name}`);
  console.log(`Schema     ${report.workspace.schema}`);
  console.log(`Renderer   ${report.workspace.renderer}`);

  console.log();
  console.log("Tools");
  console.log("────────────────────────────────");

  for (const tool of report.tools) {

    if (tool.installed) {
      console.log(`✔ ${tool.name.padEnd(18)} ${tool.version}`);
    } else {
      console.log(`✘ ${tool.name.padEnd(18)} not found`);
    }

  }

  console.log();

  console.log("Project");
  console.log("────────────────────────────────");

  console.log(
    `${report.project.gitRepository ? "✔" : "✘"} Git Repository`
  );

  console.log(
    `${report.project.foundation ? "✔" : "✘"} foundation/`
  );

  console.log(
    `${report.project.book ? "✔" : "✘"} book/`
  );

  console.log(
    `${report.project.tools ? "✔" : "✘"} tools/`
  );

  console.log();
  
}
