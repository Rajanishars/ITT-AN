import sys
def solve():
    input = sys.stdin.readline
    t_str = input()
    if not t_str:
        return
    t = int(t_str)
    out = []
    for _ in range(t):
        line1 = input().split()
        if not line1:
            break       
        n = int(line1[0])
        x = int(line1[1])
        s = int(line1[2])    
        w = input().strip()    
        dp = [-1] * (x + 1)
        dp[0] = 0
        for char in w:
            next_dp = list(dp)    
            if char == 'I':
                for j in range(x):
                    if dp[j] != -1:
                        if dp[j] + 1 > next_dp[j+1]:
                            next_dp[j+1] = dp[j] + 1
            elif char == 'E':
                for j in range(1, x + 1):
                    if dp[j] != -1 and dp[j] < j * s:
                        if dp[j] + 1 > next_dp[j]:
                            next_dp[j] = dp[j] + 1
            elif char == 'A':
                for j in range(x + 1):
                    if dp[j] != -1:
                        if dp[j] < j * s:
                            if dp[j] + 1 > next_dp[j]:
                                next_dp[j] = dp[j] + 1
                        if j < x:
                            if dp[j] + 1 > next_dp[j+1]:
                                next_dp[j+1] = dp[j] + 1
            dp = next_dp        
        out.append(str(max(dp)))
    sys.stdout.write("\n".join(out) + "\n")
if __name__ == '__main__':
    solve()
