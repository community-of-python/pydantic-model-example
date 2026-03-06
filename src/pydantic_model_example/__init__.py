import importlib.util
import pathlib
import sys
import typing

import pydantic
import pydantic_settings
from polyfactory.factories.pydantic_factory import ModelFactory


@typing.final
class Settings(pydantic_settings.BaseSettings):
    file_path: pydantic_settings.CliPositionalArg[pydantic.FilePath]
    pydantic_model: pydantic_settings.CliPositionalArg[str]

    def cli_cmd(self) -> None:  # noqa: COP007,COP009
        file_spec: typing.Final = importlib.util.spec_from_file_location("dynamic_module", pathlib.Path(self.file_path))
        if file_spec is None or file_spec.loader is None:
            raise ImportError(f"Could not load module from {self.file_path}")
        file_module: typing.Final = importlib.util.module_from_spec(file_spec)
        file_spec.loader.exec_module(file_module)
        if not hasattr(file_module, self.pydantic_model):
            raise AttributeError(f"Module {self.file_path} does not have attribute {self.pydantic_model}")
        sys.stdout.write(
            ModelFactory.create_factory(getattr(file_module, self.pydantic_model)).build().model_dump_json()
        )


def main() -> None:
    pydantic_settings.CliApp.run(Settings)
