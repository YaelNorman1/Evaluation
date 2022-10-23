

$("#submitIngredient").on("click", async function (){
    const dataFromUser= get_data_from_input();
    await playersDataModule.generateNewTeamPlayers(dataFromUser);
    let players= getPlayersIfBirthDate();
    render.renderPlayersToScreen(players)
})