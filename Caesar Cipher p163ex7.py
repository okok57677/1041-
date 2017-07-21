def main():
	message = input("Plaintext - ")
	key = eval(input("key - "))
	for ch in message:
		print(chr(ord(ch)+key),end="")
	print()
main()
