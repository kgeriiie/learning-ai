import asyncio
from fastmcp import Client
from document_mcp_server import mcp

async def main():
    async with Client(mcp) as client:
        result = await client.call_tool("answer_document_related_question", {"question": "Can I return null from a function?"})
        print(result.data.answer)

asyncio.run(main())