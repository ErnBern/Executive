module.exports = {
    name: "mute",
    description: "Mutes a user",
    category: "Admin Commands",
    permissions: ["ADMINISTRATOR"],
    minArgs: 1,
    expectedArgs: "<user>",

    callback: async ({ message, guild }) => {
        const target = message.mentions.members?.first()
        if (target === message.author) {
            message.channel.send("You can't mute yourself")
            return
        }

        if (!guild) {return 'You can only use this command in a server!'}

        const mute = message.guild.roles.cache.find(r => r.name === 'MUTED')
        const verified = message.guild.roles.cache.find(r => r.name === 'VERIFIED')
        const opinion = message.guild.roles.cache.find(r => r.name === 'OPINION')
        if (target.roles.cache.some(r => r.name === 'MUTED')) {
            await message.channel.send(`<@${target.id}> is already muted`)
            return
        } else {
        if (!target) {
            message.reply("You need to tag someone to mute!")
            return
        } 
        try {
            target.roles.add(mute)
            target.roles.remove(verified)
            target.roles.remove(opinion)
        } catch {
            console.error(err)
            message.channel.send(`<@${target.id}> can't be muted`)
            return
        }
        message.channel.send(`<@${target.id}> has been muted`)
        }
    },
}