const { Constants } = require('discord.js')

module.exports = {
  name: 'join',
  aliases: ['j', 'connect', 'cn'],
  category:'Music Commands',
  description: 'Joins your voice channel or the voice channel ID',
  expectedArgs: '<channelId>',

  callback: async ({ client, message, args }) => {
    let voiceChannel = message.member.voice.channel
    if (args[0]) {
      try {voiceChannel = await client.channels.fetch(args[0])}
      catch {
          message.channel.send(`${args[0]} is not a voice channel ID`)
          return 
      }
      if (!Constants.VoiceBasedChannelTypes.includes(voiceChannel?.type)) {
        return `<#${args[0]}> is not a valid voice channel!`
      }
    }
    if (!voiceChannel) {
        return 'You must be in a voice channel or enter a voice channel ID!'
    }
    client.distube.voices.join(voiceChannel)
    message.channel.send("Connected to VC")
  }
}