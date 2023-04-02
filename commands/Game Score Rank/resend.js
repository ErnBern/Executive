const tictactoeSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/tictactoe-schema')

module.exports = {
    name: 'resend',
    description: 'Resends the tic-tac-toe board during a game!',
    category: 'Game/Score/Rank',
    aliases: ['rs'],

    callback: async ({ message }) => {
        const result = await tictactoeSchema.findOne({player1: message.author.id}) || await tictactoeSchema.findOne({player2: message.author.id})
        if (result === null) {return 'You are not in a game'}
        let turn
        if (result.turn === 1) {turn = result.player1}
        if (result.turn === 0) {turn = result.player2}
        const msg = await message.channel.send(`${result.pos1}${result.pos2}${result.pos3}\n${result.pos4}${result.pos5}${result.pos6}\n${result.pos7}${result.pos8}${result.pos9}`)
        result.messageId = msg.id
        const turnmsg = await message.channel.send(`<@${turn}>'s turn`)
        result.turnId = turnmsg.id
        await result.save()
    }

}