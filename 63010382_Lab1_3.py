if __name__ == '__main__' :
    print("*** Reading E-Book ***")
    print("Text , Highlight : ",end='')
    inp=input()
    hl = inp[-1]
    s = inp[0 : -2]
    for i in range(len(s)) :
        if s[i]==hl : #if find 0
            print("[",end='')
            print(hl,end='')#0
            print("]",end='')
        else :
            print (s[i],end='')