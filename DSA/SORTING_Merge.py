" in merge sort we do two thinks one is divide and other is conquer  "
#ascending order:

def mergesort(nlist):
    print("splitting ",nlist)
    if len(nlist)>1:                           # 5 greater than 2 (TRUE)
        mid = len(nlist)//2
        lefthalf = nlist[:mid]                 # 0 : 2  ---- 1(data upto)  (len/2==5/2)
        righthalf = nlist[mid::]               # 2 : 4 ------ up to last 

        mergesort(lefthalf)                    # first half
        mergesort(righthalf)                   # second half
        i=j=k=0                                #recurssive function
        while i< len(lefthalf) and j< len(righthalf):        # taking one from first half and comparing with other half
            if lefthalf[i] < righthalf[j]:                   # first lo unte first half increment avutai visversa
                nlist[k] = lefthalf[i]                       # stored in nlist.
                i = i + 1                                    
            else:
                nlist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",nlist)

nlist = [30 , 50 ,10 , 40 , 20]
mergesort(nlist)
print(nlist)


#descending order:
" in merge sort we do two thinks one is divide and other is conquer  "
def mergesort(nlist):
    print("splitting ",nlist)
    if len(nlist)>1:                           # 5 greater than 2 (TRUE)
        mid = len(nlist)//2
        lefthalf = nlist[:mid]                 # 0 : 2  ---- 1(data upto)  (len/2==5/2)
        righthalf = nlist[mid::]               # 2 : 4 ------ up to last 

        mergesort(lefthalf)                    # first half
        mergesort(righthalf)                   # second half
        i=j=k=0                                #recurssive function
        while i< len(lefthalf) and j< len(righthalf):        # taking one from first half and comparing with other half
            if lefthalf[i] > righthalf[j]:                   # first lo unte first half increment avutai visversa
                nlist[k] = lefthalf[i]                       # stored in nlist.
                i = i + 1                                    
            else:
                nlist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",nlist)

nlist = [30 , 50 ,10 , 40 , 20]
mergesort(nlist)
print(nlist)