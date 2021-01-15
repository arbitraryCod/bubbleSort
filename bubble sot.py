def sort(listOfValues):
    tempList=[]
    while tempList!=listOfValues:
        tempList=listOfValues.copy()
        for i in range(len(listOfValues)-1):
            if listOfValues[i]>listOfValues[i+1]:
                z=listOfValues[i]
                listOfValues[i]=listOfValues[i+1]
                listOfValues[i+1]=z
    return listOfValues
print(sort([5,4,3,2,1]))
