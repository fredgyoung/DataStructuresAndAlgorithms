

def bubble_sort(A):

    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:

                # Swap items
                A[j], A[j-1] = A[j-1], A[j]


if __name__ == '__main__':

    A = [534, 246, 933, 127, 321, 454, 565, 220]
    bubble_sort(A)
    print(A)
