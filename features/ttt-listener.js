const schema = require('../models/ttt')
const tictactoeSchema = require('../models/tictactoe-schema.js')

module.exports = (client) => {
    client.on("messageReactionAdd", async (reaction, user) => {
        const result = await schema.findOne({accepter: user.id})
        if (!result) return
        const { author, channelId, accepter, messageId } = result
        const channel = await client.channels.fetch(channelId)
        const message = await channel.messages.fetch(messageId)
        if (user === client.user) return
        if (messageId !== reaction.message.id) return
        if (user.id !== accepter) {return}
        if (reaction.emoji.name === '✅') {
            const turn = Math.floor(Math.random() * 2)
            let ms
            if (turn === 1) {ms = await channel.send(`<@${author}>'s turn`)}
            if (turn === 0) {ms = await channel.send(`<@${accepter}>'s turn`)}
            const board = ['⬜⬜⬜',
                    '⬜⬜⬜',
                    '⬜⬜⬜']
                const msg = await channel.send(`${board[0]}\n${board[1]}\n${board[2]}`)
                await new tictactoeSchema({
                channelId: channel.id,
                player1: author,
                player2: accepter,
                turn, 
                turnId: ms.id,
                messageId: msg.id,
                pos1: ':white_large_square:',
                pos2: ':white_large_square:',
                pos3: ':white_large_square:',
                pos4: ':white_large_square:',
                pos5: ':white_large_square:',
                pos6: ':white_large_square:',
                pos7: ':white_large_square:',
                pos8: ':white_large_square:',
                pos9: ':white_large_square:',
                turns: 0,
            }).save()
            await message.delete()
            await schema.deleteOne({accepter: user.id})
        } if (reaction.emoji.name === '❌') {
            await message.delete()
            await schema.deleteOne({accepter: user.id})
        }
    })

    const check = async () => {
        const query = {
            expires: { $lt: new Date() },
        }
        const results = await schema.find(query)

        for (const result of results) {
            const { channelId, messageId } = result
            const channel = await client.channels.fetch(channelId)
            const message = await channel.messages.fetch(messageId)

            await message.delete
        }
        
        await schema.deleteMany(query)

        setTimeout(check, 1000 * 10)
    }
    check()

    
}        

module.exports.config = {
    dbName: 'TIC-TAC-TOE_VERIFIER',
    displayName: 'TIC-TAC-TOE Verifier',
}