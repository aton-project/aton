import { execSync } from "node:child_process";
import { DoctorReport, ToolStatus } from "../types/DoctorReport.js";
import { Workspace } from "../core/Workspace.js";

export class DoctorService {

  private check(name: string, command: string): ToolStatus {

    try {

      const version = execSync(command, {
        encoding: "utf8",
        stdio: ["ignore", "pipe", "ignore"],
      }).trim();

      return {
        name,
        installed: true,
        version,
      };

    } catch {

      return {
        name,
        installed: false,
      };

    }

  }

  public run(): DoctorReport {

    const workspace = Workspace.open();
    const manifest = workspace.manifest();

    return {

      tools: [

        this.check("Git", "git --version"),
        this.check("Node.js", "node --version"),
        this.check("npm", "npm --version"),
        this.check("Docker", "docker --version"),
        this.check("Docker Compose", "docker compose version"),

      ],

      workspace: {

        name: manifest.name(),
        schema: manifest.schema(),
        renderer: manifest.defaultRenderer(),

      },

      project: {

          gitRepository: workspace.hasGitRepository(),
          foundation: workspace.hasFoundation(),
          book: workspace.hasBook(),
          tools: workspace.hasTools(),

      },

    };

  }

}
