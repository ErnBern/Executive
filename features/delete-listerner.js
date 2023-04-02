const schema = require(`../models/delete-schema`)

module.exports = (client) => {
    client.on("messageReactionAdd", async (reaction, user) => {
        const results = await schema.find({guildId: reaction.message.guild.id})
        for (const result of results) {
            const { staff, msgId, chId, AcId } = result
            const ch = await client.channels.fetch(chId)
            const ac = await client.channels.fetch(AcId)
            const msg = await ac.messages.fetch(msgId)
            if (user.bot) return 
            if (msgId !== reaction.message.id) return
            if (user.id == staff) {
                if (reaction.emoji.name === '✅') {
                    ch.delete()
                    msg.delete()
                    await schema.deleteOne({
                        guildId: reaction.message.guild.id,
                        chId
                    })
                } if (reaction.emoji.name === '❌') {
                    msg.delete()
                    await schema.deleteOne({
                        guildId: reaction.message.guild.id,
                        chId
                    })
                }
            }
        }
    })
}

module.exports.config = {
    dbName: 'CHANNEL_DELETE_REQUESTS_LISTENER',
    displayName: 'Channel Delete Request Listener',
}