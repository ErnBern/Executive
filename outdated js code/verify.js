module.exports = {
    name: "Verify",
    description: "Verifies you!",
    category: "Verify",

    callback: async ({ message }) => {
        if (message.member.roles.cache.some(r => r.name === 'VERIFIED')) {
            await message.channel.send("You are already verified")
        } else {
            const verify = message.guild.roles.cache.find(r => r.name === 'VERIFIED')
            const opinion = message.guild.roles.cache.find(r => r.name === 'OPINION')
            message.member.roles.add(verify)
            message.member.roles.add(opinion)
            await message.channel.send("You have now been verified")
            await message.member.send("You have now been verified")
        }
    },
}