const mongoose = require('mongoose')
const { Schema } = mongoose

const reqString = {
    type: String,
    required: true,
}
const schema = new Schema(
    {
        channelId: reqString,
        guildId: reqString,
        staffId: reqString,
        reason: reqString,
        expires: Date,
        type: {
            type: String,
            required: true,
            enum: ['lock'],
        },
    },
    {
        timestamps: true,
    }
)

const name = 'locks'

module.exports = mongoose.models[name] || mongoose.model(name, schema)