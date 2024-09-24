letter = "Hey my name is {} and i am from {}"
country="India"
name="Abirlal"

print(letter.format(name , country))

# or formet

letter = "Hey my name is {1} and i am from {0}"
country="India"
name="Abirlal"

print(letter.format(country , name  ))

# or
Price = 49.3336
txt = f"For only {Price:.2f}dollars!"

print(txt)

# or Exampal

print (f"{2*30}")