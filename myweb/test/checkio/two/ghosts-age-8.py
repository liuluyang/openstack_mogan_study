#coding:utf8
def fb():   #make Fibonacci number
    x = 0
    y = 1
    fb_list = []
    while True:
        x,y = y,x+y
        if x > 5000:
            break
        fb_list.append(x)
    return fb_list
def make_opacity():  #make opacity-age
    base_opacity = 10000
    opacity_age = [(10000,0)]
    for i in range(1,5001):
        if i in f:
            base_opacity -=i
        else:
            base_opacity +=1
        opacity_age.append((base_opacity,i))
    return opacity_age
    
f = fb()
opacity_age = make_opacity()

def checkio(opacity):
    if opacity==10000:
        return 0
    for x,y in opacity_age:
        if x==opacity:
            return y

#code review
#逆向求解
'''
def checkio(opacity):
    fib_a, fib_b = 1,1
    age = 0

    while opacity != 10000:
        age += 1
        if age == fib_b:
            opacity += fib_b
            fib_a, fib_b = fib_b, fib_a + fib_b
        else:
            opacity -= 1
    else:
        return age
'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"