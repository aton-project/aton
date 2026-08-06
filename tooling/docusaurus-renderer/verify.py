from knowledge_model import KnowledgeModel


def verify(model: KnowledgeModel) -> None:
    """
    Verify the loaded Foundation.

    Raises RuntimeError if verification fails.
    """

    verify_duplicate_artifact_ids(
        model,
        report,
    )

def verify_duplicate_artifact_ids(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:

    seen: set[str] = set()

    for artifact in model.repository.all():

        if artifact.id in seen:
            report.error(
                artifact,
                f"Duplicate artifact ID '{artifact.id}'."
            )
        else:
            seen.add(artifact.id)
