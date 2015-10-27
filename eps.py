from decimal import Decimal
import sys
eps = sys.float_info.epsilon
x = [4,4.25]
def func(y,z):
    x.append(108 - ((815 - (1500/z))/y))
for i in range(2,101):
    func(x[i-1],x[i-2])
    print(x[i])
print(x[30])
def prov():
    return (108 - (1/(5-eps))*(815 - (1500/(5-eps)))) <= 5
if prov():
    print("Сходится к 5")
else:
    print("Несходится к 5")
