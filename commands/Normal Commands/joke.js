const { MessageEmbed } = require('discord.js')

module.exports = {
    category: "Normal Commands",
    description: "Sends a random joke!",
    slash: false,
    
    callback: async ({ message }) => {
        const jokes = ["I don't trust stairs. They're always up to something",
        "A guy walked into a bar and lost the limbo contest",
        "I had a dream that I weighed less than a thousandth of a gram. I was like, 0mg.",
        "Mom said I should do lunges to stay in shape. That would be a big step forward.",
        "Every time I take my dog to the park, the ducks try to bite him. That’s what I get for buying a pure bread dog.",
        "6:30 is my favorite time of day, hands down.",
        "Mom is mad at me because she asked me to sync her phone, so I threw it in the ocean.",
        "I wanted to eat a watch for lunch, but it was too time-consuming.",
        "I’m friends with almost all the letters of the alphabet. I just don’t know Y.",
        "Justice is a dish best served cold. If it were served warm, it would be justwater.",
        "I used to hate facial hair, but then it grew on me.",
        "We’re renovating the house, and the first floor is going great, but the second floor is another story.",
        "It’s raining cats and dogs, so be careful not to step in a poodle.",
        "At first, I thought my chiropractor wasn’t any good, but now I stand corrected.",
        "My toddler is refusing to nap. He’s guilty of resisting a rest.",
        "I used to be able to play piano by ear, but now I have to use my hands.",
        "Every night, I have a hard time remembering something, but then it dawns on me.",
        "The wedding was so beautiful, even the cake was in tiers."]
        const joke = jokes[Math.floor(Math.random() * jokes.length)]
        const thb = Math.floor((Math.random() * 5) + 1)

        if (thb === 1) {
            const emb =  new MessageEmbed()
            .setTitle("Joke:")
            .setDescription(joke)
            .setThumbnail("https://cms.qz.com/wp-content/uploads/2016/07/rtx2c9ws.jpg?quality=75&strip=all&w=1600&h=900")

            await message.channel.send({embeds: [emb]})
        } if (thb === 2) {
            const emb =  new MessageEmbed()
            .setTitle("Joke:")
            .setDescription(joke)
            .setThumbnail("https://www.thelist.com/img/gallery/the-weird-reason-you-laugh-after-getting-tickled/why-we-laugh-when-someone-tickles-us-1617641616.jpg")

            await message.channel.send({embeds: [emb]})
        } if (thb === 3) {
            const emb =  new MessageEmbed()
            .setTitle("Joke:")
            .setDescription(joke)
            .setThumbnail("https://thumbs.dreamstime.com/z/laughing-tears-pointing-emoticon-wiping-away-something-someone-his-other-hand-85083127.jpg")

            await message.channel.send({embeds: [emb]})
        } if (thb === 4) {
            const emb =  new MessageEmbed()
            .setTitle("Joke:")
            .setDescription(joke)
            .setThumbnail("https://hbr.org/resources/images/article_assets/2018/11/nov18_16_882299664.jpg")

            await message.channel.send({embeds: [emb]})
        } if (thb === 5) {
            const emb =  new MessageEmbed()
            .setTitle("Joke:")
            .setDescription(joke)
            .setThumbnail("https://www.nydailynews.com/resizer/b4-X-EjxRHa0N4VMvLYKhNER8wo=/800x530/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/HKNQL2Q4A7KR6EUUFUSPKKVUH4.jpg")

            await message.channel.send({embeds: [emb]})
        }
    },
}