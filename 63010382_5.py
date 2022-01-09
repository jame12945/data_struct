if __name__=='__main__' :
    print("*** Fun with countdown ***")
    temp=list(input("Enter List : "))
    ans=list()
    st=list()
    for i in range(int(float(len(temp)-1)/2)):
        temp.remove(' ')
    cdup=0
    for i in range(len(temp)):
        if int(temp[-i-1])==cdup+1:
            cdup=cdup+1
        elif int(temp[-i-1])==1:
            st.append(cdup)
            cdup=1
        elif cdup>0 :
            st.append(cdup)
            cdup=0
    if cdup!=0:
        st.append(cdup)

    #ans
    #len
    print("[",end='')
    print(len(st),end='')
    print(", [",end='')
    #cd
    for j in range(len(st)):
        i=int(st[-j-1])
        print("[",end='')
        while i!=0 :
            print(i,end='')
            if i!=1 :
                print(", ",end='')
            i=i-1
        print("]",end='')
        if j!=len(st)-1:
            print(", ",end='')
        else :
            print("]]")