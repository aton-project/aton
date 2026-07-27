import type { Entity } from "../domain/Entity.js";

export class EntityRepository {

  private readonly entities: Entity[] = [];

  public add(entity: Entity): void {
    this.entities.push(entity);
  }

  public findAll(): Entity[] {
    return this.entities;
  }

  public size(): number {
    return this.entities.length;
  }

}
