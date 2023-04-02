const tictactoeSchema = require('C:/Users/Linna/Documents/Executive/Executive/models/tictactoe-schema')
const sqlite3 = require('sqlite3').verbose()

function win(board, mark) {
    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for (const condtition of winningConditions) {
        if (board[condtition[0]] === mark && board[condtition[1]] === mark && board[condtition[2]] === mark) {
            return true
        }
    }
}

async function gen(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, placement, mark, res) {
    if (placement === 0) {
        if (pos1 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos1 = mark
        res.pos1 = mark
    } if (placement === 1) {
        if (pos2 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos2 = mark
        res.pos2 = mark
    } if (placement === 2) {
        if (pos3 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos3 = mark
        res.pos3 = mark
    } if (placement === 3) {
        if (pos4 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos4 = mark
        res.pos4 = mark
    } if (placement === 4) {
        if (pos5 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos5 = mark
        res.pos5 = mark
    } if (placement === 5) {
        if (pos6 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos6 = mark
        res.pos6 = mark
    } if (placement === 6) {
        if (pos7 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos7 = mark
        res.pos7 = mark
    } if (placement === 7) {
        if (pos8 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos8 = mark
        res.pos8 = mark
    } if (placement === 8) {
        if (pos9 !== ':white_large_square:') {return true}
        else {await res.save()}
        pos9 = mark
        res.pos9 = mark
    }
    return [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9]
}

module.exports = {
    name:"place",
    description:"Places an X or O on a tic-tac-toe board",
    minArgs: 1,
    expectedArgs: '<number from 1-9>',
    category:"Game/Score/Rank",

    callback: async ({ client, message, args }) => {
        const db = new sqlite3.Database('main.db',sqlite3.OPEN_READWRITE, (err) => {if (err) return console.error(err.message)})
        let content = parseInt(args[0])
        if (isNaN(content) || content <= 0 || content > 9) {
            return 'Invalid reponse please choose a number from 1-9'
        }
        const result = await tictactoeSchema.find({player1: message.author.id})
        let res
        if (result.length === 0) {
            res = await tictactoeSchema.findOne({player2: message.author.id})
            query = {player2: message.author.id}
        } else if (result.length === 1) {
            res = await tictactoeSchema.findOne({player1: message.author.id})
            query = {player1: message.author.id}
        }
        if (res === null) {return 'You are not in a game'}
        const { channelId, player1, player2, turn, turnId, messageId, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 } = res
        const channel = await client.channels.fetch(channelId)
        const msg = await channel.messages.fetch(messageId)
        const turnmsg = await channel.messages.fetch(turnId)
        content -= 1
        let mark
        let playerturn
        if (turn === 1) {
            mark = ':o2:'
            res.turn = 0
            playerturn = player2
            if (message.author.id !== player1) {
                return 'It is not your turn'
            }
        } if (turn === 0) {
            mark = ':regional_indicator_x:'
            res.turn = 1
            playerturn = player1
            if (message.author.id !== player2) {
                return 'It is not your turn' 
            } 
        }
        let board = await gen(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, content, mark, res)
        if (board === true) {return `Please choose an unmarked tile`}
        const won = win(board, mark)
        if (won === true) {
            if (playerturn === player1) {
                msg.edit(`${board[0]}${board[1]}${board[2]}\n${board[3]}${board[4]}${board[5]}\n${board[6]}${board[7]}${board[8]}`)
                turnmsg.edit(`<@${player2}> has won the game!`)
                db.all(`SELECT wins FROM wins WHERE id = '${player2}'`, [], (err, rows) => {
                    if (err) return console.error(err)
                    rows.forEach(row => {
                        let wins = Object.values(row)[0]
                        wins += 1
                        db.run(`UPDATE wins SET wins = '${wins}' WHERE id = '${player2}'`)
                    })
                })
                db.all(`SELECT loses FROM wins WHERE id = '${player1}'`, [], (err, rows) => {
                    if (err) return console.error(err)
                    rows.forEach(row => {
                        let loses = Object.values(row)[0]
                        loses += 1
                        db.run(`UPDATE wins SET loses = '${loses}' WHERE id = '${player1}'`)
                    })
                })
                await tictactoeSchema.deleteOne(query)
                message.delete()
                db.close()
                return
            }
            if (playerturn === player2) {
                msg.edit(`${board[0]}${board[1]}${board[2]}\n${board[3]}${board[4]}${board[5]}\n${board[6]}${board[7]}${board[8]}`)
                turnmsg.edit(`<@${player1}> has won the game!`)
                db.all(`SELECT wins FROM wins WHERE id = '${player1}'`, [], (err, rows) => {
                    if (err) return console.error(err)
                    rows.forEach(row => {
                        let wins = Object.values(row)[0]
                        wins += 1
                        db.run(`UPDATE wins SET wins = '${wins}' WHERE id = '${player1}'`)
                    })
                })
                db.all(`SELECT loses FROM wins WHERE id = '${player2}'`, [], (err, rows) => {
                    if (err) return console.error(err)
                    rows.forEach(row => {
                        let loses = Object.values(row)[0]
                        loses += 1
                        db.run(`UPDATE wins SET loses = '${loses}' WHERE id = '${player2}'`)
                    })
                })
                await tictactoeSchema.deleteOne(query)
                message.delete()
                db.close()
                return
            }
        }
        if (board[0] === true) {return 'Please choose an unmarked tile'}
        else {await res.save()}
        res.turns += 1
        await res.save()
        msg.edit(`${board[0]}${board[1]}${board[2]}\n${board[3]}${board[4]}${board[5]}\n${board[6]}${board[7]}${board[8]}`)
        turnmsg.edit(`<@${playerturn}>'s turn`)
        message.delete()
        if (res.turns === 9) {
            turnmsg.edit(`The game has resulted in a tie`)
            await tictactoeSchema.deleteOne(query)
            db.all(`SELECT ties FROM wins WHERE id = '${player1}'`, [], (err, rows) => {
                if (err) return console.error(err)
                rows.forEach(row => {
                    let ties = Object.values(row)[0]
                    ties += 1
                    db.run(`UPDATE wins SET ties = '${ties}' WHERE id = '${player1}'`)
                })
            })
            db.all(`SELECT ties FROM wins WHERE id = '${player2}'`, [], (err, rows) => {
                if (err) return console.error(err)
                rows.forEach(row => {
                    let ties = Object.values(row)[0]
                    ties += 1
                    db.run(`UPDATE wins SET ties = '${ties}' WHERE id = '${player2}'`)
                })
            })
            db.close()
            return
        }
    }
}