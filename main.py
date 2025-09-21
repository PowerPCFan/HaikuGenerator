import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
import ast


def print_title(console: Console, text: str) -> None:
    txt = Text(text, style="bold blue")
    console.print(Panel(txt, expand=False, padding=(0, 4)))


if __name__ == "__main__":
    console = Console()
    console.clear()

    from modules.global_vars import config
    import modules.tools as tools

    no_successful_runs_yet = True

    try:
        print_title(console, "Welcome to the Haiku Generator!")

        while True:
            table = Table(title="", show_header=True, border_style="blue", box=box.ROUNDED)
            table.add_column("Option", style="cyan bold", justify="right")
            table.add_column("Description", style="white")
            line = f"Generate {'a' if no_successful_runs_yet else 'another'} haiku"
            table.add_row("g", line)
            table.add_row("e", "Edit configuration (advanced)")
            table.add_row("f", "Reset configuration to defaults")
            table.add_row("r", "Regenerate Markov model")
            table.add_row("q", "Quit")

            console.print()
            console.print(table)
            console.print()

            choice = Prompt.ask("Choose an option", choices=["g", "e", "f", "r", "q"], default="g").lower()

            if choice == 'q':
                console.print("\n[yellow]Exiting...[/yellow]")
                break
            elif choice == 'e':
                console.clear()
                print_title(console, "Edit Configuration")
                try:
                    for field in config.__dataclass_fields__:
                        value = getattr(config, field)
                        value_type = tools.get_user_friendly_type(value)
                        prompt_text = f"Edit '{field}' (current: {value}, type: {value_type}), or press Enter to skip"
                        user_input = Prompt.ask(prompt_text, default="")

                        if user_input.strip():
                            try:
                                parsed_value = ast.literal_eval(user_input)
                                setattr(config, field, parsed_value)
                            except (ValueError, SyntaxError):
                                setattr(config, field, user_input)

                    config.save()
                    console.clear()
                    console.print("[green]Configuration updated successfully![/green]")
                except Exception as e:
                    console.print(f"[red]Error updating configuration: {e}[/red]")
            elif choice == 'f':
                console.clear()
                print_title(console, "Reset Configuration to Default")
                confirm = Prompt.ask(
                    "Are you sure you want to reset the configuration to default?", choices=["y", "n"], default="n"
                ).lower()

                if confirm == 'y':
                    try:
                        config._remove_config_file()
                        config._create_default_config()
                        config = config.load()

                        console.clear()
                        console.print("[green]Configuration reset to default successfully![/green]")
                    except Exception as e:
                        console.print(f"[red]Error resetting configuration: {e}[/red]")
                else:
                    console.print("[yellow]Reset cancelled.[/yellow]")
            elif choice == 'r':
                console.clear()
                console.print("[bold green]Regenerating Markov model...[/bold green]")
                tools.regenerate_markov_model()
                console.print("[green]Model regenerated successfully![/green]")
            elif choice == 'g':
                console.clear()
                try:
                    console.print("[bold green]Generating...[/bold green]")
                    lines: list[str] = []

                    for syllable in config.syllables:
                        lines.append(tools.generate_line(syllable_count=syllable))

                    if any(line == '' for line in lines):
                        console.print("[red]Error generating haiku. Check your sentences.json file.[/red]")
                    else:
                        no_successful_runs_yet = False
                        lines = [line.strip() for line in lines]

                        if not lines:
                            raise ValueError("Generated haiku is empty.")

                        max_length = max(len(line) for line in lines)
                        haiku_content = "\n".join(line.center(max_length) for line in lines)

                        console.clear()
                        console.print()  # newline
                        console.print(Panel(
                            haiku_content,
                            title="Your Haiku is Ready!",
                            title_align="center",
                            style="bold green",
                            border_style="purple",
                            padding=(1, 2)
                        ), justify="left")
                except Exception as e:
                    console.print(f"[red]Error generating haiku: {e}[/red]")
            else:
                console.print("[red]Invalid input. Please try again.[/red]")

    except KeyboardInterrupt:
        console.print("\n[yellow]Exiting...[/yellow]")
        sys.exit(0)
    except Exception as error:
        console.print("[red]An unexpected error occurred:[/red]")
        console.print(f"[red]{error}[/red]")
