import typer
from src.tokenize_app import tokenize_app

app = typer.Typer()
app.add_typer(tokenize_app)

if __name__ == "__main__":
    app()