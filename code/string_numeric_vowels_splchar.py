str = input("enter the string: ")
digit_count = 0
vowel_count = 0
special_count = 0
for ch in str.lower():
    if ch.isdigit():
        digit_count += 1
    elif ch.isalpha():
        if ch in ["a","e","i","o","u"]:
            vowel_count+=1
    else:
        special_count+=1
print(f"digit_count : {digit_count}")
print(f"vowel_count : {vowel_count}")
print(f"special_count : {special_count}")
