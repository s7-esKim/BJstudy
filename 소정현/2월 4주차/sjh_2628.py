x, y = map(int, input().split())

T = int(input())
cut_x_lst = [x]; cut_y_lst = [y]

for i in range(T):
    axis, cut_line = map(int, input().split())
    if axis == 0:
        cut_y_lst.append(cut_line)
    else:
        cut_x_lst.append(cut_line)

def sorted_lst(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
cut_y_lst = sorted_lst(cut_y_lst)
cut_x_lst = sorted_lst(cut_x_lst)
# ary = []


# for i in range(y):
#     ary.append([1]*x)



def minus_lst(lst):
    m_lst = [lst[0]]
    for i in range(len(lst)-1):
        m_lst.append(lst[i+1]-lst[i])
    return m_lst

def max_number(lst):
    max_num = 0
    for i in lst:
        if i >= max_num:
            max_num = i
    return max_num

    
result = max_number(minus_lst(cut_x_lst)) * max_number(minus_lst(cut_y_lst))
print(result)


