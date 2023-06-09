const fs = ('fs')
const getFiles = require('./get-files')

module.exports = (client) => {
    const commands = {}
    const suffix = '.js'
    const commandFiles = getFiles('./commands', suffix)

    for (const command of commandFiles) {
        let commandFile = require(command)
        if (commandFile.default) commandFile = commandFile.default

        const split = command.replace(/\\/g, '/').split('/')
        const commandName = split[split.length - 1].replace(suffix, '')
        
        commands[commandName.toLowerCase()] = commandFile
    }

    console.log(commands)
    
    client.on('messageCreate', (message) => {
        if (message.author.bot || !message.content.startsWith('!')) {
            return
        }

        const args = message.content.slice(1).split(/ +/)
        const commandName = args.shift().toLowerCase()
        
        if (!commands[commandName]) {
            return
        }
        try {
            commands[commandName].callback(message, ...args)
        } catch (err) {
            console.error(err)
        }
    })
}