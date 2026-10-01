# 🏆 Quiz Quest

A colorful, terminal-based quiz game. Answer 16 questions across three rounds to win up to **Rs. 150,000**, using lifelines and secured prize tiers along the way.

## Overview

QuizQuest is a command-line general-knowledge quiz inspired by classic TV quiz shows. Players work through 16 multiple-choice questions in three rounds of increasing difficulty and prize value. Clearing a round **secures** your winnings, so a later wrong answer never drops you below your last safe amount.

It is written in pure Python using only the standard library, so there is nothing to install.

## Features

- 16 multiple-choice questions on science, history, geography, Islamic history, art, and pop culture
- Three rounds with escalating difficulty and prize money
- Secured prize system: winnings are locked in at the end of each round
- Three lifelines (50/50, Audience Poll, Skip), one use each per game
- Quit at any time and keep your secured amount
- Colorful terminal interface using ANSI escape codes
- End-of-game report with questions played, correct answers, accuracy, and prize
- Replay without restarting the program
- Input validation for answers and lifeline choices

## Game Structure

| Round | Difficulty | Questions | Prize per Question | Round Total | Secured After Round |
|:-----:|:----------:|:---------:|:------------------:|:-----------:|:-------------------:|
| 1 | Easy | 8 | Rs. 5,000 | Rs. 40,000 | Rs. 40,000 |
| 2 | Medium | 5 | Rs. 10,000 | Rs. 50,000 | Rs. 90,000 |
| 3 | Final (Hard) | 3 | Rs. 20,000 | Rs. 60,000 | **Rs. 150,000** |

**Rules**

- A correct answer adds that question's prize to your total.
- Completing a round locks in your current total as your **secured amount**.
- A wrong answer ends the game, and you take home your last secured amount.
- Quitting also lets you take home your last secured amount.

## Lifelines

Each lifeline can be used once per game. 50/50 and Audience Poll can be used on the same question.

| Key | Lifeline | Description |
|:---:|----------|-------------|
| `1` | **50/50** | Removes two incorrect options |
| `2` | **Audience Poll** | Shows a simulated audience vote as percentages per option |
| `3` | **Skip Question** | Skips the current question without winning or losing money |
| `Q` | **Quit** | Ends the game and keeps your secured amount |

## Getting Started

### Prerequisites

- [Python 3.6 or higher](https://www.python.org/downloads/)
- A terminal that supports ANSI colors and emoji (Windows Terminal, macOS Terminal, iTerm2, most Linux terminals)

### Installation and Run

```bash
git clone https://github.com/malikaliiraza/quizquest.git
cd quizquest
python main.py
```

On some systems you may need to use `python3 main.py`.

## How to Play

1. Press **Enter** on the welcome screen and enter your name.
2. Type **A**, **B**, **C**, or **D** to answer each question.
3. Type **1**, **2**, or **3** to use a lifeline, or **Q** to quit.
4. Clear each round to secure your winnings.
5. Review your results and choose whether to play again.

### Sample Screen

```text
=================================================================
                 QUESTION 2 / 16
                 Prize: Rs. 5,000
=================================================================

02- Which planet is known as the Red Planet?
-----------------------------------------------------------------
A) Earth
B) Venus
C) Mars
D) Jupiter
-----------------------------------------------------------------

Available Lifelines:
  1. 50/50
  2. Audience Poll
  3. Skip Question
  Q. Quit Game

Enter A/B/C/D or Lifeline (1/2/3):
```

## Project Structure

```text
quizquest/
├── main.py      # Questions, lifelines, game loop, and UI
└── README.md
```

The game lives in a single file. Quiz data is held in four parallel lists (`questions`, `options`, `answers`, `amounts`), and `play_game()` runs the main loop.

## Customizing Questions

Keep the four lists aligned by index when adding or changing questions:

```python
questions.append("17- What is the largest ocean on Earth?")
options.append(["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"])
answers.append("C")
amounts.append(20000)
```

> **Note:** Round boundaries (after questions 8, 13, and 16) are hard-coded in `play_game()`. Adjust those indices if you change the number of questions per round.

## Known Issues

- The "Round Completed" screen appears twice at the end of Rounds 1 and 2.
- Skipping the last question of a round means the secured amount is not updated for that round.
- Question 16 is ambiguous, since Russia, Kazakhstan, and Turkey each lie in both Europe and Asia.

## Roadmap

- [ ] Fix the known issues above
- [ ] Move questions into an external JSON file
- [ ] Randomize question order within each difficulty tier
- [ ] Add a countdown timer per question
- [ ] Add a persistent high-score leaderboard
- [ ] Add unit tests for scoring and lifeline logic

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a branch : `git checkout -b feature/your-feature`
3. Commit your changes : `git commit -m "Add your feature"`
4. Push the branch : `git push origin feature/your-feature`
5. Open a Pull Request

## License

Released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Malik** — [@malikaliiraza](https://github.com/malikaliiraza)
