#import os
import openai
import typer
from rich import print
from rich.table import Table

def main():
    openai.api_key="YOUR KEY"

    print("[bold green]CHAT GPT 3 TURBO WITH PYTHON[/bold green]")

    table=Table("Command","Description")
    table.add_row("exit","exit of app")
    table.add_row("new","new conversation")
    print(table)

    # Contexto del asistente
    context = {"role": "system","content": "you are the best assitant"}
    messages = [context]
    
    while True:

        content= __prompt()
        if content == "new":
            print("🆕 New conversation has been created")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nWhat do you talking about? ")

    if prompt == "exit":
        exit = typer.confirm("✋ Are you sure?")
        if exit:
            print("👋 ¡Good Bye!")
            raise typer.Abort()

        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)