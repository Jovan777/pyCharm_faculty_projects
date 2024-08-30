def razlika(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif




list1=[5,3,2]
list2=[5,3]
lista3=razlika(list1,list2)
print(lista3)
