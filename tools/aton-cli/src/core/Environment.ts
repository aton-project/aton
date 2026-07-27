import { existsSync } from "node:fs";

export class Environment {

  public static isGitRepository(): boolean {
    return existsSync(".git");
  }

  public static hasFoundation(): boolean {
    return existsSync("foundation");
  }

  public static hasBook(): boolean {
    return existsSync("book");
  }

  public static hasTools(): boolean {
    return existsSync("tools");
  }

}
