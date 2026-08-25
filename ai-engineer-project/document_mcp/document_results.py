from dataclasses import dataclass

@dataclass
class DocumentResult:
    answer: str
    success: bool
    attempts: int