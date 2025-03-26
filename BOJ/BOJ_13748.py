import sys
input = sys.stdin.readline
# [BOJ] 13748 Periodic Strings / 문자열, 브루트포스
def is_k_periodic(s, k):
    if len(s) % k != 0:
        return False
    
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    
    for i in range(1, len(substrings)):
        prev = substrings[i-1]
        curr = substrings[i]
        
        if curr != prev[-1] + prev[:-1]:
            return False
    
    return True

def find_smallest_k(s):
    possible_k = [k for k in range(1, len(s) + 1) if len(s) % k == 0]
    
    for k in possible_k:
        if is_k_periodic(s, k):
            return k
    
    return -1

s = input().strip()
result = find_smallest_k(s)
print(result)