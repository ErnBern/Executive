const mongoose = require('mongoose')
const { Schema } = mongoose

const reqString = {
    type: String,
    required: true,
}

const schema = new Schema ({
    guildId: reqString,
    staff: reqString,
    msgId: reqString,
    chId: reqString,
    AcId: reqString,
})

const name = 'channel-deletes'

module.exports = mongoose.models[name] || mongoose.model(name, schema)