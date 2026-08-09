from model import Artifact


class ArtifactRepository:
    """
    Provides access to artifacts contained in a KnowledgeModel.
    """

    def __init__(self, artifacts: list[Artifact]) -> None:
        self._artifacts = artifacts

    def all(self) -> list[Artifact]:
        return self._artifacts

    def artifact(self, artifact_id: str) -> Artifact | None:
        for artifact in self._artifacts:
            if artifact.id == artifact_id:
                return artifact
        return None

    def by_type(self, artifact_type: str) -> list[Artifact]:
        return [
            artifact
            for artifact in self._artifacts
            if artifact.type == artifact_type
        ]

    def predicates(self) -> list[Artifact]:
        return [
            artifact
            for artifact in self._artifacts
            if artifact.metadata.get("entityType") == "predicate"
        ]

    def predicate(self, predicate_id: str) -> Artifact | None:
        for artifact in self.predicates():
            if artifact.id == predicate_id:
                return artifact
        return None

    def ontology_concepts(self) -> list[Artifact]:
        return [
            artifact
            for artifact in self._artifacts
            if artifact.metadata.get("entityType") == "ontology"
        ]

    def ontology_concept(self, concept_id: str) -> Artifact | None:
        for artifact in self.ontology_concepts():
            if artifact.id == concept_id:
                return artifact
        return None
