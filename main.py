from os import scandir
import inquirer
from parser2 import parse


def main():
    input = get_input(questions)
    selected_documents = input["documents"]  # pyright: ignore[reportOptionalSubscript]
    selected_documents = ["documents/" + x for x in selected_documents]
    print(selected_documents)
    for doc in selected_documents:
        parse(doc)


def get_input(questions):
    return inquirer.prompt(questions=questions)


def get_documents(directory="documents") -> list[str]:
    documents = []

    with scandir(directory) as docs:
        for doc in docs:
            documents.append(doc.name)

    return documents


documents = get_documents()
questions = [
    inquirer.Checkbox(
        "documents",
        message="Choose document (only choose pdf right now. idk how to make it output into output folder):",
        choices=documents,
    )
]

if __name__ == "__main__":
    main()
