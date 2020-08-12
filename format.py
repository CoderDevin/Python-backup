mylist = [122.6, 5945.45, 412655.2124, 47115.15455, 15445.1245]
for each in mylist:
    print(format(each, "10.5f"))
print("宽度超出指定值\n")

for each in mylist:
    print(format(each, ".5f"))
print("*不指定宽度，左对齐\n")

for each in mylist:
    print(format(each, "<15.5f"))  #宽度超出指定值"
print("带‘<’,左对齐\n")

for each in mylist:
    print(format(each, "15.5f"))  #宽度超出指定值"
print("无'<',右对齐\n")