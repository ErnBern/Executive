const { MessageEmbed } = require('discord.js')

module.exports = {
    name: 'ping',
    description: 'Shows your ping!',
    category: "Normal Commands",

    callback: async ({ client, message, args }) => {
        const msg = await message.channel.send('🏓 Pinging.....')
        const emb = new MessageEmbed()
        .setTitle("Pong!")
        .setThumbnail(message.member.user.displayAvatarURL({dynamic:true}))
        .addField('Your Ping:', `${Math.floor(msg.createdAt - message.createdAt)}ms`, false)
        .addField(`Executive's Ping:`, `${client.ws.ping}ms`, false)
        await message.channel.send({embeds: [emb]})
        msg.delete()
    },
}