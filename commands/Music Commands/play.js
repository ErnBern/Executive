const { DisTube } = require('distube')

module.exports = {
    name: 'play',
    description:'Plays a song in the voice channel you are in!',
    category:'Music Commands',
    aliases: ['p'],
    minArgs: 1,
    expectedArgs: '<url/query>',

    callback: async ({ client, message, args }) => {
        if (!message.member.voice.channel) return 'You need to join a voice channel'
        const music = args.join(" ")
        if (music.includes('https://open.spotify.com/')) {
            try {
                client.distube.play(message.member.voice?.channel, music, {
                    message,
                    textChannel: message.channel,
                    member: message.member, 
                })
            } catch {
                message.channel.send('There was an error when trying to play the song')
            }
            return
        } if (music.includes('https://soundcloud.com/')) {
            try {
                client.distube.play(message.member.voice?.channel, music, {
                    message,
                    textChannel: message.channel,
                    member: message.member, 
                })
            } catch {
                message.channel.send('There was an error when trying to play the song')
            }
            return
        } if  (music.includes('https://youtube.com/')) {
            try {
                client.distube.play(message.member.voice?.channel, music, {
                    message,
                    textChannel: message.channel,
                    member: message.member, 
                })
            } catch {
                message.channel.send('There was an error when trying to play the song')
            }
            return
        }
        const results = await client.distube.search(music, {
            type: 'video',
            safeSearch: false,
            limit: 5,
        })
        if (!message.member.voice.channel) {return 'Please join a voice channel'}
        client.distube.play(message.member.voice?.channel, results[0].url, {
            message,
            textChannel: message.channel,
            member: message.member, 
        })
    }
    
}