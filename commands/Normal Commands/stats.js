const { MessageEmbed, version } = require("discord.js")

module.exports = {
    name: "Stats",
    description: "The bot and our server's stats",
    category: "Normal Commands",

    callback: async ({ client, message }) => {
        let creation = `${message.channel.createdAt}`
        let creationDate = String(creation.split(" GMT-0600"))
        if (message.channel.topic === null) {var topic = "No Topic";} else {var topic = message.channel.topic}
        const emb = new MessageEmbed()
        .setTitle("Statistics")
        .setColor("WHITE")
        .addFields({name: "Members:", value: `${message.guild.memberCount}`, inline: false},
        {name:"Coding Languages:", value: `Python and JavaScript`, inline: false},
        {name:"Discord.js Version:", value:`v${version}`, inline: false},
        {name:"Discord.py Version:", value:`v1.7.3`, inline: false},
        {name:"Node.js Version:", value:`${process.version}`, inline:false},
        {name:"Python Version:", value:`v3.10.2`, inline:false},
        {name:"Lines Of Code:", value:"2228", inline:false},
        {name:"Executive Version:", value:`6`, inline:false},
        {name:"Slow Mode Delay", value: `${message.channel.rateLimitPerUser}`, inline:false},
        {name:"Channel Creation Time:", value:`${creationDate}`, inline:false})
        .setThumbnail(message.guild.iconURL({size: 4096, dynamic: true}))

        await message.channel.send({embeds: [emb]})

    },
}