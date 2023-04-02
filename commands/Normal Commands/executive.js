module.exports = {
    name: "executive",
    category: "Normal Commands",
    description: "Tells you if Executive is online!",

    callback: ({ message }) => {
        message.channel.send("Here!")
    }
}