import pymysql 

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]

def insert_data_to_tabels(ingredients_arr, table_name):
    for product in ingredients_arr:
        insert_ingredient_to_table(product, table_name)



def insert_ingredient_to_table(product, table_name):
    try:
        with connection.cursor() as cursor:
            query = f'INSERT IGNORE INTO {table_name} VALUES (null, "{product}")'
            cursor.execute(query)
            connection.commit()
            return {"Success" : "Added pokemon successfuly"}
    except TypeError as e:
        print(e)



if __name__ == "__main__":
    insert_data_to_tabels(dairy_ingredients, "dairy_ingredients")
    insert_data_to_tabels(gluten_ingredients, "gluten_ingredients")