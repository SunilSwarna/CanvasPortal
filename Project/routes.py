#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
'''
Created on 22 November ‎2019, ‏‎09:30:45
@author: Sunil Kumar Swarna
Implement a Flask system will also be used by faculty advisors to help students to create study plans.
'''

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
db_path = '810_startup.db'

# @app.route('/')
@app.route('/instructors')
def instructors():
    """
    Instructors route that will be excuted
    """

    try:
        db = sqlite3.connect(db_path)

    except Exception as e:
        return render_template('error.html',title='Error in connecting database', error=e)

    else:
        query = """ select I.CWID, I.Name , I.Dept, G.Course, count(*) as Students from instructors I join
            grades G  on I.CWID = G.InstructorCWID GROUP BY G.InstructorCWID,G.Course order by  CWID asc;"""
        
        try:
            results = db.execute(query)

        except Exception as e:
           return render_template('error.html',title='Error in executing Query', error=e)
        
        else:
            
            data = [{'CWID': cwid, 'Name': name, 'Department': department, 'Course': course, 'Students': students}
                    for cwid, name, department, course, students in results]
            db.close()

            return render_template('instructors.html', 
                                    title='Stevens Respository', 
                                    table_title='Courses and student counts',
                                    instructors=data)
app.run(debug=True)