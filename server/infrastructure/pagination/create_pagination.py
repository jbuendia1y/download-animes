import math
from pymongo.collection import Collection
from .paginated import Paginated, MetaPage


MAX_ITEMS = 25


def get_paginated_of_collection(collection: Collection, page: int = None):
    """ Return meta data of pagination """
    if not page:
        page = 1
    page *= MAX_ITEMS
    total_items = collection.count_documents()

    total_pages = math.ceil(total_items / MAX_ITEMS)

    return MetaPage(
        total_pages=total_pages,
        current_page=page,
        max_items=MAX_ITEMS
    )
