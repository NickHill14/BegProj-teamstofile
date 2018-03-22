import edit
import add
import printfile

print("Hello World\n"
      "Welcome")

opt=True
while opt:
    print("What do you want to do")
    print("""
    1."add" to add a team file
    2."edit" to edit a team file
    3."print" to print a team file
    4."exit" to exit/quit
    """)
    opt = input()
    if opt=="add":
      add.addteamnew()
    elif opt=="edit":
      edit.addteamedit()
    elif opt=="print":
      printfile.printteam()
    elif opt=="exit":
      print("\n Goodbye") 
      opt = None            #or can use False
    else:
       print("\n Not Valid Choice Try again\n")





#print.printteam()