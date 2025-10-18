from typing import Iterator, Callable, Any, TypeVar, Generic

T = TypeVar("T")

class PageIterator(Generic[T]):
    def __init__(self,
                 fetch_page: Callable[[int], list[T]],
                 page_size: int = 50
                 ):
        self.fetch_page = fetch_page
        self.page_size = page_size

    def __iter__(self) -> Iterator[T]:
        page = 1
        while True:
            items = self.fetch_page(page)
            if not items:
                break
            for item in items:
                yield  item
            page +=1