lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst = [1, 2, 3, 4, 5, 6, 7, 8]


def sliding_window(elements, window_size):
    if len(elements) <= window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        yield elements[i:i + window_size]


sw_gen = sliding_window(lst, 3)
print(next(sw_gen))
print(next(sw_gen))
print(next(sw_gen))