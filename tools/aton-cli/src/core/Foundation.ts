import { join } from "node:path";

export class Foundation {

  constructor(
    private readonly root: string
  ) {}

  public path(): string {
    return join(this.root, "foundation");
  }

}
