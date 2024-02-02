import sys
input = sys.stdin.readline
# [BOJ] 2608 로마 숫자 / 수학, 구현, 문자열
num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 
       'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

def rome_to_arab(roma):
    arab = 0
    idx = 0
    while idx != len(roma):
        if roma[idx] in num and idx != len(roma) - 1:
            chk = roma[idx] + roma[idx+1]
            if chk in num:
                arab += num[chk]
                idx += 2
            else:
                arab += num[roma[idx]]
                idx += 1
        else: 
            arab += num[roma[idx]]
            idx += 1
    return arab

def arab_to_rome(arab):
    roma = ''
    while arab != 0:
        if arab >= 1000: 
            mq = arab // 1000
            roma += 'M' * mq
            arab -= 1000 * mq

        if arab >= 100:
            hq = arab // 100
            if hq == 4: roma += 'CD'
            elif hq == 9: roma += 'CM'
            elif hq >= 5 and hq < 9: roma += 'D' + 'C' * (hq-5)
            else: roma += 'C' * hq
            arab -= 100 * hq

        if arab >= 10:
            tq = arab // 10
            if tq == 4: roma += 'XL'
            elif tq == 9: roma += 'XC'
            elif tq >= 5 and tq < 9: roma += 'L' + 'X' * (tq-5)
            else: roma += 'X' * tq
            arab -= 10 * tq

        if arab >= 1:
            if arab == 4: roma += 'IV'
            elif arab == 9: roma += 'IX'
            elif arab >= 5 and arab < 9: roma += 'V' + 'I' * (arab-5)
            else: roma += 'I' * arab
            arab = 0
        
        return roma
    
n = input().rstrip()
m = input().rstrip()

arab_n, arab_m = rome_to_arab(n), rome_to_arab(m)
arab_total = arab_n + arab_m
rome_total = arab_to_rome(arab_total)

print(arab_total, rome_total, sep='\n')