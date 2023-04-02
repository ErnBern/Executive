module.exports = {
    name:"unlock",
    category:"Admin Commands",
    description: "Unlocks a locked channel",
    permissions: ['ADMINISTRATOR'],
    
    callback: ({ message, args }) => {
        let channel = message.mentions.channels.first() || message.guild.channels.cache.get(args[0])
        const verified = message.guild.roles.cache.find(r => r.name === 'VERIFIED')

        if (!channel) channel = message.channel

        if (channel.permissionsFor(verified).has('SEND_MESSAGES') === true) {
            message.channel.send(`${channel} is already unlocked!`)
            return
        }
        
        channel.permissionOverwrites.edit(verified, { SEND_MESSAGES: true })
        message.channel.send(`Unlocked ${channel}`)
    }
}