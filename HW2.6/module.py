# def count_words(n) :
# x=input()
# # n = str(n)
# count = 0
# for i in len(x):
#     count += i
def count_letters(word):
    """
    تعداد حروف یک کلمه را می‌شمارد
    """
    return len(word)

# مثال استفاده
word = "سلام"
print(f"تعداد حروف '{word}': {count_letters(word)}")