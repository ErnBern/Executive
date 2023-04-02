const schema = require('../models/mathgame-schema')
const sqlite3 = require('sqlite3')

module.exports = (client) => {
    client.on('messageCreate', async (message) => {
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        const result = await schema.findOne({author: message.author.id})
        if (result) {
            const { answer, channel } = result
            const ch = await client.channels.fetch(channel)
            if (message.content == answer) {
                ch.send("Answer Correct!")
                db.all(`SELECT correct FROM mathgame WHERE id = ${message.author.id}`, [], (err, rows) => {
                    if (err) return console.error(err.message)
                    rows.forEach(row => {
                        let correct = Object.values(row)[0]
                        correct += 1
                        db.run(`UPDATE mathgame SET correct = '${correct}' WHERE id = ${message.author.id}`)
                        db.close()
                    })
                })
                await schema.deleteOne({author: message.author.id})
            } else if (isNaN(message.content)) {
                'pass'
            } else {
                ch.send("Answer Incorrect!")
                await schema.deleteOne({author: message.author.id})
                db.all(`SELECT incorrect FROM mathgame WHERE id = ${message.author.id}`, [], (err, rows) => {
                    if (err) return console.error(err.message)
                    rows.forEach(row => {
                        let incorrect = Object.values(row)[0]
                        incorrect += 1
                        db.run(`UPDATE mathgame SET incorrect = '${incorrect}' WHERE id = ${message.author.id}`)
                        db.close()
                    })
                })
            }
            
        }
    })
}

module.exports.config = {
    dbName: 'ASNWER_VERIFIER',
    displayName: 'Answer Verifier',
}