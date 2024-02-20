import json

jsonFile = open("jsonTexto.json", "r")
data_archivo = jsonFile.read()
jsonFile.close()

data = json.loads(data_archivo)

for x in data:
    print(x)