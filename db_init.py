# Import packages including psycopg2 for connecting to Postgres database
import os
import psycopg2
import credentialfile

# Create connection to Postgres database using environment variables of username and password
conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=credentialfile.DB_USERNAME,
    password=credentialfile.DB_PASSWORD,
)

# Open a cursor for DB operations
cur = conn.cursor()

# DDL - create the initial tables and import the data if not already existing
# Step 1: Drop the tables if they already exist to ensure latest data and avoid duplication
cur.execute('DROP TABLE IF EXISTS master_station_code_tbl;')

cur.execute('DROP TABLE IF EXISTS ticket_info;')

cur.execute('DROP TABLE IF EXISTS query_results;')

# Step 2: Create tables
cur.execute('CREATE TABLE master_station_code_tbl(master_station_code varchar (10) NOT NULL,'
                                                                'member_code varchar (10) NOT NULL);'
                                                                )

cur.execute('CREATE TABLE ticket_info(processed_date date,'
                                                    'ticket_number bigint,'
                                                    'member_code varchar (10),'
                                                    'master_code varchar (10),'
                                                    'renegotiated_date date,'
                                                    'closed_date date,'
                                                    'day_to_close int,'
                                                    'time_to_respond varchar (5),'
                                                    'compliance varchar (15));'
                                                    )

#Import master station code data and copy into Postgres table
with open('/home/ajh/learningproj/flask-tutorial/MasterStationCode.csv') as f:
    cur.copy_expert("COPY master_station_code_tbl FROM STDIN WITH CSV HEADER DELIMITER as ','", f)

#Import ticket info data and copy into Postgres table
cur.execute('SET datestyle = dmy;')
with open('/home/ajh/learningproj/flask-tutorial/ticketInfo_clean.csv') as f:
    cur.copy_expert("COPY ticket_info FROM STDIN WITH CSV HEADER DELIMITER as ','", f)

#Step 3: commit changes and close connection
conn.commit()

cur.close()
conn.close()

