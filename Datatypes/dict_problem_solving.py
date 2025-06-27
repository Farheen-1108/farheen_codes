#SUM OF THE AMINO ACID BY TAKING INPUT SEQENCE AND DIRECTLY PREDEFINING THE KEYS AND VALUES.
a_a_w = {'A': 89.1, 'C': 121.2, 'D': 133.1,'E': 147.1, 'F': 165.2, 'G': 75.1,   'H': 155.2,  'I': 131.2,  'K': 146.2,  'L': 131.2,  'M': 149.2,  'N': 132.1, 'P': 115.1, 'Q': 146.2, 'R': 174.2, 'S': 105.1, 'T': 119.1, 'V': 117.1, 'W': 204.2, 'Y': 181.2 }
seq = input("enter the sequence: ")
sum = 0
for i in seq:
    if i in a_a_w:
        sum = sum+a_a_w[i]
print(sum)
    