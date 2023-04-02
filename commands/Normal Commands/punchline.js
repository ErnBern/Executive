const { MessageEmbed } = require("discord.js")

module.exports = {
    name: 'punch_line',
    aliases: ['punchline', 'pl'],
    category: 'Normal Commands',
    description: "Sends a random joke with a punchline!",

    callback: async ({ message }) => {
        const punch_lines = ["Q: Why are balloons so expensive? A: Inflation.",
                       "Q: What do you call cheese that isn’t yours? A: Nacho cheese!",
                       "Q: What side of a tree grows the most branches? A: The outside!",
                       "Q: Why did an old man fall in a well? A: Because he couldn’t see that well!",
                       "Q: What do you call a fish with no eye? A: A fsh.",
                       "Q: What breed of dog can jump higher than a skyscraper? A: Any breed of dog. Skyscrapers can’t jump.",
                       "Q: Why are elevator jokes so good? A: They work on many levels.",
                       "Q: Why are peppers the best at archery? A: Because they habanero.",
                       "Q: Why did the computer get mad at the printer? A: Because it didn’t like its toner voice.",
                       "Q: Why is Peter Pan always flying? A: Because he Neverlands.",
                       "Q: What did the three-legged dog say when he walked into a saloon?A: “I’m looking for the man who shot my paw.”",
                       "Q: What’s the best way to watch a fly-fishing tournament? A: Live stream it.",
                       "Q: Why did the broom decide to go to bed? A: It was very sweepy.",
                       "Q: Why are nurses always running out of red crayons? A: Because they often have to draw blood.",
                       "Q: Why are abortion jokes offensive? A: Because they leave an empty feeling inside"]
        const punch_line = punch_lines[Math.floor(Math.random() * punch_lines.length)]
        const laugh = Math.floor((Math.random() * 5) + 1)
        if (laugh === 1) {
            const emb = new MessageEmbed()
            .setTitle("Punch Line")
            .setDescription(`${punch_line}`)
            .setThumbnail("https://i0.wp.com/antidotesforchimps.com/wp-content/uploads/2019/05/86fe066b8ed2eab07a9392a63db4625b.jpg?w=800&ssl=1")
            await message.channel.send({embeds: [emb]})
        } if (laugh === 2) {
            const emb = new MessageEmbed()
            .setTitle("Punch Line")
            .setDescription(`${punch_line}`)
            .setThumbnail("https://images.unsplash.com/photo-1586474714722-d1f9e551cf34?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")
            await message.channel.send({embeds: [emb]})
        } if (laugh === 3) {
            const emb = new MessageEmbed()
            .setTitle("Punch Line")
            .setDescription(`${punch_line}`)
            .setThumbnail("https://d2rd7etdn93tqb.cloudfront.net/wp-content/uploads/2018/07/girl-laughing-article-071318.jpg")
            await message.channel.send({embeds: [emb]})
        } if (laugh === 4) {
            const emb = new MessageEmbed()
            .setTitle("Punch Line")
            .setDescription(`${punch_line}`)
            .setThumbnail("https://i0.wp.com/digest.bps.org.uk/wp-content/uploads/2016/05/b61eb-thinkstockphotos-92134543.jpg?ssl=1")
            await message.channel.send({embeds: [emb]})
        } if (laugh === 5) {
            const emb = new MessageEmbed()
            .setTitle("Punch Line")
            .setDescription(`${punch_line}`)
            .setThumbnail("https://c.tenor.com/-B859OUddZIAAAAC/crying-laughing.gif")
            await message.channel.send({embeds: [emb]})
        }

    },
}