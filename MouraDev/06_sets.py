my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Matt", "Martinez", 34}
print(len(my_other_set))
print(type(my_other_set))
print(my_other_set)
my_other_set.add("Matt_Carajo")
print(my_other_set) # Un set no es una estructura ordenada
                    # Un set no admite repetidos 
my_set = {"Matt", "Martinez", 34}
my_list = list(my_set)
print(my_list)     
print(my_list[0])     
my_other_set = {"Kotlin","Swift","Python"} 

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set.union(my_set).union({"Ayelen", "la_lokita"})))

print(my_new_set.difference(my_other_set))
