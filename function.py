def countWordsFromfile():
    filename=input("enter the file name")
    num=0
    f=open(filename,'r')
    for line in f:
        words=line.split()
        num=num+len(words)
    print("numberofwords")
    print(num)
countWordsFromfile()