# seek.py

# 此示例示意sekk方法得用法

f = open('alpha_number.bin', 'rb')    #二进制读
f.read(5)
#f.seek(10, 0)
f.seek(-10, 2)
# f.seek(5, 1)

b = f.read(5)
print(b)
f.close()













