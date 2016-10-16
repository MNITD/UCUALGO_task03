def insertion_sort(data):
    counter = 0
    i = 1
    while i < len(data):
        temp = data[i]
        j = i
        while j > 0 and data[j - 1] > temp:
            data[j] = data[j - 1]
            counter += 1
            j -= 1
        data[j] = temp
        counter += 1
        i += 1

    return data, counter


def merge(set_one, begin, mid, end, set_two):
    n = begin
    m = mid
    counter = 0
    while n < end:
        counter += 1
        if begin < mid and (m >= end or (set_one[begin] <= set_one[m])):
            set_two[n] = set_one[begin]
            begin += 1
        else:
            set_two[n] = set_one[m]
            m += 1
        n += 1

    return counter


def merge_sort_actual(set_one, begin, end, set_two):
    if (end - begin) < 2:
        return 0
    counter = 0
    mid = int((begin + end) / 2)
    counter += merge_sort_actual(set_two, begin, mid, set_one)
    counter += merge_sort_actual(set_two, mid, end, set_one)
    counter += merge(set_one, begin, mid, end, set_two)

    return counter


def merge_sort(data):
    counter = merge_sort_actual(data.copy(), 0, len(data), data)
    return data, counter


def swap(data, a, b):
    t = data[a]
    data[a] = data[b]
    data[b] = t


def partition(data, begin, end):
    counter = 0
    pivot = data[end]
    wall = begin - 1
    current = begin
    while current < end:
        counter += 1
        if data[current] <= pivot:
            wall += 1
            swap(data, wall, current)
            # temp = data[wall]
            # data[wall] = data[current]
            # data[current] = temp
        current += 1
    swap(data, wall + 1, end)
    # temp = data[wall + 1]
    # data[wall + 1] = data[end]
    # data[end] = temp
    return wall + 1, counter


def quick_sort_actual(data, begin, end):
    counter = 0
    if begin < end:
        result = partition(data, begin, end)
        counter += result[1]
        counter += quick_sort_actual(data, begin, result[0] - 1)
        counter += quick_sort_actual(data, result[0] + 1, end)
    return counter


def quick_sort(data):
    counter = quick_sort_actual(data, 0, len(data) - 1)
    return data, counter


def quick_sort_3m_actual(data, begin, end):
    counter = 0
    if begin < end:
        if end - begin + 1 > 3:
            mid = int((begin + end) / 2)

            # if data[begin] > data[end]:
            #     swap(data, begin, end)
            # if data[begin] > data[mid]:
            #     swap(data, begin, mid)
            # if data[mid] > data[end]:
            #     swap(data, mid, end)

            if data[begin] < data[end]:
                if data[mid] < data[end]:
                    if data[begin] < data[mid]:
                        swap(data, mid, end)
                    else:
                        swap(data, begin, end)
            else:
                if data[end] < data[mid]:
                    if data[begin] < data[mid]:
                        swap(data, begin, end)
                    else:
                        swap(data, mid, end)

            result = partition(data, begin, end)
            counter += result[1]
            counter += quick_sort_3m_actual(data, begin, result[0] - 1)
            counter += quick_sort_3m_actual(data, result[0] + 1, end)
        else:
            # print(data[begin], data[begin + 1], data[end])
            # counter += 1
            # if data[begin] > data[end]:
            #     swap(data, begin, end)
            # counter += 1
            # if data[begin] > data[begin + 1]:
            #     swap(data, begin, begin + 1)
            # counter += 1
            # if data[begin + 1] > data[end]:
            #     swap(data, begin + 1, end)
            # print(data[begin], data[begin + 1], data[end])

            i = begin + 1
            while i < end + 1:
                temp = data[i]
                j = i
                while j > begin and data[j - 1] > temp:
                    data[j] = data[j - 1]
                    counter += 1
                    j -= 1
                counter += 1
                data[j] = temp
                i += 1

    return counter


def quick_sort_3m(data):
    counter = quick_sort_3m_actual(data, 0, len(data) - 1)
    return data, counter


# print(insertion_sort([]))
# print(insertion_sort([1, 1, 1, 1]))
# print(insertion_sort([1, 2, 3, 4, 5, 6]))
# print(insertion_sort([6, 5, 4, 3, 2, 1]))
# print(insertion_sort([2, 4, 6, 5, 3, 1]))
# print(insertion_sort([6, 4, 2, 1, 3, 5]))
# print(insertion_sort([1, 3, 5, 7]))
# print(insertion_sort([2, 4, 6, 8]))
# print(insertion_sort([3, 8, 5, 1, 2, 9]))
#
# print(merge_sort([]))
# print(merge_sort([1, 1, 1, 1]))
# print(merge_sort([1, 2, 3, 4, 5, 6]))
# print(merge_sort([6, 5, 4, 3, 2, 1]))
# print(merge_sort([2, 4, 6, 5, 3, 1]))
# print(merge_sort([6, 4, 2, 1, 3, 5]))
# print(merge_sort([1, 3, 5, 7]))
# print(merge_sort([2, 4, 6, 8]))
# print(merge_sort([3, 8, 5, 1, 2, 9]))
#
# print(quick_sort([]))
# print(quick_sort([1, 1, 1, 1]))
# print(quick_sort([1, 2, 3, 4, 5, 6]))
# print(quick_sort([6, 5, 4, 3, 2, 1]))
# print(quick_sort([2, 4, 6, 5, 3, 1]))
# print(quick_sort([6, 4, 2, 1, 3, 5]))
# print(quick_sort([1, 3, 5, 7]))
# print(quick_sort([2, 4, 6, 8]))
# print(quick_sort([3, 8, 5, 1, 2, 9]))
#
# print(quick_sort_3m([]))
# print(quick_sort_3m([1, 1, 1, 1]))
# print(quick_sort_3m([1, 2, 3, 4, 5, 6]))
# print(quick_sort_3m([6, 5, 4, 3, 2, 1]))
# print(quick_sort_3m([2, 4, 6, 5, 3, 1]))
# print(quick_sort_3m([6, 4, 2, 1, 3, 5]))
# print(quick_sort_3m([1, 3, 5, 7]))
# print(quick_sort_3m([2, 4, 6, 8]))
# print(quick_sort_3m([3, 8, 5, 1, 2, 9]))
