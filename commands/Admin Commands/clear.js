module.exports = {
    name:"clear",
    description:"Clears messages from the channel you're in!",
    permissions: ['ADMINISTRATOR'],
    maxArgs: 1,
    expectedArgs: '<amount>',
    category:"Admin Commands",
    
    callback: async ({ message, channel, args }) => {
        const amount = args.length + 2? parseInt(args.shift()) : 2
        try {
            const { size } = await channel.bulkDelete(amount, true).catch(err => {console.log(err);})
            s = size;
        } catch (err) {
            if (err.code != '10003') {return;}
            console.error(err);
        }
        const leftover = amount - s
        if (leftover > 0) {
            const messages = await channel.messages.fetch({ limit: leftover })
            try {
                messages.forEach((message) => {
                    if (!message) return;
                    message.delete()
                })
            } catch (e) {
                if (err.code != '10003') {return;}
                console.error(e);
            }
        }
    },
}