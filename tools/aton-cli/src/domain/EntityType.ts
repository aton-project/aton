export class EntityType {

  constructor(
    private readonly value: string
  ) {}

  public toString(): string {
    return this.value;
  }

}
