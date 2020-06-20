import requests


def test1(x,y):
    if x>3 and y<3:
        print(x*y)
    else:
        print(x+y)

def test2():
    test=[]
    list = [1,2,3,4,5,'test','string','test2']
    for i in list:
        test.append(i)
    print(test)

def test3():
    a=1
    while a:
        print(a)
        a+=1
        if a>=20:
            break

def test4():
    numbers=[12,37,5,42,8,3,18,2,9]
    even = []
    odd = []
    while len(numbers)>0:
        number = numbers.pop()
        if number % 2 == 0:
            even.append(number)
            print(even)
        else:
            odd.append(number)
            print(odd)


def test5():
    print(test2()+test3()+test4())
# if __name__ == '__main__':
# test1(2,5)
# test2()
test5()
