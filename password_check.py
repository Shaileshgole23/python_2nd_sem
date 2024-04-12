while True:
    password=input("Enter your password:")
    if len(password)<=12:
        print("password should be at least 13 chracters lon.")
        continue
    else:
      uppercase=False
      lowercase=False
      digit=False
      special=False
      space=False
      for char in password:
         if char.isalpha():
            if char.isupper():
               upper=True
            elif
