# Leaders in an Array: Identify all elements in an array that are greater than all
# elements to their right. For example, in [16, 17, 4, 3, 5, 2], the leaders are [17, 5, 2].

def find_leaders(list):
    n = len(list)
    leaders = []
    max_from_right = list[-1]
    leaders.append(max_from_right)
    for i in range(n-2, -1, -1):
        if list[i] > max_from_right:
            leaders.append(list[i])
            max_from_right = list[i]
    return leaders[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))  # Output: [17, 5, 2]