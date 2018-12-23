# mylist_problem.py


print("------算法1------")
print()

a = [100]
def test(x):
    x = x + x
    print(x)
test(a)
print(a)

print()
print("-------算法2------")
print()

a = [100]
def test(x):
    x += x    # 此处与上题不同，结果也会不同
    print(x)
test(a)
print(a)
