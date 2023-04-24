# Tree-View-App-with-Flask

Test project using Flask to create a web app, connect PostgreSQL database, and push one of the tables in tree view to the web app using javascript.

1) cleaning.py cleans up the date format of the CSV source files
2) db_init creates the database connection and imports the CSV files into tables
3) app.py connects to the database and outlines the functions for pulling the tables from PostgreSQL and pushing a JSON object to Flask 
