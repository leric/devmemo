from pathlib import Path
import os
from mcp.server import Server
from mcp.types import (
    TextContent,
    Tool,
    Resource,
)
from devmemo.service import DevMemoService


def gen_server(repo_path) -> Server:
    server = Server("devmemo")
    devmemo = DevMemoService(repo_path)

    @server.list_resources()
    async def list_resources() -> list[Resource]:
        file_list = os.listdir(repo_path)
        return [
            Resource(uri=f, name=f)
            for f in file_list
        ]

    @server.read_resource()
    async def read_resource(uri: str) -> str:
        assert(uri.startswith('memo/'))
        path, func = uri[5:].split('#')



    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name='update_comment',
                description="Update function comments (if nessicery) according to code change",
                inputSchema={
                    # file path
                }
            ),
            Tool(
                name='summarize',
                description="Shows the working tree status",
                inputSchema={
                    # file path
                }
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        match name:
            case 'summarize':
                summary = await devmemo.summarize(arguments['path'])
                return [TextContent(
                    type="text",
                    text=summary,
                )]
            case 'update_comment':
                comment_diff = await devmemo.update_comment(arguments['path'])
                return [TextContent(
                    type="text",
                    text=comment_diff,
                )]
            case _:
                raise ValueError(f"Unknown tool: {name}")
            
    return server