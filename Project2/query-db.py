from mysql.connector import connect
from mysql.connector import Error
import time
import pandas as pd
import xml.etree.ElementTree as ET
from prettytable import PrettyTable


TIME_FORMAT = "%Y-%m-%d"    # Time format

output_file = open('query_result.txt', 'w', encoding='utf-8')   # The output file of query. The data is in tabular format

# Connect to mySQL
try:
    passwd = input("Enter mySQL password: ")
    connection = connect(
        host = 'localhost',
        user = 'root',
        password = passwd
    )
    if connection.is_connected():
        cursor = connection.cursor()
        print("Connected to MySQL.")
except Error as e:
    print("Error while connecting to MySQL ", e)
    exit()

# Print a separator line
def separator_line():
    print("\n", 60 * "-", "\n")

# Print a list of current databases
def show_databases():
    cursor.execute("SHOW DATABASES")    
    my_data = cursor.fetchall()
    my_data = [data[0] for data in my_data]
    databases = []
    table = PrettyTable(["ID", "DATABASE"])
    # Because this project is implemented on two databases TRUONGHOC1 and TRUONGHOC2, so I just check them. 
    if "truonghoc1" in my_data:
        databases.append("TRUONGHOC1")
        table.add_row([len(databases), databases[-1]])
    if "truonghoc2" in my_data:
        databases.append("TRUONGHOC2")
        table.add_row([len(databases), databases[-1]])
        
    print(table)
    return databases
    
# Print a list of current schools in this database
def show_schools():
    cursor.execute("SELECT tentr FROM truong ORDER BY tentr ASC")   # A query of TENTR
    my_data = cursor.fetchall()
    schools = [data[0] for data in my_data]
    table = PrettyTable(["ID", "SCHOOL NAME"])
    for i in range (len(schools)):
        table.add_row([i + 1, schools[i]])
    table.add_row([len(schools) + 1, "Khác"])
    print(table)    
    return schools
    
# Print a list of current school years in this database
def show_years():
    cursor.execute("SELECT DISTINCT namhoc FROM hoc ORDER BY namhoc ASC")   # A query of NAMHOC
    my_data = cursor.fetchall()
    years = [data[0] for data in my_data]
    table = PrettyTable(["ID", "SCHOOL YEAR"])
    for i in range (len(years)):
        table.add_row([i + 1, years[i]])
    table.add_row([len(years) + 1, "Khác"])
    print(table)    
    return years

# Print a list of current ranks in this database
def show_ranks():
    ranks = ["Xuất sắc", "Giỏi", "Khá", "Trung Bình", "Yếu"]
    table = PrettyTable(["ID", "RANK"])
    for i in range (len(ranks)):
        table.add_row([i + 1, ranks[i]])
    print(table)    
    return ranks

# Choose a database
def input_database():
    
    separator_line()
    
    print("### THE LIST OF DATABASES ###")
    # Get the list of databases
    databases = show_databases()
    
    separator_line()
    
    time.sleep(0.5)
    
    print("Please select a database by entering its ID according to the table above.\n")

    while True:
        time.sleep(0.5)
        id_db = input("Enter the ID of a database: ")
        try:
            id_db = int(id_db)
            # Check valid input
            if 0 < id_db and id_db <= len(databases):
                database = databases[id_db - 1]
                break
            else:
                print("Please enter the ID which is in the table above...")
        except:
            # Input is not integer
            print("Please enter the ID which is in the table above...")
            pass
    
    time.sleep(0.5)
    print(f"You chose {database}\n")
    time.sleep(0.5)
    return database    

# Choose a school name
def input_school_name():
    
    separator_line()
    
    print("### THE LIST OF SCHOOL NAMES ###")
    time.sleep(0.5)
    
    # Get the list of school names
    schools = show_schools()
    
    separator_line()
    
    time.sleep(0.5)
    
    print("Please select a school name by entering its ID according to the table above.\n")
    
    while True:
        time.sleep(0.5)
        id_s = input("Enter the ID of a school: ")
        try:
            id_s = int(id_s)
            if id_s == len(schools) + 1:    # You chose the option Other
                print("Please enter the school name you want: ")
                while True:
                    school_name = input()
                    # Check valid input
                    if 0 < len(school_name) and len(school_name) <= 100:
                        break
                    else:
                        print("The length of the school name is not valid. Please enter other name: ") 
                break
            
            # Check valid input
            if 0 < id_s and id_s <= len(schools):
                school_name = schools[id_s - 1]
                break
            else:
                print("Please enter the ID which is in the table above...")
        except:
            # Input is not integer
            print("Please enter the ID which is in the table above...")
            pass
    
    time.sleep(0.5)
    print(f"You chose {school_name}")
    time.sleep(0.5)
    return school_name

# Choose a school year
def input_school_year():
    
    separator_line()
    
    print("### THE LIST OF SCHOOL YEAR ###")
    
    # Get the list of school years
    years = show_years()
    
    separator_line()
    
    time.sleep(0.5)
    
    print("Please select a school year by entering its ID according to the table above.\n")
    
    while True:
        time.sleep(0.5)
        id_y = input("Enter the ID of a school year : ")
        try:
            id_y = int(id_y)
            if id_y == len(years) + 1:  # You chose the option Other
                print("Please enter the school year you want (The format of school year is yyyy-yyyy): ")
                while True:
                    school_year = input()
                    # Check valid input
                    if len(school_year) == 9:
                        break
                    else:
                        print("The school year is not valid. Please enter other year (The format of school year is yyyy-yyyy): ") 
                break
            
            # Check valid input
            if 0 < id_y and id_y <= len(years):
                school_year = years[id_y - 1]
                break
            else:
                print("Please enter the ID which is in the table above...")
        except:
            # Input is not integer
            print("Please enter the ID which is in the table above...")
            pass
    
    time.sleep(0.5)
    print(f"You chose {school_year}")
    time.sleep(0.5)
    return school_year

# Choose a rank
def input_rank():
    
    separator_line()
    
    print("### THE LIST OF RANK ###")
    # Get the list of ranks
    ranks = show_ranks()
    
    separator_line()
    time.sleep(0.5)
    
    print("Please select a rank by entering its ID according to the table above.\n")
    
    while True:
        time.sleep(0.5)
        id_r = input("Enter the ID of a rank: ")
        try:
            id_r = int(id_r)
            # Check valid input
            if 0 < id_r and id_r <= len(ranks):
                rank = ranks[id_r - 1]
                break
            else:
                print("Please enter the ID which is in the table above...")
        except:
            # Input is not integer
            print("Please enter the ID which is in the table above...")
            pass
    
    time.sleep(0.5)
    print(f"You chose {rank}")
    time.sleep(0.5)
    return rank

# Input of query
def input_of_query():
    
    # Enter database
    database = input_database()
    # Connect to database
    cursor.execute(f"USE {database}")
    print(f"Used database `{database}`")
    time.sleep(0.5)
    # Enter school name
    school_name = input_school_name()
    # Enter school year
    school_year = input_school_year()
    # Enter rank
    rank = input_rank()
    
    separator_line()
    # Confirm your choice (input)
    print(f"Your input is: \n- Database: {database}\n- School name: {school_name}\n- School year: {school_year}\n- Rank: {rank}")
    separator_line()
    time.sleep(0.5)
    # Return your input
    return (database, school_name, school_year, rank)

# Print the query output in tabular format
def print_query_result(input, query_result):
    print(f"Result of query with:\n- Database: {input[0]}\n- School name: {input[1]}\n- School year: {input[2]}\n- Rank: {input[3]}", file=output_file)
    table = PrettyTable(["STT", "HOTEN", "NTNS", "DIEMTB", "XEPLOAI", "KETQUA"])
    for i in range (len(query_result)):
        row = query_result[i]
        table.add_row([i + 1, row[0], row[1].strftime(TIME_FORMAT), row[2], row[3], row[4]])
    print(table, file=output_file)



# Print the query output in XML file
def output_as_xml(input, query_result):
    # Get the query
    input_database, input_school_name, input_school_year, input_rank = input

    # Create the file name based on the input
    file_name = input_database.replace(" ", "") + "-" + input_school_name.replace(" ", "") + "-" + input_school_year.replace(" ", "") + "-" + input_rank.replace(" ", "") + ".xml"
    
    # Create the tree of XML
    # Create SimpleQuery with the attributes including database, school_name, school_year and rank_query
    SimpleQuery = ET.Element("SimpleQuery", database=input_database, school_name=input_school_name, school_year=input_school_year, rank_query=input_rank)
    # Create an instance of query
    for instance in query_result:
        # Create Student as a element of SimpleQuery
        Student = ET.SubElement(SimpleQuery, "Student")
        # Create the elements of Student including Name, NTNS, Score, Rank and Result
        Name = ET.SubElement(Student, "Name")
        NTNS = ET.SubElement(Student, "NTNS")
        Score = ET.SubElement(Student, "Score")
        Rank = ET.SubElement(Student, "Rank")
        Result = ET.SubElement(Student, "Result")
        # Insert data into elements
        Name.text = instance[0]
        NTNS.text = instance[1].strftime(TIME_FORMAT)
        Score.text = str(instance[2])
        Rank.text = instance[3]
        Result.text = instance[4]
        
    tree = ET.ElementTree(SimpleQuery)
    ET.indent(tree, space="\t", level=0)
    # Print data to XML file
    tree.write(f'XML/{file_name}', encoding='utf-8', xml_declaration=True)
    
    # Store a file name to use it in the question 5
    list_file_name = []
    try:
        with open("xml_file_name.txt", "r", encoding='utf-8') as fi:
            # Read the list of file name
            while True:
                a_file_name = fi.readline()
                a_file_name = a_file_name.strip()
                if a_file_name == "":
                    break
                list_file_name.append(a_file_name)
    except:
        pass
    
    with open("xml_file_name.txt", "w", encoding='utf-8') as fo:
        for fn in list_file_name:
            fo.write(f"{fn}\n")
        if not file_name in list_file_name: 
            fo.write(file_name)
            fo.write("\n")
        print("The file name of XML file was written into xml_file_name.txt.")
        time.sleep(1)
        
    # Return the XML file name
    return file_name

# Implement a simple query
def a_simple_query(input):
    print("Calling a simple query...")
    time.sleep(0.5)
    database, school_name, school_year, rank = input
    
    # Store the start time of this query
    start_time = time.time()
    
    # The mySQL syntax of query
    my_query = (
        f"SELECT CONCAT_WS(' ', hs.ho, hs.ten) AS hoten, hs.ntns, hoc.diemtb, hoc.xeploai, hoc.kqua FROM truong, hs, hoc WHERE hoc.mahs = hs.mahs AND hoc.matr = truong.matr AND truong.tentr = '{school_name}' AND hoc.namhoc = '{school_year}' AND hoc.xeploai = '{rank}'"
    )
    
    # Get the result of query
    cursor.execute(my_query)
    query_result = cursor.fetchall()
    
    # Store the end time of this query
    end_time = time.time()
    # Calculate the time of this query
    query_time = end_time - start_time    
    
    print("Done execution.\n")
    
    time.sleep(0.5)
    
    # Print the time of this query in terminal
    print(f"Time of query is {query_time}.\n")
    time.sleep(1)
    
    # Print the time of this query in output file
    print_query_result(input, query_result)
    print(f"Time of query is {query_time}.\n", file=output_file)
    
    # Print the number of instances of this query
    print(f"This query has {len(query_result)} instances.")
    time.sleep(1)
    
    # Message 
    print("See the result of query in file 'query_result.txt'.\n")
    time.sleep(1)
    
    # Create XML file
    print("Start creating XML file...")
    time.sleep(1)
    file_name = output_as_xml(input, query_result)
    print("Finished!")
    time.sleep(.5)
    # Message
    print(f"See the output in file {file_name}\n")
    time.sleep(1)

# Call a-simple-query function
a_simple_query(input_of_query())
# Message
print("The program has done!!!\n")