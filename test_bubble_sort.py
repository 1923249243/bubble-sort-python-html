from bubble_sort import bubble_sort


def test_bubble_sort_orders_numbers():
    sorted_numbers, steps = bubble_sort([5, 3, 8, 1, 2])

    assert sorted_numbers == [1, 2, 3, 5, 8]
    assert steps


def test_bubble_sort_handles_empty_list():
    sorted_numbers, steps = bubble_sort([])

    assert sorted_numbers == []
    assert steps == []


def test_bubble_sort_does_not_mutate_input():
    numbers = [3, 2, 1]

    bubble_sort(numbers)

    assert numbers == [3, 2, 1]
