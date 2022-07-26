"""Uso de la librería JSON para tratar tipos de dato JSON"""

"""Importamos la librería JSON"""
import json

pythonDict = {"name": "Mary", "edad": 28, "dni": "2341434"}

"""Conversión de tipo da dato JSON: dumps()"""

dictToJson = json.dumps(pythonDict)
print("El dato convertido a JSON es el siguiente: {}".format(dictToJson))
print("El tipo de dato convertido es de tipo: {}".format(type(dictToJson)))