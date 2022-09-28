import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable

countrycode = str(input("What is the countrycode?"))

#Scan the list l line by line and add 1 to the counter if the country is the one looked for

counter = 0

for item in l:
    if item == countrycode:
        counter = counter + 1

#Format and print the result

print("The countrycode appears in the list {} many times".format(counter))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
done = False
while done == False:
    try:
        Population = int(input("What is the population you are looking for?"))
        done = True
    except:
             print("Incorrect input")

#Store the population values into a list called l1 (see line 6)

l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list

lstOfRecords = list ()

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords

for item in l1:
    if item > Population:
        lstOfRecords.append(l1.index(item))

#Print the list l1

print(lstOfRecords)

#Bonus: Print the name of the cities whose index is in l1

for bonus in lstOfRecords:
   print(db.ws(ws='Sheet1').col(col=2)[bonus])


