text="python"
text1="my college is GLA university"
#remove leading and trailing whitespace like "      python"  then remove space
trimmed_text=text.strip()
print(trimmed_text)

#convert to lowercase and uppercase
lower_case= text.lower()
upper_case= text.upper()
print("lowercase:", lower_case)
print("uppercase:", upper_case)

#relace
print(text.replace("python","coding")) # replace the place of python give you answer is coding

#find the position of word like i am find GLA in text1 then GLA position is 14
index= text1.find("GLA")
print("index of 'GLA':",index)


