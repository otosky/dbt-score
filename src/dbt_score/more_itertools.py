"""Vendored utility functions from https://github.com/more-itertools/more-itertools."""
from typing import Iterable

from typing import TypeVar, Callable, Optional

T = TypeVar("T")
U = TypeVar("U")


def first_true(iterable: Iterable[T], default: Optional[U] =None, pred: Optional[Callable[[T], bool]]=None) -> T | Optional[U]:
    """Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item for which
    ``pred(item) == True`` .

        >>> first_true(range(10))
        1
        >>> first_true(range(10), pred=lambda x: x > 5)
        6
        >>> first_true(range(10), default='missing', pred=lambda x: x > 9)
        'missing'

    """
    return next(filter(pred, iterable), default)
