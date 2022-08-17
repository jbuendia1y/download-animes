from abc import ABC
from .user import User, CreateUser
from typing import List


class UserRepository(ABC):
    def find_by_id(self, user_id: str) -> User:
        pass

    def find_by_username(self, username: str) -> User:
        pass

    def find_all(self) -> List[User]:
        pass

    def create(self, data: CreateUser):
        pass
