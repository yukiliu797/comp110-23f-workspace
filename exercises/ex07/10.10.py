x: list[str] = ["comp", "110"]
x[1] = "210"
y: list[str] = x
print(y)

a: str = "24"
b: str = a
a += "6"
print(b)

c: list[int] = [2,4]
d: list[int] = c
c.append(6)
print(d)

def gup(xs: list[int]):
    start_len: int = len(xs)
    i: int = 0
    while i <= start_len - 1:
        xs.append(xs[i])
        i += 1

groceries: list[str] = ["apples", "eggs"]
print(gup(groceries))
print(groceries)

