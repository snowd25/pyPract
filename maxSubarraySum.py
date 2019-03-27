#Python Program to solve Maximum Subarray Problem using Kadane’s Algorithm
def maxSubArray(index1,lst):
	#print("In Func : ",lst)
	new_lst = []
	sum = 0
	for i in range(0,len(lst)):
		sum += lst[i]
		new_lst.append((index1,index1+i,sum))
	new_lst1 = sorted(new_lst, key = lambda s1: s1[-1])
	#print(new_lst1)
	return (new_lst1[-1])

lst1 = list(input())
#print(lst1)
nl = []
for i in range(0,len(lst1)-1):
	#print("a: ",lst1[i])
	nl.append(maxSubArray(i,lst1[i::]))
nl1 = list(sorted(nl,key = lambda x : x[-1]))
#print("nl1: ",nl1)
print("Max sum subarray starts at index {0} and ends at {1} with a sum of {2}".format(nl1[-1][0],nl1[-1][1],nl1[-1][2]))
