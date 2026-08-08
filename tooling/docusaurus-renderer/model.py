from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Relation:
    """
    Canonical internal representation of a Foundation relation.
    """

    type: str
    target: str


@dataclass(slots=True)
class Artifact:
    """
    A Foundation artifact loaded from the repository.
    """

    # Basic identity
    id: str
    type: str
    title: str
    status: str

    # Repository location
    source_dir: Path
    content_file: Path
    metadata_file: Path
    relations_file: Path | None = None

    # Artifact content
    content: str = ""

    # Parsed metadata
    metadata: dict[str, Any] = field(default_factory=dict)

    # Parsed relations
    relations: list[Relation] = field(default_factory=list)

    def __str__(self) -> str:
        return f"{self.id} ({self.type})"

    @property
    def filename(self) -> str:
        return f"{self.id}.md"
