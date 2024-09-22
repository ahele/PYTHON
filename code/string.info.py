message = input("Enter a message: ")

print("first character", message[0])
print("last character", message[-1])
print("Middle character", message[int(len(message)/2)])
print("Odd characters", message[::2])
print("Even characters", message[1::2])
print("Reversed message", message[::-1])