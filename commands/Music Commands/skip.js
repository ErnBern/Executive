const { MessageEmbed } = require("discord.js")

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

module.exports = {
    name: 'skip',
    category: 'Music Commands',
    aliases: ['s', 'fs'],
    description: 'Skips a song!',

    callback: async ({ client, message }) => {
        if (!message.member.voice.channel) return 'You need to join a voice channel to use this command'
        const queue = await client.distube.getQueue(message)
        if (queue) {
            if (queue.songs.length === 1) {
                client.distube.play(message.member.voice.channel, "https://www.youtube.com/watch?v=tbnLqRW9Ef0", {
                    message,
                    textChannel: message.channel.id,
                    member: message.member, 
                }) 
            }
            let song
            try {
                await sleep(500)
                song = await queue.skip()
            }
            catch {return `An error has occured whilst trying to skip`} 
            const emb = new MessageEmbed()
             .setTitle('Skipped Song')
             .addFields(
                 {name:'Song', value:`${queue.songs[0].name}`, inline:false},
                 {name:'Duration', value:`${queue.songs[0].formattedDuration}`, inline:false},
                 {name:'Requested By', value:`${message.author}`, inline:false}
             )
             .setThumbnail(`${queue.songs[0].thumbnail}`)
             .setColor('DARK_BUT_NOT_BLACK')
            await message.channel.send({embeds: [emb]})
        } else if (!queue) {
            return 'There is nothing to skip!'
        }
    }
}