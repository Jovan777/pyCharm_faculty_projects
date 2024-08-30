def isArithmeticProgression ( arr ):
    razlika=[]
    zbir=arr[1]-arr[0]
    s=0
    lista=[]
    while s<len(arr)-1:
       razlika.append(arr[s+1]-arr[s])
       s+=1
    for i in range(len(arr)-1):
        if (arr[i]-arr[i+1])==zbir:
            lista.append(True)
        else:
            lista.append(False)
    if all(lista):
        return True
    else:
        return False


print ( isArithmeticProgression( [0, 4, 8, 12] ) )