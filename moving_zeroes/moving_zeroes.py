'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    border = 0

    for ii in range(len(arr)):
        if arr[ii] != 0:
            # if the number isn't 0 then switch to the border
            arr[ii], arr[border] = arr[border], arr[ii]

        # increment the border
        if arr[border] != 0:
            border += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
