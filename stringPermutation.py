#Python Program to Print All Permutations of a String in Lexicographic Order using Recursion

#without using permutations builtin
def permuteStr(lst,l,r):
	if l == r:
		print("".join(lst))
	else:
		for i in range(l,r+1):
			lst[l],lst[i] =lst[i],lst[l]
			permuteStr(lst,l+1,r)
			lst[l],lst[i] =lst[i],lst[l]

# permutations using library function 
from itertools import permutations
def permuteStr1(lst):
	print("Using permutations:")
	p = permutations(lst)
	for ch in p:
		print("".join(ch))
	
str1 = input()
print("Without using permutations:")
permuteStr(list(str1),0,len(str1)-1)
permuteStr1(list(str1))

