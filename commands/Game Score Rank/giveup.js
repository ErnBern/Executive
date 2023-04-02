const schema = require('C:/Users/Linna/Documents/Executive/Executive/models/mathgame-schema')
const sqlite3 = require('sqlite3')

module.exports = {
    name:'giveup',
    description: 'Forfeits a math question',
    category: 'Game/Score/Rank',
    aliases: ['gp'],

    callback: async ({ message }) => {
        const result = await schema.findOne({author: message.author.id})
        if (!result) return `You do not have a math question`
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        db.all(`SELECT incorrect FROM mathgame WHERE id = '${message.author.id}'`, [], (err, rows) => {
            if (err) return console.error(err.message)
            rows.forEach(row => {
                let incorrect = Object.values(row)[0]
                db.run(`UPDATE mathgame SET incorrect = '${incorrect + 1}' WHERE id = '${message.author.id}'`)
            })
        })
        db.close()
        message.channel.send("You have forfeited your math question")
        await schema.deleteOne({author: message.author.id})
    },
}