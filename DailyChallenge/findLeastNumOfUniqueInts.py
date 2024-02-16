
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        map = {}
        for i in arr:
            map[i] = map.get(i, 0) + 1

        n = len(arr)

        # List to track the frequencies of frequencies
        # The maximum possible frequency of any element
        # will be n, so we'll initialize this list with size n + 1
        count_of_frequencies = [0] * (n + 1)

        # Populating count_of_frequencies list
        for count in map.values():
            count_of_frequencies[count] += 1

        # Variable to track the remaining number of unique elements
        remaining_unique_elements = len(map)

        # Traversing over all possible frequencies
        for i in range(1, n + 1):
            # For each possible frequency i, we'd like to remove as
            # many elements with that frequency as possible.
            # k // i represents the number of maximum possible elements
            # we could remove with k elements left to remove.
            # count_of_frequencies[i] represents the actual number of elements
            # with frequency i.
            num_elements_to_remove = min(k // i, count_of_frequencies[i])

            # Removing the maximum possible elements
            k -= (i * num_elements_to_remove)

            # num_elements_to_remove is the count of unique elements removed
            remaining_unique_elements -= num_elements_to_remove

            # If the number of elements that can be removed is less
            # than the current frequency, we won't be able to remove
            # any more elements with a higher frequency so we can return
            # the remaining number of unique elements
            if k < i:
                return remaining_unique_elements

        # We have traversed all possible frequencies i.e.,
        # removed all elements. Returning 0 in this case.
        return 0

'''
# Idea-1 (use sorting)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the frequency of each element
        frequency = {}
        for elem in arr:
            frequency[elem] = frequency.get(elem, 0) + 1

        # Sort the elements based on frequency, and then by value if frequencies are equal
        sorted_arr = sorted(arr, key=lambda x: (frequency[x], x))

        # convet sorted array (after k index) into set to count least elements 
        arr=set(sorted_arr[k:])
        return len(arr)
        # T.C -> O(n logn)
        # S.C -> O(n)
'''
