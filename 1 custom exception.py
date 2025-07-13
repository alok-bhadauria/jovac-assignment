total = int(input("Enter total marks: "))
obtained = int(input("Enter obtained marks: "))

if obtained > total:
    raise Exception("Invalid Score: Obtained marks cannot be greater than total marks.")

percentage = round((obtained/total)*100, 2)
print("Percentage:", percentage)