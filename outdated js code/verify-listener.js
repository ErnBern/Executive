module.exports = (client) => {
    client.on('messageReactionAdd', async (reaction, user) => {
        console.log('test')
        console.log(reaction.message.id)
        if (user.bot) return
        if (970309252533088267 == reaction.message.id) {
            const guild = await client.guilds.fetch(reaction.message.guild.id)
            const member = guild.members.cache.get(user.id)
            const verify = guild.roles.cache.find(r => r.name === 'VERIFIED')
            const opinion = guild.roles.cache.find(r => r.name === 'OPINION')
            member.roles.add(verify)
            member.roles.add(opinion)
            console.log('asdwasd')
        }
    })
}

module.exports.config = {
    dbName: 'VERIFY',
    displayName: 'Verify',
}