const lockSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/lock-schema')

module.exports = {
    name:"templock",
    description:"Temporarily locks the channel you're in",
    aliases: ["tl"],
    permissions: ['ADMINISTRATOR'],
    minArgs: 1,
    expectedArgs: '<duration> <reason>',
    category: "Admin Commands",
    
    callback: async ({
        args,
        member: staff,
        guild,
        client,
        message,
    }) => {
        if (!guild) {return 'You can only use this command in a server!'}
        const duration = args.shift()
        if (args.length < 0) {
            var reason = args.join(" ")
        } else {
            var reason = "None"
        }
        let channel = message.channel
        let channelId = channel.id

        let time 
        let type 
        try {
            const split = duration.match(/\d+|\D+/g)
            time = parseInt(split[0])
            type = split[1].toLowerCase()
        } catch (e) {
            return "Invalid time format! Example format: \"10d\" where 'd' = days, 'h' = hours, 'm' = minutes"
        }

        if (type === "s") {
            time *= 1
        } else if (time === 'h') {
            time *= 60
        } else if (type === 'd') {
            time *= 60 * 24
        } else if (type !== 'm') {
            return 'Please use "s", "m", "h" or "d", for seconds, minutes, hours, and days'
        }

        const expires = new Date()
        expires.setMinutes(expires.getMinutes() + time)

        const result = await lockSchema.findOne({
            guildId: guild.id,
            channelId,
            type: 'mute',
        })
        if (result) {
            return `<#${channelId}> is already locked!`
        }
        try {
            const verified = message.guild.roles.cache.find(r => r.name === 'VERIFIED')
            if (channel.permissionsFor(verified).has('SEND_MESSAGES') === false) {
                message.channel.send(`${channel} is already locked!`)
                return
            }
            channel.permissionOverwrites.edit(verified, { SEND_MESSAGES: false })

            await new lockSchema({
                channelId,
                guildId: guild.id,
                staffId: staff.id,
                reason,
                expires,
                type:'lock',
            }).save()
        } catch (ignored) {
            return 'Lock failed'
        }

        message.channel.send(`<#${channelId}> has been locked for ${duration}`)
    },
}