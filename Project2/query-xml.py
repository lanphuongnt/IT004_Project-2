# import xml.etree.ElementTree as ET
import time
import lxml.etree as ET
from prettytable import PrettyTable

# Get the name of query 4
# Exit the program if query-db.py hasn't run yet

try:
    xmlfile = open("xml_file_name.txt", "r", encoding='utf-8')
except:
    print("Invalid XML file. Please check xml_file_name.txt.\nMake sure you have RUN file query-db.py and NOT modified xml_file_name.txt before!!!")
    exit()
    
# Declare the name of file output
output_file = "query-xml.out"

# Read the list of file name
def get_list_xml_file_name():
    list_file_name = []
    while True:
        a_file_name = xmlfile.readline()
        a_file_name = a_file_name.strip()
        if a_file_name == "":
            break
        list_file_name.append(a_file_name)
    return list_file_name

def print_list_xml_file(list_file_name):
    table = PrettyTable(["ID", "FILENAME"])
    for i in range (len(list_file_name)):
        table.add_row([i + 1, list_file_name[i]])
    print(table)
    
# Get the XML file name in xml_file_name.txt
while True:
    list_file_name = get_list_xml_file_name()
    print("-- THE LIST OF CURRENT XML FILE --")
    print_list_xml_file(list_file_name)
    
    print("Please select a XML file by entering its ID according to the table above.\n")

    while True:
        try:
            id = int(input("Enter the ID of XML file: "))
            if 0 < id and id <= len(list_file_name):
                file_name = list_file_name[id - 1]
                break
            else:
                print("Please enter the ID which is in the table above...")
        except:
            print("Please enter the ID which is in the table above...")
            
    # Exit the program if the file doesn't has extenstion .xml
    if file_name[-4:] == ".xml":
        print(f"This query gets data from {file_name}")
        time.sleep(0.5)
        break
    else:
        print("Invalid XML file. Please check xml_file_name.txt.\nMake sure you have run file query-db.py and NOT modified xml_file_name.txt before!!!")
        exit()
     
# Input the score range
while True:
    print("Enter the score range...")
    time.sleep(0.1)
    while True:
        # Re-enter if score is not a number
        try: 
            low_score = float(input("Enter low score between 0 and 10: "))
            
            # Re-enter if score is not between 0 and 10
            if low_score < 0 or low_score > 10:
                print("Invalid score.")
            else:
                break
        except:
            print("Invalid score.")
            pass
        time.sleep(0.5)
        
    while True:
        # Re-enter if score is not a number
        try: 
            high_score = float(input("Enter high score between 0 and 10: "))
            
            # Re-enter if score is not between 0 and 10
            if high_score < 0 or high_score > 10:
                print("Invalid score.")
            else:
                break
        except:
            print("Invalid score.")
            pass
        time.sleep(0.5)
        
    # Re-enter if low score is greater than high score
    if low_score <= high_score:
        break
    else:
        print("Invalid score range.")
        time.sleep(0.5)

# Make a tree of XML data
tree = ET.parse(f'XML/{file_name}')

# Get the root of tree
root = tree.getroot()

# Print data to output_file
with open(output_file, "w", encoding='utf-8') as output:
    output.write(f"The list of students in {file_name} whose score is in the score range [{low_score}, {high_score}].\n\n")

    # XPath to find Student whose Score between low_score and high_score
    xpath_expression = f".//Student[{low_score} <= number(Score) and number(Score) <= {high_score}]"
    matching_students = root.xpath(xpath_expression)
    
    # Create a table to store data
    table = PrettyTable(["STT", "HOTEN", "NTNS", "DIEMTB"])
    
    for i in range(len(matching_students)):
        # Get information about Name, NTNS and Score
        table.add_row([i + 1, matching_students[i][0].text, matching_students[i][1].text, matching_students[i][2].text])
        
    output.write(str(table))
    output.write(f"\n\nThe query has {len(matching_students)} instances.\n")
print(f"Query is done. Please see the result in query-xml.out")

