const { MessageEmbed } = require("discord.js")

module.exports = {
    name:"coinflip",
    aliases:["cf"],
    category:"Game/Score/Rank",
    description:"A coinflip but in discord!",

    callback: async ({ message }) => {
        const results = ["Heads", "Tails"]
        const result = results[Math.floor(Math.random() * results.length)]
        if (result === "Heads") {await message.channel.send({embeds: [new MessageEmbed().setTitle("Heads!")]})}
        if (result === "Tails") {await message.channel.send({embeds: [new MessageEmbed().setTitle("Tails!")]})}
    }
}