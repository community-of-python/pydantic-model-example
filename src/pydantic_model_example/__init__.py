import pydantic
from pydantic_settings import BaseSettings, CliApp, CliPositionalArg


class Settings(BaseSettings):
    file_path: CliPositionalArg[pydantic.FilePath]
    pydantic_model: CliPositionalArg[str]

    def cli_cmd(self) -> None:
        # TODO: import file path, 
        print(self.model_dump())


def main() -> None:
    CliApp.run(Settings)
