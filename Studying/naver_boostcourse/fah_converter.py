def convert_c_to_f(celcius_value):
    return celcius_value * 9.0 / 5 + 32

if __name__ == '__main__':
    test = "GGG"
    print(test)
# import로 호출시 모듈의 모든 내용을 호출하게 됨 -> test라는 내용도 자동 호출되기 때문에 출력이 되는 것임
# 방지하기 위해서 if __name__ == '__main__':를 사용하면 됨