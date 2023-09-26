m1 = "Thirty"
m2 = "Days"
m3 = "Of"
m4 = "Python"
print(m1 +" "+ m2 +" "+ m3 +" "+ m4)

n1 = "Coding"
n2 = "For"
n3 = "All"
print (n1 + " "+ n2 +" "+ n3)

Company = "Coding For All"
print(Company)

print(len(Company))

print(Company.upper())
print(Company.lower())
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())

Company.index("Coding")

Paratodo = "Python for everyone matt"
print(Paratodo.replace("everyone","All"))


xCompany = Company.split()
print(xCompany)

replace = "Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
repl2 = replace.replace(",", " ")
print(repl2)

Company_slice = Company[10]
print(Company_slice)

print(Company[::-1])

print(Company.rfind('m'))

replace3 = "Facebook", "Google", "Apple", "IBM", "Oracle", "Amazon"
repl3 = " ".join(replace3)
print(repl3)