const punishmentSchema = require('../models/punishment-schema')

module.exports = (client) => {
    client.on('guildMemberAdd', async (member) => {
        const result = await punishmentSchema.findOne({
            guildId: member.guild.id,
            userId: member.guild.id,
            type: 'mute',
        })

        if (result) {
            const mutedRole = member.guild.roles.cache.find(
                (role) => role.name === 'MUTED'
            )
            
            if (mutedRole) {
                member.roles.add()
        }
        }

    })

    const check = async () => {
        const query = {
            expires: { $lt: new Date() },
        }
        const results = await punishmentSchema.find(query)

        for (const result of results) {
            const { guildId, userId, type } = result
            const guild = await client.guilds.fetch(guildId)
            if (!guild) {
                console.log(`Guild "${guildId}" no longer uses this bot.`)
                continue
            }

            if (type === 'ban') {
                guild.members.unban(userId, 'Ban expired')
            } else if (type === 'mute') {
                const muteRole = guild.roles.cache.find((role) => role.name === 'MUTED')
                if (!muteRole) {
                    console.log(`Guild "${guildID}" has no muted role`)
                    continue
                }

            const member = guild.members.cache.get(userId)
            const verfied = guild.roles.cache.find((role) => role.name === 'VERIFIED')
            const opinion = guild.roles.cache.find((role) => role.name === 'OPINION')
            if (!member) {
                continue
            }
            member.roles.add(opinion)
            member.roles.add(verfied)
            member.roles.remove(muteRole)
            }
        }
        
        await punishmentSchema.deleteMany(query)

        setTimeout(check, 1000 * 10)
    }
    check()
}


module.exports.config = {
    dbName: 'EXPIRED_PUNISHMENTS',
    displayName: 'Expired Punishments',
}