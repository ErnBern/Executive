const sqlite3 = require('sqlite3').verbose()

module.exports = (client) => {
    client.on('messageCreate', (message) => {
        if (message.author.bot) return
        if (message.author.length < 3) return
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        db.all(`SELECT * FROM levels WHERE id = '${message.author.id}'`, [], (err, rows) => {
            if (err) return console.error(err.message)
            let len = 0
            rows.forEach(row => {
                len += 1
            })
            if (len === 0) {
                let sql = 'INSERT INTO levels(id, xp, username) VALUES(?,?,?)'
                db.run(sql, [`${message.author.id}`, 0, `${message.author.username}#${message.author.discriminator}`])
            }
        })
        db.all(`SELECT xp FROM levels WHERE id = '${message.author.id}'`, [], (err, rows) => {
            if (err) return console.error(err.message)
            rows.forEach(row => {
                let xp = Object.values(row)[0]
                xp += 1
                db.run(`UPDATE levels SET xp = '${xp}' WHERE id = '${message.author.id}'`)
            })
            
        })
        
    })
}

module.exports.config = {
    dbName: 'LEVELER',
    displayName: 'Leveler',
}