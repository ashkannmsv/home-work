the_Place_Of_Teimur = int(input("What floor is Teimur in? "))
floor_Luck = int(input("What floor is the lock? "))
shart = True
carry = ""
shomarande = 1
while shart :
    distance = input()
    if the_Place_Of_Teimur != floor_Luck :
        if carry == distance :
            shomarande += 1           
        elif shomarande % 2 == 0 :
            if carry == "U" :
                if the_Place_Of_Teimur + shomarande != floor_Luck :
                    the_Place_Of_Teimur += shomarande 
                shomarande = 1 
            elif carry == "D" :
                if shomarande < the_Place_Of_Teimur  and the_Place_Of_Teimur - shomarande != floor_Luck:
                    the_Place_Of_Teimur -= shomarande
                shomarande = 1
        else :
            shomarande = 1        
    if distance == "S" :
        if the_Place_Of_Teimur > 0 :
            the_Place_Of_Teimur -= 1
        shomarande = 1      

    carry = distance
    if distance == "Khaste Shodam!" :
        shart = False
print(F"Teimor is in the {the_Place_Of_Teimur} floor") 