def longest_switching_slice(A):
    n = len(A)
    max_length = 1
    current_length = 1

    for i in range(1, n):
        if (A[i] % 2 == 0 and A[i - 1] % 2 != 0) or (A[i] % 2 != 0 and A[i - 1] % 2 == 0):
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


print(longest_switching_slice([3, 2, 3, 2, 3]))
