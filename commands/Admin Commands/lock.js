module.exports = {
    name:"lock",
    category:"Admin Commands",
    expectedArgs: '<channel or none>',
    description: "Locks a channel",
    
    callback: ({ message, args }) => {
        let channel = message.mentions.channels.first() || message.guild.channels.cache.get(args[0])
        const verified = message.guild.roles.cache.find(r => r.name === 'VERIFIED')

        if (!channel) channel = message.channel

        if (channel.permissionsFor(verified).has('SEND_MESSAGES') === false) {
            message.channel.send(`${channel} is already locked!`)
            return
        }
        
        channel.permissionOverwrites.edit(verified, { SEND_MESSAGES: false })
        message.channel.send(`Locked ${channel}`)
    }
}