from fastapi import APIRouter, status , Response
from .queries import check_if_ingredient_in_table
import requests



router = APIRouter()

@router.get("/ingredient/{product_name}", status_code=status.HTTP_200_OK)
def get_recipes_by_ingredient(product_name, dairy_sensitivity='', gluten_sensitivity=''):
    try:
        res =  requests.get(f'https://recipes-goodness.herokuapp.com/recipes/{product_name}')
        recipes_list= res.json()
        if not dairy_sensitivity and not gluten_sensitivity:
            return recipes_list["results"]
        else:
            return filter_recipes_by_sensitivity(recipes_list["results"], dairy_sensitivity, gluten_sensitivity)
    except requests.exceptions.HTTPError as e:
        return  {"Error" :"ingredient doesn't exist"}


# wanted to put these funcs in diffrent file
def filter_recipes_by_sensitivity(recipes_list, dairy_sensitivity, gluten_sensitivity):
    filtered_recipes= list(filter(lambda recipe: check_if_recipe_is_sensitive(recipe, dairy_sensitivity, gluten_sensitivity), recipes_list))
    return filtered_recipes


def check_if_recipe_is_sensitive(recipe, dairy_sensitivity, gluten_sensitivity):
    if dairy_sensitivity and gluten_sensitivity:
        for ingredient in recipe["ingredients"]:
            if not check_if_ingredient_in_table(ingredient, dairy_sensitivity) and not check_if_ingredient_in_table(ingredient, gluten_sensitivity):
                return True
            else:
                return False
    elif dairy_sensitivity and not gluten_sensitivity:
        for ingredient in recipe["ingredients"]:
            if not check_if_ingredient_in_table(ingredient, dairy_sensitivity):
                return True
            else:
                return False
    else:
        for ingredient in recipe["ingredients"]:
            if not check_if_ingredient_in_table(ingredient, gluten_sensitivity):
                return True
            else:
                return False