module.exports = {
    name:'disconnect',
    aliases:['dc'],
    description:' Makes the bot disconnect from the VC',
    category: 'Music Commands',

    callback: async ({ client, message }) => {
        client.distube.voices.leave(message)
        message.channel.send("Disconnected from VC")
    }

    
}