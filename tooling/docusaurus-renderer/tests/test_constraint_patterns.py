import unittest

from constraint_pattern_registry import is_known_constraint_pattern


class ConstraintPatternRegistryTests(unittest.TestCase):

    def test_any_concept_is_known(self):
        self.assertTrue(
            is_known_constraint_pattern("ANY-CONCEPT")
        )

    def test_unknown_pattern_is_not_known(self):
        self.assertFalse(
            is_known_constraint_pattern("UNKNOWN-PATTERN")
        )

    def test_empty_pattern_is_not_known(self):
        self.assertFalse(
            is_known_constraint_pattern("")
        )

    def test_arbitrary_concept_is_not_a_pattern(self):
        self.assertFalse(
            is_known_constraint_pattern("ONT-Artifact")
        )


if __name__ == "__main__":
    unittest.main()


class ConstraintMatchingTests(unittest.TestCase):

    def _ontology(self, concept_id):
        from model import Artifact

        return Artifact(
            id=concept_id,
            type="ontology",
            ontology_type=None,
            title=concept_id,
            status="Draft",
            source_dir=__import__("pathlib").Path("."),
            content_file=__import__("pathlib").Path("."),
            metadata_file=__import__("pathlib").Path("."),
            metadata={"entityType": "ontology"},
        )

    def _model(self):
        from artifact_repository import ArtifactRepository
        from knowledge_model import KnowledgeModel

        artifacts = [
            self._ontology("ONT-Artifact"),
            self._ontology("ONT-ADR"),
        ]

        return KnowledgeModel(
            artifacts=artifacts,
            repository=ArtifactRepository(artifacts),
        )

    def test_any_concept_matches_known_concept(self):
        from verification import matches_constraint

        model = self._model()

        self.assertTrue(
            matches_constraint(
                "ONT-Artifact",
                None,
                "ANY-CONCEPT",
                model,
            )
        )

    def test_any_concept_does_not_match_unknown_concept(self):
        from verification import matches_constraint

        model = self._model()

        self.assertFalse(
            matches_constraint(
                "ONT-Unknown",
                None,
                "ANY-CONCEPT",
                model,
            )
        )

    def test_concrete_concept_requires_exact_match(self):
        from verification import matches_constraint

        model = self._model()

        self.assertTrue(
            matches_constraint(
                "ONT-Artifact",
                "ONT-Artifact",
                None,
                model,
            )
        )

        self.assertFalse(
            matches_constraint(
                "ONT-ADR",
                "ONT-Artifact",
                None,
                model,
            )
        )

    def test_unknown_pattern_does_not_match(self):
        from verification import matches_constraint

        model = self._model()

        self.assertFalse(
            matches_constraint(
                "ONT-Artifact",
                None,
                "UNKNOWN-PATTERN",
                model,
            )
        )


class SemanticVerificationTests(unittest.TestCase):

    def _artifact(
        self,
        artifact_id,
        ontology_type,
        relations=None,
        metadata=None,
    ):
        from pathlib import Path
        from model import Artifact

        return Artifact(
            id=artifact_id,
            type="artifact",
            ontology_type=ontology_type,
            title=artifact_id,
            status="Draft",
            source_dir=Path("."),
            content_file=Path("."),
            metadata_file=Path("."),
            metadata=metadata or {},
            relations=relations or [],
            content=f"# {artifact_id}\n",
        )

    def _ontology(self, concept_id):
        from pathlib import Path
        from model import Artifact

        return Artifact(
            id=concept_id,
            type="ontology",
            ontology_type=None,
            title=concept_id,
            status="Draft",
            source_dir=Path("."),
            content_file=Path("."),
            metadata_file=Path("."),
            metadata={"entityType": "ontology"},
            content=f"# {concept_id}\n",
        )

    def _model(self, source, target, predicate):
        from artifact_repository import ArtifactRepository
        from knowledge_model import KnowledgeModel

        artifacts = [
            self._ontology("ONT-ADR"),
            self._ontology("ONT-Artifact"),
            source,
            target,
            predicate,
        ]

        return KnowledgeModel(
            artifacts=artifacts,
            repository=ArtifactRepository(artifacts),
        )


    def test_any_concept_allowed_pair_is_accepted(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                )
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source=None,
                    target=None,
                    source_pattern="ANY-CONCEPT",
                    target_pattern="ANY-CONCEPT",
                )
            ],
            content="# References\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)

        self.assertTrue(
            report.ok,
            msg=[
                issue.message
                for issue in report.issues
            ],
        )


    def test_source_pattern_with_concrete_target_is_accepted(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                ),
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source=None,
                    target="ONT-Artifact",
                    source_pattern="ANY-CONCEPT",
                )
            ],
            content="# References\\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)

        self.assertTrue(
            report.ok,
            msg=[
                issue.message
                for issue in report.issues
            ],
        )


    def test_concrete_source_with_target_pattern_is_accepted(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                ),
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source="ONT-ADR",
                    target=None,
                    target_pattern="ANY-CONCEPT",
                )
            ],
            content="# References\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)


        self.assertTrue(
            report.ok,
            msg=[
                issue.message
                for issue in report.issues
            ],
        )


    def test_constraint_pair_mismatch_is_rejected(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                ),
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source=None,
                    target="ONT-RFC",
                    source_pattern="ANY-CONCEPT",
                )
            ],
            content="# References\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)

        self.assertFalse(report.ok)

        self.assertTrue(
            any(
                issue.rule == "relation-allowed-pair-violation"
                for issue in report.issues
            )
        )


    def test_source_pattern_mismatch_is_rejected(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                ),
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source="ONT-RFC",
                    target=None,
                    target_pattern="ANY-CONCEPT",
                )
            ],
            content="# References\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)

        self.assertFalse(report.ok)

        self.assertTrue(
            any(
                issue.rule == "relation-allowed-pair-violation"
                for issue in report.issues
            )
        )


    def test_concrete_source_and_target_mismatch_is_rejected(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                ),
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source="ONT-RFC",
                    target="ONT-Artifact",
                )
            ],
            content="# References\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)

        self.assertFalse(report.ok)

        self.assertTrue(
            any(
                issue.rule == "relation-allowed-pair-violation"
                for issue in report.issues
            )
        )


    def test_target_pattern_mismatch_is_rejected(self):
        from model import AllowedPair, Artifact, Relation

        source = self._artifact(
            "ADR-TEST",
            "ONT-ADR",
            relations=[
                Relation(
                    type="references",
                    target="ART-TEST",
                ),
            ],
        )

        target = self._artifact(
            "ART-TEST",
            "ONT-Artifact",
        )

        predicate = Artifact(
            id="PRED-references",
            type="predicate",
            ontology_type=None,
            title="References",
            status="Draft",
            source_dir=source.source_dir,
            content_file=source.content_file,
            metadata_file=source.metadata_file,
            metadata={"entityType": "predicate"},
            allowed_pairs=[
                AllowedPair(
                    source="ONT-ADR",
                    target="ONT-RFC",
                )
            ],
            content="# References\n",
        )

        model = self._model(
            source,
            target,
            predicate,
        )

        from verification import verify

        report = verify(model)

        self.assertFalse(report.ok)

        self.assertTrue(
            any(
                issue.rule == "relation-allowed-pair-violation"
                for issue in report.issues
            )
        )
