# ⚽ Football Quiz Arena

**Test your football knowledge. Beat the clock of history. Climb the scoreboard.**

Football Quiz Arena is an interactive, terminal-based quiz game built with Python. It challenges players with questions about football history, FIFA World Cups, legendary players, famous clubs, football rules, tactics, and EA SPORTS FIFA/FC games.

Every round selects 10 random questions from a question bank, shuffles the answer options, and calculates your score as you play. No two rounds need to feel the same!

---

## 🎮 Features

- **100-question quiz bank:** Explore a broad collection of football trivia.
- **10 questions per round:** Each game randomly selects 10 distinct questions.
- **Multiple-choice gameplay:** Four answer options for every question.
- **Difficulty selection:** Choose Easy, Medium, Hard, or Mixed.
- **Randomized answers:** Options are shuffled to keep the game challenging.
- **Live scoring:** Earn points for every correct answer.
- **Streak bonuses:** Earn extra points for maintaining a streak of correct answers.
- **Instant feedback:** See whether your answer is correct, along with an explanation.
- **Performance summary:** Review your score, accuracy, correct answers, and best streak.
- **Answer review:** Revisit incorrect answers at the end of the game.
- **Replay option:** Start another round without restarting the program.

## 📚 Question Categories

Questions cover several areas of football:

| Category                  | Topics                                                    |
| ------------------------- | --------------------------------------------------------- |
| 🌍 World Cup              | Tournament winners, finals, records and memorable moments |
| ⭐ Players                 | Legendary footballers, awards and international stars     |
| 🏟️ Clubs                 | Famous clubs, stadiums and club history                   |
| 📏 Rules                  | Match regulations, cards, penalties and offside           |
| 🎮 FIFA / EA SPORTS FC    | Game modes, player attributes and gameplay                |
| 🧠 Tactics                | Formations, pressing, positions and football terminology  |
| 🏆 International Football | European Championship, Copa América and women's football  |
| ⚽ Trivia                  | Additional football facts and milestones                  |

## 🛠️ Built With

- **Language:** Python 3
- **Modules:** `random`, `time`
- **Interface:** Command-line / terminal
- **External dependencies:** None

The project uses Python's standard library, so there is no need to install third-party packages.

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check your installation with:

```bash
python --version
```

On some systems, you may need:

```bash
python3 --version
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Suyash282611/football-quiz-arena.git
```

**2. Navigate into the project folder**

```bash
cd football-quiz-arena
```

**3. Run the game**

```bash
python main.py
```

That's it! The game runs directly in your terminal.

> If you use a different repository name, replace `football-quiz-arena` in the commands above with your actual repository name.

## 🕹️ How to Play

**Step 1 — Enter your name**

Start the game by entering your name. Your results will be displayed at the end of the round.

**Step 2 — Select a difficulty**

Choose one of the available modes:

- `1` — Easy
- `2` — Medium
- `3` — Hard
- `4` — Mixed

**Step 3 — Answer the questions**

Each round contains 10 randomly selected questions. Enter `A`, `B`, `C`, or `D` to submit your answer.

**Step 4 — Build your streak**

Answer consecutive questions correctly to earn bonus points.

**Step 5 — Review your performance**

At the end of the round, view your final score, accuracy, best streak, and a review of the questions you answered incorrectly.

**Step 6 — Play again**

Start a fresh round or exit the game.

## 🧮 Scoring System

| Action           |                                          Points |
| ---------------- | ----------------------------------------------: |
| Correct answer   |                                             +10 |
| Incorrect answer |                                              +0 |
| Streak bonus     | +5 per correct answer once the streak reaches 3 |

The streak bonus applies to every correct answer from the third consecutive correct answer onward. Your final score therefore depends on both accuracy and consistency.

## 📂 Project Structure

```text
football-quiz-arena/
│
├── main.py       # Question bank and game logic
└── README.md     # Project documentation
```

The game currently keeps its question bank and game logic in a single Python file, making it easy to run and understand.

A future version could separate the question bank into its own module or JSON file.

## 🧠 What I Learned

Building this project helped me practise and apply several Python fundamentals:

- Lists and nested data structures
- Tuples and structured question data
- Functions and code organization
- Loops and conditional statements
- User input and input validation
- Random selection and shuffling
- Score tracking and state management
- String formatting and terminal output
- Basic exception prevention through validation
- Designing a program around reusable functions

More importantly, this project helped me understand how individual Python concepts can work together to create a complete interactive application.

## 🔮 Future Improvements

This project is a work in progress, and there are several features I would like to explore:

- [ ] Move questions into a separate JSON file.
- [ ] Add a persistent leaderboard and high scores.
- [ ] Introduce a timed challenge mode.
- [ ] Add more questions and expand the difficulty levels.
- [ ] Add category-specific quiz modes.
- [ ] Allow users to add their own questions.
- [ ] Improve the terminal interface with menus and progress indicators.
- [ ] Add unit tests for scoring, question selection and answer validation.
- [ ] Explore a graphical interface in a future version.

## ⚠️ Notes

This is an educational, fan-made football trivia project. Football facts and historical records should be checked against reliable sources, particularly when expanding the question bank.

The game runs locally and does not require an internet connection.

## 👨‍💻 Author

**Suyash**

Electronics and Communication Engineering Student

- GitHub: [@Suyash282611](https://github.com/Suyash282611)
- LinkedIn: (www.linkedin.com/in/suyash-negi-a26643363)

---

If you enjoy football trivia, challenge yourself to a round and see how much you really know!

**Made with Python and a love for football. ⚽**
