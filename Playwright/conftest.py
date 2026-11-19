from dataclasses import dataclass

import pytest


@dataclass
class User:
    email: str
    password: str


@pytest.fixture(scope='session')
def user(request) -> User:
    return User(**request.param)
