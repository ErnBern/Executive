module.exports = {
    name:"new",
    description:"Creates a new channel!",
    category:"Admin Commands",
    permissions: ['ADMINISTRATOR'],
    minArgs: 1,
    exepectArgs: '<new_channel_name>',
    
    callback: async ({ client, message, args }) => {
        const channelNameQuery = args.join(" ")
        const ch = await message.guild.channels.create(channelNameQuery)
        message.channel.send(`Made ${ch}`)
        const channelId = ch.id
        const channel = await client.channels.fetch(channelId)
        const verified = message.guild.roles.cache.find(r => r.name === 'VERIFIED')
        const everyone = message.guild.roles.cache.find(r => r.name === '@everyone')
        channel.permissionOverwrites.edit(verified, { VIEW_CHANNEL: false })
        channel.permissionOverwrites.edit(everyone, { VIEW_CHANNEL: false })
    },
}