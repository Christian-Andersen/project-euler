from pathlib import Path
import importlib
import pytest
import requests


def get_done_problems():
    done_problems = set()
    for i in Path("done").iterdir():
        if not i.name.endswith(".py"):
            continue
        assert i.name.startswith("p")
        problem_number = i.name[1:-3]
        done_problems.add(problem_number)
    return done_problems


def get_answers():
    done_problems = get_done_problems()
    response = requests.get(
        "https://raw.githubusercontent.com/lucky-bai/projecteuler-solutions/refs/heads/master/Solutions.md"
    )
    response.raise_for_status()

    answers = [i.split(".") for i in response.text.splitlines()[4:]]
    answers = [(line[0].strip(), line[1].strip()) for line in answers]
    answers = [(line[0], line[1]) for line in answers if (line[0] and line[1])]
    answers = [(line[0], line[1]) for line in answers if (line[0] in done_problems)]
    return answers


@pytest.mark.parametrize("problem, answer", get_answers())
def test_problem(problem, answer):
    module = importlib.import_module(f"done.p{problem}")
    assert str(module.main()).strip() == answer
