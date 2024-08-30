lista_d=[[30, 12, 2012], [21, 5, 2005], [25, 3, 2007], [18, 10, 2018], [3, 2, 2018], [12, 10, 2000], [26, 10, 2003], [6, 12, 2018], [29, 12, 2008], [12, 2, 2017], [9, 11, 2016], [10, 1, 2013], [5, 9, 2020], [8, 5, 2012], [23, 10, 2019], [5, 7, 2013], [2, 7, 2016], [23, 8, 2018], [17, 8, 2011], [15, 3, 2012], [6, 4, 2002], [17, 6, 2008], [26, 2, 2004], [10, 2, 2016], [15, 4, 2010], [21, 8, 2007], [28, 3, 2013], [30, 4, 2008], [18, 10, 2002], [11, 9, 2008], [31, 5, 2012], [8, 4, 2003], [16, 1, 2005], [10, 6, 2007], [26, 8, 2004], [2, 9, 2020]]

def provera_datuma(datum):
    datumi=[]
    datum1=input().split('.')
    datum2=input().split('.')
    for i in range(len(datum1)):
        datum1[0] = int(datum1[0])
        datum1[1] = int(datum1[1])
        datum1[2] = int(datum1[2])
    for i in range(len(datum2)):
        datum2[0] = int(datum2[0])
        datum2[1] = int(datum2[1])
        datum2[2] = int(datum2[2])

    for i in range(len(datum)):
        if (datum[i][2] > datum1[2]):
            if datum[i][2] < datum2[2]:
                datumi.append(datum[i])

    return datumi

print(provera_datuma(lista_d))