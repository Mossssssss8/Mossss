
import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                password="RFMcgy59905",
                                host="node8599-advweb-19.app.ruk-com.cloud",
                                port="11069",
                                database="CloudDB")

        
    cursor = connection.cursor()
    # Print PostGress Connectiob properties.
    print(connection.get_dsn_parameters(),"\n")

    #Print PostGress Version.
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record , "\n")
    
except (Exception , psycopg2.Error) as error: 
    print("Error While Connecting to PostgressSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgressSQL connection is Closed")
            