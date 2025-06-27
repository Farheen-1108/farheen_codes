size = int(input("enter the pateints input: "))
list = []
gene=[]
for i in range(size):
    temp = float(input(f"enter the list of patients {i} is: "))
    list.append(temp)
for temp in list:
    if i<=5:
        gene.append("Underexpressed")
    elif 5<i<15:
        gene.append("Normal")
    else:
        gene.append("Overexpressed")
print(gene)