from parser.parser import Parser

file = open("example.json")
schema = file.read()

print("Parsing schema")

parser = Parser(schema)

print("Parsed schema ")
