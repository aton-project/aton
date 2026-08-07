from dataclasses import dataclass, field

from verification_issue import VerificationIssue


@dataclass(slots=True)
class VerificationReport:
    """
    Result of a Foundation verification.
    """

    issues: list[VerificationIssue] = field(default_factory=list)

    def add(self, issue: VerificationIssue) -> None:
        self.issues.append(issue)

    def error(
        self,
        artifact,
        message: str,
    ) -> None:
        self.add(
            VerificationIssue(
                severity="error",
                rule="verification",
                artifact=artifact.id,
                message=message,
            )
        )

    @property
    def ok(self) -> bool:
        return not any(
            issue.severity == "error"
            for issue in self.issues
        )
