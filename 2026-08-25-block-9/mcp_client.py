import asyncio
from fastmcp import Client
from mcp_server import mcp

async def main():
    async with Client(mcp) as client:
        result = await client.call_tool("generate_answer", {"question": "According to the text, what specific reason is given for why people prefer digital tablets over physical books?"})
        print(result.data.answer)

asyncio.run(main())