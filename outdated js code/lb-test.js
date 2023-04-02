const sqlite3 = require('sqlite3').verbose()
const { MessageEmbed } = require('discord.js')

module.exports = {
    name:'lb',
    aliases: ['lbt'],
    description: 'Shows the level leaderboard',
    category:'Game/Score/Rank',
    testOnly: true,

    callback: async ({ message }) => {
        const db = new sqlite3.Database('test.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        db.all(`SELECT xp FROM levels`, [], async (err, rows) => {
            if (err) return console.error(err.message)
            let levels = []
            rows.forEach(row => levels.push(row.xp))
            console.log(levels)
            levels.sort(function(a, b){return a-b})
            console.log(levels)
            let repeats = 0
            const sortedList = levels.reverse()
            console.log(sortedList)
            let leaderboard = []
            for (const xp of sortedList) {
                db.all(`SELECT username FROM levels WHERE xp = '${xp}'`, [], async (err, rows) => {
                    if (err) return console.error(err)
                    repeats += 1
                    if (rows.length > 1) {
                        let l = `${xp / 100}`
                        let level = l.split('.')[0]
                        console.log(repeats)
                        console.log(xp) 
                        leaderboard.push(`${repeats}. This position is tied by ${rows.length} people. XP: ${xp}, LEVEL: ${level}`)
                    }
                    else {
                        console.log(repeats)
                        console.log(xp)
                        let l = `${xp / 100}`
                        let level = l.split('.')[0] 
                        const username = rows[0].username
                        leaderboard.push(`${repeats}. ${username}, XP: ${xp}, LEVEL: ${level}`)
                    }
                })
            }
            console.log(leaderboard)
            const emb = new MessageEmbed()
             .setTitle('Level Leaderboard')
             .setDescription(`${leaderboard[0]}\n${leaderboard[1]}\n${leaderboard[2]}\n${leaderboard[3]}
             ${leaderboard[4]}\n${leaderboard[5]}\n${leaderboard[6]}\n${leaderboard[7]}\n${leaderboard[8]}\n${leaderboard[9]}\n`)
             .setColor('PURPLE')
            await message.channel.send({embeds: [emb]})
        })
    }
}