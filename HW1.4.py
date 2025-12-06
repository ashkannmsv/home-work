number = int(input("Enter a number:"))
if number > 0 and number % 2 ==0 :
     print("The number is positive and even.")
elif number > 0 and number % 2 == 1 :
     if number % 3 == 0 :
          print("It is a positive odd number and is divisible by three.")
     else :
          print("It is a positive odd number but not divisible by three.")
elif number < 0 and number % 2 == 0 :
     print("The number is negative and even.")
elif number < 0 and number % 2 == 1 :
     print("The number is negative and odd.")
elif number == 0 :
     print("Numer is zero.") 
else :
     print("What you wrote is not a number.") 


print("-----------------------------------------------------")


clock = int(input("Enter a hour:"))
if 5 <= clock <=11 :
     print("کیییییری بیدار شو کیییری")
elif 12 <= clock <= 17 :
     print("بیریم قهوه بزنیم")
elif 18 <= clock <= 22 :
     print("ستاره بچینی بوس بوس شب به خیرررر")
elif (23 <= clock <= 23) or (0 <= clock <= 4) :
     print("کسکش بزار بخوابیم صبح باید زود بیدار شیم")
else :
     print("ساعت کیر در باسنتون نیست هرزگاهی وارد کنید(لطفا بین 1 تا 23)")