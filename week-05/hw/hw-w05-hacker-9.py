if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrlist = set(arr)
    arrlist.remove(max(arrlist))
    print(max(arrlist))