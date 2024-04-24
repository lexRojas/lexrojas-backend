import mysql.connector

#---LOCAL DATABASE ----

# _hostname ='localhost'
# _username ='basedatos'
# _password ='basedatos'
# _database ='notario'

#---HEROKU DATABASE ----

             
_hostname = 'erxv1bzckceve5lh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
_username = 'k1hpp1oicmrsuqfh'
_password = 'iei93plst88ydzp5'
_database = 'vmy3gj1q7kthw5c8' 
             


# Database configuration
db_config = {
    'host': _hostname,
    'user': _username,
    'password': _password,
    'database': _database,
}

# Create a connection to the database
conn = mysql.connector.connect(**db_config)







