def sum_pair(array):
    array = list(map(lambda x: str(abs(x)), array))
    h = {}
    for i in array:
        if len(i) > 2:
            s = i[0] + i[-1]
            if s[0] == s[-1] and s not in h:
                h[s] = [int(i)]
            else:
                h[s].append(int(i))
    # print(h)
    maxn = 0
    for key in h:
        if len(h[key]) >= 2:
            h[key].sort()
            print(h)
            maxn = max(maxn, h[key][-1] + h[key][-2])
    return maxn


def main():
    testcase = [101, 1991]
    testcase1 = [101, 2]
    testcase2 = [101, 2002, 1991, 2442]
    testcase3 = [1, 2, 3, 4, 101, 838, 828, 808]
    testcase4 = [1]
    return sum_pair(testcase3) if sum_pair(testcase3) > 0 else -1


if __name__ == "__main__":
    print(main())
