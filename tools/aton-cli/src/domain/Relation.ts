import { EntityId } from "./EntityId.js";

export interface Relation {

  type: string;

  target: EntityId;

}
