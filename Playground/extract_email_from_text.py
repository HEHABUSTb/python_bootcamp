text = 'Please email us at mentor@rahulshettyacademy.com with below template to receive response '

split = text.split()
print(split)

email = [word for word in split if '@' in word]
print(email)


email2 = next((word for word in text.split() if '@' in word), 'Email not found')