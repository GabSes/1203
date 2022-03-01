from Tasks import Tasks
from Query import Q

def read_file():
    QList = []

    with open('read1.txt') as a:
        lines = a.readlines()

    for line in lines:
        temper=line.split()
        if temper[0] == 'Register':
            QList.append(Q(temper[1],temper[2],temper[2]))

    b = int(lines[-1])
    return QList, b

QList, b = read_file()
answers=Tasks.main_function(QList, b)
for answer in answers:
    print(answer)