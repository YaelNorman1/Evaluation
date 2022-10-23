import pymysql 

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def check_if_ingredient_in_table(product, table_name):
    try:
        with connection.cursor() as cursor:
            query = f'''SELECT *
                        FROM {table_name} 
                        WHERE ingredient_name = "{product}"'''
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except TypeError as e:
        print(e)

