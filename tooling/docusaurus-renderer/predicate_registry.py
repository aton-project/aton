"""
ATON predicate migration registry.

This registry defines the migration state of relation predicates
according to RFC-0028.

It does not define predicate semantics or allowed source-to-target
Concept pairs. Those are defined by the Predicate artifacts themselves.
"""

PREDICATE_STATES: dict[str, str] = {
    # Canonical Predicates
    "references": "canonical",
    "dependsOn": "canonical",
    "refines": "canonical",
    "specializes": "canonical",
    "governs": "canonical",

    # Explicit inverse Predicate
    "referencedBy": "inverse",

    # Deprecated legacy spelling
    "referenced-by": "deprecated",

    # Semantically unresolved legacy Predicates
    "children": "unresolved",
    "related": "unresolved",
    "relatedTo": "unresolved",
}


def predicate_state(predicate: str) -> str | None:
    """
    Return the migration state of a relation predicate.

    Returns None when the predicate is not known to the migration
    registry.
    """
    return PREDICATE_STATES.get(predicate)
