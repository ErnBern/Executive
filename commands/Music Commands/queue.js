const { MessageEmbed } = require('discord.js')

module.exports = {
    testOnly: true,
    name: 'queue',
    aliases: ['q'],
    description: "Displays the current songs in queue",
    category: 'Music Commands',
    callback: async ({ client, message }) => {
      const queue = client.distube.getQueue(message)
      if (!queue) return `There is nothing in the queue`
      let ntbq = []
      let realqueue
      const q = queue.songs
        .map(
          (song, i) => `${i === 0 ? 'Playing:' : `${i}.`} ${song.name} - ***${song.formattedDuration}*** `)
        .join('\n')
      const que = q.split(`\n`)
      let i = 0
      for (const song of que) {
        ntbq.push(song)
        i += 1
        if (i === 51) {
          realqueue = ntbq.join('\n')
          break
          }
      }
      try {
        const emb = new MessageEmbed()
        .setTitle("Server Queue")
        .setDescription(q)
        .setColor('DARK_BUT_NOT_BLACK')
        await message.channel.send({embeds: [emb]})
      } catch {
        const emb = new MessageEmbed()
        .setTitle("Server Queue")
        .setDescription(realqueue)
        .setColor('DARK_BUT_NOT_BLACK')
        await message.channel.send({embeds: [emb]})
      }
    }
}