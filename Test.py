import csv
import numpy as np
import random
import psycopg2


def create_pg_data(Iter : int = 30):
     """
     Method used to create random students data 

     """

     # * Tuples for random generation.
     randomNames = (
          'James', 'Robert', 
          'John', 'Michael',
          'David', 'Tom', 
          'Nick', 'Chris', 
          'Jack', 'Thompson',
          'William', 'Richard',
          'Joseph', 'Thomas',
          'Charles', 'Daniel'
     );
     #  * Tuple containing random last names
     randomLastNames = (
          'Smith', 'Johnson',
          'Brown', 'Jones',
          'Garcia', 'Miller',
          'Davis', 'Rodriguez',
          'Martinez', 'Hernandez',
          'Lopez', 'Gonzalez',
          'Wilson', 'Anderson',
          'Thomas', 'Taylor',
          'Moore', 'Jackson',
          'White', 'Harris'
     );

     # * Tuple containing random email addresses
     emails = (
          'dogoba9335@djpich.com', 'frode@yahoo.com',
          'neonatus@me.com', 'nogin@msn.com',
          'salesgeek@icloud.com', 'seasweb@hotmail.com',
          'saridder@att.net', 'cgarcia@sbcglobal.net',
          'seano@comcast.net', 'gator@me.com',
          'goldberg@msn.com', 'frode@yahoo.com',
     );

     # * Tuple containing random company names
     companies = (
          'Apple', 'Jatco',
          'Samsung', 'VP',
          'Nvidia', 'PO',
          'Amd', 'Python',
          'Nissan', 'ItEH',
          'Microsoft', 'Google',
     );

     # * Tuple containing random street addresses
     streets = (
          '11 Beacon Lane', '56 Wild Rose Street',
          'Faribault, MN 55021', 'Westlake, OH 44145',
          '86 Mountainview Street', '7966 El Dorado St.',
          'Spartanburg, SC 29301', 'Amarillo, TX 79106',
          '9125 Oklahoma Street', '8371 W. Lees Creek Lane',
          'Marysville, OH 43040', 'Smyrna, GA 30080',
     );

     # * Tuple containing random city names
     cities = (
          'Struidmery', 'Glona',
          'Edrusa', 'Pluridge',
          'Yagend', 'Ylens',
          'Trudburg', 'Encecaster',
          'Kheding', 'Acoridge',
          'Ganbu', 'Iblusall',
     );

     # * Tuple containing random state names
     states = (
          'Naeset', 'Aslore',
          'Maapolis', 'Raxnard',
          'Eqikgend', 'Aneross',
          'Zlauginia', 'Antaset',
          'Cine', 'Anbusas',
          'Crury', 'Okhance',
     );
     
     # * Generate a random ZIP code
     randomZIP = np.random.randint(30000, 31000)

     # * Generate a random phone number
     randomPhone = ['000-000-000']

     # * Generate a random birthday
     randomBirthday = ['1994-02-16']
     
     # * Generate a random sex
     randomSex = ['M', 'F']


     currentDate = 'current_timestamp'

     # * Establish a connection to the database

     try:

          connection = psycopg2.connect(
               host="localhost",
               database="inegi_db",
               user="postgres",
               password="Cesarw123zxc."
          );

          print("Connecting to database");

     except Exception as e:
          print(e);

     # * Create a cursor object to perform SQL queries
     cur = connection.cursor();
     
     '''print(np.random.choice(randomNames))
     print(np.random.choice(randomLastNames))
     print(np.random.choice(emails))
     print(np.random.choice(companies))
     print(np.random.choice(streets))
     print(np.random.choice(cities))
     print(np.random.choice(states))
     print(np.random.choice(randomZIP))
     print(np.random.choice(randomPhone))
     print(np.random.choice(randomBirthday))
     print(np.random.choice(randomSex))
     print(currentDate)'''


     for _ in range(Iter):

          # Execute an SQL query
          cur.execute("INSERT INTO customer (first_name, last_name, email, company, street, city, state, zip, phone, birth_date, sex, date_entered) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp)", 
                    (np.random.choice(randomNames), np.random.choice(randomLastNames), np.random.choice(emails), np.random.choice(companies), np.random.choice(streets), np.random.choice(cities), np.random.choice(states), np.random.choice(randomZIP), np.random.choice(randomPhone), np.random.choice(randomBirthday), np.random.choice(randomSex)));
          connection.commit();
          count = cur.rowcount

     cur.execute("SELECT * FROM customer");

     # Fetch the results
     results = cur.fetchall();

     print(results);
     # Close the cursor and connection
     cur.close();
     connection.close();


create_pg_data(1000);