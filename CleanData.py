import os 


def CheckNum(strng) :
    if strng.isnumeric() :
        return True 
    try :
        if (strng.split(' ')[0]+strng.split(' ')[1]).isnumeric() :
            return True
    except :
        return False

def LoadData(Folder)
    Data = ''
    files = os.listdir('data/'+Folder)
    for a in files :
        if '.txt' in a :
            f = open('./data/'+Folder+'/'+a,'r')
            ata = f.read()
            Data += ata
            f.close()
    return Data

def ProcessData(Data) :
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
                if Tada[k][i-j] in ['Afficher cette discussion' , 'En réponse à ' , '·' , '' ] or Tada[k][i-j][0]=='#'  :
                    Tada[k].pop(i-j)
                    j+=1
                try :
                    if Tada[k][1][0] == '@' :
                        Tada[k] = Tada[k][2:]
                except :
                    pass
                
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
        try :
            if  (a[0][0]).isnumeric() :
                Data.append(a[1:])
        except :
            pass


    Tada = []
    for i in range(len(Data)) :
        if len(Data[i])==2 :
            Data[i].pop(1)
        Tada.append(Data[i])

    return Tada







