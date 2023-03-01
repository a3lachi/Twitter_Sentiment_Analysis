import os 
import pandas as pd


def CheckNum(strn) :
    if strn.isnumeric() :
        return True 
    elif strn[-2:]==' k' :
        return CheckNum(strn.split('k')[0])
    else :
        spl = strn.split(' ')
        try :
            if (spl[0]+spl[1]).isnumeric() :
                return True
            else :
                if ',' in (spl[0]+spl[1]) :
                    return True 
        except :
            return False 
    return False 

## Load all data in folder and return it as a string
def LoadData(Folder) :
    Data = ''
    files = os.listdir('data/'+Folder)
    for a in files[:10] :
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
        Tada.append(list(a.split('\n'))[1:])

    df = pd.DataFrame(columns=['User','Tweet'])


    ## Extract 'User'
    for i in range(len(Tada)) :
        if len(Tada[i])>1 and len(Tada[i][1])>1 :
            Tada[i]=[Tada[i][1]]+Tada[i][4:]
        Tada[i].pop(-1)
        ##print(Tada[i][:3])

    ## eliminate En réponse à and likes/retweet/shares/seens
    for i in range(len(Tada)) :
        if len(Tada[i])>1 and Tada[i][1]=='En réponse à ' :
            Tada[i].pop(1)
            Tada[i].pop(1)
        j=0
        while j < len(Tada[i]) :
            try :
                if CheckNum(Tada[i][j]) :
                    Tada[i].pop(j)
                else :
                    j+=1
            except :
                j+=1
            
        ##print(Tada[i])
    for i in range(len(Tada)) :
        try :
            if Tada[i][1] == '  et  ' :
                Tada[i].pop(1)
                Tada[i].pop(1)
        except :
            pass

    ## print(df.head(20))

    ## remove GIF ALT
    for i in range(len(Tada)) :
        j=0
        while j < len(Tada[i]) :
            if Tada[i][j]=='GIF' or Tada[i][j]=='ALT' :
                Tada[i].pop(j)
            else :
                j+=1


    

    return Tada 


Data = LoadData('26FEB')



Tada = ProcessData(Data)


for a in Tada :
    try :
        k = a.index('Citer le Tweet')
        if k>-1 :
            print(a[k+5:])
    except :
        pass












