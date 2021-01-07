###############################################################################
# Bubble Sort
###############################################################################


def bubble_sort(nums: list[int]) -> None:
    """Implements a bubble sort algorithm."""

    swap = True
    while swap:
        swap = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                swap = True
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


###############################################################################
# Selection Sort
###############################################################################


def selection_sort(nums: list[int]) -> None:
    """Implements a selection sort algorithm."""

    suffix = 0
    while suffix != len(nums):
        for i in range(suffix, len(nums)):
            if nums[i] < nums[suffix]:
                nums[suffix], nums[i] = nums[i], nums[suffix]
        suffix += 1


###############################################################################
# Merge Sort
###############################################################################


def merge(left: list[int], right: list[int]) -> list[int]:
    """Implements a merge."""

    i = 0
    j = 0

    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def merge_sort(nums: list[int]) -> list[int]:
    """Recursive merge sort."""

    if len(nums) < 2:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


###############################################################################
# The Main Function
###############################################################################


def main() -> None:
    """The main function."""

    xs = [5, 2, 3, 1]

    # Merge sort
    print(merge_sort(xs))

    # Bubble sort
    bubble_sort(xs)
    print(xs)

    xs = [5, 2, 3, 1]

    # Selection sort
    selection_sort(xs)
    print(xs)


if __name__ == "__main__":
    main()
