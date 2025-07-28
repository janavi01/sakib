def MergeSort(array):
    if len(array)>1:
        mid=int(len(array)/2)
        L=array[:mid]
        R=array[mid:]
        MergeSort(L)
        MergeSort(R)
        i=0
        j=0
        k=0
        while i <len(L)and j <len(R):
            if L[i]<=R[j]:
                array[k]=L[i]
                i=i+1
                k=k+1
            elif L[i]>R[j]:
               array[k]=R[j]
               j=j+1
               k=k+1
            while i<len(L):
              array[k]=L[i]
              k=k+1
              i=i+1
            while j<len(R):
              array[k]=R[j]
              k=k+1
              j=j+1

array1=[8,9,2,5,7,1,6,4,3,0]
print("Unsorted List",array1)
MergeSort(array1)
print("Sorted List", array1)
