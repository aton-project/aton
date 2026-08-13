"""
ATON constraint pattern registry.

This registry defines the canonical Constraint Patterns
according to RFC-0029.

Constraint Pattern semantics are defined here and are not
embedded directly in the semantic verification logic.
"""

CONSTRAINT_PATTERNS: set[str] = {
    "ANY-CONCEPT",
}


def is_known_constraint_pattern(
    pattern: str,
) -> bool:
    """
    Return True when the Constraint Pattern is canonically defined.
    """
    return pattern in CONSTRAINT_PATTERNS
