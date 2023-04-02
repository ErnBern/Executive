module.exports = {
    name: 'loop',
    aliases: ['lp'],
    category: 'Music Commands',
    description: 'Lets you loop the queue or song',
    minArgs: 1,
    expectedArgs: '<song/queue/off>',
    callback: async ({ client, message, args }) => {
      const queue = client.distube.getQueue(message)
      if (!queue) return `There is nothing playing!`
      let mode
      switch (args[0]) {
        case 'off':
          mode = 0
          break
        case 'song':
          mode = 1
          break
        case 'queue':
          mode = 2
          break
      }
      mode = queue.setRepeatMode(mode)
      mode = mode ? (mode === 2 ? 'Repeat queue' : 'Repeat song') : 'Off'
      message.channel.send(`Set repeat mode to \`${mode}\``)
    }
}