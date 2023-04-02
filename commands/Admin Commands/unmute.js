module.exports = {
    name: "unmute",
    description: "Unmutes a user",
    category: "Admin Commands",
    permissions: ["ADMINISTRATOR"],
    minArgs: 1,
    expectedArgs: "<user>",

    callback: async ({ message, guild }) => {
        const target = message.mentions.members?.first()

        if (!guild) {return 'You can only use this command in a server!'}

        const mute = message.guild.roles.cache.find(r => r.name === 'MUTED')
        const verified = message.guild.roles.cache.find(r => r.name === 'VERIFIED')
        const opinion = message.guild.roles.cache.find(r => r.name === 'OPINION')
        if (!target.roles.cache.some(r => r.name === 'MUTED')) {
            await message.channel.send(`<@${target.id}> is already unmuted`)
            return
        } else {
        if (!target) {
            message.reply("You need to tag someone to unmute!")
            return
        } 
        try {
            target.roles.remove(mute)
            target.roles.add(verified)
            target.roles.add(opinion)
        } catch {
            message.channel.send(`<@${target.id}> can't be unmuted`)
            return
        }
        message.channel.send(`<@${target.id}> has been unmuted`)
        }
    },
}