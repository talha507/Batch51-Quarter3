# ----------------Answer # 1
# Names of Each Friend
name1:str="Anton"
name2:str="Beth"
name3:str="Chen"
name4:str="Drew"
name5:str="Ethan"
# Ages of Each Friend
age1:int=3
age2:int=4
age3:int=5
age4:int=6
age5:int=7
# For Output
print("Answer of 1")
print(name1, "is", age1, "years old.")
print(name2, "is", age2, "years old.")
print(name3, "is", age3, "years old.")
print(name4, "is", age4, "years old.")
print(name5, "is", age5, "years old.")

# ----------------Answer # 2
name:str = "Alice"
age:int = 30
city:str = "New York"
sentence=f"{name} is {age} years old and lives in {city}."
# For Output
print("Answer of 2")
print(sentence)

# ----------------Answer # 3
s3:str = "HEllo WoRlD"
# For Output
print("Answer of 3")
print(s3.capitalize())
print(s3.upper())
print(s3.lower())

# ----------------Answer # 4
s4:str = "the quick brown fox jumps over the lazy dog"
s4index = s4.find("fox")
s4count = s4.count("the")
# For Output
print("Answer of 4")
print("index of 'fox' is ", s4index)
print("'the' appears ", s4count, "times")

# ----------------Answer # 5
s5:str = "I love programming in Python"
s5replace = s5.replace("Python","Java")
# For Output
print("Answer of 5")
print(s5replace)

# ----------------Answer # 6
s6:str = "apple,banana,cherry,dates"
s6split = s6.split(",")
s6join = " ".join(s6split)
# For Output
print("Answer of 6")
print(s6split)
print(s6join)

# ----------------Answer # 7
s7:str = "         Python is fun!         "
s7strip = s7.strip()
s7ljust = s7strip.ljust(20, "*")
s7rjust = s7strip.rjust(20, "*")
# For Output
print("Answer of 7")
print(s7strip)
print(s7ljust)
print(s7rjust)

# ----------------Answer # 8
num:int = 45
binNum = bin(num)
# For Output
print("Answer of 8")
print(binNum)

# ----------------Answer # 9
base:int = 3
exponent:int = 4
result:int = base ** exponent
# For Output
print("Answer of 9")
print(result)

# ----------------Answer # 10
value:float = 12.34567
nearestint = round(value)
decimalint = round(value, 2)
# For Output
print("Answer of 10")
print("Rounded to nearest integer : ", nearestint)
print("Rounded to two decimal places : ", decimalint)