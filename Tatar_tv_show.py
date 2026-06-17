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
        k = int(line1[1])        
        s = input().strip()        
        counts = [0] * k
        for i in range(n):
            if s[i] == '1':
                counts[i % k] += 1        
        possible = True
        for count in counts:
            if count % 2 != 0:
                possible = False
                break                
        if possible:
            out.append("YES")
        else:
            out.append("NO")            
    sys.stdout.write("\n".join(out) + "\n")
if __name__ == '__main__':
    solve()
