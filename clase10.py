numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Irmin",
               "Apellido": "Corona",
               "Altura": 1.75,
               "Edad": 34}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Irmin": {"Apellido": "Corona",
               "Altura": 1.75,
               "Edad": 34},
                "Sally": {"Apellido": "Sha",
               "Altura": 1.65,
               "Edad": 27}}
print(contacts["Sally"])