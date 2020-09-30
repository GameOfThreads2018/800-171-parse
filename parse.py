import csv 
import json

class Control:
    def __init__(self, id, title, prose):
        self.id = id
        self.title = title
        self.prose = prose

    def to_dict(self):
        return  {'id': self.id, 'title': self.title , 'prose': self.prose}

filepath = input("Enter filepath: ")

def parse_source(filepath):
     control_list = []
     with open(filepath, newline = '', encoding = 'utf-8') as fp:
        line = csv.reader(fp)
        for row in line:
            control_list.append(Control(row[0], row[1], row[2]))
        return control_list

control_list = parse_source(filepath)
response = [control.to_dict() for control in control_list]
json_string = json.dumps( {'controls' : response})
print(json_string)

