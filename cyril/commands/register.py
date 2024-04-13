from typing import Annotated, List

import typer

from cyril.commands.ask import question as q
from cyril.commands.bash import question as sh
from cyril.commands.keyboard import question as kb
from cyril.commands.terraform import question as tf
from cyril.config import settings
from cyril.load_env.load import LoadEnv

app = typer.Typer(
    help=settings.HELP_GENERAL,
)

instance_gen: LoadEnv


@app.command()
def ask(
    prompt: Annotated[
        List[str], typer.Argument(help="Ask a question to prompt a detailed response.")
    ]
):
    """
        Ask a question to prompt a detailed response.

    Parameters:
        prompt (str): The question to be asked.

    Returns:
        str: The response to the question.

    Example:
        response = "Can you tell me about your experience with Python?"
        response = "Sure! I've been using Python for several years now. I initially started with basic scripting tasks,
        but gradually, I've delved deeper into web development and data analysis using libraries like FastApi
        and Pandas. Overall, Python has been an integral part of my workflow and I find its versatility
        quite remarkable."
    """
    q(prompt, instance_gen.instance)


@app.command()
def bash(
    prompt: Annotated[
        List[str], typer.Argument(help="Ask questions about Bash or CLI commands.")
    ]
):
    """
    Ask a question about a Bash or CLI command and return the response in one line.

    Parameters:
        prompt (str): The question to ask about Bash or CLI.

    Returns:
        str: The response to the question in one line.

    Example:
        prompt = "How can I recursively remove a directory using rm?"
        response = "Use the command 'rm -r <directory_name>'."
    """
    sh(prompt, instance_gen.instance)


@app.command()
def terraform(prompt: Annotated[List[str], typer.Argument(help="TERRAFORM")]):
    """
    Ask a question specific to Terraform and provide the most relevant answer.

    Parameters:
        prompt (str): The question related to Terraform.

    Returns:
        str: The most pertinent response related to Terraform.

    Example:
        prompt = "How do I create a new AWS EC2 instance with Terraform?"
        response = To create a new AWS EC2 instance with Terraform, you can define a resource block in your .tf file like this:

        resource "aws_instance" "example" {
          ami           = "ami-0c55b159cbfafe1f0"
          instance_type = "t2.micro"
        }

        After defining the resource block, run 'terraform init' to initialize the working directory followed by
        'terraform apply' to apply the changes and create the EC2 instance.
    """
    tf(prompt, instance_gen.instance)


@app.command()
def keyboard(
    prompt: Annotated[
        List[str], typer.Argument(help="Ask anything about keyboard and switch")
    ]
):
    """
    Ask a question about keyboard shortcuts and return the response.

    Parameters:
        prompt (str): The question to ask about keyboard shortcuts.

    Returns:
        str: The most pertinent response related to Terraform.
    """
    kb(prompt, instance_gen.instance)


@app.callback()
def pre_process():
    """
    Load the global instance of LoadEnv.
    """
    global instance_gen
    instance_gen = LoadEnv()
