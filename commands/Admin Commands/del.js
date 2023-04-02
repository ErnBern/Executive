const schema = require(`C:/Users/Linna/Documents/Executive/Executive/models/delete-schema`)
const { MessageEmbed } = require("discord.js")

module.exports = {
    name:"delete",
    category:"Admin Commands",
    description:"The channel you're in",
    permissions: ['ADMINISTRATOR'],

    callback: async ({ message }) => {
        message.delete()
        const channel = message.mentions.channels.first() || message.channel

        const emb = new MessageEmbed()
        .setTitle("Confirm")
        .setDescription(`You are about to delete text channel <#${channel.id}> please react to confirm your decision`)
        .setColor("GREEN")

        msg = await message.channel.send({embeds: [emb]})
        msg.react("✅")
        msg.react("❌")
        const msgId = msg.id
        const res = await schema.findOne({
            guildId: message.guild.id,
            chId: message.channel.id
        })
        if (res) {
            res.msgId = msgId
            res.staff = message.author.id
            await res.save()
        } else {
            await new schema({
                guildId: message.guild.id,
                staff: message.author.id,
                msgId,
                chId: channel.id,
                AcId: message.channel.id,
            }).save()
        }
        
    },
}