import random


# ============================================================
#                         QUESTIONS
# ============================================================

questions = [
    "01- Which food can remain edible for thousands of years if properly preserved?",
    "02- Which planet is known as the Red Planet?",
    "03- Which Pakistani city is famous for the shrine of Bahauddin Zakariya?",
    "04- Which animal has three hearts?",
    "05- Who painted the Mona Lisa?",
    "06- Who was the first muezzin of Islam?",
    "07- What was the name of the mosque built by Prophet Muhammad ﷺ after arriving in Madinah?",
    "08- Which animal has fingerprints similar to humans?",
    "09- Which country has more pyramids than Egypt?",
    "10- What is the name of the AI assistant in Iron Man?",
    "11- Which bird can fly backwards?",
    "12- Which ancient civilization developed the concept of zero as a number?",
    "13- Which planet rotates in the opposite direction to most planets in our Solar System?",
    "14- Which two countries share the world's longest international land border?",
    "15- Which country gifted the Statue of Liberty to the United States?",
    "16- Which country is located in both Europe and Asia?"
]


# ============================================================
#                          ANSWERS
# ============================================================

answers = [
    "B",
    "C",
    "A",
    "D",
    "B",
    "C",
    "A",
    "D",
    "B",
    "C",
    "A",
    "D",
    "B",
    "C",
    "A",
    "D"
]


# ============================================================
#                          OPTIONS
# ============================================================

options = [
    ["A) Bread", "B) Honey", "C) Rice", "D) Sugar"],

    ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],

    ["A) Multan", "B) Lahore", "C) Karachi", "D) Sahiwal"],

    ["A) Dolphin", "B) Shark", "C) Whale", "D) Octopus"],

    ["A) Pablo Picasso", "B) Leonardo da Vinci",
     "C) Vincent van Gogh", "D) Michelangelo"],

    ["A) Abu Bakr (RA)", "B) Umar ibn al-Khattab (RA)",
     "C) Bilal ibn Rabah (RA)", "D) Uthman ibn Affan (RA)"],

    ["A) Masjid Quba", "B) Masjid al-Haram",
     "C) Masjid an-Nabawi", "D) Masjid al-Aqsa"],

    ["A) Chimpanzee", "B) Monkey", "C) Orangutan", "D) Koala"],

    ["A) Egypt", "B) Sudan", "C) Mexico", "D) Iraq"],

    ["A) FRIDAY", "B) HAL 9000", "C) JARVIS", "D) Ultron"],

    ["A) Hummingbird", "B) Swift", "C) Kingfisher", "D) Woodpecker"],

    ["A) Roman Civilization", "B) Greek Civilization",
     "C) Egyptian Civilization", "D) Ancient Indian Civilization"],

    ["A) Mars", "B) Venus", "C) Uranus", "D) Neptune"],

    ["A) Russia and China", "B) Brazil and Argentina",
     "C) Canada and United States", "D) India and Pakistan"],

    ["A) France", "B) Spain", "C) Italy", "D) Germany"],

    ["A) Russia", "B) Kazakhstan", "C) Greece", "D) Turkey"]
]


# ============================================================
#                           AMOUNTS
# ============================================================

amounts = [
    5000, 5000, 5000, 5000,
    5000, 5000, 5000, 5000,
    10000, 10000, 10000, 10000, 10000,
    20000, 20000, 20000
]


# ============================================================
#                           COLORS
# ============================================================

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"


# ============================================================
#                       WELCOME SCREEN
# ============================================================

def welcome_screen():

    print("\n" + CYAN + "=" * 65 + RESET)
    print(CYAN + "                 🏆 QUIZQUEST 🏆" + RESET)
    print(CYAN + "=" * 65 + RESET)

    print("\n        Test Your Knowledge!")
    print("        Win Up To Rs. 150,000")

    print("\n" + "=" * 65)

    print("                 GAME STRUCTURE")
    print("                 ----------------")
    print("                 🟢 Round 1 - Easy")
    print("                 🟡 Round 2 - Medium")
    print("                 🔴 Final Round - Hard")

    print("\n" + "=" * 65)

    input("Press Enter to Start the Game...")


# ============================================================
#                         ROUND DISPLAY
# ============================================================

def show_round(round_number):

    if round_number == 1:

        print("\n" + GREEN + "=" * 65 + RESET)
        print(GREEN + "              🟢 ROUND 1 — EASY" + RESET)
        print(GREEN + "              8 Questions" + RESET)
        print(GREEN + "              Rs. 5,000 Each" + RESET)
        print(GREEN + "=" * 65 + RESET)

    elif round_number == 2:

        print("\n" + YELLOW + "=" * 65 + RESET)
        print(YELLOW + "             🟡 ROUND 2 — MEDIUM" + RESET)
        print(YELLOW + "             5 Questions" + RESET)
        print(YELLOW + "             Rs. 10,000 Each" + RESET)
        print(YELLOW + "=" * 65 + RESET)

    else:

        print("\n" + RED + "=" * 65 + RESET)
        print(RED + "              🔴 FINAL ROUND — HARD" + RESET)
        print(RED + "              3 Questions" + RESET)
        print(RED + "              Rs. 20,000 Each" + RESET)
        print(RED + "=" * 65 + RESET)


# ============================================================
#                         50/50
# ============================================================

def fifty_fifty(question_number):

    correct_answer = answers[question_number]

    wrong_options = ["A", "B", "C", "D"]

    wrong_options.remove(correct_answer)

    removed_options = random.sample(wrong_options, 2)

    print("\n" + MAGENTA + "🆘 50/50 LIFELINE ACTIVATED!" + RESET)
    print("Two incorrect options have been removed.\n")

    for option in options[question_number]:

        letter = option[0]

        if letter not in removed_options:
            print(option)


# ============================================================
#                       AUDIENCE POLL
# ============================================================

def audience_poll(question_number):

    correct_answer = answers[question_number]

    correct_percentage = random.randint(50, 75)

    remaining = 100 - correct_percentage

    first_wrong = random.randint(1, remaining - 2)
    second_wrong = random.randint(
        1,
        remaining - first_wrong - 1
    )

    third_wrong = (
        remaining -
        first_wrong -
        second_wrong
    )

    wrong_percentages = [
        first_wrong,
        second_wrong,
        third_wrong
    ]

    poll = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    poll[correct_answer] = correct_percentage

    wrong_answers = [
        letter
        for letter in ["A", "B", "C", "D"]
        if letter != correct_answer
    ]

    for i in range(3):
        poll[wrong_answers[i]] = wrong_percentages[i]

    print("\n" + MAGENTA + "📊 AUDIENCE POLL" + RESET)
    print("-" * 30)

    for letter in ["A", "B", "C", "D"]:
        print(f"Option {letter}: {poll[letter]}%")

    print("-" * 30)


# ============================================================
#                       ROUND COMPLETE
# ============================================================

def round_complete(round_number, secured_amount):

    print("\n" + GREEN + "=" * 65 + RESET)
    print(GREEN + "              🎉 CONGRATULATIONS! 🎉" + RESET)
    print(
        GREEN +
        f"              ROUND {round_number} COMPLETED!" +
        RESET
    )
    print(
        YELLOW +
        f"              🔒 AMOUNT SECURED: "
        f"Rs. {secured_amount:,}" +
        RESET
    )
    print(GREEN + "=" * 65 + RESET)

    print(
        "\nIf you get a wrong answer in the next round, "
        f"you will still take home Rs. {secured_amount:,}."
    )

    input("\nPress Enter to continue...")


# ============================================================
#                        MAIN GAME
# ============================================================

def play_game():

    total_amount = 0
    secured_amount = 0

    correct_count = 0
    attempted_questions = 0

    fifty_used = False
    audience_used = False
    skip_used = False

    player_name = input("\nEnter your name: ")

    print("\n" + CYAN + "=" * 65 + RESET)
    print(f"             Welcome, {player_name}!")
    print("             Your game is about to begin.")
    print(CYAN + "=" * 65 + RESET)

    input("\nPress Enter to continue...")

    for i in range(len(questions)):

        # ====================================================
        # ROUND 1
        # ====================================================

        if i == 0:

            show_round(1)

            input("\nPress Enter to start Round 1...")

        # ====================================================
        # ROUND 2
        # ====================================================

        elif i == 8:

            round_complete(
                1,
                secured_amount
            )

            show_round(2)

            input("\nPress Enter to start Round 2...")

        # ====================================================
        # FINAL ROUND
        # ====================================================

        elif i == 13:

            round_complete(
                2,
                secured_amount
            )

            show_round(3)

            input("\nPress Enter to start the FINAL ROUND...")

        # ====================================================
        # QUESTION DISPLAY
        # ====================================================

        print("\n" + BLUE + "=" * 65 + RESET)

        print(
            BLUE +
            f"                 QUESTION {i + 1} / 16" +
            RESET
        )

        print(
            YELLOW +
            f"                 Prize: Rs. {amounts[i]:,}" +
            RESET
        )

        print(BLUE + "=" * 65 + RESET)

        print("\n" + questions[i])

        print("-" * 65)

        for option in options[i]:
            print(option)

        print("-" * 65)

        # ====================================================
        # LIFELINES
        # ====================================================

        print("\n" + MAGENTA + "Available Lifelines:" + RESET)

        if not fifty_used:
            print("  1. 50/50")

        if not audience_used:
            print("  2. Audience Poll")

        if not skip_used:
            print("  3. Skip Question")

        print("  Q. Quit Game")

        # ====================================================
        # ANSWER INPUT
        # ====================================================

        while True:

            user_answer = input(
                "\nEnter A/B/C/D or Lifeline (1/2/3): "
            ).strip().upper()

            # ------------------------------------------------
            # QUIT GAME
            # ------------------------------------------------

            if user_answer == "Q":

                print("\n" + YELLOW + "=" * 65 + RESET)
                print(YELLOW + "             GAME QUIT BY PLAYER" + RESET)
                print(
                    YELLOW +
                    f"             Amount to take home: "
                    f"Rs. {secured_amount:,}" +
                    RESET
                )
                print(YELLOW + "=" * 65 + RESET)

                return (
                    player_name,
                    secured_amount,
                    correct_count,
                    attempted_questions
                )

            # ------------------------------------------------
            # 50/50
            # ------------------------------------------------

            elif user_answer == "1" and not fifty_used:

                fifty_fifty(i)

                fifty_used = True

                print("\n50/50 lifeline has been used.")

                continue

            # ------------------------------------------------
            # AUDIENCE POLL
            # ------------------------------------------------

            elif user_answer == "2" and not audience_used:

                audience_poll(i)

                audience_used = True

                print("\nAudience Poll lifeline has been used.")

                continue

            # ------------------------------------------------
            # SKIP
            # ------------------------------------------------

            elif user_answer == "3" and not skip_used:

                print(
                    "\n" +
                    MAGENTA +
                    "⏭️ QUESTION SKIPPED!" +
                    RESET
                )

                skip_used = True

                attempted_questions += 1

                if i < len(questions) - 1:

                    print(
                        "\n" +
                        CYAN +
                        "=" * 65 +
                        RESET
                    )

                    print(
                        CYAN +
                        f"              ➡️ NEXT QUESTION: "
                        f"{i + 2} / 16" +
                        RESET
                    )

                    print(
                        CYAN +
                        "=" * 65 +
                        RESET
                    )

                    input("Press Enter to continue...")

                break

            # ------------------------------------------------
            # VALID ANSWER
            # ------------------------------------------------

            elif user_answer in ["A", "B", "C", "D"]:

                attempted_questions += 1

                # ============================================
                # CORRECT ANSWER
                # ============================================

                if user_answer == answers[i]:

                    total_amount += amounts[i]

                    correct_count += 1

                    print(
                        "\n" +
                        GREEN +
                        "=" * 65 +
                        RESET
                    )

                    print(
                        GREEN +
                        "              ✅ CORRECT ANSWER!" +
                        RESET
                    )

                    print(
                        GREEN +
                        f"              You won: "
                        f"Rs. {amounts[i]:,}" +
                        RESET
                    )

                    print(
                        GREEN +
                        f"              Current Amount: "
                        f"Rs. {total_amount:,}" +
                        RESET
                    )

                    print(
                        GREEN +
                        "=" * 65 +
                        RESET
                    )

                    # ========================================
                    # ROUND 1 COMPLETED
                    # ========================================

                    if i == 7:

                        secured_amount = total_amount

                        round_complete(
                            1,
                            secured_amount
                        )

                    # ========================================
                    # ROUND 2 COMPLETED
                    # ========================================

                    elif i == 12:

                        secured_amount = total_amount

                        round_complete(
                            2,
                            secured_amount
                        )

                    # ========================================
                    # GAME COMPLETED
                    # ========================================

                    elif i == 15:

                        print(
                            "\n" +
                            GREEN +
                            "=" * 65 +
                            RESET
                        )

                        print(
                            GREEN +
                            "          🏆 CONGRATULATIONS! 🏆" +
                            RESET
                        )

                        print(
                            GREEN +
                            "          YOU WON THE FINAL ROUND!" +
                            RESET
                        )

                        print(
                            YELLOW +
                            f"          💰 FINAL PRIZE: "
                            f"Rs. {total_amount:,}" +
                            RESET
                        )

                        print(
                            GREEN +
                            "=" * 65 +
                            RESET
                        )

                    # ========================================
                    # NEXT QUESTION
                    # ========================================

                    elif i < len(questions) - 1:

                        print(
                            "\n" +
                            CYAN +
                            "=" * 65 +
                            RESET
                        )

                        print(
                            CYAN +
                            f"              ➡️ NEXT QUESTION: "
                            f"{i + 2} / 16" +
                            RESET
                        )

                        print(
                            CYAN +
                            "=" * 65 +
                            RESET
                        )

                        input("Press Enter to continue...")

                    break

                # ============================================
                # WRONG ANSWER
                # ============================================

                else:

                    print(
                        "\n" +
                        RED +
                        "=" * 65 +
                        RESET
                    )

                    print(
                        RED +
                        "              ❌ WRONG ANSWER!" +
                        RESET
                    )

                    print(
                        RED +
                        f"              Correct Answer: "
                        f"{answers[i]}" +
                        RESET
                    )

                    print(
                        YELLOW +
                        f"              🔒 Amount to Take Home: "
                        f"Rs. {secured_amount:,}" +
                        RESET
                    )

                    print(
                        RED +
                        "=" * 65 +
                        RESET
                    )

                    return (
                        player_name,
                        secured_amount,
                        correct_count,
                        attempted_questions
                    )

            # ------------------------------------------------
            # INVALID INPUT
            # ------------------------------------------------

            else:

                print(
                    RED +
                    "Invalid input! Please enter A, B, C, D, "
                    "1, 2, 3 or Q." +
                    RESET
                )

    return (
        player_name,
        total_amount,
        correct_count,
        attempted_questions
    )


# ============================================================
#                       FINAL RESULT
# ============================================================

def show_result(
    player_name,
    total_amount,
    correct_count,
    attempted_questions
):

    print("\n" + CYAN + "=" * 65 + RESET)
    print(CYAN + "                  🏆 GAME OVER 🏆" + RESET)
    print(CYAN + "=" * 65 + RESET)

    print(f"\nPlayer Name      : {player_name}")
    print(f"Questions Played : {attempted_questions}")
    print(f"Correct Answers  : {correct_count}")

    if attempted_questions > 0:

        accuracy = (
            correct_count /
            attempted_questions
        ) * 100

        print(f"Accuracy         : {accuracy:.2f}%")

    print(
        YELLOW +
        f"\n💰 FINAL AMOUNT  : Rs. {total_amount:,}" +
        RESET
    )

    if total_amount == 150000:

        print(
            "\n" +
            GREEN +
            "🎉 INCREDIBLE! YOU WON THE MAXIMUM PRIZE! 🎉" +
            RESET
        )

    elif total_amount >= 90000:

        print(
            "\n" +
            GREEN +
            "🌟 Excellent Performance!" +
            RESET
        )

    elif total_amount >= 40000:

        print(
            "\n" +
            YELLOW +
            "👏 Great Job! You cleared Round 1!" +
            RESET
        )

    else:

        print(
            "\n" +
            YELLOW +
            "👍 Good effort! Keep learning and try again!" +
            RESET
        )

    print("\n" + CYAN + "=" * 65 + RESET)


# ============================================================
#                       START PROGRAM
# ============================================================

while True:

    welcome_screen()

    (
        player_name,
        total_amount,
        correct_count,
        attempted_questions
    ) = play_game()

    show_result(
        player_name,
        total_amount,
        correct_count,
        attempted_questions
    )

    play_again = input(
        "\nWould you like to play again? (Y/N): "
    ).strip().upper()

    if play_again != "Y":

        print("\n" + CYAN + "=" * 65 + RESET)

        print(
            CYAN +
            "       Thank you for playing QUIZQUEST! 🏆" +
            RESET
        )
        print(
            CYAN +
            "              See you next time!" +
            RESET
        )
        print(CYAN + "=" * 65 + RESET)
        break