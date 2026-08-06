from dataclasses import dataclass, field

from model import Artifact
from artifact_repository import ArtifactRepository


@dataclass(slots=True)
class KnowledgeModel:

    artifacts: list[Artifact] = field(default_factory=list)

    repository: ArtifactRepository | None = None
