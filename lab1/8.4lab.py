x = float(input())
y = float(input())
def IsPointInSquare(x, y):
    return abs(x)+abs(y) <= 1
if IsPointInSquare(x,y)==1:
    print("YES")
else:
    print("NO")