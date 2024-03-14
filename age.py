age = input("What is your age")
age = int(age)
if age >= 18:
    print("You are an Adult")
    print("You are Studying in University")
    print("You can Drive")
elif age < 18 and age > 12:
    print("you are a teenager")
    print("study hard for your future")
    print("you might have experienced your first crush")
else:
    print("you are a kid and you have so much to learn")

