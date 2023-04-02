const mongoose = require('mongoose')
const { Schema } = mongoose

const reqString = {
    type: String,
    required: true,
}
const reqNum = {
    type: Number,
    required: true
}

const schema = new Schema ({
    author: reqString,
    question: reqString,
    answer: reqNum, 
    channel: reqString
})

const name = 'math-games'

module.exports = mongoose.models[name] || mongoose.model(name, schema)