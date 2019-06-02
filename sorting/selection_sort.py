"""
Selection Sort

In-place sort. Requires no additional storage space.
Does not scale well.

1) Find minimum value in list
2) Swap with the value in the current position
3) Repeat until the array is sorted

"""


def selection_sort(A):

    for i in range(len(A)):
        index_of_minimum = i
        for j in range(i + 1, len(A)):
            if A[j] < A[index_of_minimum]:
                index_of_minimum = j

        # Swap items
        A[i], A[index_of_minimum] = A[index_of_minimum], A[i]


if __name__ == '__main__':

    A = [534, 246, 933, 127, 321, 454, 565, 220]
    selection_sort(A)
    print(A)
