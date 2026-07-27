import { join } from "node:path";
import { EntityRepository } from "../repository/EntityRepository.js";

export class Foundation {

  private readonly repository = new EntityRepository();

  constructor(
    private readonly root: string
  ) {}

  public path(): string {
    return join(this.root, "foundation");
  }

  public repository(): EntityRepository {
    return this.repository;
  }

}
