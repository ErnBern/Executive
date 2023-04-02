module.exports = {
    name:"unban",
    description:"Unbans a user!",
    category:"Admin Commands",
    permissions:['ADMINISTRATOR'],
    minArgs: 1,
    expectedArgs:"<user>",

    callback: async ({ message, args }) => {

        if (isNaN(args[0])) {
            message.reply("You need to give the id of someone to unban!")
            return
        }
        try {
            let user = await message.guild.members.unban(args[0])
            message.channel.send(`${user.tag} has been unbanned`)
            return
        } catch {
            return message.channel.send('Failed to unban the user')
        }
        
        
    }
}