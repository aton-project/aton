from knowledge_model import KnowledgeModel
from verification_report import VerificationReport

def verify(model: KnowledgeModel) -> VerificationReport:
    """
    Verify the loaded Foundation.

    Raises RuntimeError if verification fails.
    """

    report = VerificationReport()

    for artifact in model.repository.all():
        print(artifact.id)
        print(type(artifact.relations))
        print(artifact.relations)
        break

    verify_duplicate_artifact_ids(model, report)
    verify_missing_content(model, report)
    verify_missing_title(model, report)
    verify_unknown_relation_targets(model, report)
    verify_duplicate_relations(model, report)
    verify_self_references(model, report)

    return report


def verify_duplicate_artifact_ids(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that all artifact IDs are unique.
    """

    print("Verifying duplicate artifact IDs...")

    seen: set[str] = set()

    for artifact in model.repository.all():

        if artifact.id in seen:
            report.error(
                artifact,
                f"Duplicate artifact ID '{artifact.id}'.",
            )
        else:
            seen.add(artifact.id)


def verify_missing_content(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that all artifacts contain content.
    """

    print("Verifying missing content...")

    for artifact in model.repository.all():

        if not artifact.content or not artifact.content.strip():
            report.error(
                artifact,
                "Artifact has no content.",
            )


def verify_missing_title(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that all artifacts have a title.
    """

    print("Verifying missing title...")

    for artifact in model.repository.all():

        if not artifact.title or not artifact.title.strip():
            report.error(
                artifact,
                "Artifact has no title.",
            )


def verify_unknown_relation_targets(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that all relation targets reference existing artifacts.
    """

    print("Verifying unknown relation targets...")

    for artifact in model.repository.all():

        for relation_type, targets in artifact.relations.items():

            for target in targets:

                if model.repository.artifact(target) is None:
                    report.error(
                        artifact,
                        f"Unknown relation target '{target}'.",
                    )


def verify_duplicate_relations(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that an artifact does not contain duplicate relations.
    """

    print("Verifying duplicate relations...")

    for artifact in model.repository.all():

        seen: set[tuple[str, str]] = set()

        for relation_type, targets in artifact.relations.items():

            for target in targets:

                key = (relation_type, target)

                if key in seen:
                    report.error(
                        artifact,
                        f"Duplicate relation '{relation_type}' to '{target}'.",
                    )
                else:
                    seen.add(key)


def verify_self_references(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that artifacts do not reference themselves.
    """

    print("Verifying self references...")

    for artifact in model.repository.all():

        for relation_type, targets in artifact.relations.items():

            for target in targets:

                if target == artifact.id:
                    report.error(
                        artifact,
                        f"Self reference detected via relation "
                        f"'{relation_type}' to '{target}'.",
                    )
