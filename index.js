const DiscordJS = require('discord.js')
const { Intents} = DiscordJS
const path = require('path')
const WOKCommands = require('wokcommands')
const { DisTube } = require('distube')
require('dotenv/config')

const client = new DiscordJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
        Intents.FLAGS.GUILD_MEMBERS,
        Intents.FLAGS.DIRECT_MESSAGES,
        Intents.FLAGS.GUILD_BANS,
        Intents.FLAGS.GUILD_VOICE_STATES
    ]
})

const { SpotifyPlugin } = require('@distube/spotify')
const { SoundCloudPlugin } = require('@distube/soundcloud')
const { YtDlpPlugin } = require('@distube/yt-dlp')
client.distube = new DisTube(client, {
  leaveOnStop: false,
  emitNewSongOnly: true,
  emitAddSongWhenCreatingQueue: false,
  emitAddListWhenCreatingQueue: false,
  plugins: [
    new SpotifyPlugin({
      emitEventsAfterFetching: true
    }),
    new SoundCloudPlugin(),
    new YtDlpPlugin()
  ],
  youtubeDL: false

})

/* client.distube.on("playSong", async (message, song) => {
    const emb = new MessageEmbed()
     .setTitle("Now Playing")
     .addFields({name:'Song:', value:`${song.name}`, inline:false}, {name:'Duration:', value:`${song.formattedDuration}`, inline:false},
     {name:'Requested By', value:`${song.user}`, inline:false})
     .setColor('DARK_BUT_NOT_BLACK')
    await message.channel.send({embeds: [emb]})
}) 
 */
client.on('ready', async () => {
    console.log(`We have logged in as ${client.user.tag}`)
    //let handler = require('./command-handler.js')  
    //if (handler.default) handler = handler.default
    //handler(client)
    new WOKCommands(client, {
        commandsDir: path.join(__dirname, 'commands'),
        testServers: ['944072240331374712'],
        featuresDir: path.join(__dirname, 'features'),
        mongoUri: process.env.MONGO_URI  
    })
    .setCategorySettings([
        {
            name: 'Normal Commands',
            emoji: "🙂"
        },
        {
            name:'Admin Commands',
            emoji:"🛡️"
        },
        {
            name:"Polls",
            emoji:"🗳️"
        },
        {
            name:"Game/Score/Rank",
            emoji:'🎮'
        },
        {
            name:"Documentation",
            emoji:"📚"
        },
        {
            name:"Music Commands",
            emoji: '🎶'
        }
    ])
})

client.on('messageCreate', (message) => {
    if (message.author.bot) {return}
    if ((message.content.startsWith('Hi')) || (message.content.startsWith('hi')) || (message.content.startsWith('Hello')) || (message.content.startsWith('hello'))) {
        const content = message.content.split(" ")
        if (content[0] === 'hi' || content[0] === 'hello' || content[0] === 'Hi' || content[0] === 'Hello') {message.reply({content: `Hello ${message.author.username}!`,})}
        }
    else if ((message.content.startsWith('bye')) || (message.content.startsWith('Bye')) || (message.content.startsWith('Goodbye')) || (message.content.startsWith('goodbye'))) {message.reply({content: `Goodbye ${message.author.username}!`,})}
    else if ((message.content.startsWith('Sup')) || (message.content.startsWith('sup'))) {
        const content = message.content.split(" ")
        if (content[0] === "Sup" || content[0] === "sup") {message.reply({content: `Sup ${message.author.username}`,})}
    } else if ((message.content.startsWith("yo") || message.content.startsWith("Yo"))) {
        const content = message.content.split(" ")
        if (content[0] === 'yo' || content[0] === 'Yo') {message.reply({content: `Yo ${message.author.username}!`,})}
    }
    else if ((message.content.startsWith('Peace')) || (message.content.startsWith('peace'))) {
        const content = message.content.split(" ")
        if (content === "peace" || content === "Peace") {message.reply({content: `Peace ${message.author.username}!`,})}
    }
})

client.login(process.env.TOKEN)