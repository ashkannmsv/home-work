shart = True

while shart :
    world = input("Enter a world :")
    rworld = ""
    for i in world :
        rworld = i + rworld
    if world == rworld :
        print("The word is a palindrome.")
    else :        
        print(rworld)
    if world == "-1" :
        break         