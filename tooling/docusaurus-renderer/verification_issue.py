from dataclasses import dataclass


@dataclass(slots=True)
class VerificationIssue:
    """
    A single verification issue.
    """

    severity: str
    rule: str
    artifact: str | None
    message: str
