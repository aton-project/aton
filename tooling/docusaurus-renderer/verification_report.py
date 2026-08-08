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
        rule: str = "unknown",
    ) -> None:
        self.add(
            VerificationIssue(
                severity="error",
                rule=rule,
                artifact=artifact.id if artifact else None,
                message=message,
            )
        )

    def warning(
        self,
        artifact,
        message: str,
        rule: str = "unknown",
    ) -> None:
        self.add(
            VerificationIssue(
                severity="warning",
                rule=rule,
                artifact=artifact.id if artifact else None,
                message=message,
            )
        )

    @property
    def ok(self) -> bool:
        return not any(
            issue.severity == "error"
            for issue in self.issues
        )
