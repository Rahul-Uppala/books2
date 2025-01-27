My Books Database Application 📚

This is a Python-based GUI application built using Tkinter for managing a book database. The application connects to a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on books.

Features

* Add Books: Add new books with title, author, and ISBN.
* View Records: Display all books stored in the database.
* Modify Records: Update the details of existing books.
* Delete Records: Remove a book from the database.
* Clear Screen: Reset input fields and list view.
* Exit Application: Safely close the application.

Requirements

* Python 3.x
* PostgreSQL
* psycopg2 library for database connection
* Tkinter (comes with Python)


Setup Instructions


1. Clone the repository:bash    git clone <repository_url> 
         cd <repository_folder>
	
2. Install required Python libraries: pip install psycopg2 
3. Configure PostgreSQL:
Update the dbConfig in postgres_config.py with your database credentials.
Ensure your database has a books table with the following structure:sql  

CREATE TABLE books (    
id SERIAL PRIMARY KEY,    
title VARCHAR(255),    
author VARCHAR(255),    
isbn VARCHAR(13)
);

4. Run the application:bash python app.py  

