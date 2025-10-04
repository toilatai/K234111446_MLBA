import sqlite3
import pandas as pd

try:
    sqliteConnection = sqlite3.connect('../database/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')
    query = 'SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall())
    print(df)
    cursor.close()

except sqlite3.Error as error:
    print('Error occurred ', error)

finally:
    if 'sqliteConnection' in locals() and sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
