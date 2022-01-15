# Programe par Eliot CASSIDY
# TODO : add variable to sort ascending or descending

def merge_sort(values: list[int]) -> list[int]:
    """merge_sort sorts inputs in O(n log n)

    Args:
        values (list[int]): [-4, 16, 6, 1, 20, 5]

    Returns:
        list[int]: [-4, 1, 5, 6, 16, 20]
    """
    assert isinstance(values, list)