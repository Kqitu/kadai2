def cha(b):
    if b[0]==0:
        b[0]='S'
    elif b[0]==1:
        b[0]='C'
    elif b[0]==2:
        b[0]='D'
    else: 
        b[0]='H'
    if b[1]==1:
        b[1]='A'
    elif b[1]==11:
        b[1]='J'
    elif b[1]==12:
        b[1]='Q'
    elif b[1]==13:
        b[1]='K'
    else:
        b[1]=str(b[1])
    return b

def chksu(a):
    csu=[]
    for i in range(4):
        csu.append(a.count(i))
        g=False
    if max(csu)==5:
        g=True    
    return g

def chkyaku(a,c):
    g=chksu(a)
    d=[]
    for i in range(1,14):
        d.append(c.count(i))
    if max(d)==2:
        if d.count(max(d))==2:
            return '２ペア'
        return '１ペア'
    elif max(d)==3:
        if sorted(d)[-2]==2:
            return 'フルハウス'
        return '３カード'
    elif max(d)==4:
        return '４カード'
    else:
        d.append(d[0])
        print(d)
        for i in range(10):
            e=[1,1,1,1,1]
            print(d[i:i+5])
            if d[i:i+5]==e and g==True:
                if i==9:
                    return 'ロイヤルストレートフラッシュ'
                return 'ストレートフラッシュ'
            elif d[i:i+5]==e:
                return 'ストレート'
    if g==True:
        return 'フラッシュ'
    else:
        return 'ぶた'
    

card=[]
su=[]
kazu=[]
for i in range(5):
    b=list(map(int,input().split()))
    su.append(b[0])
    kazu.append(b[1])
    card.append(''.join(cha(b)))

print(' '.join(card))
print(chkyaku(su,kazu))