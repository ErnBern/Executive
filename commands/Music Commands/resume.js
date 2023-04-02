module.exports = {
    name: 'resume',
    category:'Music Commands',
    description: 'Unpauses the music if paused!',
   
    callback: async ({ client, message }) => {
      if (!message.member.voice.channel) return 'You need to join a voice channel'
      const queue = client.distube.getQueue(message)
      if (!queue) return message.channel.send(`There is nothing in the queue right now!`)
      queue.resume()
    }
  }