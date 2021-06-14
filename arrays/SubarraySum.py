#Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S

#function takes in two values: A = array, S = sum to find
def subsum(A,S): 
    #iterate through each item as a start point in the sub array
    for i in range(len(A)): 
        #reset sub as empty array
        sub = []
        #move through remaining array and add items
        for j in range(i,len(A)):
            sub.append(A[j])
            #if the sub array has a sum equal to s then return the subarray
            if(sum(sub) == S):
                return sub
            #if the sub array is greater than s then move to next starting item
            if(sum(sub)>S):
                break

print(subsum([7,8,9,1,2,3,4],10))