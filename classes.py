class point:
    def __init__(self,stroka="0,0"):
        self.x = float(stroka[:stroka.index(",")])
        self.y = float(stroka[stroka.index(",")+1:])
    def __add__(self,other):
        return(str(self.x + other.x) + ','+str(self.y + other.y))
    def __str__(self):
        return('(' + str(self.x) + ',' + str(self.y)+')')
    def rast(self):
        return float((self.x**2 + self.y**2)**0.5)
maximum = None
for i in range(int(input())):
    A = point(input())
    if maximum == None or maximum.rast() < A.rast():
        maximum = A
print(maximum)
