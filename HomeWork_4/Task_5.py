
f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')
f3 = open('file3.txt', 'w')
file1 = f1.readline()
file2 = f2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            f3.write(str(int(file1[i])+int(file2[i])))
        else:
            f3.write(str(file1[i]))
    else:
        f3.write(str(file1[i]))
f1.close
f2.close
f3.close

# data = input('Введите текст: ')
# file = open('text.txt','a')
# file.write(data + '\n')



# file.close()
# file = open('text.txt', 'r')


# print(file.read())
# for line in file:
#     print(line, end="")

# file.close()
