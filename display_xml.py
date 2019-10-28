#display xml data

#import flask
from flask import Flask

#import xml 
import xml.etree.ElementTree as ET 

app = Flask(__name__)

@app.route('/')
def example_display_xml():
    tree = ET.parse("data.xml")
    root = tree.getroot()
    count1 =0 
    count2 = 0
    count3=0
    count4=0
    string1 = "<table style = 'width 100%'> <tr> <th>Name</th><th>Organization number </th><th>PersonalNumber</th><th>PersonalNumber</th></tr>"
    for child in root.findall('record/Name'):
        count2 =0
        count3=0
        count4=0
        count1 = count1+ 1
        string1 += "<tr><td>"+ child.text + "</td>"
        for child in root.findall('record/OrganisationNumber'):
            count2 = count2+1
            if(count1 == count2):
                string1 += "<td>"+ child.text + "</td>"
        for child in root.findall('record/PersonalNumber'):
            count3 = count3 + 1
            if(count1 == count3):
                string1 += "<td>"+ child.text + "</td>"
        for  child in root.findall('record/PersonalNumber'):
            count4 = count4 +1
            if(count1 == count4):
                string1 += "<td>"+ child.text + "</td>"

    return string1 + "</tr></table>"

if __name__ == "__main__":
    app.run(debug=True)

