function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

module.exports = {
    name: 'clearqueue',
    aliases: ['cq'],
    description: 'Clears the queue!',
    category: 'Music Commands',
    
    callback: async ({ client, message }) => {
        const queue = client.distube.getQueue(message)
        if (!queue) return 'There is nothing in the queue!'
        const songs = queue.songs
        if (songs.length < 2) {
            message.channel.send(`You can't clear a queue that has less than 2 songs`)
            return
        }

        let i = 0

        while (i < songs.length) {
            songs.pop()
        }
        if (songs.length === 0) {
            client.distube.play(message.member.voice.channel, "https://www.youtube.com/watch?v=tbnLqRW9Ef0", {
                message,
                textChannel: message.channel.id,
                member: message.member, 
            })
            client.distube.play(message.member.voice.channel, "https://www.youtube.com/watch?v=tbnLqRW9Ef0", {
                message,
                textChannel: message.channel.id,
                member: message.member, 
            }) 
        }
        await sleep(2000)
        queue.skip()
        
        message.channel.send("The queue has been cleared")
    }
}