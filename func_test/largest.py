def large(x,y):
    if x>y:
        a=x
        b=y
    else:
        a=y
        b=x

    m1 = a%b
    while True:
        if(m1==0 or m1==1):
            break
        a=b
        b=a%b
        # print(a,b)

    print(b)
# large(96,15)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 示例用法
num1 = 16
num2 = 12
result = gcd(num1, num2)
print(f"{num1} 和 {num2} 的最大公约数是 {result}")
