import pymysql 


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def insert_ingredient_to_table(product, table_name):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT IGNORE INTO {table_name} VALUES (null, "{product}")'
            cursor.execute(query)
            connection.commit()
            return {"Success" : "Added pokemon successfuly"}
    except TypeError as e:
        print(e)