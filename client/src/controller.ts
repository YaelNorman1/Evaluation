const recipesModule= new RecipesDataModule();
const render= new Render();

$("#submitIngredient").on("click", async function (){
    const ingredientFromUser= get_data_from_input();
    await recipesModule.generateAllRecipes(ingredientFromUser);
    render.renderRecipesToScreen(recipesModule.getRecipes())
    // i need to add the query params of sensetivity
})

function get_data_from_input() : object{
    const ingredientName = (<HTMLInputElement>document.getElementById("input_ingredient")).value;
    return {'ingredientName': ingredientName};
}