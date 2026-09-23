#check if it contains any hidden message or not
m=input("Enter a string: ")
a=input("Enter the hidden message: ")

if a in m:
	print("Secret message found!")
else:
	print("No secret message found!") 