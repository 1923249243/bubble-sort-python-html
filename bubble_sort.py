def bubble_sort(numbers):
    """Return a sorted copy of numbers and the algorithm steps."""
    result = list(numbers)
    steps = []
    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            compared = [j, j + 1]

            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                action = "swap"
            else:
                action = "keep"

            steps.append(
                {
                    "pass": i + 1,
                    "compared": compared,
                    "action": action,
                    "array": list(result),
                }
            )

        if not swapped:
            break

    return result, steps
