class point:
    def __init__(self,stroka="0,0"):
        self.x = float(stroka[:stroka.index(",")])
        self.y = float(stroka[stroka.index(",")+1:])
    def __add__(self,other):
        return(str(self.x + other.x) + ','+str(self.y + other.y))
    def __str__(self):
        return('(' + str(self.x) + ',' + str(self.y)+')')
    def rast(self, other):
        return str((other.x +self.x)/2) + ',' + str((other.y + self.y)/2)
n = int(input())
A = point(input())
for i in range(n-1):
    B = point(input())
    A = point(A.rast(B))
print(A)
