const { MessageEmbed } = require("discord.js")

module.exports = {
    category: "Normal Commands",
    description: "Sends a random fact!",
    slash: false,

    callback: async (message, ...args) => {
        const facts = ["Cybercrime is up 600% due to the COVID-19 pandemic",
        "Remote work has increased the average cost of a data breach by $137,000",
        "More than half a million Zoom user accounts were compromised and sold on the dark web",
        "There are 11,762 recorded breaches between January 1, 2005 and May 31 2020",
        "In 2020, the average time to identify a breach was 207 days",
        "43% of cyberattacks target small businesses",
        "$3.86 million is the global average cost of a data breach",
        "95% of cybersecurity breaches are a result of human error",
        "On average only 5% of companies folders are properly protected",
        "94% of malware is delivered via email",
        "Only 16% of executives say their organizations are well prepared to deal with cyber risk",
        "Over 77% of organizations do not have a cyber security incident response plan",
        "89% of healthcare organizations experienced a data breach in the past two years",
        "Healthcare cybersecurity breaches cost the most of any other industry",
        "Over 6,000 new computer viruses are created and released every month",
        "90% of emails contain some form of malware!", "The Firefox logo isn’t a fox… it’s a red panda!",
        "Samsung is 38 years and 1 month older than Apple.",
        "One Petabyte (PB) = 1024 (TB). To put this in perspective, a 50PB hard drive could hold the entire written works of mankind from the beginning of recorded history in all languages.",
        "Alexa is always listening to your conversations. Alexa stores all of your dialogue history in the cloud to improve the Alexa experience.",
        "On average, people read 10% slower from a screen than from paper.",
        "The first computer mouse was made in 1964 by Doug Engelbart. It was rectangular and made from wood!",
        "On average, there is only one reply per 12 million spam emails sent.",
        "Surgeons that grew up playing video games more than three hours per week make 37% fewer errors and have a 42% faster completion rate when performing laparoscopic surgery and suturing.",
        "NASA’s internet speed is 91 GB per second",
        "Until 2010, carrier pigeons were faster than the internet",
        "In 1971, the first ever computer virus was developed named Creeper it was made as an experiment just to see how it spread between computers. The virus simply displayed the message: I’m the creeper, catch me if you can!",
        "Think Cyber Joined Youtube On January 14th, 2022",
        "The worldwide information security market is forecast to reach $170.4 billion in 2022",
        "88% of organizations worldwide experienced spear phishing attempts in 2019",
        "68% of business leaders feel their cybersecurity risks are increasing",
        "Data breaches exposed 36 billion records in the first half of 2020",
        "45% of breaches featured hacking, 17% involved malware and 22% involved phishing",
        "The top malicious email attachment types are .doc and .dot which make up 37%, the next highest is .exe at 19.5%",
        "An estimated 300 billion passwords are used by humans and machines worldwide",
        "The average time to identify a breach in 2020 was 207 day",
        "Personal data was involved in 58% of breaches in 2020",
        "Security breaches have increased by 11% since 2018 and 67% since 2014",
        "64% of Americans have never checked to see if they were affected by a data breach",
        "56% of Americans don’t know what steps to take in the event of a data breach",
        "In 2020, a Twitter breach targeted 130 accounts, including those of past presidents and Elon Musk, resulted in attackers swindling $121,000 in Bitcoin through nearly 300 transactions",
        "In 2020, Marriott disclosed a security breach impacted data of more than 5.2 million hotel guests",
        "The 2019 MGM data breach resulted in hackers leaking records of 142 million hotel guests",
        "In 2018, Under Armor reported that its “My Fitness Pal” was hacked, affecting 150 million users",
        "The Equifax breach cost the company over $4 billion in total",
        "100,000 groups in at least 150 countries and more than 400,000 machines were infected by the Wannacry virus in 2017, at a total cost of around $4 billion",
        "In 2016, Uber reported that hackers stole the information of over 57 million riders and drivers",
        "Uber tried to pay off hackers to delete the stolen data of 57 million users and keep the breach quiet",
        "In one of the biggest breaches of all time 3 billion Yahoo accounts were hacked in 2013",
        "The average ransomware payment rose 33% in 2020 over 2019, to $111,605",
        "In 2018, an average of 10,573 malicious mobile apps were blocked per day",
        "The average cost of a ransomware attack on businesses is $133,000",
        "48% of malicious email attachments are office files",
        "About 20% of malicious domains are very new and used around one week after they are registered",
        "After declining in 2019, phishing increased in 2020 to account for 1 in every 4,200 emails",
        "1 in 13 web requests lead to malware",
        "Phishing attacks account for more than 80% of reported security incidents",
        "$17,700 USD is lost every minute due to a phishing attack",
        "In 2023, the total number of DDoS attacks worldwide will be 15.4 million",
        "30% of data breaches involve internal actors",
        "1 in 36 mobile devices have high- risk apps installed"]
        const fact = facts[Math.floor(Math.random() * facts.length)]
        const th = Math.floor((Math.random() * 6) + 1)
        if (th === 1) {
            const emb = new MessageEmbed()
            .setTitle("Fact:")
            .setDescription(fact)
            .setThumbnail('https://yt3.ggpht.com/ytc/AKedOLRWMPjm1WyrBVD22h1g0kUXkfOsphMpa95av_NftQ=s900-c-k-c0x00ffffff-no-rj')

            await message.channel.send({
                embeds: [emb]
            })
        } if (th === 2) {
            const emb = new MessageEmbed() 
            .setTitle("Fact:")
            .setDescription(fact)
            .setThumbnail('https://thumbs.dreamstime.com/b/fact-square-grunge-stamp-fact-sign-fact-fact-stamp-125006414.jpg')
            
            await message.channel.send({
                embeds: [emb]
            })
        } if (th === 3) {
            const emb = new MessageEmbed()
            .setTitle("Fact:")
            .setDescription(fact)
            .setThumbnail("https://www.factdialogue.org/frontend_standard/img/logo.png?v3")
            
            await message.channel.send({
                embeds: [emb]
            })
        } if (th === 4) {
            const emb = new MessageEmbed()
            .setTitle("Fact:")
            .setDescription(fact)
            .setThumbnail("https://tomsbytwo.files.wordpress.com/2016/04/facts.jpg")
            
            await message.channel.send({
                embeds: [emb]
            })
        } if (th === 5) {
            const emb = new MessageEmbed()
            .setTitle("Fact:")
            .setDescription(fact)
            .setThumbnail("https://thumbs.dreamstime.com/b/fact-square-grunge-stamp-fact-sign-fact-fact-stamp-125006414.jpg")
            
            await message.channel.send({
                embeds: [emb]
            })
        } if (th === 6) {
            const emb = new MessageEmbed()
            .setTitle("Fact:")
            .setDescription(fact)
            .setThumbnail("https://jamesproclaimsdotcom1.files.wordpress.com/2021/01/55295-4-fact-image-free-transparent-image-hd.png")
            
            await message.channel.send({
                embeds: [emb]
            })
        }
    },
}