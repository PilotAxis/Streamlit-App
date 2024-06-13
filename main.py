# importing required modules

from os import system
import re
import streamlit as st
import mysql.connector

# creating required database if not exists

def create_database():
    mydb = mysql.connector.connect(host="localhost", user="root", password="lenovok8note")
    m = mydb.cursor()
    m.execute("CREATE DATABASE users;")

# creating the table

def create_table():
    mydb = mysql.connector.connect(host="localhost", user="root", password="lenovok8note", database="users")
    m = mydb.cursor()
    m.execute("SHOW TABLES;")
    data = m.fetchall()
    for i in data:
        if (i == ('usersdata',)):
            break
        else:
            m.execute("CREATE TABLE usersdata(Id INT(11) PRIMARY KEY, Name VARCHAR(1000), Gender VARCHAR(7), Email_Id TEXT(1000), Phone_no VARCHAR(15), Address TEXT(1000), Class TEXT(1000), Section VARCHAR(20))")

#Make a regular expression for validating an Email

regex = r'\b[A-Za-z0-9._%+-]+@[A-za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Create Streamlit App

def main():
    st.title("Students Records Management System");
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
                sql = "insert into usersdata(id, name, gender, email, phone, address, classs, section) values(%s, %s, %s, %s, %s, %s, %s, %s)"
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
        m.execute("SELECT * FROM usersdata")
        data = m.fetchall()
        if len(data) == 0:
            st.warning("No records found")
        else:
            for row in data:
                st.write(row)

    elif option == "Edit":
        st.subheader("Edit a Record")
        m = mydb.cursor()
        m.execute("SELECT * FROM usersdata")
        data = m.fetchall()
        if len(data) == 0:
            st.warning("No records found")
        else:
            id = st.number_input("Enter the id of the record to be edited")
            name = st.text_input("Enter New Name")
            gender = st.text_input("Enter New Gender")
            email = st.text_input("Enter New Email")
            phone = st.text_input("Enter New Phone Number")
            address = st.text_input("Enter New Address")
            classs = st.text_input("Enter New Class")
            section = st.text_input("Enter New Section")
            if st.button("Edit"):
                sql = "UPDATE usersdata SET name = %s, gender = %s, email = %s, phone = %s, address = %s, classs = %s, section = %s WHERE id = %s"
                data = (name, gender, email, phone, address, classs, section, id)
                m = mydb.cursor()
                m.execute(sql, data)
                mydb.commit()
                st.success("Record updated successfully")

    elif option == "Delete":
        st.subheader("Delete a Record")
        m = mydb.cursor()
        m.execute("SELECT * FROM usersdata")
        data = m.fetchall()
        if len(data) == 0:
            st.warning("No records found")
        else:
            id = st.number_input("Enter the id of the record to be deleted")
            if st.button("Delete"):
                sql = "DELETE FROM usersdata WHERE id = %s"
                data = (id,)
                m = mydb.cursor()
                m.execute(sql, data)
                mydb.commit()
                st.success("Record deleted successfully")

if __name__ == "__main__":
    create_database()
    create_table()
    mydb = mysql.connector.connect(host="localhost", user="root", password="lenovok8note", database="users")
    main()
