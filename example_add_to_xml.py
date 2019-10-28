#add data to xml using flask
#flask imports
from flask import Flask,request

#xml imports
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

app = Flask(__name__)

@app.route('/')
def example_to_add_data_to_xml ():
    tree = ET.parse('test.xml')
    root = tree.getroot()
    record = ET.Element("record")
    Name = ET.SubElement(record,"Name")
    OrganisationNumber = ET.SubElement(record,"OrganisationNumber")
    PersonalNumber = ET.SubElement(record,"PersonalNumber")
    PhoneNumber = ET.SubElement(record,"PhoneNumber")
    Name.text = "Shreyas Basutkar"
    OrganisationNumber.text = "16480228-4443"
    PersonalNumber.text = "16480228-300400"
    PhoneNumber.text = "1-174-712-034445" 
    root.append(record)
    tree.write("test.xml")
    return "added"

if __name__ == "__main__":
    app.run(debug=True)