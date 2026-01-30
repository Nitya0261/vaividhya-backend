// const events = [
//     {
//         event_id: "adarena",
//         event_name: "Ad Arena",
//         price: 50,
//         category: "Marketing",
//         description: "A creative advertising challenge where participants design innovative ad campaigns.",
//         max_participants: 100
//     },
//     {
//         event_id: "ai-hunting",
//         event_name: "AI Hunting",
//         price: 50,
//         category: "Artificial Intelligence",
//         description: "Solve AI-based challenges using logic and analytical thinking.",
//         max_participants: 100
//     },
//     {
//         event_id: "ai-prompt-battle",
//         event_name: "AI Prompt Battle",
//         price: 50,
//         category: "Artificial Intelligence",
//         description: "Compete to create the most effective AI prompts.",
//         max_participants: 100
//     },
//     {
//         event_id: "ai-quiz",
//         event_name: "AI Quiz",
//         price: 50,
//         category: "Quiz",
//         description: "Test your knowledge of AI concepts and technologies.",
//         max_participants: 100
//     },
//     {
//         event_id: "ai-shape-cipher",
//         event_name: "AI Shape Cipher",
//         price: 50,
//         category: "Puzzle",
//         description: "Decode hidden messages using AI-based shape patterns.",
//         max_participants: 100
//     },
//     {
//         event_id: "bgmi",
//         event_name: "BGMI Tournament",
//         price: 50,
//         category: "Gaming",
//         description: "A competitive Battlegrounds Mobile India tournament.",
//         max_participants: 100
//     },
//     {
//         event_id: "biz-brain-challenge",
//         event_name: "Biz Brain Challenge",
//         price: 50,
//         category: "Business",
//         description: "Solve real-world business problems strategically.",
//         max_participants: 100
//     },
//     {
//         event_id: "blind-code",
//         event_name: "Blind Code",
//         price: 50,
//         category: "Coding",
//         description: "Code solutions with limited or hidden information.",
//         max_participants: 100
//     },
//     {
//         event_id: "brain-booster-math",
//         event_name: "Brain Booster Math",
//         price: 50,
//         category: "Mathematics",
//         description: "Boost your logical and mathematical skills.",
//         max_participants: 100
//     },
//     {
//         event_id: "break-the-bot",
//         event_name: "Break The Bot",
//         price: 50,
//         category: "Cybersecurity",
//         description: "Find vulnerabilities and break automated systems.",
//         max_participants: 100
//     },
//     {
//         event_id: "bridge-battle",
//         event_name: "Bridge Battle",
//         price: 100,
//         category: "Engineering",
//         description: "Design and test bridges under given constraints.",
//         max_participants: 100
//     },
//     {
//         event_id: "bull-vs-bear",
//         event_name: "Bull vs Bear",
//         price: 50,
//         category: "Finance",
//         description: "Stock market simulation and trading strategies.",
//         max_participants: 100
//     },
//     {
//         event_id: "case-catalyst",
//         event_name: "Case Catalyst",
//         price: 50,
//         category: "Management",
//         description: "Analyze business cases and propose solutions.",
//         max_participants: 100
//     },
//     {
//         event_id: "cricket-carnival",
//         event_name: "Cricket Carnival",
//         price: 50,
//         category: "Sports",
//         description: "Cricket-based fun and competitive challenges.",
//         max_participants: 100
//     },
//     {
//         event_id: "dream-to-deal",
//         event_name: "Dream To Deal",
//         price: 50,
//         category: "Entrepreneurship",
//         description: "Turn innovative ideas into business deals.",
//         max_participants: 100
//     },
//     {
//         event_id: "drone-dash",
//         event_name: "Drone Dash",
//         price: 100,
//         category: "Robotics",
//         description: "Race drones through challenging obstacle courses.",
//         max_participants: 100
//     },
//     {
//         event_id: "escape-room",
//         event_name: "Escape Room",
//         price: 50,
//         category: "Puzzle",
//         description: "Solve clues and puzzles to escape within time.",
//         max_participants: 100
//     },
//     {
//         event_id: "fold-and-build",
//         event_name: "Fold and Build",
//         price: 50,
//         category: "Design",
//         description: "Create innovative structures using folding techniques.",
//         max_participants: 100
//     },
//     {
//         event_id: "free-fire-pro",
//         event_name: "Free Fire Pro",
//         price: 50,
//         category: "Gaming",
//         description: "Competitive Free Fire gaming event.",
//         max_participants: 100
//     },
//     {
//         event_id: "logo-hunt",
//         event_name: "Logo Hunt",
//         price: 50,
//         category: "Design",
//         description: "Identify brands and logos using creative clues.",
//         max_participants: 100
//     },
//     {
//         event_id: "ludo-king",
//         event_name: "Ludo King",
//         price: 50,
//         category: "Gaming",
//         description: "Classic Ludo competition with a fun twist.",
//         max_participants: 100
//     },
//     {
//         event_id: "mystic-mover",
//         event_name: "Mystic Mover",
//         price: 50,
//         category: "Fun",
//         description: "Mystery-based coordination and movement game.",
//         max_participants: 100
//     },
//     {
//         event_id: "puzzle-hunt",
//         event_name: "Puzzle Hunt",
//         price: 50,
//         category: "Puzzle",
//         description: "Solve multiple puzzles across different levels.",
//         max_participants: 100
//     },
//     {
//         event_id: "quantum-quest-physics",
//         event_name: "Quantum Quest Physics",
//         price: 50,
//         category: "Physics",
//         description: "Physics-based challenges and problem solving.",
//         max_participants: 100
//     },
//     {
//         event_id: "reverse-coding",
//         event_name: "Reverse Coding",
//         price: 50,
//         category: "Coding",
//         description: "Reverse engineer logic from given outputs.",
//         max_participants: 100
//     },
//     {
//         event_id: "robo-war",
//         event_name: "Robo War",
//         price: 100,
//         category: "Robotics",
//         description: "Battle robots in a combat-style arena.",
//         max_participants: 100
//     },
//     {
//         event_id: "robo-rush",
//         event_name: "Robo Rush",
//         price: 100,
//         category: "Robotics",
//         description: "Speed-based robot racing challenge.",
//         max_participants: 100
//     },
//     {
//         event_id: "robo-football",
//         event_name: "Robo Football",
//         price: 100,
//         category: "Robotics",
//         description: "Football matches played using robots.",
//         max_participants: 100
//     },
//     {
//         event_id: "spin-mania",
//         event_name: "Spin Mania",
//         price: 50,
//         category: "Fun",
//         description: "Luck-based spinning game with rewards.",
//         max_participants: 100
//     },
//     {
//         event_id: "treasure-hunt",
//         event_name: "Treasure Hunt",
//         price: 50,
//         category: "Adventure",
//         description: "Search, solve clues, and uncover hidden treasures.",
//         "max_participants": 100
//     }
// ];

const events = [
    {
        event_id: "the-bridge-battle",
        event_name: "THE BRIDGE BATTLE",
        price: 100,
        category: "NON TECHNICAL",
        description: "A thrilling team challenge where strategy, balance, and coordination decide who conquers the bridge.",
        max_participants: 100
    },
    {
        event_id: "among-us",
        event_name: "AMONG US IN REAL LIFE",
        price: 50,
        category: "NON TECHNICAL",
        description: "A real-life version of the popular game filled with deception, teamwork, and suspense.",
        max_participants: 100
    },
    {
        event_id: "survivour-drop",
        event_name: "SURVIVOUR DROP CHALLENGE",
        price: 50,
        category: "NON TECHNICAL",
        description: "Test your endurance and focus as you try to outlast others in this survival-based challenge.",
        max_participants: 100
    },
    {
        event_id: "chemical-detective",
        event_name: "THE CHEMICAL DETECTIVE",
        price: 50,
        category: "NON TECHNICAL",
        description: "Solve clues and uncover mysteries using logical thinking and basic chemistry concepts.",
        max_participants: 100
    },
    {
        event_id: "robo-mind-matrix",
        event_name: "ROBO MIND MATRIX",
        price: 50,
        category: "TECHNICAL",
        description: "A technical challenge that tests your problem-solving skills in robotics and logical reasoning.",
        max_participants: 100
    },
    {
        event_id: "mini-masti-for-1-min",
        event_name: "MINI MASTI FOR 1 MIN",
        price: 50,
        category: "NON TECHNICAL",
        description: "Quick, fun, and exciting one-minute games designed to entertain and energize participants.",
        max_participants: 100
    },
    {
        event_id: "treasure-hunt",
        event_name: "TREASURE HUNT",
        price: 50,
        category: "NON TECHNICAL",
        description: "Follow clues, solve puzzles, and race against time to find the hidden treasure.",
        max_participants: 100
    },
    {
        event_id: "word-wizard-english",
        event_name: "WORD WIZARD ENGLISH",
        price: 50,
        category: "NON TECHNICAL",
        description: "Showcase your vocabulary and language skills through fun and challenging word games.",
        max_participants: 100
    },
    {
        event_id: "reel-rush",
        event_name: "REEL RUSH",
        price: 50,
        category: "NON TECHNICAL",
        description: "Create engaging and creative reels within a limited time to impress the judges.",
        max_participants: 100
    },
];



events.forEach((ele) => {
    try {
        fetch("https://vaividhya-backend.onrender.com/api/events", {
            method: 'POST', // Specify the method
            headers: {
                'Content-Type': 'application/json; charset=UTF-8', // Inform the server about the data type
            },
            body: JSON.stringify(ele), // Convert the JavaScript object to a JSON string
        }).then(() =>
            console.log("✅ Events inserted successfully:"))
    } catch (err) {

        console.error("❌ Error inserting events:");
    }
})