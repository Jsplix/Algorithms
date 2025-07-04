from collections import defaultdict
# [BOJ] 1622 공통 순열 / 문자열, 정렬
while True:
    try:
        a = input()
        b = input()

        a_dict = defaultdict(int)
        for c in a:
            a_dict[c] += 1
        
        result = []
        for c in b:
            if a_dict[c]:
                cnt = result.count(c)
                if not cnt: result.append(c)
                else:
                    if cnt < a_dict[c]: result.append(c)
                    else: continue
            else: continue
        result.sort()
        print(''.join(result))
    except:
        break