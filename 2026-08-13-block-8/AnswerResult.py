from dataclasses import dataclass

@dataclass
class AnswerResult:
    answer: str
    success: bool
    attempts: int
