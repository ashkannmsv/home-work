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

#////////////////////////////////////////////////////////////////////////////////////////////


# کدت کاملا درست کار میکنه و کارت رو عالی انجام دادی و نمره کامل رو میگیری ولی برای تجربه و اموزش بیشتر چندتا نکنه رو اینجا نوشتم که اگه دوست داشتی بخونشون : 



#شرط اول خط 29 از لحاظ عملکردی درست کار میکنه ولی احتیاج به اینکار نیست و میتونی مساوی 23 قرارش بدی
#برنامه نوشته شده کاملا درست کار میکنه و اوکیه ولی برای استفاده خیلی بهینه نیست چون:
# 1. اگر میخوای که درصورتی که کاربر مقداری خارج از انتظار وارد کرده باشه بهش ارور بدی ، بهتره اینکار رو قبل از بررسی کردن ها بکنی . اینجوری سرعت کار برنامت میره بالا
# 2. برای تمام شرط هایی که گذاشتی کامپیوتر مجبوره که بین 2 تا 5 مورد رو بررسی بکنه و این توی پروژه های بزرگتر یا حلقه های عظیم سرعت برنامت رو کاهش میده و سخت افزار رو بیشتر درگیر میکنه

#نمونه کد پیشنهادی نسبت به مواردی که گفتم : 
# پیشنهاد میکنم برای حوانایی راحت تر کد رو از کامنت در بیاری 

# clock = int(input("Enter a hour: "))

# if clock > 23 or (clock < 0):
#      print("ساعت کیر در باسنتون نیست هرزگاهی وارد کنید(لطفا بین 0 تا 23)")

# elif (clock <= 4) or (clock == 23):
#      print("کسکش بزار بخوابیم صبح باید زود بیدار شیم")

# elif clock <= 11 :
#      print("کیییییری بیدار شو کیییری")

# elif clock <= 17 :
#      print("بیریم قهوه بزنیم")

# else :
#      print("ستاره بچینی بوس بوس شب به خیرررر")
