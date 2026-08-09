# references

## Meaning

An artifact explicitly refers to another artifact as a source of information
or context.

The Predicate expresses a directional semantic relationship from the
referencing artifact to the referenced artifact.

## Allowed Pairs

The Predicate is valid only for the following explicit source-to-target
Concept pair:

- Artifact -> Artifact

No other source-to-target Concept pair is permitted by this Predicate.

## Inverse

The inverse Predicate is:

    referencedBy

The inverse relationship is:

- Artifact -> Artifact

The existence of the inverse Predicate does not permit `references` to be
used in the inverse direction.

## Direction

The Predicate is directional:

    Artifact -> references -> Artifact

It does not imply a reverse `references` relation.

The inverse Predicate `referencedBy` SHALL be used for the reverse direction.

## Semantic Validation

A relation using `references` is semantically valid only when its exact
source-to-target Concept pair is contained in the defined `allowedPairs`.

Therefore:

    Artifact -> references -> Artifact

is valid.

The Predicate does not permit other source-to-target Concept combinations.

A Concept being related to another Concept through specialization or taxonomy
SHALL NOT implicitly make an otherwise undefined pair valid.

## Cardinality

No cardinality constraint is defined for this Predicate.
