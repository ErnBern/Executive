module.exports = {
    name: "disenfranchise",
    description: "Revokes a member's the ability to vote in daily and random opinion!",
    category: "Admin Commands",
    permissions: ["ADMINISTRATOR"],
    minArgs: 1,
    expectedArgs: "<user>",

    callback: async ({ message, guild }) => {
        const target = message.mentions.members?.first()

        if (!guild) {return 'You can only use this command in a server!'}

        const opinion = message.guild.roles.cache.find(r => r.name === 'OPINION')
        if (target.roles.cache.some(r => r.name === 'OPINION')) {
            await message.channel.send(`<@${target.id}> has already has had their ability to vote revoked`)
            return
        } else {
        if (!target) {
            message.reply("You need to tag someone to take away their ability to vote")
            return
        } 
        try {
            target.roles.remove(opinion)
        } catch {
            message.channel.send(`Can't take away <@${target.id}>'s ability to vote`)
            return
        }
        message.channel.send(`<@${target.id}> has had their ability to vote revoked`)
        }
    },
}