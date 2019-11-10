import sqlite3
from prettytable import PrettyTable

DB_FILE = 'C:/Users/sunil/Downloads/sql/810_startup.db'
db = sqlite3.connect(DB_FILE)

query = """ select I.CWID, I.Name , I.Dept, G.Course, count(*) as Students from HW11_instructors I join
    HW11_grades G  on I.CWID = G.Instructor_CWID GROUP BY G.Course order by  CWID desc;"""

pt = PrettyTable(field_names = ['CWID', 'Name', 'Dept', 'Course', 'Students'])

print(f"\nInstructor Summary From DataBase")
for row in db.execute(query):
    pt.add_row(list(row))
print(pt)

db.close()