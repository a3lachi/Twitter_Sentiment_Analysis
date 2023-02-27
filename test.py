import time 

def Dotmatch(s,p) :
    if (len(s)==len(p)) :
        for i in range(len(s)) :
            if s[i]=='.' :
                return 0
            elif s[i]!=p[i] :
                return 1
        return 2
    else :
        return 3 

def isMatch(s, p):
    print('s --> ' ,s)
    print('p --> ', p)
    pi = p.split('*')
    print('mfrqa --> ',pi)
    ppi = len(pi)
    b=0
    bb=len(pi[b])
    if(ppi>1) :
        while (b<ppi and pi[b]!='' and s[:bb]!='') :
            bb=len(pi[b])
            print(pi[b],' -- ',s[:bb])
            zlt = Dotmatch(pi[b],s[:bb])
            if zlt == 2 :
                s=s[bb:]
            elif zlt in [0,1] :
                b+=1

        return s==''
    else :
        if Dotmatch(p,s)==3 :
            return False 



print(isMatch("mississippi",'mis*is*ip*.'))