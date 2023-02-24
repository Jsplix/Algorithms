import sys
input = sys.stdin.readline
# [BOJ] 4659 비밀번호 발음하기 / 구현, 문자열
vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    test_case = input().rstrip()
    if test_case == 'end': break
    flag = True
    if 'a' in test_case or 'e' in test_case or 'i' in test_case or 'o' in test_case or 'u' in test_case:
        char_seq = 1
        vowel_seq = 1 if test_case[0] in vowel else 0
        conso_seq = 0 if vowel_seq else 1 # 첫번째 글자가 모음이면 0
        for i in range(1, len(test_case)):
            if test_case[i] in vowel: 
                vowel_seq += 1
                conso_seq = 0
            else: 
                vowel_seq = 0
                conso_seq += 1

            if test_case[i-1] == test_case[i]: char_seq += 1
            else: char_seq = 1

            if char_seq == 2 or vowel_seq == 3 or conso_seq == 3:
                if char_seq == 2 and (test_case[i] != 'e' and test_case[i] != 'o'): flag = False
                if vowel_seq == 3 or conso_seq == 3: flag = False
        
        if not flag: print('<'+test_case+'>' + ' is not acceptable.')
        else: print('<'+test_case+'>' + ' is acceptable.')
    else: print('<'+test_case+'>' + ' is not acceptable.')