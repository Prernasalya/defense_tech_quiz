# Python quiz game

questions = ("What is the primary purpose of a ballistic Missile Defense(BMD)?",
             "Which of the technologies is commonly used in unmanned aerial vehicles(UAVs)?",
             "What does the acronym 'DRDO' stand for?",
             "Which is a major advantage of AI in modern warfare?",
             "Stealth technology in defense aircraft is used to:",
             "The Integrated Guided Missile Development Program(IGMDP) of India was initiated under whose leadership?",
             "What is the primary role of Electronic Warfare(EW) systems?",)

options = (("A. Launch nuclear weapons", "B. Detect and destroy incoming missiles", "C. Protect against cyberattacks ", "D. Jam enemy communication systems"),
           ("A. LiDAR and GPS", "B. Jet propulsion", "C. Cryogenics", "D. Blockchain"),
           ("A. Department of Research and Development fro Ordinance", "B. Defense Rockets and Detonation Office", "C. Directorate of Rocket Design and Operations", "D. Defense Research and Development Organisation"),
           ("A. Reduced communication range", "B. Lower data accuracy", "C. Real-time decision making", "D. Limited Mobility"),
           ("A. Reduce radar detection", "B. Improve fuel efficiency", "C. Increase weapon load", "D. Amplify engine noise"),
           ("A. Vikram Sarabhai", "B. Homi Bhabha", "C. R.Chidambaram", "D. A.P.J. Abdul Kalam"),
           ("A. Destroy tanks and vehicles", "B. Supply food and medical aid", "C. Disrupt enemy electronics and communication", "D. Launch satellites into orbits"))

answers = ("B", "A", "D", "C", "A", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[question_num] :
        print(option)

    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess in answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")

    question_num += 1


print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("          RESULTS         ")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Your score is {score}")

if score >= 5:
    print("You won this game!")
else:
    print()
    print("Oops, you lost this game!"
          "Try again and secure a score greater than or equal to 5 to win!")