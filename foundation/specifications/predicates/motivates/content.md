# motivates

## Meaning

A Note or Finding provides rationale, evidence, observation, or an
identified problem that contributes to an architectural or engineering
Decision.

The Predicate expresses a directional semantic relationship from the
source artifact providing the motivation to the Decision being
motivated.

## Allowed Pairs

The Predicate is valid only for the following explicit
source-to-target Concept pairs:

- Note -> ADR
- Finding -> ADR

No other source-to-target Concept pair is permitted by this Predicate.

## Inverse

The inverse Predicate is:

    motivatedBy

The inverse relationship is:

- ADR -> Note
- ADR -> Finding

The existence of the inverse Predicate does not permit `motivates` to be
used in the inverse direction.

## Direction

The Predicate is directional:

    Note -> motivates -> ADR

    Finding -> motivates -> ADR

It does not imply:

    ADR -> motivates -> Note

    ADR -> motivates -> Finding

The inverse Predicate `motivatedBy` SHALL be used for the reverse
direction.

## Semantic Validation

A relation using `motivates` is semantically valid only when its exact
source-to-target Concept pair is contained in the defined
`allowedPairs`.

Therefore:

    Note -> motivates -> ADR

is valid.

    Finding -> motivates -> ADR

is valid.

The following are invalid:

    Note -> motivates -> Decision

    Finding -> motivates -> Decision

    Note -> motivates -> Finding

    Finding -> motivates -> Note

A Concept being related to another Concept through specialization or
taxonomy SHALL NOT implicitly make an otherwise undefined pair valid.

## Cardinality

No cardinality constraint is defined for this Predicate.
