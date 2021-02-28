Write a Program for found a subset with given sum .

Source Code : -

#A recursive solution for subset sum
#problem

#Returns true if there is a subset
#of set[] with sun equal to given sum

def isSubsetSum(set,n,sum):
    if(sum == 0):
        return True
    if(n == 0 and sum!=0):
        return False
    #if last element is greater than
    #sum, then ignore it
    if(set[n-1]>sum):
        return isSubsetSum(set,n-1,sum);

    #else, check if sum can be obtained
    #by any of the following
    #(a)including the last element
    #(b)excluding the last element
    return isSubsetSum(set,n-1,sum) or isSubsetSum(set,n-1,sum-set[n-1])
#driver program to test above function
set = [3,34,4,12,5,2]
sum = 9
n=len(set)
if(isSubsetSum(set,n,sum)==True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")



OUTPUT : -

Found a subset with given sum
