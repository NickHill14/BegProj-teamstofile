#while input()!='1':

def printteam():
    try:
        f = open(input("Which file do you want to open: "))
        print(f.read().split(','))
        f.close()
    except FileNotFoundError:
        print("error1\nCould not find file")
    except NameError:
            print("error2")

#print("Enter 1 to exit \n or enter to try again")



#f=open("tmlist.txt","r")
#print (f.read().split())
#f.close