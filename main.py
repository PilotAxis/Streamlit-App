# importing required modules

from os import system
import re
import streamlit as st
import mysql.connector

# making connection with the database

mydb = mysql.connector.connect(
    host="localhost",
    user="your_username", # Enter your mysql username (default = 'root')
    password="your_password", # Enter your mysql password
    database="users"
)

mycursor=mydb.cursor()
print("Connection Established")

#Make a regular expression for validating an Email

regex = r'\b[A-Za-z0-9._%+-]+@[A-za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Create Streamlit App

def check_student(student_id):
    #query to select all rows from employee(empdata) table
    
    sql = 'select * from data where id=%s'
    #making cursor buffered to make rowcount method work properly
    
    m = mydb.cursor(buffered=True)
    data = (student_id,)
    m.execute(sql, data)

    #rowcount method to find number of rows with given values
    
    r = m.rowcount
    if r == 1:
        return True
    else:
        return False

def main():
    st.title("Students Records Management System");
    st.subheader("By Ahmed Majid");
    option = st.sidebar.selectbox("Select an Operation", ("Add", "View", "Edit", "Delete"))

    if option == "Add":
        st.subheader("Add a Record")
        id = st.number_input("Enter student's id")
        name = st.text_input("Enter student's name")
        gender = st.selectbox("Enter student's gender", ("Male", "Female"))
        email = st.text_input("Enter student's email")
        phone = st.text_input("Enter student's phone number")
        address = st.text_input("Enter student's address")
        classs = st.text_input("Enter student's class")
        section = st.text_input("Enter student's section")
        if st.button("Add"):
            if re.fullmatch(regex, email):
                sql = "insert into data(id, name, gender, email_id, phone_no, address, classs, section) values(%s, %s, %s, %s, %s, %s, %s, %s)"
                data = (id, name, gender, email, phone, address, classs, section)
                m = mydb.cursor()
                m.execute(sql, data)
                mydb.commit()
                st.success("Record inserted successfully")
            else:
                st.warning("Invalid Email")

    elif option == "View":
        st.subheader("View Records")
        m = mydb.cursor()
        m.execute("SELECT * FROM data")
        data = m.fetchall()
        if len(data) == 0:
            st.warning("No records found")
        else:
            for row in data:
                st.write(row)

    elif option == "Edit":
        st.subheader("Edit a Record")
        m = mydb.cursor()
        m.execute("SELECT * FROM data")
        data = m.fetchall()
        if len(data) == 0:
            st.warning("No records found")
        else:
            id = st.number_input("Enter the id of the record to be edited")
            choice = st.selectbox("What do want to Update?", ("Name", "Gender", "Email", "Phone", "Address", "Class", "Section"))
            if choice == "Name":
                name = st.text_input("Enter New Name")
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET name = %s where id = %s"
                        data = (name, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")
                else:
                    st.warning("Record not found")
            elif choice == "Gender":
                gender = st.selectbox("Enter New Gender", ("Male", "Female"))
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET gender = %s where id = %s"
                        data = (gender, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")
            elif choice == "Email":
                email = st.text_input("Enter New Email")
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET email_id = %s where id = %s"
                        data = (email, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")
            elif choice == "Phone":
                phone = st.text_input("Enter New Phone Number")
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET phone_no = %s where id = %s"
                        data = (phone, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")
            elif choice == "Address":
                address = st.text_input("Enter New Address")
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET address = %s where id = %s"
                        data = (address, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")
            elif choice == "Class":
                classs = st.text_input("Enter New Class")
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET classs = %s where id = %s"
                        data = (classs, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")
            elif choice == "Section":
                section = st.text_input("Enter New Section")
                if (check_student(id) == True):
                    if st.button("Edit"):
                        sql = "UPDATE data SET section = %s where id = %s"
                        data = (section, id)
                        m = mydb.cursor()
                        m.execute(sql, data)
                        mydb.commit()
                        st.success("Record updated successfully")

    elif option == "Delete":
        st.subheader("Delete a Record")
        m = mydb.cursor()
        m.execute("SELECT * FROM data")
        data = m.fetchall()
        if len(data) == 0:
            st.warning("No records found")
        else:
            id = st.number_input("Enter the id of the record to be deleted")
            if (check_student(id) == True):
                if st.button("Delete"):
                    sql = "DELETE FROM data WHERE id = %s"
                    data = (id,)
                    m = mydb.cursor()
                    m.execute(sql, data)
                    mydb.commit()
                    st.success("Record deleted successfully")
if __name__ == "__main__":
    main()