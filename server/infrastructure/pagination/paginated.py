from pydantic.generics import GenericModel
from pydantic import BaseModel
from typing import Generic, Sequence, TypeVar


T = TypeVar("T")


class MetaPage(BaseModel):
    total_pages: int
    max_items: int
    current_page: int


class Paginated(GenericModel, Generic[T]):
    total_pages: int
    current_page: int
    data: Sequence[T]


def create_paginated(items: Sequence[T], total_pages: int, current_page: int) -> Paginated[T]:
    return Paginated(
        data=items,
        total_pages=total_pages,
        current_page=current_page
    )
