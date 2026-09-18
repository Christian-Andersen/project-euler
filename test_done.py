import importlib
from pathlib import Path

import pytest
import requests


def get_done_problems() -> set[str]:
    done_problems = set()
    for i in Path("done").iterdir():
        if not i.name.startswith("p") or not i.name.endswith(".py"):
            continue
        problem_number = i.name[1:-3]
        done_problems.add(problem_number)
    return done_problems


def get_answers() -> list[tuple[str, str]]:
    done_problems = get_done_problems()
    response = requests.get(
        "https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/refs/heads/master/Solutions.md",
        timeout=30,
    )
    response.raise_for_status()

    answers = [i.split(".") for i in response.text.splitlines()[4:]]
    answers = [(line[0].strip(), line[1].strip()) for line in answers if len(line) >= 2]  # noqa: PLR2004
    answers = [(line[0], line[1]) for line in answers if (line[0] and line[1])]
    return [(line[0], line[1]) for line in answers if (line[0] in done_problems)]


@pytest.mark.parametrize(("problem", "answer"), get_answers())
def test_problem(problem: str, answer: str) -> None:
    module = importlib.import_module(f"done.p{problem}")
    assert str(module.main()).strip() == answer  # noqa: S101
