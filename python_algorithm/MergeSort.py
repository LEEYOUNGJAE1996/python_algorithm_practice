# # MergeSort

# The merge_sort function takes an input list arr.
# It checks if the length of arr is less than or equal to
# 1. If it is, the function returns the arr as it is, as a list with 0 or 1 elements is already sorted.
# If the length of arr is greater than 1,
# the function splits it into two halves by finding the middle index mid.
# The left half is arr[:mid] and the right half is arr[mid:].
# The function then calls itself recursively on the left and right halves,
# i.e., left = merge_sort(left) and right = merge_sort(right). This continues until all sublists have a length of 0 or 1.
# Once the sublists are all sorted, the merge_sort function calls the merge function
# to merge the sorted left and right sublists into a single sorted list.
# The merge function takes two sorted lists left and right as input and returns
#  a single sorted list by comparing elements from both lists and appending the smaller element to the result list.

# The function initializes an empty list result to store the final sorted list
# and two indices i and j to keep track of the current position in the left and right lists, respectively.
# The function then enters a while loop that continues until one of the left or right lists is fully processed.
# In each iteration of the loop, the function compares the current elements of left[i] and right[j] and appends the smaller one to result.
# The index of the list from which the element was taken is then incremented by 1.
# After the while loop, the function appends any remaining elements from the left or right list that were not processed in the loop to result.
# Finally, the merge function returns result as the sorted list.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print("Merging:", result)
    return result


arr = [34, 15, 6, 3, 56, 22, 74, 33, 22, 74, 2]
sorted_arr = merge_sort(arr)
print("Sorted:", sorted_arr)
