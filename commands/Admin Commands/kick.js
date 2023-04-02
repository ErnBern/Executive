module.exports = {
    name:"kick",
    description:"Kicks a user!",
    category:"Admin Commands",
    permissions:['ADMINISTRATOR'],
    minArgs: 1,
    expectedArgs:"<user> <reason>",

    callback: ({ message, args }) => {
        const target = message.mentions.members?.first()

        if (!target) {
            message.reply("You need to tag someone to kick!")
            return
        } if (!target.kickable) {
            message.reply("Cannot kick that member!")
            return
        }

        args.shift()
        if (args.length < 0) {
            var reason = args.join(" ")
        } else {
            var reason = "None"
        }
        target.kick(reason)

        message.channel.send(`<@${target.id}> has been kicked for ${reason}`)
    },
}