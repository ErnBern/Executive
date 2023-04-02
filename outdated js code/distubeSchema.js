const mongoose = require('mongoose')
const { Schema } = mongoose

const reqString = {
    type: String,
    required: true,
}

const schema = new Schema({
    guild: reqString,
    channel: reqString,
    skip: {
        type: Boolean,
        required: true
    }
})
const name = 'distubes'

module.exports = mongoose.models[name] || mongoose.model(name, schema)