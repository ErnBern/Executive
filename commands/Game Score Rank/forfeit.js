const tictactoeSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/tictactoe-schema')
const sqlite3 = require('sqlite3')

module.exports = {
    name:'forfeit',
    category: 'Game/Score/Rank',
    description: 'Forfeits a game of tic-tac-toe!',
    aliases: ['ff'],

    callback: async ({ client, message }) => {
        const db = new sqlite3.Database('test.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        const result = await tictactoeSchema.find({player1: message.author.id})
        let res
        let query
        if (result.length === 0) {
            res = await tictactoeSchema.findOne({player2: message.author.id})
            query = {player2: message.author.id}
        } else if (result.length === 1) {
            res = await tictactoeSchema.findOne({player1: message.author.id})
            query = {player1: message.author.id}
        } if (!res) {return `You are not in a game`}
        const { channelId, turnId, player1, player2 } = res
        if (player1 === message.author.id) {
            db.all(`SELECT loses FROM tictactoe WHERE id = '${message.author.id}'`, [], (err, rows) => {
                if (err) return console.error(err.message)
                rows.forEach(row => {
                    let loses = Object.values(row)[0]
                    loses += 1
                    db.run(`UPDATE tictactoe SET loses = '${loses}' WHERE id = '${message.author.id}'`)
                })
            })
            db.all(`SELECT wins FROM tictactoe WHERE id = '${player2}'`, [], (err, rows) => {
                if (err) return console.error(err.message)
                rows.forEach(row => {
                    let wins = Object.values(row)[0]
                    wins += 1
                    db.run(`UPDATE tictactoe SET wins = '${wins}' WHERE id = '${player2}'`)
                })
            })
        } if (player2 === message.author.id) {
            db.all(`SELECT loses FROM tictactoe WHERE id = '${message.author.id}'`, [], (err, rows) => {
                if (err) return console.error(err.message)
                rows.forEach(row => {
                    let loses = Object.values(row)[0]
                    loses += 1
                    db.run(`UPDATE tictactoe SET loses = '${loses}' WHERE id = '${message.author.id}'`)
                })
            })
            db.all(`SELECT wins FROM tictactoe WHERE id = '${player1}'`, [], (err, rows) => {
                if (err) return console.error(err.message)
                rows.forEach(row => {
                    let wins = Object.values(row)[0]
                    wins += 1
                    db.run(`UPDATE tictactoe SET wins = '${wins}' WHERE id = '${player1}'`)
                })
            })
        }
        db.close()
        const channel = await client.channels.fetch(channelId)
        const msg = await channel.messages.fetch(turnId)
        msg.edit(`<@${message.author.id}> has forfeited the match!`)
        message.delete()
        await tictactoeSchema.deleteOne(query)
    }
}