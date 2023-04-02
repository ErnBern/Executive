const schema = require('C:/Users/Linna/Documents/Executive/Executive/models/mathgame-schema')
const sqlite3 = require('sqlite3')

module.exports = {
    name:'mathquestion',
    description: 'A random math question!',
    aliases: ['mq'],
    category: 'Game/Score/Rank',

    callback: async ({ message }) => {
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        const result = await schema.findOne({author: message.author.id})
        if (result !== null) {return 'Please answer/give up your question before starting a new one!'}
        const picker = Math.floor(Math.random() * 4)
        db.all(`SELECT * FROM mathgame WHERE id = '${message.author.id}'`, [], (err, rows) => {
            if (err) return console.error(err)
            let len = 0
            rows.forEach(row => {
              len += 1  
            })
            if (len === 0) {
                let sql = `INSERT INTO mathgame(id, username, correct, incorrect) VALUES(?,?,?,?)`
                db.run(sql, [`${message.author.id}`, `${message.author.username}#${message.author.discriminator}`, 0, 0])
                db.close()
            }
        })
        let question
        let answer
        let term1
        let term2
        if (picker === 0) {
            term1 = Math.floor((Math.random() * 10) + 1)
            term2 = Math.floor((Math.random() * 10) + 1)
            question = `${term1} + ${term2} = ?`
            answer = term1 + term2
        } if (picker === 1) {
            term1 = Math.floor((Math.random() * 10) + 1)
            term2 = Math.floor((Math.random() * 10) + 1)
            question = `${term1} - ${term2} = ?`
            answer = term1 - term2
        } if (picker === 2) {
            term1 = Math.floor((Math.random() * 10) + 1)
            term2 = Math.floor((Math.random() * 10) + 1)
            question = `${term1} x ${term2} = ?`
            answer = term1 * term2
        } if (picker === 3) {
            term1 = Math.floor((Math.random() * 10) + 1)
            term2 = Math.floor((Math.random() * 10) + 1)
            question = `${term1} ÷ ${term2} = ?\n This is a division question, please round up to the nearest tenth!`
            answer = Math.round((term1 / term2) * 10) / 10
        }
        message.reply(question)
        await new schema({
            author: message.author.id,
            question,
            answer,
            channel: message.channel.id
        }).save()
    }
}