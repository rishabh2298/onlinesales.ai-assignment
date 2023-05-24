#-------------------------------------------------------------------------------
# Name:        Task - 2
# Purpose:      Scripting
#
# Author:      Rishabh Mishra
#
# Created:     24-05-2023
# Copyright:   (c) WIN-10 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


## import module to read excel and write into csv file

import pandas as pd;
import glob;



## creating funtion for converting excel file into csv file

def excel_to_csv(input_file, output_file):

    ## Read excel file

    df = pd.read_excel(input_file);


    ## Convert data frame to CSV and save

    df.to_csv(output_file);




## creating function to return top-3 deparments by average salaries

def get_top_department(department_file, employee_file, salaries_file):

    ## read department csv file
    department = pd.read_csv(department_file);

    ## read employee csv file
    employee = pd.read_csv(employee_file);

    ## read salaries csv file
    salary = pd.read_csv(salaries_file);



    ## merging data into one data frame so that we can do grouping of department
    ## and calcualte average salary according to unique-department

    ## left_on = department_id of employees table
    ## right_on = department_id of department table

    all_data = employee.merge(department, left_on="DEPT_ID", right_on="ID");

    ## left_on = employee_id of employees table
    ## right_on = employee_id of salaries table

    all_data = all_data.merge(salary, left_on="ID", right_on="EMP_ID");


    ## Group by department_id to calculate average salary

    final_data = all_data.groupby("DEPT_ID")["AMT"].mean().reset_index();

    ## sort data in descending order by average salary

    sort_data = final_data.sort_values("AMT", ascending=False);


    ## fetch top-3 result
    ## head() will return top-3 result from sort_data

    result = sort_data.head(3)


    return result;






## STEP - 1 :-  Only if file has ".xlsx" extension

## location of "excel sheet having .xlsx extention"
## update location to each variables accordingly

departments = "path_directory/departments.xlsx";
employees = "path_directory/employees.xlsx"
salaries = "path_directory/salaries.xlsx";

## if above files are extension of ".xlsx" which is excel file then call
## excel_to_csv() funtion to convert it into ".csv" extension :-

## uncomment below method to convert ".xlsv" to ".csv" line-107,108,109 and
## line-103,104,105 is the location of ".csv" file

## Output files :-
department_file = "path_directory/departments.csv";
employee_file = "path_directory/departments.csv";
salaries_file = "path_directory/departments.csv";

## excel_to_csv(departments, department_file);
## excel_to_csv(employees, employee_file);
## excel_to_csv(salaries, salaries_file);

## output_file (line-103,104,105) is the location of ".csv" file of each spreedsheet so pass
## the location where you want your ".xlsx" file will be save in form of ".csv" file



## Assumption : if you don't have ".xlsx" file then don't call excel_to_csv()
## method and start with step-2 directly




## STEP - 2 : Start with ".csv" file extension Only

## update values in line-103,104,105 with correct path where you want to store
## your ".csv" file of each ".xlsx" file during process


## function-call to get top-3 departments for Output Report

top_departments = get_top_department(department_file, employee_file, salaries_file);


## Printing Result

print(top_departments);
