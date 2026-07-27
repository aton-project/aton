import { existsSync } from "node:fs";
import { join } from "node:path";

import { ProjectLocator } from "./ProjectLocator.js";
import { Manifest } from "./Manifest.js";
import { Foundation } from "./Foundation.js";

export class Workspace {

  private readonly manifestModel: Manifest;
  private readonly foundationModel: Foundation;

  private constructor(
    private readonly root: string
  ) {
    this.manifestModel = new Manifest(this.root);
    this.foundationModel = new Foundation(this.root);
  }

  public static open(): Workspace {

    const root = ProjectLocator.findRoot();

    if (!root) {
      throw new Error("No ATON workspace found.");
    }

    return new Workspace(root);

  }

  public getRoot(): string {
    return this.root;
  }

  public manifest(): Manifest {
    return this.manifestModel;
  }

  public hasManifest(): boolean {
    return existsSync(join(this.root, "aton.yaml"));
  }

  public hasGitRepository(): boolean {
    return existsSync(join(this.root, ".git"));
  }

  public foundation(): Foundation {
    return this.foundationModel;
  }

  public hasFoundation(): boolean {
    return existsSync(join(this.root, "foundation"));
  }

  public hasBook(): boolean {
    return existsSync(join(this.root, "book"));
  }

  public hasTools(): boolean {
    return existsSync(join(this.root, "tools"));
  }
}
