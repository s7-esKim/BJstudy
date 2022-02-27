T = int(input())

height_array = []
for i in range(T):
    height_array.append(list(map(int, input().split())))

def sorted_lst(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i][0] > lst[j][0]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def sorted_reverse_lst(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i][0] < lst[j][0]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


height_array = sorted_lst(height_array)

def max_h(array):
    max_height = 0
    for lst in array:
        if lst[1] > max_height:
            max_height = lst[1]
    return max_height


def find_idx(array, num):
    for i in range(len(array)):
        if array[i][1] == num:
            return i

idx = find_idx(height_array, max_h(height_array))

no_reverse_lst = height_array[:idx+1]

reverse_lst = sorted_reverse_lst(height_array[idx:])

def section_s(arr):
    # print(arr)
    max_h = arr[0][1]
    max_x = arr[0][0]
    section = 0
    for lst in arr:
        if lst[1] >= max_h:
            section += abs(lst[0]-max_x) * max_h
            # print(abs(lst[0]-max_x) * max_h)
            max_x = lst[0]
            max_h = lst[1]
    return section

print(section_s(no_reverse_lst)+section_s(reverse_lst)+max_h(height_array))
