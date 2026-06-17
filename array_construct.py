def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(1)
            continue    
        ans = []
        if n % 2 != 0:
            ans.append(2 * n)
            for i in range(1, n):
                if i % 2 != 0:
                    ans.append(i + 1)
                else:
                    ans.append(n + (i // 2) + 1)
        else:
            ans.append(n + 2)
            ans.append(1)
            ans.append(2 * n - 1)
            for i in range(2, n - 1):
                ans.append(i)    
        print(*(ans))
if __name__ == '__main__':
    solve()
