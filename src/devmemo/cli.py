import logging
import sys
import click
import os

@click.group()
def main():
    """DevMemo - A tool to help record software project information."""
    pass

@main.command()
def init():
    """Initialize DevMemo in the current project."""
    click.echo("Initializing DevMemo...")

@main.command()
def summarize():
    """Summarize current changes before commit."""
    click.echo("Summarizing changes...")

@main.command()
@click.argument('file', type=click.Path())
@click.argument('func', required=False, nargs=-1)
def history(file: str, func: str | None):
    """
    Show the history of a function in file.
    
    @param file Full path to the file to query
    @param func Function to query, if not specified, show history of top level entity in file.
    """
    click.echo(f"Showing history of {func} in {file}...")

@main.command()
async def server():
    """Start MCP server."""
    from devmemo.mcp_server import gen_server
    from mcp import stdio_server
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    # get current working directory
    root_path = os.getcwd()
    server = gen_server(root_path)
    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options, raise_exceptions=True)


if __name__ == '__main__':
    main()
