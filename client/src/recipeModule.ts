class RecipesDataModule {
    recipes : Recipe [];


    constructor() {
        this.recipes= []
    }

    public async generateAllRecipes(ingredientFromUser : object){
        await this.getRecipesFromServer(ingredientFromUser).then(data => {
            this.recipes.splice(0)
            this.assignDataIntoRecipe(data)
        })
    }
    
    private getRecipesFromServer(ingredientFromUser : object){
        type ObjectKey = keyof typeof ingredientFromUser;
        const ingredient = 'ingredientName' as ObjectKey
        return $.get(`/ingredient/${ingredientFromUser[ingredient]}`);
    }

    private assignDataIntoRecipe(recipes: any[]){
        // return recipes.map((r:Recipe) => new Recipe(r.title, r.ingredients, r.strInstructions, r.thumbnail))
        for (const recipe of recipes){
            const title= recipe.title
            const ingredients= recipe.ingredients
            const strInstructions= recipe.strInstructions
            const thumbnail= recipe.thumbnail
            this.recipes.push({title:title, ingredients: ingredients, strInstructions: strInstructions, thumbnail: thumbnail})
        }
    }

    public getRecipes() : Recipe[] {
        return this.recipes;

    }
}