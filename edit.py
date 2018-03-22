
def addteamedit():
    f=open(input("which file would you like to edit"),"r+")   #adds on to existing file, w would rewrite
    print(f.read())
    team=f.write("team:     "+input("add team: ")+"\n")
    player1=f.write("player:   "+input("add player: ")+"\n")
    player2=f.write("player:   "+input("add player: ")+"\n")
    player3=f.write("player:   "+input("add player: ")+"\n")

    print(team,": ",player1,", ",player2,", ",player3)
    f.close()

#addteamedit()
