module.exports = {
    name: 'pause',
    category: 'Music Commands',
    description: 'Pauses the music!',
    testOnly: true,

    callback: async ({ client, message }) => {
        if (!message.member.voice.channel) return 'You need to join a voice channel to use this command'
        const queue = await client.distube.getQueue(message)

        if (queue) {
            queue.pause()
        } else if (!queue) {
            return
        }

    }

}