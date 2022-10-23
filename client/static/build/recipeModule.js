"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
class RecipesDataModule {
    constructor() {
        this.recipes = [];
    }
    generateAllRecipes(ingredientFromUser) {
        return __awaiter(this, void 0, void 0, function* () {
            yield this.getRecipesFromServer(ingredientFromUser).then(data => {
                this.recipes.splice(0);
                this.assignDataIntoRecipe(data);
            });
        });
    }
    getRecipesFromServer(ingredientFromUser) {
        const ingredient = 'ingredientName';
        return $.get(`/ingredient/${ingredientFromUser[ingredient]}`);
    }
    assignDataIntoRecipe(recipes) {
        // return recipes.map((r:Recipe) => new Recipe(r.title, r.ingredients, r.strInstructions, r.thumbnail))
        for (const recipe of recipes) {
            const title = recipe.title;
            const ingredients = recipe.ingredients;
            const strInstructions = recipe.strInstructions;
            const thumbnail = recipe.thumbnail;
            this.recipes.push({ title: title, ingredients: ingredients, strInstructions: strInstructions, thumbnail: thumbnail });
        }
    }
    getRecipes() {
        return this.recipes;
    }
}
