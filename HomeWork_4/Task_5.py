# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

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


