"""Saara text yahin hai. Yahan edit karo; app.py bas dikhata hai.
[square brackets] mein jo hai wo placeholder hai, apna likh dena."""

NAME = "Chhaya"
MOM_PHONE = "1234567890"  # <- Maa ka number, sirf digits (e.g. +919876543210)

SPLASH_TITLE = "Happy Birthday, Chhaya 🎂"
SPLASH_LINE = ["Ek chhota sa gift tumhare liye. Just for you."]

ENVELOPES = [
    {
        "title": "💌 Open when you feel low",
        "lines": [
            "Aaj ka din thoda bhari lag raha hoga. Jo kuch tum chupchap utha rahi ho, I know wo aasan nahi hai.",
            "Par suno, tum akele nahi ho. Aaj sab kuch akele uthana zaroori nahi hai.",
            "Main yahan hoon, tumhare saath.",
        ],
    },
    {
        "title": "💌 Open when you miss me",
        "lines": [
            "Main yahin hoon, tumhare saath. Bas ek call door.",
            "Our focus is 'us'. Bas hum dono.",
            "I'm so glad it's you. I'm choosing this, one day at a time.",
        ],
    },
    {
        "title": "💌 Open when you can't sleep",
        "lines": [
            "Dimaag zyada chal raha hai? Phone side rakh do.",
            "Abhi sirf saans lo. Jo bhi hai, kal dekh lenge, saath mein.",
            "Tum safe ho yahan. Goodnight.",
        ],
    },
    {
        "title": "💌 Open when you doubt yourself",
        "lines": [
            "Tum IIT Bombay me MSc kar rahi ho! Ye choti baat nahi hai.",
            "Tum bahot capable ho aur tumne har mushkil din ko cross kiya hai. Apne aap par thoda bharosa rakho. Mujhe tumpe yakeen hai.",
        ],
    },
    {
        "title": "💌 Open when something funny is needed",
        "lines": [
            "Sameer Hills wala U-turn yaad hai? 'Okay!' bol kar turant mukar jana. 😂",
            "Ya phir Kanjurmarg me us dukandaar ke paas wapas ja kar ladai karna?",
            "Hum sach me ek ajeeb par best team hain.",
        ],
    },
    {
        "title": "💌 Open when you want to talk to Mom",
        "lines": [
            "Mummy se baat karne ke liye sab kuch perfect hona zaroori nahi hai.",
            "Bas itna kehna kaafi hai: *'Maa, aaj thoda low lag raha hai'*. Ya phir bas unki aawaz sun lena.",
        ],
        "show_call": True,
    },
]

VOICE_NOTES = [
    {
        "title": "🎧 Happy Birthday",
        "file": "audio/voice1.mp3",
        "script": "Happy Birthday Chhaya. Tumhara aana meri life me bohot special raha hai. Main chahta hoon ki aaj tum sach me thoda relax karo aur smile karo. I'm here.",
    },
    {
        "title": "🎧 A funny memory",
        "file": "audio/voice2.mp3",
        "script": "Kanjurmarg wala scene socho... tumne aur maine milkar us dukandaar ko wapas aakar kitna sunaya tha paise kam karwane ke liye! Kitni mehnat ki thi online price check karke.",
    },
    {
        "title": "🎧 You're not alone",
        "file": "audio/voice3.mp3",
        "script": "Ek baat hamesha yaad rakhna. Mera present aur mera focus sirf aur sirf tum par hai. Let's just focus on us. Tum akeli nahi ho.",
    },
]

MEMORIES = [
    ("🕶️ Kanjurmarg", "Chashma theek karwane gaye, ek book stall mila, bargaining ki, phir online sasta dekh kar wapas jaakar ladai ki aur price kam karwaya! Epic team effort."),
    ("⛰️ Sameer Hills", "Library ke baad maine pucha Sameer Hills chalein? Tum boli 'okay!' aur phir turant mana kar diya! Haha."),
    ("🎬 The Movies", "Spider-Man, Avengers... andhere me bas tumhare paas baithkar screen dekhna bhi mujhe bahut acha lagta hai."),
    ("🌙 Unplanned Night", "Ek simple dinner jo late-night adventure ban gaya. Cab nahi mili toh last minute hotel! Par tumhare saath aise fasne me bhi mazaa hai."),
    ("🐚 Oceanos", "Ye oceanos collect karna. Chhoti chhoti cheezein jo humari special memories ban gayi."),
    ("🍿 Next", "Tumhari choice ki ek aaram wali movie. Popcorn meri taraf se."),
    ("🌅 Soon", "Humara next unplanned trip ya date. Dekhte hain aage kya hota hai."),
]

GRATEFUL_INTRO = ""
GRATEFUL = [
    "Tum sabki itni care karti ho, even jab tum khud theek nahi hoti.",
    "Tumne mere liye Flipkart se order kiya, bina kuch sochey.",
    "Tumne mere liye paneer aur paratha banaya, ek baar nahi, kai baar.",
    "Jab mujhe paise ki zaroorat thi, tumne bina jhijhak madad ki.",
    "Tum bohot resilient ho. Tumne hamesha khud ko sambhala hai.",
    "IIT me tumhara hard work aur padhai ko lekar focus.",
    "Humara comfort zone, jahan silence bhi acha lagta hai.",
]
LOVE_LIST_TITLE = "Teen cheezein jo mujhe tumhare baare mein pasand hain"
LOVE_LIST = [
    "Tumhari smile, jab main kuch bewaqoofon wali harkate karta hu ya tum karti ho",
    "jab ham bahar ghumne jate h to chill sb , happy happy wo sb",
    "Tum",
]

NEXT_UP = [
    "Ek quiet movie night hum dono ke liye",
    "Bina kisi fix plan ke sham ko walk pe chalna",
    "Saath baithkar tumhara padhna aur mera kuch aur kaam karna",
    "Ek dinner jisme hum definitely pehle se cab book karenge, haha",
    "Kuch aasan sa khana mil kar banana (main paneer paratha try karunga, hopefully jalega nahi 😅)",
]
NEXT_UP_DONE = "Bas yahi list hai. Chalo ek-ek karke karte hain. 💗"

SMILE_MEMORIES = [
    "Kanjurmarg ka wo dukandaar bechara. 😂",
    "Tumhara famous Sameer Hills U-Turn.",
    "Dinner ke baad cabs ka na milna aur humara pareshan hona.",
    "Hum sach me ek ajeeb par best team hain. 😄",
]

WISHES = [
    ("🌿 Rest", "Tumhe sach me thoda sukoon aur aaram mile is saal."),
    ("🤍 Feeling heard", "Tumhe lagay ki log tumhe sach me samajhte hain."),
    ("🌸 Good people", "Ache aur calm log tumhare aas paas rahein."),
    ("✨ Small joys", "Chhoti chhoti khushiyan jo tumhara din acha banayein."),
]

# (file, caption)
PHOTOS = [
    ("assets/us1.jpg", "movie wala theatrew"),
    ("assets/us2.jpg", "love"),
    ("assets/us3.jpg", "garmi ki aag"),
    ("assets/us4.jpg", "beack ke kinare, tumhare sahare"),
    ("assets/us5.jpg", "1st meet"),
    ("assets/us6.jpg", "ramen"),
    ("assets/us7.jpg", "1st Movie night (beach night bhi)"),
    ("assets/us8.jpg", "me you and naruto"),
    ("assets/us9.jpg", "kissy"),
    ("assets/us10.jpg", "Good times"),
    ("assets/us11.jpg", "Another good day"),
    ("assets/us12.jpg", "Maa beti 💗"),
]

CLOSING = ["I hope tumhe ye chhota sa gift acha laga ho."]
CLOSING_LINE = "I'm always just a call away. 💗"
SIGNATURE = "- Shivam"

# ---------- Password screen ----------
PASSWORD = "15/06/2026"  # day/month/year; "15-6-2026" bhi chalega
LOCK_HINT = "Hint: jab maine tumhe pehli baar text kiya tha (dd/mm/yyyy)"
HEART_CAPTION = "Dil ko chhuo 💗"
