import pathlib
import subprocess
import typing

import faker
import pytest


def run_cli_cmd(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["pydantic-model-example", *arguments], capture_output=True, text=True)  # noqa: PLW1510, S603, S607


@pytest.fixture
def example_file_path() -> str:
    return str(pathlib.Path(__file__).parent / "example_file.py")


@pytest.fixture
def example_model() -> str:
    return "ExampleModel"


def test_cli_cmd_with_example_model(example_file_path: str, example_model: str) -> None:
    run_result: typing.Final = run_cli_cmd([example_file_path, example_model])

    assert run_result.returncode == 0
    assert "name" in run_result.stdout
    assert "age" in run_result.stdout
    assert "email" in run_result.stdout
    assert "isActive" in run_result.stdout


def test_cli_cmd_with_nonexistent_file(faker: faker.Faker) -> None:
    run_result: typing.Final = run_cli_cmd([faker.pystr(), faker.pystr()])

    assert run_result.returncode != 0
    assert "Validation error" in run_result.stderr or "Path does not point to a file" in run_result.stderr


def test_cli_cmd_with_missing_attribute(example_file_path: str, faker: faker.Faker) -> None:
    run_result: typing.Final = run_cli_cmd([example_file_path, faker.pystr()])

    assert run_result.returncode != 0
    assert "does not have attribute" in run_result.stderr
