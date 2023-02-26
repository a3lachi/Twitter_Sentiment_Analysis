import os 

Data = ''
files = os.listdir('data')
for a in files[:10] :
    if '.txt' in a :
        f = open('./data/'+a,'r')
        ata = f.read()
        Data += ata
        f.close()

Data = Data.split("------------------------------")

Tada = []

for a in Data :
    Tada.append(list(a.split('\n')))

for k in range(len(Tada)) : 
    j=0
    i=0
    while (i-j<len(Tada[k])) :
        if Tada[k][i-j] == '' :
            Tada[k].pop(i-j)
            j+=1
        elif 'Afficher cette' in Tada[k][i-j] :
            Tada[k].pop(i-j)
            j+=1
        elif Tada[k][i-j] == '·' :
            Tada[k].pop(i-j)
            j+=1
        i+=1
    try : 
        if Tada[k][-4].isnumeric() or (Tada[k][-4].split(' ')[0]+Tada[k][-4].split(' ')[1]).isnumeric() :
            Tada[k] = Tada[k][:-4]
    except : 
        pass
    k+=1


for a in Tada :
    try :
        print(a[-4] + '--' +a[-3] + '--' +a[-2] + '--' +a[-1]  )
    except :
        print("HADaaa",a)






