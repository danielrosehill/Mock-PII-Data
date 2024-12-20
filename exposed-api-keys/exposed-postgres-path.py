import psycopg2
from psycopg2.extras import RealDictCursor

# Define the PostgreSQL connection URL (synthetic example)
postgres_url = "postgresql://danielpostgres:242429xs8@ourpostgres.example.com:5432/mydatabase"

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(postgres_url)
    
    # Create a cursor to execute queries
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    
    # Define the SQL query to read data from a table
    query = "SELECT * FROM my_table LIMIT 10;"
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection:
        connection.close()
