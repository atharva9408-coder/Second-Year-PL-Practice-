msg=input("Enter message with secret code: ")
c=input("Enter the secret msg to find:")
if(c in msg):
	print("Secret Message found!")
else:
	print("Secret message not found")