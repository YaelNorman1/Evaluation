class Render {

    renderRecipesToScreen(recipes :Recipe[]) {
        $('.recipes-container').empty();
        const source = $('#recipe-template').html();
        const template = Handlebars.compile(source);
        for (const recipe of recipes) {
            const newHTML = template({recipe});
            $('.recipes-container').append(newHTML);   
        }
    }
}
