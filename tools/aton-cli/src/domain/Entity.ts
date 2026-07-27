import { EntityId } from "./EntityId.js";
import { EntityType } from "./EntityType.js";
import type { Metadata } from "./Metadata.js";
import type { Relation } from "./Relation.js";

export interface Entity {

  id: EntityId;

  type: EntityType;

  metadata: Metadata;

  content: string;

  relations: Relation[];

}
