#Examples
# flask example and dealing with api get method

#flask imports here
from flask import Flask,request

#xml imports here
import xml.etree.ElementTree as ET   #for reading xml file

#global variables are defined here


app = Flask(__name__)

#basic start
@app.route('/')
def hello_there():
    return "hello there"


#xml read here
@app.route('/xml')
def xml_here():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    return "read successful"

#xml send request and search the value given 
@app.route('/search')
def xml_request():
    tree = ET.parse('data.xml')
    root = tree.getroot()
    nam = request.args.get('name')
    name=nam.replace("%"," ")
    print(name)
    #find the name given in the recourd
    count = 0
    counter = 0
    for n in root.findall('./record/Name'):
        count = count +1
        if(n.text == name):
            counter = count
            break

    if(counter != count):
        return "not matched"

    #find other data of the record
    count = 0
    OrganisationNumber = ""
    for n in root.findall('./record/OrganisationNumber'):
        count = count + 1
        if(count == counter):
            OrganisationNumber += n.text
    
    count = 0
    PersonalNumber = ""
    for n in root.findall('./record/PersonalNumber'):
        count = count + 1
        if(count == counter):
            PersonalNumber += n.text

    count = 0
    PhoneNumber = ""
    for n in root.findall('./record/PhoneNumber'):
        count = count + 1
        if(count == counter):
            PhoneNumber += n.text
    
    return "Orgamization number =" + OrganisationNumber + " " + "  Personal number = " + PersonalNumber + "  Phone number" + PhoneNumber



if __name__ == '__main__':
    app.run()


# in this I have explain how xml data can be worked as an api to given webpage if needed