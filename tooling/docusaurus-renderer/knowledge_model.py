from dataclasses import dataclass, field

from model import Artifact


@dataclass(slots=True)
class KnowledgeModel:
    """
    Runtime representation of the loaded ATON Foundation.
    """

    artifacts: list[Artifact] = field(default_factory=list)
