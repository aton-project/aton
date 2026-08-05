from pathlib import Path

import yaml

from knowledge_model import KnowledgeModel
from model import Artifact

ROOT = Path(__file__).resolve().parents[2]

FOUNDATION = ROOT / "foundation"


def determine_type(relative_path: Path) -> str:
    """
    Determine the artifact type from the repository path.

    Examples:
        constitution/CONSTITUTION              -> constitution
        specifications/rfc/RFC-0001           -> rfc
        specifications/adr/ADR-0001           -> adr
        specifications/ax/AX-0001             -> ax
        specifications/glossary/TERM-0001     -> glossary
    """

    parts = relative_path.parts

    if "specifications" in parts:
        i = parts.index("specifications")
        return parts[i + 1].lower()

    return parts[0].lower()


def load_artifact(metadata_file: Path) -> Artifact | None:

    artifact_dir = metadata_file.parent

    content_file = artifact_dir / "content.md"

    if not content_file.is_file():
        print(f"WARNING: Missing content.md: {artifact_dir}")
        return None

    relations_file = artifact_dir / "relations.yaml"

    metadata = yaml.safe_load(
        metadata_file.read_text(encoding="utf-8")
    ) or {}

    relations = []

    if relations_file.exists():
        try:
            relations = yaml.safe_load(
                relations_file.read_text(encoding="utf-8")
            ) or []
        except Exception as e:
            print(f"WARNING: Invalid relations file: {relations_file}")
            print(f"         {e}")

    relative = artifact_dir.relative_to(FOUNDATION)

    return Artifact(
        id=metadata.get("id", artifact_dir.name),
        type=determine_type(relative),
        title=metadata.get("title", ""),
        status=metadata.get("status", ""),
        source_dir=artifact_dir,
        content_file=content_file,
        metadata_file=metadata_file,
        relations_file=relations_file if relations_file.exists() else None,
        content=content_file.read_text(encoding="utf-8"),
        metadata=metadata,
        relations=relations,
    )


def load_foundation() -> KnowledgeModel:

    artifacts: list[Artifact] = []

    for metadata_file in sorted(FOUNDATION.rglob("metadata.yaml")):

        artifact = load_artifact(metadata_file)

        if artifact:
            artifacts.append(artifact)

    artifacts.sort(key=lambda a: a.id)

    return KnowledgeModel(
        artifacts=artifacts
    )

