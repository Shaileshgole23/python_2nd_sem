single_quoted='hello ,world!'
print(single_quoted)
double_quoted="hello again!"
print(double_quoted)
escaped_string="she said, \"hello\""
print(escaped_string)
escaped_string1='she said,"hello"'
print(escaped_string1)
 
print('\'hello\'')

#concatenation 
first_name="hii"
last_name="hello"
full_name= first_name+" " + last_name
print(full_name)

#repetition
repeated_text="welcome\n" * 10 # if you remove \n then result is welcomewelcomewelcomewelcome
#and use \t for space like welcome welcome welcome
print(repeated_text)

#length
text="python"
length=len(text)
print("length:",length)

