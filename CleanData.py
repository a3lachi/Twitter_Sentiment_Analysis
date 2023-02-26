import os 


files = os.listdir('data')
for a in files[:10] :
    if '.txt' in a :
        f = open('./data/'+a,'r')
        Data = f.read()
        f.close()

Data = Data.split("------------------------------")

Tada = []

for a in Data :
    Tada.append(list(a.split('\n')))

for a in Tada : 
    j=0
    i=0
    while (i-j<len(a)) :
        if a[i-j] == '' :
            a.pop(i-j)
            j+=1
        elif 'Afficher cette' in a[i-j] :
            a.pop(i-j)
            j+=1
        elif a[i-j] == '·' :
                a.pop(i-j)
                j+=1

        i+=1


for a in Tada :
    try :
        if not a[-4].isnumeric() :
            print(a[-4])
    except :
        print(a)






