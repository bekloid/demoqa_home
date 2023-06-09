# задача 2
x = int(input())
y = int(input())
def co(x,y):
     return max(x,y)
print(co(x,y))


# задача 3
x = int(input())
y = int(input())
def mod(x,y):
    from math import fabs
    if fabs(x) - fabs(y) == 135 or fabs(y) - fabs(x) ==135:
              return 'yes'
    else:
              return 'no'
print(mod(x,y))

# задача 4
month = int(input())
def seasons(months:list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))-> int:
    if month in months[-1:1]:
        return "зима"
    if month in months[-2: -4]:
        return "осень"
    if month in months[2: 4]:
        return "весна"
    if month in months [5: 7]:
        return "лето"
print(seasons(month))  #неверный вывод


#задача 5
def ten(x, y, z):
    if x > 10 and y > 10 and z > 10:
        return 'yes'
    else:
        return 'no'


print(ten(5, 15, 18))

# задача 7
y = int(input())
m = int(input())
def days(y,m):
    return 29*m*y
print(days(y, m))