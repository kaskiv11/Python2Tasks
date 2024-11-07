file = open('file.txt', 'r')
for line in file:
    print(line)


file1 = open('file.txt', 'w')
file1.write('This is the first line\n')
file1.write('Next code')
file.close()