str = input("enter the string: ")
vowel_count_upper= 0
vowel_count_lower= 0
cons_count_l = 0
cons_count_u = 0
for ch in str:
    if ch.isalpha() and ch.islower():
        if ch in ["a","e","i","o","u"]:
            vowel_count_lower+=1
        else:
            cons_count_l += 1
    if ch.isalpha() and ch.isupper():
        if ch in ["A","E","I","O","U"]:
            vowel_count_upper+=1
        else:
            cons_count_u += 1        
print("vowel_count_lower",vowel_count_lower)
print("vowel_count_upper",vowel_count_upper)
print("cons_count_l",cons_count_l)
print("cons_count_u",cons_count_u)