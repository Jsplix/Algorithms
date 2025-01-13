import sys
input = sys.stdin.readline
# [BOJ] 6825 Body Mass Index / 수학, 사칙연산
mass = float(input())
height = float(input())
bmi = mass / height**2
if bmi > 25: print("Overweight")
elif 18.5 <= bmi <= 25: print("Normal weight")
else: print("Underweight")