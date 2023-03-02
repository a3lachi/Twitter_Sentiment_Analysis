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
        Tada.append(list(a.split('\n'))[1:])


    ## Extract 'User'
    for i in range(len(Tada)) :
        if len(Tada[i])>1 and len(Tada[i][1])>1 :
            Tada[i]=[Tada[i][1]]+Tada[i][4:]
        Tada[i].pop(-1)

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
            if Tada[i][j] in ['GIF' , 'ALT' , 'Afficher cette discussion']  :
                Tada[i].pop(j)
            elif Tada[i][j]=='Citer le Tweet' :
                Tada[i].pop(j)
                Tada[i].pop(j)
                Tada[i].pop(j)
                Tada[i].pop(j)
                Tada[i].pop(j)
            else :
                j+=1

    Data = []
    c = 0
    for a in Tada :
        if len(a)>1 :
            tweet = a[1]
            for tw in a[2:] :
                tweet+=tw 
            Data.append([a[0],tweet])
    

    df = pd.DataFrame(Data,columns=['User','Tweet'])
    return df


Data = LoadData('26FEB')

DataFrame = ProcessData(Data)


print('')
print('TOTAL: ',len(DataFrame.index))



print(DataFrame.head(10))










