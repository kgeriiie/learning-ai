from fastmcp import FastMCP
from document_mcp.document_results import DocumentResult
from document_mcp.process_document import async_answer_it

mcp = FastMCP("document-mcp")

@mcp.tool
async def answer_document_related_question(question: str) -> DocumentResult:
    """Answer a question about the Clean Code book using retrieval-augmented generation.

        Retrieves the most relevant passages from the book and uses an LLM to
        generate a grounded answer based on them.

        Args:
            question: A natural language question about the book's content.

        Returns:
            DocumentResult with the answer text, whether generation succeeded, and
            how many attempts it took.
    """
    return await async_answer_it(question)

if __name__ == "__main__":
    mcp.run()