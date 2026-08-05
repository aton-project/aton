from knowledge_model import KnowledgeModel


def verify(model: KnowledgeModel) -> None:
    """
    Verify the loaded Foundation.

    Raises RuntimeError if verification fails.
    """

    ids = set()

    for artifact in model.artifacts:

        if artifact.id in ids:
            raise RuntimeError(
                f"Duplicate artifact id: {artifact.id}"
            )

        ids.add(artifact.id)
