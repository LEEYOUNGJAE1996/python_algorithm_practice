def binarySearch(a[], key, left, right):
    # a[mid] = key 인 인덱스 mid 를 반환
    if (left <= right) then {
        mid = (left, right)/2
        case {
            key = a[mid]: return mid
            key < a[mid]: return binarySearch(a, key, left, mid-1)
            key > a[mid]: return binarySearch(a, key, mid + 1, right)
        }
    }
    else return -1
