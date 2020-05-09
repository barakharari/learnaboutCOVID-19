def binarySearch(data, searchValue, low, high):
    if high < low:
        return []
    mid = int((low + high) / 2)
    if data[mid] < searchValue:
        return binarySearch(data, searchValue, mid, high)
    elif data[mid] > searchValue:
        return binarySearch(data, searchValue, low, mid)
    else:
        return data[mid]
