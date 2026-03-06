import typing

import pydantic
import pydantic_settings


@typing.final
class Settings(pydantic_settings.BaseSettings):
    file_path: pydantic_settings.CliPositionalArg[pydantic.FilePath]
    pydantic_model: pydantic_settings.CliPositionalArg[str]

    def cli_cmd(self) -> None:  # noqa: COP007,COP009
        # TODO: import file path, find attribute called pydantic_model
        print(self.model_dump())


def main() -> None:
    pydantic_settings.CliApp.run(Settings)
