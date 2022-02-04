def searchMatrix(matrix, target):
#         # Approach01
#         m=len(matrix)
#         n=len(matrix[0])
#         row=0
#         column=n-1

#         while(row<m and column>-1):
#             #print(row,column)
#             if matrix[row][column]<target:
#                 row+=1
#             elif matrix[row][column]>target:
#                 column-=1
#             else:
#                 return True

#         return False

    #Approach02 // Binary Search
    if target<matrix[0][0]: return False

    row=len(matrix)
    col=len(matrix[0])

    low=0
    high=row*col-1

    while low<=high:
        midIdx=low+(high-low)//2

        elem=matrix[midIdx//col][midIdx%col]
        #print(low, high,midIdx,midIdx//col, midIdx%col,elem)
        if target==elem: return True
        elif target<elem: high=midIdx-1
        else: low=midIdx+1

    return False

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix,target))
