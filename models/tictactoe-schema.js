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

const schema = new Schema(
    {
        channelId: reqString,
        player1: reqString,
        player2: reqString,
        turn: reqNum,
        turnId: reqString,
        messageId: reqString,
        pos1: reqString,
        pos2: reqString,
        pos3: reqString,
        pos4: reqString,
        pos5: reqString,
        pos6: reqString,
        pos7: reqString,
        pos8: reqString,
        pos9: reqString,
        turns: reqNum,
    }
)

const name = 'tictactoes'

module.exports = mongoose.models[name] || mongoose.model(name, schema)