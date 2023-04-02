const { MessageEmbed } = require("discord.js")

module.exports = {
    name: 'eightball',
    aliases: ['8ball', '8_ball', '8b'],
    category: 'Normal Commands',
    description: 'An eightball in discord!',
    minArgs: 1,
    expectedArgs: '<question>',

    
    callback: async ({ message, args }) => {
        const question = args.join(' ')
        const responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
        "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
        "My sources say no.",
        "Outlook not so good.", "Outlook good.", "Signs point to yes.",
        "Very doubtful.", "Without a doubt.",
        "Yes.", "Yes – definitely.", "You may rely on it.",
        "I don't know but I do know that you should subscribe to Think Cyber!"]
        const response = responses[Math.floor(Math.random() * responses.length)]
        const emb = new MessageEmbed()
        .setTitle("Eightball")
        .addField("Question:",  question, true)
        .addField("Response:", response, true)
        .setThumbnail("https://magic-8ball.com/wp-content/themes/astra-child/assets/images/magicBallStart.webp")

        await message.channel.send({embeds: [emb]})
    },
}