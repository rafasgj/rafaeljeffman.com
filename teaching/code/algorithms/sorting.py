"""Sorting algorithms."""

def merge_sort(data):
    """Sort data using merge sort."""
    A = data
    B = data[::-1]
    n = len(data)

    def merge(start, mid, end):
        i, j = start, mid
        for k in range(i, end):
            if i < mid and (j >= end or A[i] <= A[j]):
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j]
                j += 1

    w = 1
    while w < n:
        i = 0
        while i < n:
            merge(i, min(i + w, n), min(i + w * 2, n))
            i += w * 2
        A, B = B, A
        w *= 2

    return A


def counting_sort(data, k=None, key=lambda i: i):
    """Sort data using counting sort."""
    if k is None:
        k = len(data)
    count = [0 for _ in range(k)]
    output = data[:]
    for i in data:
        count[key(i)] += 1
    for i in range(1, k):
        count[i] += count[i - 1]
    for i in data[::-1]:
        count[key(i)] -= 1
        output[count[key(i)]] = i

    return output


def radix_sort(data):
    """Sort data using radix sort based on counting sort."""
    n = len(data)
    digits = [(i // n, i % n) for i in data]
    digits = counting_sort(digits, key=lambda i: i[1])
    digits = counting_sort(digits, key=lambda i: i[0])
    return [i[0] * n + i[1] for i in digits]


if __name__ == "__main__":
    from random import randint

    def check_order(data):
        """Verify if list is sorted."""
        print(f"Data: {data}")
        for i in range(1, len(data)):
            if data[i] < data[i - 1]:
                return (False, i, data[i-1:i+1])
        return (True,)

    ordered = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    rnd = [randint(0, 10**2) for _ in range(10)]
    print(f"Ordered array: {ordered}")
    print(f"Inverted array: {ordered[::-1]}")
    print(f"Random array: {rnd}")
    print("Checking merge sort...")
    print(f"Sorted array: {check_order(merge_sort(ordered[:]))}")
    print(f"Inverted array: {check_order(merge_sort(ordered[::-1]))}")
    print(f"Random array: {check_order(merge_sort(rnd[:]))}")
    print("Checking counting sort...")
    print(f"Sorted array: {check_order(counting_sort(ordered[:]))}")
    print(f"Inverted array: {check_order(counting_sort(ordered[::-1]))}")
    print(f"Random array: {check_order(counting_sort(rnd[:], max(rnd)+1))}")
    print("Checking radix sort...")
    result = check_order(radix_sort([len(ordered)*i for i in ordered]))
    print(f"Sorted array: {result}")
    result = check_order(radix_sort([len(ordered)*i for i in ordered[::-1]]))
    print(f"Inverted array: {result}")
    print(f"Random array: {check_order(radix_sort(rnd[:]))}")
