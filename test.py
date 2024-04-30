import re

password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
if re.match(password_pattern, 'secret'):
    print("valid")
else:
    print("invalid")