const lockSchema = require('../models/lock-schema')

module.exports = (client) => {
    const check = async () => {
        const query = {
            expires: { $lt: new Date() },
        }
        const results = await lockSchema.find(query)

        for (const result of results) {
            const { guildId, channelId, type } = result
            const guild = await client.guilds.fetch(guildId)
            const channel = await client.channels.fetch(channelId)
            if (!guild) {
                console.log(`Guild "${guildId}" no longer uses this bot.`)
                continue
            }
            
            if (type === 'lock') {
                try {
                    const verified = guild.roles.cache.find(r => r.name === 'VERIFIED')
                    if (channel.permissionsFor(verified).has('SEND_MESSAGES') === true) {
                        console.log(`<#${channelId}> is already unlocked!`)
                        return
                    }
                    
                    channel.permissionOverwrites.edit(verified, { SEND_MESSAGES: true })
                } catch (err) {console.error(err)}
            }
        }
        
        await lockSchema.deleteMany(query)

        setTimeout(check, 1000 * 10)
    }
    check()
}


module.exports.config = {
    dbName: 'EXPIRED_LOCKS',
    displayName: 'Expired Locks',
}