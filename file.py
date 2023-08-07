# 读文件
# file = open('致橡树.txt', 'r', encoding='UTF-8')
# print(file.read())
# file.close()

# 写文件
# file = open('致橡树.txt', 'a', encoding='UTF-8')
# file.write('\n标题：《致橡树》')
# file.close()

# 复制文件
with open('致橡树.txt', 'rb') as file1, open('zxs.txt', 'wb') as file2:
    data = file1.read(512)
    while data:
        file2.write(data)
        data = file1.read()
print('复制完成')