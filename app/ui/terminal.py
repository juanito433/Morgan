from rich.console import Console

console = Console()

def mostrar_inicio():

    console.print(
        """
[bold cyan]
╔══════════════════════════════╗
║       MORGAN AI v0.2         ║
╚══════════════════════════════╝
[/bold cyan]
"""
    )

def mostrar_usuario(texto):

    console.print(
        f"[bold green]Señor[/bold green] > {texto}"
    )

def mostrar_morgan(texto):

    console.print(
        f"[bold cyan]Morgan[/bold cyan] > {texto}"
    )