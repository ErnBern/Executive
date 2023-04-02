const { MessageEmbed } = require('discord.js')
const tictactoeSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/ttt')
const tttSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/tictactoe-schema')
const sqlite3 = require('sqlite3').verbose()

module.exports = {
    name:"tictactoe",
    minArgs: 1,
    maxArgs: 1,
    expectedArgs: '<user>',
    description: "Tic-tac-toe but in discord!",
    aliases: ['ttt'],
    category: "Game/Score/Rank",

    callback: async ({ message }) => {
        const player1 = message.author.id
        const player2 = message.mentions.members?.first().id
        if (player1 === player2) {return `You can't play against yourself`}
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        db.all(`SELECT * FROM wins WHERE id = '${player1}'`, [], (err, rows) => {
            if (err) return console.err(error.message)
            let len = 0
            rows.forEach(row => {
                len += 1
            })
            if (len === 0) {
                sql = `INSERT INTO wins(id, username, wins, loses, ties) VALUES(?,?,?,?,?)`
                db.run(sql, [`${player1}`, `${message.author.username + '#' + message.author.discriminator}`, 0, 0, 0])
                db.close() 
            }
        })
        db.all(`SELECT * FROM wins WHERE id = '${player2}'`, [], (err, rows) => {
            if (err) return console.err(error.message)
            let len = 0
            rows.forEach(row => {
                len += 1
            })
            if (len === 0) {
                sql = `INSERT INTO wins(id, username, wins, loses, ties) VALUES(?,?,?,?,?)`
                db.run(sql, [`${player2}`, `${message.mentions.users.first().username + '#' + message.mentions.users.first().discriminator}`, 0, 0, 0])
                db.close() 
            }
        })
        const result = await tictactoeSchema.findOne({author: player1})
        const res = await tttSchema.findOne({player1: player1})
        const res2 = await tttSchema.findOne({player2: player2})
        if (res && res2) {return `You and <@${player2}> need to end your games before starting a new one!`}
        if (res) {return 'Please end your game before starting a new one!'}
        if (res2) {return `<@${player2}> needs to end their game before starting a new one!`}
        if (result) {return 'You have already challenged someone to a game'}
        const expires = new Date()
        expires.setMinutes(expires.getMinutes() + 10)

        emb = new MessageEmbed()
         .setTitle("Tic-tac-toe")
         .setDescription(`<@${player1}> has challenged <@${player2}> to a match of tic-tac-toe`)
         .setColor("RED")
         try {
            message.delete()
        } catch {
            console.log('The message has already been deleted')
        }
        const msg = await message.channel.send({embeds: [emb]})
        msg.react("✅")
        msg.react("❌")
        await new tictactoeSchema({
            messageId: msg.id,
            accepter: player2,
            author: message.author.id,
            channelId: message.channel.id,
            expires,
        }).save()
    }
}