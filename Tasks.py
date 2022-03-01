class Tasks:

    def min(QList):
        minInt=0
        count=0
        for Q in QList:
            if Q.new < QList[minInt].new:
                minInt=count
            count+=1
            
        return minInt

    def main_function(QList, n):
        answers=[]
        for i in range(n):
            min=Tasks.min(QList)
            answers.append(QList[min].Q_num)
            QList[min].new=QList[min].new + QList[min].old
        return answers
