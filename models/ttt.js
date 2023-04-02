const mongoose = require('mongoose')
const { Schema } = mongoose

const reqString = {
    type: String,
    required: true,
}

const schema = new Schema({
    author: reqString,
    messageId: reqString,
    accepter: reqString,
    channelId: reqString,
    expires: Date,
},
{timestamps:true})

const name = 'tictactoe-listens'

module.exports = mongoose.models[name] || mongoose.model(name, schema)