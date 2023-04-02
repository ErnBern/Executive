module.exports = {
    name: "randomnumber",
    description: "Generates a randomnumber",
    category: "Normal Commands",
    aliases: ["rn", "rannum"],
    maxArgs: 2,
 
    callback: async ({ message, args }) => {
        let arg = parseInt(args[0])
        let arg1 = parseInt(args[1])
        function nc(num) {
            if (num < args[0]) {return false}
            else {return true}
        }
        
        if (args.length === 0) {
            message.channel.send(`${Math.floor((Math.random() * 10000000) + 1)}`)
        } else if (args.length === 1) {message.channel.send(`${Math.floor((Math.random() * args[0]) + 1)}`)}
        else if (arg > arg1) {message.channel.send("Invalid argument!")}
        else {
            if (args[0] > 0 && args[1] > 0) {
                generator()
                function generator() {
                    let num = Math.floor((Math.random() * args[1]) + 1)
                    let verify = nc(num)
                    if (verify === true) {message.channel.send(`${num}`)}
                    else {generator()}
                }
                } else if (args[0] < 0 && args[1] < 0) {
                    let a = args.shift()
                    let a1 = args.shift()
                    let arg = a.split('-')[1]
                    let arg1 = a1.split('-')[1]
                    negativeGenerator(arg, arg1)
                        function negativeGenerator(arg, arg1) {
                            let num = Math.floor((Math.random() * arg) + 1)
                            let verify = ncg(num, arg1)
                            if (verify === true) {message.channel.send(`-${num}`)}
                            else {negativeGenerator(arg, arg1)}
                            function ncg(num, arg) {
                                if (num < arg) return false
                                else return true
                            }
                            }
                        } 
                else if (args[0] < 0) {
                    neg()
                    function neg() {
                        let num = Math.floor((Math.random() * args[1]) + 1) + Math.floor((Math.random() * args[0]) + 1)
                        let verify = nc(num)
                        if (verify === true) {message.channel.send(`${num}`)}
                        else {neg()}
                } 
                } 
            
        } 
    },
}