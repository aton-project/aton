import { existsSync } from "node:fs";
import { dirname, join } from "node:path";

export class ProjectLocator {

  public static findRoot(start: string = process.cwd()): string | null {

    let current = start;

    while (true) {

      if (existsSync(join(current, "aton.yaml"))) {
        return current;
      }

      if (existsSync(join(current, ".git"))) {
        return current;
      }

      const parent = dirname(current);

      if (parent === current) {
        return null;
      }

      current = parent;

    }

  }

}
