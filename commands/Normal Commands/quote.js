const { MessageEmbed } = require('discord.js')

module.exports = {
    name:"quote",
    description:"Sends a random quote",
    category:"Normal Commands",

    callback: async ({ message }) => {
        const q = [
            "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion'.- Muhammad Ali",
            "I've been poor and I've been rich, and rich is better. - Bessie Smith",
            "What is love? ... It is the morning and the evening star. - Sinclair Lewis",
            "We want far better reasons for having children than ... knowing how to prevent them. - Dora Russell",
            "A good plan implemented today is better than a perfect plan implemented tomorrow. - General George Smith Patton",
            "You cannot help men permanently by doing for them what they could and should do for themselves. - Abraham Lincoln",
            "A politician is an animal which can sit on a fence and yet keep both ears to the ground. - H. L. Mencken",
            "Cruelty, like every other vice, requires no motive outside of itself; it only requires opportunity. - George Eliot",
            "Part of the inhumanity of the computer is that, once it is competently programmed and working smoothly, it is completely honest. - Isaac Asimov",
            "You will become as small as your controlling desire; as great as your dominant aspiration. - James Allen",
            "There are two ways of spreading light: to be the candle or the mirror that reflects it. - Edith Wharton",
            "Bore: n. a person who talks when you wish him to listen. -  Ambrose Gwinett Bierce",
            "All you have to do to be a millionaire, is earn a million dollars. - Noah Amy",
            "Who overrefines his argument brings himself to grief. -Francesco Petrarca Petrarch",
            "Theatre director: a person engaged by the management to conceal the fact that the players cannot act. -James Agate",
            "It always seems impossible until it's done. - Nelson Mandela"
            ]
        const pos = Math.floor(Math.random() * 10)
        const quote = q[pos]
        const emb = new MessageEmbed()

        if (pos === 0) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTQ3NjYxMzk4NjkwNzY4NDkz/muhammad_ali_photo_by_stanley_weston_archive_photos_getty_482857506.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 1 ) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRyZ4A3ZMGxmdJCTCQSi2FLDoI4zMNVqmUzTXg0FbunQ0EFkzB1")
            await message.channel.send({embeds: [emb]})
        } if (pos === 2) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://cdn.britannica.com/65/10265-004-33F7388B/Sinclair-Lewis.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 3) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://spartacus-educational.com/TUrussellD.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 4) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://upload.wikimedia.org/wikipedia/commons/2/2f/General_George_S_Patton.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 5) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://upload.wikimedia.org/wikipedia/commons/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 6) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://i.guim.co.uk/img/media/6883ccf966c87c85b5fd95ea3e0ac66f615ea3a3/0_356_2336_1401/master/2336.jpg?width=620&quality=85&auto=format&fit=max&s=b4c0ea6d3205b3a2650f1ccdb2744a77")
            await message.channel.send({embeds: [emb]})
        } if (pos === 7) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://upload.wikimedia.org/wikipedia/commons/4/48/George_Eliot%2C_por_Fran%C3%A7ois_D%27Albert_Durade.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 8) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTg1MjM2NDkyMzg0MjE2NzIz/gettyimages-3240525jpg--.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 9) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcRBcIg3IpARXzFal8tyIN5a9QvPXyI9nKayKm6zKSPCjiYpVtfJ_K-UFJFp02kc")
            await message.channel.send({embeds: [emb]})
        } if (pos === 10) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://upload.wikimedia.org/wikipedia/commons/5/52/Edith_Newbold_Jones_Wharton_%28cropped_02%29.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 11) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://upload.wikimedia.org/wikipedia/commons/d/da/Ambrose_Bierce_1892-10-07.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 12) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://cdn.discordapp.com/attachments/497937146188005377/950555695936315393/CA5327F0-EB69-45C5-8901-0046E22B840E.jpg")
            await message.channel.send({embed: [emb]})
        } if (pos === 13) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://www.theatermania.com/s/tm-photos-production/100196.jpg")
            await message.channel.send({embeds: [emb]})
        } if (pos === 14) {
            emb.setTitle("Quote:").setDescription(quote).setThumbnail("https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTY2MzU2NjgxMDUwMDM5OTk5/_photo-by-per-anders-petterssongetty-images.jpg")
            await message.channel.send({embeds: [emb]})
        } 
    },
}