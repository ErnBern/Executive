module.exports = {
    name: "franchise",
    description: "Gives a member the ability to vote in daily and random opinion!",
    category: "Admin Commands",
    permissions: ["ADMINISTRATOR"],
    minArgs: 1,
    expectedArgs: "<user>",

    callback: async ({ message, guild }) => {
        const target = message.mentions.members?.first()

        if (!guild) {return 'You can only use this command in a server!'}

        const opinion = message.guild.roles.cache.find(r => r.name === 'OPINION')
        if (target.roles.cache.some(r => r.name === 'OPINION')) {
            await message.channel.send(`<@${target.id}> can already vote`)
            return
        } else {
        if (!target) {
            message.reply("You need to tag someone to give the ability to vote to")
            return
        } 
        try {
            target.roles.add(opinion)
        } catch {
            message.channel.send(`<@${target.id}> can't be given the ability to vote`)
            return
        }
        message.channel.send(`<@${target.id}> has been given the ability to vote`)
        }
    },
}