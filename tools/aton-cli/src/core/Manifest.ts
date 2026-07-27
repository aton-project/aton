import { readFileSync } from "node:fs";
import { join } from "node:path";

import { parse } from "yaml";

import type { ManifestData } from "../types/ManifestData.js";

export class Manifest {

  private readonly data: ManifestData;

  constructor(root: string) {

    const file = readFileSync(
      join(root, "aton.yaml"),
      "utf8"
    );

    this.data = parse(file) as ManifestData;

  }

  public schema(): string {
    return this.data.schema;
  }

  public name(): string {
    return this.data.workspace.name;
  }

  public defaultRenderer(): string {
    return this.data.renderer.default;
  }

}
