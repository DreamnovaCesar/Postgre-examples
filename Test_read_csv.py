import csv
import numpy as np
import random
import psycopg2


def read_pg_data():
     """
     Method used to create random students data 

     """

     try:
          # * Connect to the PostgreSQL database
          connection = psycopg2.connect(
               host="localhost",
               database="inegi_db",
               user="postgres",
               password="Cesarw123zxc."
          );

          # * Print message indicating successful connection
          print("Connecting to database");

     except Exception as e:
          print(e);

     # * Create a cursor object to perform SQL queries
     cur = connection.cursor();

     # * Execute an SQL query to retrieve student data
     cur.execute('''
     
     SELECT id, last_name, zip 
     FROM customer
     ORDER BY zip DESC
     FETCH FIRST 10 ROWS ONLY''');
     
     # * Fetch the results
     results = cur.fetchall();

     print(results);
     # * Close the cursor and connection


     # * Open a CSV file for writing
     with open('report.csv', 'w', newline='') as csvfile:
          writer = csv.writer(csvfile)

          '''# Write the header row
          writer.writerow(['first_name', 'last_name', 
                              'email', 'company', 
                              'street', 'city', 
                              'state', 'zip', 
                              'phone', 'birth_date',
                              'sex', 'date_entered'
                              ])'''

          # * Write the header row
          writer.writerow(['first_name', 'last_name', 'zip' ]);
          
          # * Execute an SQL query
          cur.execute('''
     
          SELECT id, first_name, last_name, zip 
          FROM customer
          ORDER BY zip DESC
          FETCH FIRST 10 ROWS ONLY'''
                      
          );

          # * Fetch the results and write them to the CSV file
          results = cur.fetchall()
          for row in results:
               writer.writerow(row)
     
     # * Close the cursor and connection
     cur.close();
     connection.close();

# Call the read_pg_data() method to retrieve and write student data to a CSV file
read_pg_data();
