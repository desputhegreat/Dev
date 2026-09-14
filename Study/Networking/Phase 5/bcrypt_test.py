import bcrypt

password = "mypass123".encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# Now check it:
attempt = "mypass123".encode('utf-8')
print(bcrypt.checkpw(attempt, hashed))   # True

wrong_attempt = "wrongpass".encode('utf-8')
print(bcrypt.checkpw(wrong_attempt, hashed))   # False
