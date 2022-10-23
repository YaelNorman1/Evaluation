from queries import insert_ingredient_to_table

dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]

def insert_data_to_tabels(ingredients_arr, table_name):
    for product in ingredients_arr:
        insert_ingredient_to_table(product, table_name)



if __name__ == "__main__":
    insert_data_to_tabels(dairy_ingredients, "dairy_ingredients")
    insert_data_to_tabels(gluten_ingredients, "gluten_ingredients")