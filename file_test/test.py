f = open('D:/Py_work/file_test/test.txt', 'w', encoding='utf-8')
f.writelines('1\n')
f.writelines('2\n')
f.writelines('0\n')
f.close()

with open('D:/Py_work/file_test/test.txt') as f1:
    maxx = f1.readline(0)
    for line in f1:
        if line >= maxx:
            maxx = line
    print(maxx)