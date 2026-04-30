"""CLI using Typer."""

import typer

app = typer.Typer(name="CLI using Typer")


@app.callback()
def main_callback():
    """Welcome message printed before any command."""
    typer.echo("👋 Welcome to the Animal Shelter CLI!")


@app.command()
def say_hi(name: str):
    """Say hello to the user."""
    typer.echo(f"Hello: {name}")


@app.command()
def goodbye():
    """Say goodbye to the user."""
    typer.echo("Goodbye!")


if __name__ == "__main__":
    app()
