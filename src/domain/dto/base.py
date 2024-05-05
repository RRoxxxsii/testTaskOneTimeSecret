from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class BaseDTO:

    def dict(self) -> dict:
        return {k: str(v) for k, v in asdict(self).items()}

