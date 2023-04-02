const { MessageEmbed } = require('discord.js')
const sqlite3 = require('sqlite3').verbose()

module.exports = {
    name: 'score',
    minArgs: 1,
    maxArgs: 1,
    category: 'Game/Score/Rank',
    expectedArgs: '<tic-tac-toe/tictactoe/ttt/mathquestion/mq',
    description: 'Shows your tic-tac-toe/math score',
    aliases: ['sc'],

    callback: async ({ message, args }) => {
        const checker = args.shift()
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        if (checker === 'tic-tac-toe' || checker === 'tictactoe' || checker === 'ttt') {
            let wins
            let loses
            let ties
            db.all(`SELECT * FROM wins WHERE id = '${message.author.id}'`, [], async (err, rows) => {
                if (err) return console.error(err.message)
                let len = 0
                rows.forEach(row => {
                    const values = Object.values(row)
                    len += 1
                    wins = values[2]
                    loses = values[3]
                    ties = values[4]
                })
                if (len === 0) {
                    const sql = `INSERT INTO wins(id,username,wins,loses,ties) VALUES(?,?,?,?,?)`
                    db.run(sql, [`${message.author.id}`, `${message.author.username}#${message.author.discriminator}`, 0, 0, 0])
                    wins, loses, ties = 0, 0, 0
                }
                const emb = new MessageEmbed()
                 .setTitle(`${message.author.username}'s Score`)
                 .addFields({name: 'Wins:', value:`${wins}`, inline: false},
                 {name: 'Loses:', value:`${loses}`, inline:false},
                 {name: 'Ties:', value:`${ties}`, inline:false})
                 .setThumbnail(message.member.user.displayAvatarURL({dynamic:true}))
                 .setColor('RED')
                await message.channel.send({embeds: [emb]})
                db.close()
            })
        } if (checker === 'mq' || checker === 'mathquestion') {
            let correct
            let incorrect
            db.all(`SELECT * FROM mathgame WHERE id = '${message.author.id}'`, [], async (err, rows) => {
                if (err) return console.error(err.message)
                let len = 0
                rows.forEach(row => {
                    const values = Object.values(row)
                    len += 1
                    correct = values[2]
                    incorrect = values[3]
                })
                if (len === 0) {
                    const sql = `INSERT INTO mathgame(id,username,correct,incorrect) VALUES(?,?,?,?)`
                    db.run(sql, [`${message.author.id}`, `${message.author.username}#${message.author.discriminator}`, 0, 0])
                    correct = 0
                    incorrect = 0
                    console.log(correct, incorrect)
                }
                const emb = new MessageEmbed()
                 .setTitle(`${message.author.username}'s Score`)
                 .addFields({name: 'Correct Answers:', value:`${correct}`, inline: true},
                 {name: 'Incorrect Answers:', value:`${incorrect}`, inline:true})
                 .setThumbnail(message.member.user.displayAvatarURL({dynamic:true}))
                 .setColor('BLUE')
                await message.channel.send({embeds: [emb]})
                db.close()
            })
        }
    }
}