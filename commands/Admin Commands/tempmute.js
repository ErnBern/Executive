const punishmentSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/punishment-schema')

module.exports = {
    name:"tempmute",
    description:"Temporarily mutes a user!",
    aliases: ["tm"],
    permissions: ['ADMINISTRATOR'],
    minArgs: 2,
    expectedArgs: '<user> <duration> <reason>',
    category: "Admin Commands",
    
    callback: async ({
        args,
        member: staff,
        guild,
        client,
        message,
    }) => {
        if (!guild) {return 'You can only use this command in a server!'}

        let userId = args.shift()
        const duration = args.shift()
        if (args.length < 0) {
            var reason = args.join(" ")
        } else {
            var reason = "None"
        }
        let user
        
        user = message.mentions.users?.first()

        if (!user) {
            userId = userId.replace(/[<a!>]/g, '')
            user = await client.users.fetch(userId)

            if (!user) {return `Could not find a user with the ID "${userId}"`}
        }
        userId = user.id

        let time 
        let type 
        try {
            const split = duration.match(/\d+|\D+/g)
            time = parseInt(split[0])
            type = split[1].toLowerCase()
        } catch (e) {
            return "Invalid time format! Example format: \"10d\" where 'd' = days, 'h' = hours, 'm' = minutes"
        }

        if (time === 'h') {
            time *= 60
        } else if (type === 'd') {
            time *= 60 * 24
        } else if (type !== 'm') {
            return 'Please use "m", "h" or "d", for minutes, hours, and days'
        }

        const expires = new Date()
        expires.setMinutes(expires.getMinutes() + time)

        const result = await punishmentSchema.findOne({
            guildId: guild.id,
            userId,
            type: 'mute',
        })
        if (result) {
            return `<@${userId}> is already muted!`
        }
        try {
            const member = await guild.members.fetch(userId)
            if (member) {
                const muteRole = guild.roles.cache.find((role) => role.name === 'MUTED')
                if (!muteRole) {
                    return 'This server does not have a "MUTED" role!'
                }
                member.roles.add(muteRole)
                try {
                    const verified = guild.roles.cache.find((role) => role.name === 'VERIFIED')
                    const opinion= guild.roles.cache.find((role) => role.name === 'OPINION')
                    member.roles.remove(verified)
                    member.roles.remove(opinion)
                } catch {"pass"}
            }
            await new punishmentSchema({
                userId,
                guildId: guild.id,
                staffId: staff.id,
                reason,
                expires,
                type:'mute',
            }).save()
        } catch (ignored) {
            return 'Cannot mute the user!'
        }

        message.channel.send(`<@${userId}> has been muted for ${duration}`)
    },
}