import os 
import pandas as pd


def CheckNum(strn) :
    if strn.isnumeric() :
        return True 
    elif 'k' in strn :
        return CheckNum(strn.split('k')[0])
    else :
        try :
            spl = strn.split(' ')
            if (spl[0]+spl[1]).isnumeric() :
                return True
        except :
            return False

## Load all data in folder and return it as a string
def LoadData(Folder) :
    Data = ''
    files = os.listdir('data/'+Folder)
    for a in files[:4] :
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
            pada = pd.DataFrame([Tada[i][1]],columns=['User'])
            df = pd.concat([df,pada])

            Tada[i]=Tada[i][4:]
        Tada[i].pop(-1)

    ## eliminate En réponse à
    for a in Tada :
        if len(a)>0 and a[0]=='En réponse à ' :
            a.pop(0)
            a.pop(0)
        print(a[-4:])

    ## print(df.head(20))


##Data = LoadData('26FEB')



##ProcessData(Data)



print(CheckNum('903,1 k')==True)







