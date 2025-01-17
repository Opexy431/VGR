import pandas as pd
import mysql.connector

# MySQL connection details
db_config = {
    'user': 'Emmanuel',
    'password': '123456',
    'host': 'localhost',
    'database': 'mydatabase'
}

def upload_csv_to_mysql(csv_file, table_name):
    # Read CSV file
    data = pd.read_csv(csv_file)
    
    # Establish a database connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Insert data into MySQL table
    for index, row in data.iterrows():
        # Debugging: Print the row data
        print(f"Inserting row {index}: {row.to_dict()}")  # Convert row to dictionary for better readability
        
        try:
            cursor.execute(
                f"""
                INSERT INTO {table_name} (
                    `Game_Title`, 
                    `User_Rating`, 
                    `Age_Group_Targeted`, 
                    `Price`, 
                    `platform`, 
                    `Requires_Special_Device`, 
                    `Developer`, 
                    `Publisher`, 
                    `Release_Year`, 
                    `Genre`, 
                    `Multiplayer`, 
                    `Game_Length_Hours`, 
                    `Graphics_Quality`, 
                    `Soundtrack_Quality`, 
                    `Story_Quality`, 
                    `User_Review_Text`, 
                    `Game_Mode`, 
                    `Min_Number_of_Players`
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """,
                (
                    row['Game Title'],
                    row['User Rating'],
                    row['Age Group Targeted'],
                    row['Price'],
                    row['Platform'],
                    row['Requires Special Device'],
                    row['Developer'],
                    row['Publisher'], 
                    row['Release Year'],
                    row['Genre'],
                    row['Multiplayer'],
                    row['Game Length (Hours)'],
                    row['Graphics Quality'],
                    row['Soundtrack Quality'],
                    row['Story Quality'],
                    row['User Review Text'],
                    row['Game Mode'],
                    row['Min Number of Players']
                )
            )
        except mysql.connector.Error as err:
            print(f"Error inserting row {index}: {err}")  # Print error message if insertion fails
    
    # Commit and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Data uploaded successfully")

# Upload data from CSV to MySQL
upload_csv_to_mysql('VGR.csv', 'VGR')