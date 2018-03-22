
def addteamnew():
    f=open(input("Enter new file name with .txt: "),"w+")      #creates new file
    player1=f.write(input("add player: "+"\n"))
    player2=f.write(input("add player: "+"\n"))
    player3=f.write(input("add player: "+"\n"))
    f.close()

#addteamnew()