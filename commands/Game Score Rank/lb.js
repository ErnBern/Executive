const sqlite3 = require('sqlite3').verbose()
const { MessageEmbed } = require('discord.js')

module.exports = {
    name:'leaderboard',
    aliases: ['lb'],
    description: 'Shows the level leaderboard',
    category:'Game/Score/Rank',

    callback: async ({ message }) => {
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        db.all(`SELECT username, xp FROM levels`, [], async (err, rows) => {
            if (err) return console.error(err.message)
            let levels = []
            let obs = []
            rows.forEach(row => {
                levels.push(row.xp)
                obs.push(row)
            })
            levels.sort(function(a, b){return a-b})
            let repeats = 0
            const sortedList = levels.reverse()
            let leaderboard = []
            let usernames = []
            for (const xp of sortedList) {
                repeats += 1
                for (const ob of obs) {
                    if (ob.xp === xp) {
                        let l = `${xp / 100}`
                        let level = l.split('.')[0]
                        if (!leaderboard.includes(`${repeats - 1}. ${ob.username}, XP: ${xp}, LEVEL: ${level}`)) {
                            if (leaderboard.includes(`${repeats}. ${usernames[usernames.length - 1]}, XP: ${xp}, LEVEL: ${level}`)) continue
                            else {leaderboard.push(`${repeats}. ${ob.username}, XP: ${xp}, LEVEL: ${level}`)}
                            usernames.push(ob.username)
                        }
                    }
                }
            }
            const emb = new MessageEmbed()
             .setTitle('Level Leaderboard')
             .setDescription(`${leaderboard[0]}\n${leaderboard[1]}\n${leaderboard[2]}\n${leaderboard[3]}
             ${leaderboard[4]}\n${leaderboard[5]}\n${leaderboard[6]}\n${leaderboard[7]}\n${leaderboard[8]}\n${leaderboard[9]}\n`)
             .setColor('PURPLE')
            await message.channel.send({embeds: [emb]})
        })
    }
}