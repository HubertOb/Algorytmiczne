class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1
        self.idzie = False


def g(v):
    if v.g != -1:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g


def f(v):
    if v.f != -1:
        return v.f
    f1 = g(v)
    f2 = v.fun
    for u in v.emp:
        f2 += g(u)
    v.f = max(f1, f2)
    return v.f


def solution(v,z=0):
    if z==0:
        if v.f>v.g:
            v.idzie=True
            for u in v.emp:
                solution(u,1)
        else:
            for u in v.emp:
                solution(u,0)
    else:
        for u in v.emp:
            solution(u, 0)


a1 = Employee(50)
a2 = Employee(10)
a3 = Employee(25)
a4 = Employee(40)
a5 = Employee(17)
a6 = Employee(0)
a7 = Employee(25)
a8 = Employee(0)
a9 = Employee(0)
a10 = Employee(0)
a11 = Employee(0)
a12 = Employee(0)
a13 = Employee(5)
a14 = Employee(20)
a15 = Employee(15)
a16 = Employee(10)
a17 = Employee(6)
a18 = Employee(17)
a19 = Employee(500)
a20 = Employee(20)
a21 = Employee(10)
a22 = Employee(100)
a1.emp.append(a2)
a1.emp.append(a3)
a1.emp.append(a4)
a2.emp.append(a5)
a2.emp.append(a6)
a2.emp.append(a7)
a6.emp.append(a8)
a6.emp.append(a9)
a9.emp.append(a10)
a9.emp.append(a11)
a9.emp.append(a12)
a4.emp.append(a13)
a4.emp.append(a14)
a4.emp.append(a15)
a4.emp.append(a16)
a13.emp.append(a17)
a13.emp.append(a18)
a15.emp.append(a19)
a15.emp.append(a20)
a19.emp.append(a21)
a21.emp.append(a22)

f(a1)
solution(a1)
print("1.   ", a1.f, a1.g, a1.idzie)
print("2.   ", a2.f, a2.g, a2.idzie)
print("3.   ", a3.f, a3.g, a3.idzie)
print("4.   ", a4.f, a4.g, a4.idzie)
print("5.   ", a5.f, a5.g, a5.idzie)
print("6.   ", a6.f, a6.g, a6.idzie)
print("7.   ", a7.f, a7.g, a7.idzie)
print("8.   ", a8.f, a8.g, a8.idzie)
print("9.   ", a9.f, a9.g, a9.idzie)
print("10.  ", a10.f, a10.g, a10.idzie)
print("11.  ", a11.f, a11.g, a11.idzie)
print("12.  ", a12.f, a12.g, a12.idzie)
print("13.  ", a13.f, a13.g, a13.idzie)
print("14.  ", a14.f, a14.g, a14.idzie)
print("15.  ", a15.f, a15.g, a15.idzie)
print("16.  ", a16.f, a16.g, a16.idzie)
print("17.  ", a17.f, a17.g, a17.idzie)
print("18.  ", a18.f, a18.g, a18.idzie)
print("19.  ", a19.f, a19.g, a19.idzie)
print("20.  ", a20.f, a20.g, a20.idzie)
print("21.  ", a21.f, a21.g, a21.idzie)
print("22.  ", a22.f, a22.g, a22.idzie)
