
import mssql_python

SERVER = r"DESKTOP-IFO80R1\SQLEXPRESS"

connection_string = (
    f"Server={SERVER};"
    "Database=project;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    conn = mssql_python.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT @@SERVERNAME, DB_NAME()
    """)

    result = cursor.fetchone()

    print("Connection successful!")
    print("Server:", result[0])
    print("Database:", result[1])

    conn.close()

except Exception as e:
    print("Connection failed:")
    print(e)
