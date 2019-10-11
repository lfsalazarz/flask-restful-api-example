from pydantic.dataclasses import dataclass


@dataclass
class LoginSchema:
    id: str
