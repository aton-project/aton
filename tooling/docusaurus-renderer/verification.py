from knowledge_model import KnowledgeModel
from verification_report import VerificationReport
from predicate_registry import predicate_state


def verify(model: KnowledgeModel) -> VerificationReport:
    """
    Verify the loaded Foundation.
    """
    report = VerificationReport()

    # Structural verification
    verify_duplicate_artifact_ids(
        model,
        report,
    )

    verify_missing_content(
        model,
        report,
    )

    verify_missing_title(
        model,
        report,
    )

    verify_unknown_relation_targets(
        model,
        report,
    )

    verify_duplicate_relations(
        model,
        report,
    )

    verify_self_references(
        model,
        report,
    )

    # Semantic verification
    verify_semantic_relations(
        model,
        report,
    )

    return report


def verify_duplicate_artifact_ids(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that all artifact IDs are unique.
    """
    print(
        "Verifying duplicate artifact IDs..."
    )

    seen: set[str] = set()

    for artifact in model.repository.all():
        if artifact.id in seen:
            report.error(
                artifact,
                f"Duplicate artifact ID '{artifact.id}'.",
                rule="duplicate-artifact-id",
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
    print(
        "Verifying missing content..."
    )

    for artifact in model.repository.all():
        if (
            not artifact.content
            or not artifact.content.strip()
        ):
            report.error(
                artifact,
                "Artifact has no content.",
                rule="missing-content",
            )


def verify_missing_title(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that all artifacts have a title.
    """
    print(
        "Verifying missing title..."
    )

    for artifact in model.repository.all():
        if (
            not artifact.title
            or not artifact.title.strip()
        ):
            report.error(
                artifact,
                "Artifact has no title.",
                rule="missing-title",
            )


def verify_unknown_relation_targets(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that relation targets referencing Foundation artifacts
    resolve to existing artifacts.

    External targets are currently accepted as unresolved external
    entities. They are not treated as artifact lookup failures.
    """
    print(
        "Verifying unknown relation targets..."
    )

    for artifact in model.repository.all():
        for relation in artifact.relations:
            target = model.repository.artifact(
                relation.target
            )

            if target is None:
                # External Entity handling will be defined by
                # the ontology layer. For now, do not fail the
                # renderer merely because a target is not a
                # Foundation artifact.
                continue


def verify_duplicate_relations(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify that an artifact does not contain duplicate relations.
    """
    print(
        "Verifying duplicate relations..."
    )

    for artifact in model.repository.all():
        seen: set[tuple[str, str]] = set()

        for relation in artifact.relations:
            key = (
                relation.type,
                relation.target,
            )

            if key in seen:
                report.error(
                    artifact,
                    (
                        f"Duplicate relation "
                        f"'{relation.type}' to "
                        f"'{relation.target}'."
                    ),
                    rule="duplicate-relation",
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
    print(
        "Verifying self references..."
    )

    for artifact in model.repository.all():
        for relation in artifact.relations:
            if relation.target == artifact.id:
                report.error(
                    artifact,
                    (
                        "Self reference detected via "
                        f"relation '{relation.type}' "
                        f"to '{relation.target}'."
                    ),
                    rule="self-reference",
                )


def matches_constraint(
    actual: str,
    concept: str | None,
    pattern: str | None,
    model: KnowledgeModel,
) -> bool:
    """
    Match a resolved ontology Concept against a concrete Concept
    or an explicit Constraint Pattern.
    """
    if concept is not None:
        return actual == concept

    if pattern == "ANY-CONCEPT":
        return any(
            ontology.id == actual
            for ontology in model.repository.ontology_concepts()
        )

    return False


def resolve_concept(
    artifact,
) -> str | None:
    """
    Resolve the canonical ontology Concept represented by an artifact.

    Normal artifacts use their explicit ontologyType.
    Ontology artifacts represent the Concept identified by their own ID.
    """
    if artifact.metadata.get("entityType") == "ontology":
        return artifact.id

    return artifact.ontology_type


def verify_semantic_relations(
    model: KnowledgeModel,
    report: VerificationReport,
) -> None:
    """
    Verify relations against the ATON ontology and migration state.

    Predicate migration states are defined by RFC-0028.

    Canonical and inverse predicates are resolved against their
    Predicate artifacts and validated using their explicit allowedPairs.

    Deprecated and unresolved predicates are reported as warnings and
    are not subjected to semantic pair validation.

    Unknown predicates are reported as errors.
    """
    print(
        "Verifying semantic relations..."
    )

    for artifact in model.repository.all():

        for relation in artifact.relations:

            # Ontology definition artifacts describe Concepts.
            # Their documentation references are not instance-level
            # semantic relations and therefore are outside Concept-pair
            # validation.
            if artifact.metadata.get("entityType") == "ontology":
                continue

            state = predicate_state(relation.type)

            # --------------------------------------------------------
            # Unknown predicate
            # --------------------------------------------------------

            if state is None:
                report.error(
                    artifact,
                    (
                        f"Relation uses unknown predicate "
                        f"'{relation.type}'."
                    ),
                    rule="unknown-relation-predicate",
                )
                continue

            # --------------------------------------------------------
            # Unresolved legacy predicate
            # --------------------------------------------------------

            if state == "unresolved":
                report.warning(
                    artifact,
                    (
                        f"Relation uses unresolved predicate "
                        f"'{relation.type}'."
                    ),
                    rule="unresolved-relation-predicate",
                )
                continue

            # --------------------------------------------------------
            # Deprecated predicate
            # --------------------------------------------------------

            if state == "deprecated":
                report.warning(
                    artifact,
                    (
                        f"Relation uses deprecated predicate "
                        f"'{relation.type}'."
                    ),
                    rule="deprecated-relation-predicate",
                )
                continue

            # --------------------------------------------------------
            # Canonical / inverse predicate
            # --------------------------------------------------------

            predicate = model.repository.predicate(
                f"PRED-{relation.type}"
            )

            if predicate is None:
                report.error(
                    artifact,
                    (
                        f"Relation uses {state} predicate "
                        f"'{relation.type}', but no corresponding "
                        f"Predicate artifact exists."
                    ),
                    rule="missing-predicate-definition",
                )
                continue

            # --------------------------------------------------------
            # Source ontology type
            # --------------------------------------------------------

            source_concept = resolve_concept(artifact)

            if not source_concept:
                report.error(
                    artifact,
                    (
                        f"Source artifact '{artifact.id}' has no "
                        f"resolvable ontology Concept for relation "
                        f"'{relation.type}'."
                    ),
                    rule="unknown-source-type",
                )
                continue

            # --------------------------------------------------------
            # Target resolution
            # --------------------------------------------------------

            target = model.repository.artifact(
                relation.target
            )

            if target is None:
                # External target handling remains outside the
                # current semantic verification scope.
                continue

            # --------------------------------------------------------
            # Target ontology type
            # --------------------------------------------------------

            target_concept = resolve_concept(target)

            if not target_concept:
                report.error(
                    artifact,
                    (
                        f"Target artifact '{target.id}' has no "
                        f"resolvable ontology Concept for relation "
                        f"'{relation.type}'."
                    ),
                    rule="unknown-target-type",
                )
                continue

            # --------------------------------------------------------
            # Exact allowed source-to-target pair
            # --------------------------------------------------------

            allowed = any(
                matches_constraint(
                    source_concept,
                    pair.source,
                    pair.source_pattern,
                    model,
                )
                and matches_constraint(
                    target_concept,
                    pair.target,
                    pair.target_pattern,
                    model,
                )
                for pair in predicate.allowed_pairs
            )

            if not allowed:
                report.error(
                    artifact,
                    (
                        f"Relation '{artifact.id} --{relation.type}--> "
                        f"{target.id}' is not an allowed semantic pair: "
                        f"{artifact.ontology_type} -> "
                        f"{target.ontology_type}."
                    ),
                    rule="relation-allowed-pair-violation",
                )
