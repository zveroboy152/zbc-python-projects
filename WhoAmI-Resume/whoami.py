first_name="zvero"  #This is a string, a literal string
last_name="boy"

#This is a print, it prints things!  
#
# The .capitalize() method is a built-in string method in Python. It is used to capitalize the first letter of a string.
print(" ")
print("You are: "+first_name.capitalize()+" "+last_name.capitalize())
print(" ")
#This is an input that asks for your job.  | 
job = input("What is your job? ")
print(" ")
print(job.capitalize())
print(" ")
job = job.capitalize()
print(" ")
career = int(input("How many years have you been working as a " + job + "? "))
print(" ")
careerdays=str(career*365) 
careerhours=str(career*8760)
print(" ")
print("You have been working as a" + job + "for a total of " + careerdays + " days, and " + careerhours + " hours.  Wow, that's a lot of numbers.")
print(" ")