const { MessageEmbed } = require("discord.js")

module.exports = {
    name:"poll",
    description:"A poll with a simple thumbs up and down!",
    category:"Polls",
    minArgs: 1,
    expectedArgs: "<question>",
    
    callback: async ({ message, args}) => {
        if (message.member.roles.cache.some(r => r.name === 'TC HELPER') || message.member.roles.cache.some(r => r.name === 'TC MEMBERS') || message.member.roles.cache.some(r => r.name === 'FOUNDER')) {
            await message.delete()
            const question = args.join(" ")
            const emb = new MessageEmbed()
            .setTitle("Opinion")
            .setDescription(`${question}`)

            msg = await message.channel.send({embeds: [emb]})
            msg.react("👍")
            msg.react("👎")
        } else if (message.member.roles.cache.some(r => r.name === "Server Booster")) {
            await message.delete()
            const question = args.join(" ")
            const emb = new MessageEmbed()
            .setTitle("Opinion")
            .setDescription(`${question}`)

            msg = await message.channel.send({embeds: [emb]})
            msg.react("👍")
            msg.react("👎")
        } else {return "You do not have the required roles to use this command! You need one of the following: Server Booster, Founder, TC MEMBERS, TC HELPER"}
    },
}