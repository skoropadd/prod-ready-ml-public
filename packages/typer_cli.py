# typer_cli.py
"""CLI using Typer."""

from typing import Annotated

import typer

app = typer.Typer(name="CLI using Typer")


@app.command()
def say_hi(name: str):
    """Say hello to the user."""
    typer.echo(f"Hello: {name}")


@app.command()
def goodbye():
    """Say goodbye to the user."""
    typer.echo("Goodbye!")


@app.command()
def greet(name: str):
    """Print a greeting message to a person."""
    typer.echo(f"Greetings, {name}!")


@app.command()
def welcome(
    name: str,
    greeting: Annotated[str, typer.Option(help="Custom greeting text")] = "Hello",
    enthusiastic: Annotated[bool, typer.Option(help="Add exclamation marks")] = False,
):
    """Welcome a person with an optional custom greeting."""
    suffix = "!!!" if enthusiastic else ""
    typer.echo(f"{greeting} {name}{suffix}")


if __name__ == "__main__":
    app()
