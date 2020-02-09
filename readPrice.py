def readNumber1(n):
    units = [''] + list('십백천')
    nums = '일이삼사오육칠팔구'
    result = []
    i = 0
    while n > 0:
        n, r = divmod(n, 10)
        if r > 0:
            result.append(nums[r-1] + units[i])
        i += 1
    return ''.join(result[::-1])


def readNumber(n):
    a, b = [readNumber1(x) for x in divmod(n, 10000)]
    if a:
        return a + "만" + b
    return b
