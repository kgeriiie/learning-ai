from fastmcp import FastMCP
import sys
import os

current_dir = os.path.dirname(__file__)
block_8_dir = os.path.join(current_dir, "..", "2026-08-13-block-8")
sys.path.append(block_8_dir)

from task_01 import answer_it
from AnswerResult import AnswerResult

mcp = FastMCP("geri-mcp")

@mcp.tool
def generate_answer(question) -> AnswerResult:
    """Answer a question using a fixed text corpus via RAG (retrieval-augmented generation).

        Retrieves the most relevant sentences from the stored corpus and uses an LLM
        to select the correct answer among them.

        Args:
            question: A natural language question to answer based on the corpus.

        Returns:
            AnswerResult with the answer text, whether generation succeeded, and how
            many attempts it took.
        """
    
    return answer_it(question)


if __name__ == "__main__":
    mcp.run()