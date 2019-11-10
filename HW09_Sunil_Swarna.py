#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
'''
Created on 31 ‎October ‎2019, ‏‎09:30:45
@author: Sunil Kumar Swarna
Implement a system will also be used by faculty advisors to help students to create study plans.
'''

import os
from collections import defaultdict
from prettytable import PrettyTable

class Student():
    """
    Student class having details of a particular student & methods like add course detials for that student
    """

    def __init__(self, cwid, name, major):
        """ Student class hold all of the details of a student """

        self.cwid = cwid
        self.name = name
        self.major = major
        self.courses_grade_information = defaultdict(str)
    
    def add_course_grade(self,course, grade):
        """  Add course & grade for a student """

        self.courses_grade_information[course] = grade

    def pretty_table_student(self):
        """ Pretty table printout information for student """
        completed, remaining, electives = Major.compute_remaining_courses(self.major, self.courses_grade_information, self.name)
        return [self.cwid, self.name, self.major, completed, remaining, electives]

class Instructor():
    """
    Instructor class having details of a particular Instructor & methods like add course he teaches & no of students for that Instructor
    """

    def __init__(self, cwid, name, department):
        """ Instructor class hold all of the details of a Instructor """

        self.cwid = cwid
        self.name = name
        self.department = department
        self.courses = defaultdict(int)
    
    def add_course_noofstudents (self, course):
        """  Add course the instructor teaches & number of students """

        self.courses[course] += 1

    def pretty_table_instructor(self):
        """ Pretty table printout information for instructor """
        return [self.cwid, self.name, self.department], self.courses


class Major():
    """
    Major class having major required & non required classes
    """

    majors = defaultdict(str)
    valid_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']

    def __init__(self, major, compulsory, course):
        """ Major class having static method to storre info abt grades """

        Major.majors[major] = {}
        Major.majors[major]['R'] = []
        Major.majors[major]['E'] = []         
        Major.add_course_to_major(major, compulsory, course)

    @staticmethod
    def add_course_to_major(major, compulsory, course):
        Major.majors[major][compulsory].append(course)

    @staticmethod
    def compute_remaining_courses(major, courses, name):
        completed = set([ course for course, grade in courses.items() if grade in Major.valid_grades])
        required = set(Major.majors[major]['R']) - completed
        electives = None if len(set(Major.majors[major]['E']).intersection(completed))>0 else set(Major.majors[major]['E']) - completed 
        return sorted(completed), required, electives
        
class Container:
    """ 
    It is a repository that hold the students, instructors and grades for a single University
    """
    
    def __init__(self, directory):
        """ constrctor that holds for a particular university & calling the pretty table information """

        self.directory = directory
        self.student_info = {}
        self.insructors_info = {}
        self.majors_info = set([])
        self.analyze_files()

    def analyze_files(self):
        """ function that process the directory & process instrctors, students & grades information"""

        if not os.path.exists(self.directory):
            print(f"No such directory {self.directory}")

        students_file = 'students.txt'
        instructors_file = 'instructors.txt'
        grades_file = 'grades.txt'
        majors_file = 'majors.txt'

        if students_file in os.listdir(self.directory):
            for cwid, name, major in self.file_reading_gen(os.path.join(self.directory, students_file), 3, ";", True): 
                self.student_info[cwid] = Student(cwid, name, major)
        else:
            print(
                f"Can't open {students_file} for reading!..")
        
        if instructors_file in os.listdir(self.directory):
            for cwid, name, department in self.file_reading_gen(os.path.join(self.directory, instructors_file), 3, "|", True): 
                self.insructors_info[cwid] = Instructor(cwid, name, department)
        else:
            print(
                f"Can't open {instructors_file} for reading!..")

        if grades_file in os.listdir(self.directory):
            for studentCwid, course, grade, instructorCwid in  self.file_reading_gen(os.path.join(self.directory, grades_file), 4, "|", True):
                
                if studentCwid in self.student_info.keys():
                    self.student_info[studentCwid].add_course_grade(course, grade)
                else:
                    print(f"Found grade for unknow student {studentCwid}")
                
                if instructorCwid in self.insructors_info.keys():
                    self.insructors_info[instructorCwid].add_course_noofstudents(course) 
                else:
                    print(f"Found grade for unknow instrcutor {instructorCwid}")

        else:
            print(f"Can't open {grades_file} for reading!..")

        Major.majors ={}
        if majors_file in os.listdir(self.directory):
            for major, reqrele, course in self.file_reading_gen(os.path.join(self.directory, majors_file), 3, "\t", True):
                if major not in self.majors_info: 
                    self.majors_info.add(major)
                    Major(major, reqrele, course)
                else:
                    Major.add_course_to_major(major, reqrele, course)

            
        else:
            print(
                f"Can't open {majors_file} for reading!..")

        # print(Major.majors)


    def file_reading_gen(self, path, fields, sep=',', header=False):
        """
        Generator function that opens a file for reading and returns one line from the file at a time.
        Reading text files with a fixed number of fields, separated by a pre-defined character, is a common task.
        """

        try:
            fp = open(path, "r")

        except FileNotFoundError:
            print(f"Can't open {path} for reading!..")

        else:
            with fp:
                line_number = 0
                if header and len(next(fp).split(sep)) != fields:
                    fp.seek(0)
                    print(
                        f"'{path}' has {len(fp.readline().split(sep))} fields on line 0 but expected {fields}")

                if header:
                    line_number += 1

                for line in fp:
                    line = line.strip().split(sep)
                    line_number += 1
                    if len(line) != fields:
                        print(
                            f"'{path}' has {len(line)} fields on line {line_number} but expected {fields}")
                    yield tuple(line)

    def students_summary(self):
        """ Pretty table for printing the student summary"""

        student_list = []

        pt = PrettyTable(field_names = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives'])
        print(f"\nStudent Summary")
        for student_instance in self.student_info.values():
            pt.add_row(student_instance.pretty_table_student())
            student_list.append(student_instance.pretty_table_student())

        print(pt)

        return student_list

    def instructor_summary(self):
        """ Pretty table for printing the instructor summary"""
        
        instructor_list = []

        pt = PrettyTable(field_names = ['CWID', 'Name', 'Dept', 'Course', 'Students'])
        print(f"\nInstructor Summary")
        for instructor_instance in self.insructors_info.values():
            instructor_information, courses = instructor_instance.pretty_table_instructor()
            for course, noof_students in courses.items():
                instructor_information.extend([course, noof_students])
                pt.add_row(instructor_information)
                instructor_list.append(instructor_information)
                instructor_information = instructor_information[0:3]
            
        print(pt)

        return instructor_list

    def major_summary(self):
        """ Pretty table for printing the major summary"""

        pt = PrettyTable(field_names = ['Dept', 'Required', 'Electives'])
        print(f"\nMajors Summary")
        for major in Major.majors.keys():
            pt.add_row([major, sorted(Major.majors[major]['R']), sorted(Major.majors[major]['E'])])

        print(pt)
def main():
    try:
        stevens = Container('C:/Users/sunil/Downloads/HE-04/stevensdata')
        stevens.major_summary()
        stevens.students_summary()
        stevens.instructor_summary()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()  # Main routine for priting the data in the code


#changes to make
'''
make the pt headers as class atributes & use them in pretty ybale
use yield for pretty table in instrctor
'''

#In the test file
'''
expected  in dic witk key as cwid & value is the data
calculated alos in dic with pretty yable code
for instrctor dictionary & tuple
cauculates with tuple() 
'''