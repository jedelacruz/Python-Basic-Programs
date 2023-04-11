# this program checks if you can apply as a flight attendant

print("=============== Flight Attendant Form ===============")

print()
name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height (CM): "))
piercings = input("Facial Piercings (Y/N): ")
tattoos = input("Visible Tattoos (Y/N): ")
hdegree = input("Highschool Degree (Y/N): ")

print()
print("====================== Results ======================")
print()

print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height))
print("Facial Piercings: " + piercings.upper())
print("Visible Tattoos: " + tattoos.upper())
print("Highschool Degree: " + hdegree.upper())
print()

if (age >= 21 and height >= 157.48 and height <= 190.50 and piercings.upper() == "N" and tattoos.upper() == "N" and hdegree.upper() == "Y"):
    print("Congratulations " + name + " you can apply as a Flight Attendant")
else:
    print("Sorry " + name + " you cannot apply")
