import csv 
import json

class Control:
    def __init__(self, id, title, properties):
        self.id = id
        self.title = title
        self.properties = properties

    def to_dict(self):
        return  {'id': self.id, 'title': self.title , 'properties': self.properties}

    ############### UNFINISHED this would be nested part of JSON. properties would break up into sub properties  ###################
class Property:
    def __init__(self, prop_1, prop_2, prop_3, prop_4):
        self.prop_1 = prop_1
        self.prop_2 = prop_2
        self.prop_3 = prop_3
        self.prop_4 = prop_4

    def to_dict(self):
        return  {'control policies ': prop_1, 'enforcement mechanisms': prop_2 , 'other systems':  prop_3, 'access authorizations' :  prop_4}


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

