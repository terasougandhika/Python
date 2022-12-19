
#uppercase vowels
def conVowUpp(str):
	
	# Stores the length
	# of str
	N = len(str)
	str1 =""
	for i in range(N):
		if (str[i] == 'a' or str[i] == 'e' or
			str[i] == 'i' or str[i] == 'o' or
			str[i] == 'u'):
			c = (str[i]).upper()
			str1 += c
		else:
			str1 += str[i]
	print(str1)
if __name__ == '__main__':
	
	str = input("Enter the string: ")
	conVowUpp(str)

# count vowles individually
print("Counting Vowels: ")
print("a: ",str.count('a'))
print("e: ",str.count('e'))
print("i: ",str.count('i'))
print("o: ",str.count('o'))
print("u: ",str.count('u'))

#vowels count 
add = 0
for x in str:
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A'
       or x == 'E' or x == 'I' or x == 'O' or x == 'U'):
        add = add + 1
print("There are total of",add,"vowels")

#list the string
List_words = str.split()
print("list of words: ", List_words)
print("length of list: ", len(List_words))
