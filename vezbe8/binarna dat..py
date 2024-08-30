with open('fajl.txt','r') as inputfile, open('bin.dat', 'wb') as outputfile:
    data=inputfile.read()
    outputfile.write(data.encode('ascii')) #kodirati dati string u ascii kod

with open('outfile.txt','w+') as izlazni_fajl, open('bin.dat','rb') as ulazni_fajl:
    string=ulazni_fajl.read().decode('ascii')
    izlazni_fajl.write(string)