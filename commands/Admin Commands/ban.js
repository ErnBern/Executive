module.exports = {
    name:"ban",
    description:"Bans a user!",
    category:"Admin Commands",
    permissions:['ADMINISTRATOR'],
    minArgs: 1,
    expectedArgs:"<user> <reason>",

    callback: ({ message, args }) => {
        const target = message.mentions.members?.first()

        if (!target) {
            message.reply("You need to tag someone to ban!")
            return
        } if (!target.bannable) {
            message.reply("Cannot ban that member!")
            return
        }

        args.shift()
        if (args.length < 0) {
            var reason = args.join(" ")
        } else {
            var reason = "None"
        }
        target.ban({
            reason,
            days: 0
        })

        message.channel.send(`<@${target.id}> has been banned for ${reason}`)
    },
}