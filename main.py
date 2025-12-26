import random
import timeit
from typing import List, Dict, Optional

# Merge Sort


def merge_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    middle: int = len(array) // 2
    left_half: List[int] = merge_sort(array[:middle])
    right_half: List[int] = merge_sort(array[middle:])
    return merge(left_half, right_half)


def merge(left: List[int], right: List[int]) -> List[int]:
    merged: List[int] = []
    left_index: int = 0
    right_index: int = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Insertion Sort


def insertion_sort(array: List[int]) -> List[int]:
    sorted_array: List[int] = array.copy()
    for current_index in range(1, len(sorted_array)):
        current_value: int = sorted_array[current_index]
        position: int = current_index - 1
        while position >= 0 and sorted_array[position] > current_value:
            sorted_array[position + 1] = sorted_array[position]
            position -= 1
        sorted_array[position + 1] = current_value
    return sorted_array

# Timsort (built-in sorted)


def timsort(array: List[int]) -> List[int]:
    return sorted(array)


def test_sorting_algorithms() -> None:
    test_sizes: List[int] = [100, 1000, 5000, 10000]
    timing_results: Dict[int, Dict[str, Optional[float]]] = {}

    for size in test_sizes:
        random_array: List[int] = [
            random.randint(
                0, 10000) for _ in range(size)]
        timing_results[size] = {
            'merge_sort': timeit.timeit(
                lambda: merge_sort(random_array),
                number=3),
            'insertion_sort': timeit.timeit(
                lambda: insertion_sort(random_array),
                number=3) if size <= 1000 else None,
            'timsort': timeit.timeit(
                lambda: timsort(random_array),
                number=3)}

    for size in timing_results:
        print(f"Size: {size}")
        for algorithm in timing_results[size]:
            if timing_results[size][algorithm] is not None:
                print(
                    f"  {algorithm}: {
                        timing_results[size][algorithm]:.5f} сек")
        print()


if __name__ == "__main__":
    test_sorting_algorithms()
