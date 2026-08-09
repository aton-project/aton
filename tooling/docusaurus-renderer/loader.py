from pathlib import Path
from typing import Any

import yaml

from artifact_repository import ArtifactRepository
from knowledge_model import KnowledgeModel
from model import AllowedPair, Artifact, Relation


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
        index = parts.index("specifications")

        if index + 1 < len(parts):
            return parts[index + 1].lower()

    return parts[0].lower() if parts else ""


def parse_relations(data: Any, relations_file: Path) -> list[Relation]:
    """
    Normalize all supported Foundation relation serialization formats into
    the canonical internal representation:

        list[Relation]

    Supported formats:

    1. Legacy list format:

        - type: refines
          target: AX-0001

    2. Mapping format:

        references:
          - RFC-0001

        dependsOn:
          - ADR-0003

    3. Embedded relation object format:

        relations:
          - type: refines
            target: AX-0001

    An empty relation set may be represented as:

        []

    or:

        relations: []
    """

    result: list[Relation] = []

    if data is None:
        return result

    # ------------------------------------------------------------
    # Legacy list format
    # ------------------------------------------------------------

    if isinstance(data, list):

        for entry in data:

            if not isinstance(entry, dict):
                print(
                    f"WARNING: Invalid relation entry in: "
                    f"{relations_file}"
                )
                continue

            relation_type = entry.get("type")
            target = entry.get("target")

            if not isinstance(relation_type, str):
                print(
                    f"WARNING: Relation without valid type in: "
                    f"{relations_file}"
                )
                continue

            if not isinstance(target, str):
                print(
                    f"WARNING: Relation without valid target in: "
                    f"{relations_file}"
                )
                continue

            result.append(
                Relation(
                    type=relation_type,
                    target=target,
                )
            )

        return result

    # ------------------------------------------------------------
    # Mapping format
    # ------------------------------------------------------------

    if isinstance(data, dict):

        # Embedded relation object format:
        #
        # relations:
        #   - type: refines
        #     target: AX-0001

        if "relations" in data:

            embedded = data.get("relations")

            if embedded is None:
                return result

            if not isinstance(embedded, list):
                print(
                    f"WARNING: 'relations' must be a list in: "
                    f"{relations_file}"
                )
                return result

            return parse_relations(
                embedded,
                relations_file,
            )

        # Mapping format:
        #
        # references:
        #   - RFC-0001
        #
        # dependsOn:
        #   - ADR-0003

        for relation_type, targets in data.items():

            if not isinstance(relation_type, str):
                print(
                    f"WARNING: Invalid relation type in: "
                    f"{relations_file}"
                )
                continue

            if targets is None:
                continue

            if not isinstance(targets, list):
                print(
                    f"WARNING: Relation targets for "
                    f"'{relation_type}' must be a list in: "
                    f"{relations_file}"
                )
                continue

            for target in targets:

                if not isinstance(target, str):
                    print(
                        f"WARNING: Invalid relation target for "
                        f"'{relation_type}' in: "
                        f"{relations_file}"
                    )
                    continue

                result.append(
                    Relation(
                        type=relation_type,
                        target=target,
                    )
                )

        return result

    # ------------------------------------------------------------
    # Unsupported format
    # ------------------------------------------------------------

    print(
        f"WARNING: Unsupported relations format in: "
        f"{relations_file}"
    )

    return result


def parse_allowed_pairs(
    data: Any,
    constraints_file: Path,
) -> list[AllowedPair]:
    """
    Parse the canonical semantic constraint representation.

    Expected format:

        allowedPairs:
          - source: Note
            target: ADR
    """
    result: list[AllowedPair] = []

    if data is None:
        return result

    if not isinstance(data, dict):
        print(
            f"WARNING: Invalid constraints format in: "
            f"{constraints_file}"
        )
        return result

    allowed_pairs = data.get("allowedPairs", [])

    if not isinstance(allowed_pairs, list):
        print(
            f"WARNING: 'allowedPairs' must be a list in: "
            f"{constraints_file}"
        )
        return result

    for entry in allowed_pairs:
        if not isinstance(entry, dict):
            print(
                f"WARNING: Invalid allowed pair in: "
                f"{constraints_file}"
            )
            continue

        source = entry.get("source")
        target = entry.get("target")

        if not isinstance(source, str):
            print(
                f"WARNING: Allowed pair without valid source in: "
                f"{constraints_file}"
            )
            continue

        if not isinstance(target, str):
            print(
                f"WARNING: Allowed pair without valid target in: "
                f"{constraints_file}"
            )
            continue

        result.append(
            AllowedPair(
                source=source,
                target=target,
            )
        )

    return result


def load_artifact(metadata_file: Path) -> Artifact | None:

    artifact_dir = metadata_file.parent

    content_file = artifact_dir / "content.md"

    if not content_file.is_file():
        print(
            f"WARNING: Missing content.md: {artifact_dir}"
        )
        return None

    relations_file = artifact_dir / "relations.yaml"

    metadata = yaml.safe_load(
        metadata_file.read_text(encoding="utf-8")
    ) or {}

    if not isinstance(metadata, dict):
        print(
            f"WARNING: Invalid metadata format: "
            f"{metadata_file}"
        )
        return None

    relations: list[Relation] = []

    if relations_file.is_file():

        try:
            raw_relations = yaml.safe_load(
                relations_file.read_text(encoding="utf-8")
            )

            relations = parse_relations(
                raw_relations,
                relations_file,
            )

        except Exception as exc:
            print(
                f"WARNING: Invalid relations file: "
                f"{relations_file}"
            )
            print(f"         {exc}")

    relative = artifact_dir.relative_to(FOUNDATION)

    constraints_file = artifact_dir / "constraints.yaml"

    allowed_pairs: list[AllowedPair] = []

    if constraints_file.is_file():
        try:
            raw_constraints = yaml.safe_load(
                constraints_file.read_text(encoding="utf-8")
            )

            allowed_pairs = parse_allowed_pairs(
                raw_constraints,
                constraints_file,
            )

        except Exception as exc:
            print(
                f"WARNING: Invalid constraints file: "
                f"{constraints_file}"
            )
            print(f"         {exc}")


    return Artifact(
        id=metadata.get(
            "id",



            artifact_dir.name,
        ),
        type=determine_type(relative),
        ontology_type=metadata.get(
            "ontologyType",
        ),
        title=metadata.get(
            "title",
            "",
        ),
        status=metadata.get(
            "status",
            "",
        ),
        source_dir=artifact_dir,
        content_file=content_file,
        metadata_file=metadata_file,
        relations_file=(
            relations_file
            if relations_file.is_file()
            else None
        ),
        constraints_file=(
            constraints_file
            if constraints_file.is_file()
            else None
        ),
        content=content_file.read_text(
            encoding="utf-8"
        ),
        metadata=metadata,
        relations=relations,
        allowed_pairs=allowed_pairs,
    )


def load_foundation() -> KnowledgeModel:

    artifacts: list[Artifact] = []

    for metadata_file in sorted(
        FOUNDATION.rglob("metadata.yaml")
    ):

        artifact = load_artifact(
            metadata_file
        )

        if artifact:
            artifacts.append(artifact)

    artifacts.sort(
        key=lambda artifact: artifact.id
    )

    model = KnowledgeModel(
        artifacts=artifacts,
    )

    model.repository = ArtifactRepository(
        model.artifacts
    )

    return model
