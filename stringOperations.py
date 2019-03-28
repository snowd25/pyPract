#Python Program to Replace all Occurrences of a with $in a String.Give input in string format in quotes. as input() expects input in python format to evaluate.
def sReplace(str1):
	return str1.replace('a','$')

#Python Program to Remove the nth Index Character from a Non-Empty String
def sRemove(str1,n):
	return str1[:n] + str1[n+1:]

#Python sorted() to check if two strings are anagram or not
def sAnagram(str1,str2):
	return sorted(str1) == sorted(str2)

#Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def sExchange(str):
	return str[-1] + str[1:-1] + str[0]

#Python Program to Count the Number of Vowels in a String
def sVowel(str):
	lst = ['a','e','i','o','u']
	cnt = 0
	for i in str:
		if i in lst :
			cnt+=1
	return cnt

#Python Program to Calculate the Length of a String Without Using a Library Function
def sLen(str):
	cnt=0
	for i in str:
		cnt+=1
	return cnt


#Python Program to Remove the Characters of Odd Index Values in a String
def sOddIndexChar(str):
	lst = [x for x in str]
	lst2 = []
        for i in range(len(lst)):
		if i%2==0:
			lst2.append(lst[i])
        return ''.join(lst2)

#Program to Calculate the Number of Words and the Number of Characters Present in a String
def sNumWordsNChar(str):
	numC,numW = 0,1
	for a in str:
		numC += 1
		if a == ' ':
			numW += 1
	print("No. of words: {0} No. of Char: {1}".format(numW,numC))

#Python Program to Check if a String is a Palindrome or Not
def sPalindrome(str1):
	return str1[::1] == str[::-1]

#Python Program to Check if a String is a Pangram or Not

#Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically
def sHypenSort(str):
        lst2 = []
	print(str)
        for i in str:
        	if i != '-':
		 lst2.append(i)
	lst2.sort()
        return '-'.join(lst2)

#Python Program to Check if a Substring is Present in a Given String
def sSubStr(str,substr):
	return str.find(substr)

#Python Program to Count the Occurrences of Each Word in a Given String Sentence
def sWordOccur(str):
	lst = str.split(' ')
	dict1 = {i:lst.count(i) for i in lst}
	#for index,word in enumerate(lst):
	#	dict1[word] = index
 	return dict1

str = input("Enter for sReplace : ")
print(sReplace(str))

str = input("Enter for sRemove : ")
n = input("Enter index")
print(sRemove(str,n))

str1 = input("Enter string 2 for sAnagram : ")
str2 = input("Enter string 2 for sAnagram : ")
print(sAnagram(str1,str2))

str1 = input("Enter str for sExchange : ")
print(sExchange(str1))

str1 = input("Enter str for sVowel : ")
print(sVowel(str1))

str1 = input("Enter str for sLen : ")
print(sLen(str1))

str1 = input("Enter str for sOddIndexChar : ")
print(sOddIndexChar(str1))

str1 = input("Enter str for sNumWordsNChar : ")
sNumWordsNChar(str1)

str1 = input("Enter str for sHypenSort : ")
print(sHypenSort(str1))

str1 = input("Enter str for sSubStr: ")
substr1 = input("Enter str for sSubStr: ")
print(sSubStr(str1,substr1))

str1 = input("Enter str for sWordOccur: ")
print(sWordOccur(str1))
