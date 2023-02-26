import os 


def CheckNum(strng) :
    if strng.isnumeric() :
        return True 
    try :
        if (strng.split(' ')[0]+strng.split(' ')[1]).isnumeric() :
            return True
    except :
        return False

Data = ''
files = os.listdir('data')
for a in files[4:50] :
    if '.txt' in a :
        f = open('./data/'+a,'r')
        ata = f.read()
        Data += ata
        f.close()

Data = Data.split("------------------------------")

Tada = []

for a in Data :
    Tada.append(list(a.split('\n')))

k=0
while  k<len(Tada) :
    if len(Tada[k])>3 :
        #Tada[k].pop(2) 
        j=0
        i=0
        while (i-j<len(Tada[k])) :
            if Tada[k][i-j] in ['Afficher cette discussion' , 'En réponse à ' , '·' , '' ]  :
                Tada[k].pop(i-j)
                j+=1
            if Tada[k][1][0] == '@' :
                Tada[k] = Tada[k][2:]
            
            i+=1

        try :
            if CheckNum(Tada[k][-4]) :
                Tada[k] = Tada[k][:-4]
            elif  CheckNum(Tada[k][-3]) :
                Tada[k] = Tada[k][:-3]
            elif  CheckNum(Tada[k][-2]) :
                Tada[k] = Tada[k][:-2]
            elif  CheckNum(Tada[k][-1]) :
                Tada[k] = Tada[k][:-1]
        except :
            pass

        k+=1

    else :
        Tada.pop(k)


Data = []
for a in Tada :
    if  (a[0][0]).isnumeric() :
        Data.append(a[1:])


j=0
for a in Data :
    if len(a)==2 :
        j+=1
        print(a)

print(j)




