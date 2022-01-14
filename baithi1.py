name = input("Nhập tên của bạn:")
print(name)
x=len(name)
d = dict()
for i in range(1, x + 1):
    d[i] = i * i
print(d)