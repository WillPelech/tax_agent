from typing import Protocol
from mcp import ClientSession
from mcp.types import TextContent

class ToolRegistry(Protocol):
    async def call_tool(self,name:str, args:dict)-> str:
        ...

class McpToolRegistry:
    def __init__(self,session:ClientSession):
        self.session = session
    async def call_tool(self,name:str, args:dict)-> str:
        result = await self.session.call_tool(name,args)
        return "\n".join(block.text for block in result.content if isinstance(block, TextContent))





