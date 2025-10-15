from typing import List, Callable, Optional

class InterleavingIterator:
    """
    Interleaving iterator for two arrays (Part 1) or a list of iterables (Part 3).
    Supports optional filtering (Part 4).
    Accepts lists or any iterable; converts to iterator internally.
    """
    def __init__(self, iterables: List, filter_func: Optional[Callable[[int], bool]] = None):
        self.iterators = [iter(it) for it in iterables]
        self.filter_func = filter_func
        self.next_elements = [self._get_next(i) for i in range(len(self.iterators))]
        self.index = 0

    def _get_next(self, idx):
        while True:
            try:
                val = next(self.iterators[idx])
                if self.filter_func is None or self.filter_func(val):
                    return val
            except StopIteration:
                return None

    def __iter__(self):
        return self

    def __next__(self):
        if all(x is None for x in self.next_elements):
            raise StopIteration
        n = len(self.next_elements)
        for _ in range(n):
            idx = self.index % n
            val = self.next_elements[idx]
            self.index += 1
            if val is not None:
                self.next_elements[idx] = self._get_next(idx)
                return val
        raise StopIteration

    @classmethod
    def from_two_arrays(cls, array1, array2):
        """Part 1: InterleavingIterator for two arrays."""
        return cls([array1, array2])

class RangeIterator:
    """
    Range-based iterator (Part 2).
    """
    def __init__(self, start: int, end: int, step: int):
        self.current = start
        self.end = end
        self.step = step
        self.started = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.started:
            self.started = True
            if self.current >= self.end:
                raise StopIteration
            return_val = self.current
        else:
            self.current += self.step
            if self.current >= self.end:
                raise StopIteration
            return_val = self.current
        return return_val

# Example usage:
if __name__ == "__main__":
    # Part 1
    it = InterleavingIterator.from_two_arrays([1,2,3], [4,5,6])
    print(list(it))  # Output: [1,4,2,5,3,6]

    # Part 2
    r = RangeIterator(1, 10, 2)
    print(list(r))  # Output: [1,3,5,7,9]

    # Part 3
    arrs = [[1,2,3], [4,5,6], [7,8]]
    it3 = InterleavingIterator(arrs)
    print(list(it3))  # Output: [1,4,7,2,5,8,3,6]

    # Part 4
    arrs = [[1,2,3], [4,5,6], [7,8]]
    it4 = InterleavingIterator(arrs, filter_func=lambda x: x % 2 == 1)
    print(list(it4))  # Output: [1,7,3,5]
