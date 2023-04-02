const { MessageEmbed } = require('discord.js')

module.exports = async (client) => {

    client.distube.on("playSong", async (queue, song) => {
        const emb = new MessageEmbed()
         .setTitle("Now Playing")
         .addFields({name:'Song:', value:`${song.name}`, inline:false}, {name:'Duration:', value:`${song.formattedDuration}`, inline:false},
         {name:'Requested By', value:`${song.user}`, inline:false})
         .setColor('DARK_BUT_NOT_BLACK')
         .setThumbnail(`${song.thumbnail}`)
        if (song.url === 'https://www.youtube.com/watch?v=tbnLqRW9Ef0') return
        await queue.textChannel.send({embeds: [emb]})
    })

    client.distube.on("addSong", async (queue, song) => {
        const emb = new MessageEmbed()
         .setTitle("Added to Queue")
         .addFields({name:'Song:', value:`${song.name}`, inline:false}, {name:'Duration:', value:`${song.formattedDuration}`, inline:false},
         {name:'Requested By', value:`${song.user}`, inline:false})
         .setColor('DARK_BUT_NOT_BLACK')
         .setThumbnail(`${song.thumbnail}`)
        if (song.url === 'https://www.youtube.com/watch?v=tbnLqRW9Ef0') return
        await queue.textChannel.send({embeds: [emb]})
    })

    client.distube.on('searchInvalidAnswer', async queue => {
        try {
            queue.textChannel.send('Invalid number of results.')
        } catch (e) {console.error(e)}
    })
    client.distube.on('searchNoResult', async queue => {
        try {
            queue.textChannel.send('No result found!')
        } catch (e) {console.error(e)}
    })
    client.distube.on("searchResult", () => {})
    client.distube.on("searchDone", () => {})
    client.distube.on("searchCancel", () => {})
}

module.exports.config = {
    dbName: 'DISTUBE',
    displayName: 'Distube'
}