const sqlite3 = require('sqlite3').verbose()
const { MessageEmbed } = require('discord.js')

function checker(number) {
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (numbers.includes(number)) {
        number *= 10
        return number
    } else if (number === undefined) {
        number = 0
        return number
    } else {
        return number
    }
}

module.exports = {
    name:'rank',
    description: 'Shows your rank!',
    category:'Game/Score/Rank',

    callback: async ({ message }) => {
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        db.all(`SELECT id, xp FROM levels`, [], async (err, rows) => {
            if (err) return console.error(err.message)
            let rank = []
            let objects = []
            let experience = []
            let mobj = []
            rows.forEach(row => {
                objects.push(row)
                experience.push(row.xp)
            })
            for (const obj of objects) {
                if (obj.id == message.author.id) {
                    mobj.push(obj)
                }
            }
            experience.sort(function(a, b){return a-b})
            const sortedList = experience.reverse()
            for (const xp of sortedList) {
                if (xp === mobj[0].xp) break
                rank.push(`rank`)
            }
            const l = `${mobj[0].xp / 100}`
            const level = l.split('.')[0]
            const lo = l.split('.')[1]
            const leftover = checker(lo)
            let progessbar = []
            if (leftover < 20) progessbar = ':white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:'
            if (leftover <= 20 && leftover < 40) progessbar = ':blue_square::white_large_square::white_large_square::white_large_square::white_large_square:'
            if (40 <= leftover && leftover< 60) progessbar = ':blue_square::blue_square::white_large_square::white_large_square::white_large_square:'
            if (60 <= leftover && leftover < 80) progessbar = ':blue_square::blue_square::blue_square::white_large_square::white_large_square:'
            if (80 <= leftover && leftover < 90) progessbar = ':blue_square::blue_square::blue_square::blue_square::white_large_square:'
            if (90 <= leftover && leftover<= 99) progessbar = ':blue_square::blue_square::blue_square::blue_square::blue_square:'
            const emb = new MessageEmbed()
             .setTitle('Rank')
             .addFields(
                 {name:`Name:`, value: `${message.author}`, inline:true},
                 {name:'Level:', value:`${level}`, inline:true},
                 {name:'Rank:', value:`${rank.length + 1}`, inline:true},
                 {name:'Progess Bar', value:`${progessbar}`, inline:false}
             )
             .setColor('ORANGE')
             .setThumbnail(message.member.user.displayAvatarURL({dynamic:true}))
            await message.channel.send({embeds: [emb]})
        })
    }
}