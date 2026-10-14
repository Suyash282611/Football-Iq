
import random as r
import time

# ============================================================
# FOOTBALL QUIZ ARENA
# 100 questions | 10 questions per game
# Python standard library only
# ============================================================

# FORMAT:
# (question, correct_answer, [wrong1, wrong2, wrong3],
#  category, difficulty, explanation)

QUESTIONS = [

    # ==================== WORLD CUP ====================

    ("Who won the first FIFA World Cup in 1930?",
     "Uruguay", ["Brazil", "Italy", "Argentina"],
     "World Cup", "Easy", "Uruguay hosted and won the inaugural tournament."),

    ("Which country has won the most men's FIFA World Cups?",
     "Brazil", ["Germany", "Italy", "Argentina"],
     "World Cup", "Easy", "Brazil has won five men's World Cup titles."),

    ("Who won the 2022 FIFA World Cup?",
     "Argentina", ["France", "Croatia", "Brazil"],
     "World Cup", "Easy", "Argentina defeated France on penalties in the final."),

    ("Who won the 2018 FIFA World Cup?",
     "France", ["Croatia", "Belgium", "Germany"],
     "World Cup", "Easy", "France defeated Croatia 4-2 in the final."),

    ("Who won the 2014 FIFA World Cup?",
     "Germany", ["Argentina", "Brazil", "Netherlands"],
     "World Cup", "Easy", "Germany defeated Argentina 1-0 after extra time."),

    ("Which country hosted the 2010 FIFA World Cup?",
     "South Africa", ["Brazil", "Germany", "Mexico"],
     "World Cup", "Easy", "South Africa was the first African host of the men's World Cup."),

    ("Who won the 2006 FIFA World Cup?",
     "Italy", ["France", "Germany", "Portugal"],
     "World Cup", "Easy", "Italy defeated France in a penalty shootout."),

    ("Who won the 2002 FIFA World Cup?",
     "Brazil", ["Germany", "Turkey", "South Korea"],
     "World Cup", "Easy", "Brazil defeated Germany 2-0 in the final."),

    ("Who won the 1998 FIFA World Cup?",
     "France", ["Brazil", "Italy", "Germany"],
     "World Cup", "Easy", "France won its first World Cup on home soil."),

    ("Who won the 1986 FIFA World Cup?",
     "Argentina", ["West Germany", "France", "Brazil"],
     "World Cup", "Easy", "Argentina won with Diego Maradona as captain."),

    ("Who scored the winning goal in the 2010 World Cup final?",
     "Andrés Iniesta", ["David Villa", "Xavi", "Fernando Torres"],
     "World Cup", "Medium", "Iniesta scored in extra time against the Netherlands."),

    ("Who scored the famous Hand of God goal?",
     "Diego Maradona", ["Pelé", "Lionel Messi", "Gabriel Batistuta"],
     "World Cup", "Medium", "Maradona scored it against England in 1986."),

    ("Who won the Golden Boot at the 2018 World Cup?",
     "Harry Kane", ["Kylian Mbappé", "Antoine Griezmann", "Romelu Lukaku"],
     "World Cup", "Medium", "Kane scored six goals in the tournament."),

    ("Who won the Golden Boot at the 2022 World Cup?",
     "Kylian Mbappé", ["Lionel Messi", "Olivier Giroud", "Julián Álvarez"],
     "World Cup", "Medium", "Mbappé scored eight goals in Qatar."),

    ("Which country finished third at the 2018 World Cup?",
     "Belgium", ["England", "Croatia", "Brazil"],
     "World Cup", "Medium", "Belgium defeated England in the third-place match."),

    ("Which country won the 1970 FIFA World Cup?",
     "Brazil", ["Italy", "Uruguay", "England"],
     "World Cup", "Medium", "Brazil defeated Italy 4-1 in the final."),

    ("Which country won the 1966 FIFA World Cup?",
     "England", ["West Germany", "Brazil", "Portugal"],
     "World Cup", "Easy", "England defeated West Germany 4-2 after extra time."),

    ("Who won the Golden Ball at the 2014 World Cup?",
     "Lionel Messi", ["James Rodríguez", "Thomas Müller", "Arjen Robben"],
     "World Cup", "Hard", "Messi received the tournament's Golden Ball."),

    ("Which country hosted the 2014 FIFA World Cup?",
     "Brazil", ["South Africa", "Russia", "Germany"],
     "World Cup", "Easy", "Brazil hosted the tournament in 2014."),

    ("Which country reached the semi-finals as a host in the 2002 World Cup?",
     "South Korea", ["Japan", "China", "Saudi Arabia"],
     "World Cup", "Medium", "South Korea reached the semi-finals as co-host."),

    # ==================== PLAYERS ====================

    ("Which player is known by the nickname CR7?",
     "Cristiano Ronaldo", ["Lionel Messi", "Neymar", "Kylian Mbappé"],
     "Players", "Easy", "CR7 combines Ronaldo's initials and shirt number."),

    ("Which country does Lionel Messi represent?",
     "Argentina", ["Spain", "Uruguay", "Portugal"],
     "Players", "Easy", "Messi captained Argentina to the 2022 World Cup."),

    ("Which country does Erling Haaland represent?",
     "Norway", ["Denmark", "Sweden", "Finland"],
     "Players", "Easy", "Haaland represents Norway internationally."),

    ("Which French player is nicknamed Zizou?",
     "Zinedine Zidane", ["Thierry Henry", "Didier Drogba", "Franck Ribéry"],
     "Players", "Easy", "Zizou is Zidane's famous nickname."),

    ("Which player is associated with the Siuuu celebration?",
     "Cristiano Ronaldo", ["Kylian Mbappé", "Erling Haaland", "Antoine Griezmann"],
     "Players", "Easy", "Ronaldo popularised the jump-and-turn celebration."),

    ("Which Brazilian striker was nicknamed O Fenômeno?",
     "Ronaldo Nazário", ["Ronaldinho", "Kaká", "Adriano"],
     "Players", "Medium", "O Fenômeno means The Phenomenon."),

    ("Which player won the 2018 Ballon d'Or?",
     "Luka Modrić", ["Cristiano Ronaldo", "Antoine Griezmann", "Lionel Messi"],
     "Players", "Medium", "Modrić won the award after an outstanding year."),

    ("Which player scored a hat-trick in the 2022 World Cup final?",
     "Kylian Mbappé", ["Lionel Messi", "Olivier Giroud", "Antoine Griezmann"],
     "Players", "Medium", "Mbappé scored three goals for France in the final."),

    ("Which country did Didier Drogba represent?",
     "Ivory Coast", ["Ghana", "Senegal", "Cameroon"],
     "Players", "Easy", "Drogba was a legendary Ivory Coast striker."),

    ("Which player is famous for the Cruyff Turn?",
     "Johan Cruyff", ["Marco van Basten", "Ruud Gullit", "Dennis Bergkamp"],
     "Players", "Medium", "Cruyff popularised the move during his playing career."),

    ("Which goalkeeper is renowned for the sweeper-keeper style?",
     "Manuel Neuer", ["Oliver Kahn", "Jens Lehmann", "Petr Čech"],
     "Players", "Medium", "Neuer is known for playing aggressively outside his box."),

    ("Which player won the 2023 Ballon d'Or?",
     "Lionel Messi", ["Erling Haaland", "Kylian Mbappé", "Kevin De Bruyne"],
     "Players", "Medium", "Messi won after Argentina's 2022 World Cup triumph."),

    ("Who is nicknamed the Egyptian King?",
     "Mohamed Salah", ["Riyad Mahrez", "Sadio Mané", "Achraf Hakimi"],
     "Players", "Easy", "Salah is widely known by this nickname."),

    ("Which player scored the fastest goal in men's World Cup history?",
     "Hakan Şükür", ["Ronaldo Nazário", "Miroslav Klose", "Robbie Keane"],
     "Players", "Hard", "Şükür scored after approximately 11 seconds in 2002."),

    ("Which player won the 2022 Yashin Trophy?",
     "Emiliano Martínez", ["Thibaut Courtois", "Alisson Becker", "Manuel Neuer"],
     "Players", "Hard", "Martínez received the 2022 award for goalkeepers."),

    ("Which legendary Brazilian footballer was known as the King of Football?",
     "Pelé", ["Romário", "Rivaldo", "Zico"],
     "Players", "Easy", "Pelé is widely regarded as one of football's greatest players."),

    ("Which position did Paolo Maldini primarily play?",
     "Defender", ["Striker", "Goalkeeper", "Central midfielder"],
     "Players", "Medium", "Maldini excelled at left-back and centre-back."),

    ("Who captained Croatia to the 2018 World Cup final?",
     "Luka Modrić", ["Ivan Rakitić", "Mario Mandžukić", "Ivan Perišić"],
     "Players", "Medium", "Modrić captained Croatia during its historic run."),

    ("Which player is famous for the Panenka penalty technique?",
     "Antonín Panenka", ["Zinedine Zidane", "David Beckham", "Roberto Baggio"],
     "Players", "Medium", "Panenka chipped his decisive penalty in the 1976 European final."),

    ("Which player won the Golden Ball at the 2022 World Cup?",
     "Lionel Messi", ["Kylian Mbappé", "Luka Modrić", "Antoine Griezmann"],
     "Players", "Medium", "Messi was named the tournament's best player."),

    # ==================== CLUB FOOTBALL ====================

    ("Which club plays its home matches at Anfield?",
     "Liverpool", ["Manchester United", "Chelsea", "Everton"],
     "Clubs", "Easy", "Anfield is Liverpool's historic home ground."),

    ("Which club is nicknamed Los Blancos?",
     "Real Madrid", ["Barcelona", "Atlético Madrid", "Sevilla"],
     "Clubs", "Easy", "The nickname refers to Real Madrid's traditional white kit."),

    ("Which club is associated with Camp Nou?",
     "Barcelona", ["Real Madrid", "Valencia", "Villarreal"],
     "Clubs", "Easy", "Camp Nou has historically been Barcelona's home stadium."),

    ("Which Italian club is nicknamed the Old Lady?",
     "Juventus", ["AC Milan", "Inter Milan", "Roma"],
     "Clubs", "Medium", "La Vecchia Signora is Juventus's Italian nickname."),

    ("Who won the 2023 UEFA Champions League?",
     "Manchester City", ["Inter Milan", "Real Madrid", "Bayern Munich"],
     "Clubs", "Easy", "City defeated Inter Milan 1-0 in the final."),

    ("Who won the 2020 UEFA Champions League?",
     "Bayern Munich", ["Paris Saint-Germain", "Liverpool", "Real Madrid"],
     "Clubs", "Medium", "Bayern defeated PSG 1-0 in the final."),

    ("Which club did Messi join after leaving Barcelona in 2021?",
     "Paris Saint-Germain", ["Manchester City", "Inter Miami", "Chelsea"],
     "Clubs", "Easy", "Messi joined PSG in August 2021."),

    ("Which club is nicknamed the Red Devils?",
     "Manchester United", ["Liverpool", "Arsenal", "Bayern Munich"],
     "Clubs", "Easy", "The Red Devils is Manchester United's nickname."),

    ("Which German club plays at Signal Iduna Park?",
     "Borussia Dortmund", ["Bayern Munich", "RB Leipzig", "Bayer Leverkusen"],
     "Clubs", "Medium", "Signal Iduna Park is Dortmund's home stadium."),

    ("Who won the first Premier League season in 1992-93?",
     "Manchester United", ["Arsenal", "Blackburn Rovers", "Liverpool"],
     "Clubs", "Medium", "Manchester United won the inaugural Premier League season."),

    ("Which club is famous for its La Masia academy?",
     "Barcelona", ["Ajax", "Real Madrid", "Bayern Munich"],
     "Clubs", "Medium", "La Masia is Barcelona's renowned youth academy."),

    ("Which club did Cristiano Ronaldo join from Manchester United in 2009?",
     "Real Madrid", ["Juventus", "Barcelona", "Inter Milan"],
     "Clubs", "Easy", "Ronaldo joined Real Madrid in 2009."),

    ("Who won the 2012 UEFA Champions League final?",
     "Chelsea", ["Bayern Munich", "Barcelona", "Real Madrid"],
     "Clubs", "Medium", "Chelsea defeated Bayern Munich on penalties."),

    ("Which club is based in Naples?",
     "Napoli", ["Lazio", "Atalanta", "Torino"],
     "Clubs", "Easy", "Napoli represents Naples in Italian football."),

    ("Which club won three consecutive Champions League titles from 2016 to 2018?",
     "Real Madrid", ["Barcelona", "Bayern Munich", "Atlético Madrid"],
     "Clubs", "Hard", "Real Madrid won three successive titles under Zidane."),

    ("Which club plays at the Emirates Stadium?",
     "Arsenal", ["Tottenham Hotspur", "Chelsea", "West Ham United"],
     "Clubs", "Easy", "The Emirates Stadium is Arsenal's home ground."),

    ("Which club is known as the Nerazzurri?",
     "Inter Milan", ["AC Milan", "Juventus", "Napoli"],
     "Clubs", "Medium", "Nerazzurri refers to Inter's black-and-blue colours."),

    ("Who won the 2021 UEFA Champions League final?",
     "Chelsea", ["Manchester City", "Real Madrid", "Paris Saint-Germain"],
     "Clubs", "Medium", "Chelsea defeated Manchester City 1-0."),

    ("Which club is famous for its Basque-player policy?",
     "Athletic Club", ["Real Sociedad", "Osasuna", "Getafe"],
     "Clubs", "Hard", "Athletic Club has a long-standing Basque-player tradition."),

    ("Which club is nicknamed the Yellow Submarine?",
     "Villarreal", ["Valencia", "Sevilla", "Real Betis"],
     "Clubs", "Medium", "El Submarino Amarillo is Villarreal's nickname."),

    # ==================== FOOTBALL RULES ====================

    ("How many players does each team normally start with?",
     "11", ["9", "10", "12"],
     "Rules", "Easy", "A standard team starts with eleven players, including the goalkeeper."),

    ("How long is a standard football match before added time?",
     "90 minutes", ["80 minutes", "100 minutes", "120 minutes"],
     "Rules", "Easy", "A normal match has two 45-minute halves."),

    ("Which card means a player is sent off?",
     "Red", ["Yellow", "Blue", "Green"],
     "Rules", "Easy", "A red card means dismissal from the match."),

    ("What is awarded for a direct-free-kick offence inside the defender's penalty area?",
     "Penalty kick", ["Corner kick", "Throw-in", "Goal kick"],
     "Rules", "Easy", "The attacking team is awarded a penalty."),

    ("What does VAR stand for?",
     "Video Assistant Referee", ["Verified Action Review", "Virtual Assistant Referee", "Video Analysis Rule"],
     "Rules", "Easy", "VAR stands for Video Assistant Referee."),

    ("What is the minimum number of players a team must have to continue a match?",
     "7", ["5", "6", "8"],
     "Rules", "Hard", "A match cannot continue if a team has fewer than seven players."),

    ("Can a player be penalised for offside directly from a goal kick?",
     "No", ["Yes, always", "Only inside the penalty area", "Only during extra time"],
     "Rules", "Hard", "There is no offside offence when receiving the ball directly from a goal kick."),

    ("What restart is awarded when the attacking team last touches the ball before it crosses the goal line without a goal?",
     "Goal kick", ["Corner kick", "Throw-in", "Dropped ball"],
     "Rules", "Medium", "The defending team takes a goal kick."),

    ("How far away must opponents normally stand at a free kick?",
     "9.15 metres", ["5 metres", "7 metres", "11 metres"],
     "Rules", "Medium", "The normal minimum distance is 9.15 metres."),

    ("What does a yellow card signify?",
     "A caution", ["An automatic goal", "A substitution", "The end of the match"],
     "Rules", "Easy", "A yellow card is a formal caution."),

    # ==================== EA SPORTS FIFA / FC ====================

    ("Which company develops EA SPORTS FC?",
     "EA Sports", ["Konami", "Ubisoft", "2K"],
     "Gaming", "Easy", "EA Sports develops the series formerly branded FIFA."),

    ("What was the first game released under the EA SPORTS FC name?",
     "EA SPORTS FC 24", ["EA SPORTS FC 23", "EA SPORTS FC 25", "EA SPORTS FC 26"],
     "Gaming", "Easy", "EA SPORTS FC 24 launched in 2023."),

    ("Which series preceded EA SPORTS FC?",
     "FIFA", ["Football Manager", "Rocket League", "eFootball"],
     "Gaming", "Easy", "EA used the FIFA name for many years before rebranding."),

    ("Which company developed Pro Evolution Soccer?",
     "Konami", ["EA Sports", "Sega", "Capcom"],
     "Gaming", "Easy", "Konami developed Pro Evolution Soccer, later rebranded as eFootball."),

    ("What did FUT traditionally stand for in FIFA games?",
     "FIFA Ultimate Team", ["Football United Tournament", "Final Ultimate Tactics", "Football User Training"],
     "Gaming", "Medium", "FUT was the Ultimate Team mode in FIFA-branded games."),

    ("Which mode lets you manage a club across multiple seasons?",
     "Career Mode", ["Kick-Off", "Skill Games", "Volta Arcade"],
     "Gaming", "Easy", "Career Mode supports long-term club management."),

    ("What does the pace attribute represent?",
     "Speed", ["Vision", "Composure", "Positioning"],
     "Gaming", "Easy", "Pace represents speed-related player attributes."),

    ("What does a weak-foot rating represent?",
     "Ability with the non-dominant foot", ["Maximum stamina", "Defensive awareness", "Goalkeeper reflexes"],
     "Gaming", "Medium", "Weak foot reflects ability with the less-preferred foot."),

    ("What is the main purpose of the transfer market in Ultimate Team?",
     "Trade eligible player items", ["Change real-world league tables", "Edit official match results", "Modify console hardware"],
     "Gaming", "Easy", "The market allows eligible Ultimate Team items to be traded."),

    ("What does an overall player rating broadly summarize?",
     "General in-game ability", ["Stadium capacity", "Referee experience", "Real-world transfer spending"],
     "Gaming", "Easy", "Overall ratings summarise a player's in-game attributes."),

    ("Which attribute is most associated with shot conversion?",
     "Finishing", ["Aggression", "Jumping", "Defensive awareness"],
     "Gaming", "Medium", "Finishing is particularly relevant when converting chances."),

    ("What does goalkeeper handling generally measure?",
     "Ability to catch and control the ball", ["Free-kick accuracy", "Team sprint speed", "Striker finishing"],
     "Gaming", "Medium", "Handling relates to securing and controlling the ball."),

    ("What is a common purpose of Skill Games?",
     "Practise gameplay mechanics", ["Manage real-world transfers", "Edit league standings", "Change hardware settings"],
     "Gaming", "Easy", "Skill Games offer practice for passing, shooting and other mechanics."),

    ("Which mode is designed for quick individual matches?",
     "Kick-Off", ["Career Mode", "Manager Career only", "Training Arena only"],
     "Gaming", "Easy", "Kick-Off is designed for quick matches."),

    ("What does a formation setting change?",
     "The team's tactical shape", ["The console frame rate", "The controller battery", "The stadium's real location"],
     "Gaming", "Easy", "A formation changes the team's player arrangement."),

    ("What is a common benefit of a fast winger?",
     "Threatening space behind defenders", ["Automatically winning every tackle", "Preventing all counterattacks", "Improving referee decisions"],
     "Gaming", "Easy", "Pace can help wingers beat defenders and exploit open space."),

    ("What is a loan move in Career Mode?",
     "A temporary move to another club", ["Permanent retirement", "A change to the real-world league", "Automatic deletion of a player"],
     "Gaming", "Easy", "A loan sends a player to another club temporarily."),

    ("What does a through pass generally try to do?",
     "Send the ball into space for a teammate", ["Change the camera", "Pause the game", "Substitute the goalkeeper"],
     "Gaming", "Easy", "Through passes try to release teammates into space."),

    ("What is the purpose of a chemistry style in editions that use it?",
     "Modify selected player attributes", ["Change the referee", "Alter the stadium roof", "Change the number of players"],
     "Gaming", "Medium", "Chemistry Styles can boost selected attributes."),

    ("What is Create-a-Club in supported Career Mode editions?",
     "A feature for creating a custom club", ["A penalty-only mode", "A stadium camera setting", "A goalkeeper training drill"],
     "Gaming", "Medium", "Create-a-Club lets players build a custom club in supported editions."),

    # ==================== INTERNATIONAL FOOTBALL ====================

    ("Who won the 2023 FIFA Women's World Cup?",
     "Spain", ["England", "United States", "Sweden"],
     "International", "Medium", "Spain defeated England 1-0 in the final."),

    ("Who won the 2019 FIFA Women's World Cup?",
     "United States", ["Netherlands", "Germany", "Japan"],
     "International", "Easy", "The United States defeated the Netherlands in the final."),

    ("Which country hosted the 2022 men's World Cup?",
     "Qatar", ["Russia", "United Arab Emirates", "Saudi Arabia"],
     "International", "Easy", "Qatar hosted the tournament in 2022."),

    ("Who won the 2015 FIFA Women's World Cup?",
     "United States", ["Japan", "Germany", "Canada"],
     "International", "Medium", "The United States defeated Japan in the final."),

    ("Who won the 2021 Copa América final?",
     "Argentina", ["Brazil", "Uruguay", "Chile"],
     "International", "Easy", "Argentina defeated Brazil 1-0."),

    ("Who won the 2024 Copa América?",
     "Argentina", ["Colombia", "Uruguay", "Brazil"],
     "International", "Medium", "Argentina defeated Colombia after extra time."),

    ("Who won UEFA Euro 2024?",
     "Spain", ["England", "France", "Germany"],
     "International", "Easy", "Spain defeated England 2-1 in the final."),

    ("Who won UEFA Euro 2016?",
     "Portugal", ["France", "Germany", "Wales"],
     "International", "Easy", "Portugal defeated France after extra time."),

    ("Who won the 2004 UEFA European Championship?",
     "Greece", ["Portugal", "Czech Republic", "France"],
     "International", "Medium", "Greece defeated hosts Portugal in the final."),

    ("Who won UEFA Euro 2008?",
     "Spain", ["Germany", "Italy", "Russia"],
     "International", "Medium", "Spain defeated Germany in the final."),

    # ==================== TACTICS AND KNOWLEDGE ====================

    ("What is a hat-trick?",
     "One player scores three goals in a match", ["A team scores three own goals", "A player makes three assists", "A goalkeeper saves three penalties"],
     "Tactics", "Easy", "A hat-trick means scoring three goals in a match."),

    ("What is a clean sheet?",
     "Conceding no goals", ["Scoring in every half", "Winning by three goals", "Keeping possession for 90 minutes"],
     "Tactics", "Easy", "A clean sheet means the team did not concede a goal."),

    ("What is a through ball intended to do?",
     "Pass into space behind the defence", ["Clear the ball into the stands", "Pass only backwards", "Take a corner kick"],
     "Tactics", "Medium", "A through ball aims to release a teammate into space."),

    ("What does a false nine generally do?",
     "Drop deeper from the striker position", ["Play as goalkeeper", "Play only as centre-back", "Take every corner"],
     "Tactics", "Medium", "A false nine drops deeper to link play and create space."),

    ("What does a high defensive line mean?",
     "Defenders position themselves farther up the pitch", ["Defenders stand on the goal line", "The goalkeeper never leaves the box", "The team plays without defenders"],
     "Tactics", "Medium", "A high line compresses space by positioning defenders higher."),

    ("What is pressing in football?",
     "Applying pressure to opponents in possession", ["Waiting for the final whistle", "Taking only long throw-ins", "Keeping everyone in the penalty area"],
     "Tactics", "Easy", "Pressing attempts to force mistakes and regain possession."),

    ("Which formation has four defenders, three midfielders and three forwards?",
     "4-3-3", ["4-4-2", "3-5-2", "5-3-2"],
     "Tactics", "Easy", "The numbers describe outfield players, excluding the goalkeeper."),

    ("What does a double pivot usually refer to?",
     "Two deeper central midfielders", ["Two goalkeepers", "Two centre-forwards only", "Two penalty takers"],
     "Tactics", "Medium", "A double pivot consists of two deeper central midfielders."),

    ("What is an assist?",
     "A contribution credited with setting up a goal", ["A goalkeeper save", "A yellow card", "Any successful tackle"],
     "Tactics", "Easy", "An assist is credited according to the competition's statistical rules."),

    ("Which position primarily operates in the centre of defence?",
     "Centre-back", ["Winger", "Striker", "Centre-forward"],
     "Tactics", "Easy", "Centre-backs are central defenders."),

    # ==================== MORE FOOTBALL TRIVIA ====================

    ("Which country is home to Ajax?",
     "Netherlands", ["Belgium", "Denmark", "Switzerland"],
     "Trivia", "Easy", "Ajax is based in Amsterdam."),

    ("Which country is home to Bayern Munich?",
     "Germany", ["Austria", "Switzerland", "Netherlands"],
     "Trivia", "Easy", "Bayern Munich is based in Munich, Germany."),

    ("Who won the Golden Boot at the 2014 World Cup?",
     "James Rodríguez", ["Lionel Messi", "Thomas Müller", "Neymar"],
     "Trivia", "Medium", "Rodríguez scored six goals in the tournament."),

    ("Which country won the 2011 AFC Asian Cup?",
     "Japan", ["Australia", "South Korea", "Saudi Arabia"],
     "Trivia", "Medium", "Japan defeated Australia in the final."),

    ("Which country won the 2013 FIFA Confederations Cup?",
     "Brazil", ["Spain", "Italy", "Uruguay"],
     "Trivia", "Medium", "Brazil defeated Spain 3-0 in the final."),

    ("Which club won the 2005 Champions League final after trailing 3-0?",
     "Liverpool", ["AC Milan", "Chelsea", "Barcelona"],
     "Trivia", "Medium", "Liverpool came back to draw and won on penalties."),

    ("Which country won the 1992 UEFA European Championship?",
     "Denmark", ["Germany", "Netherlands", "Sweden"],
     "Trivia", "Hard", "Denmark won after entering the finals late."),

    ("Which club did David Beckham join after leaving Manchester United?",
     "Real Madrid", ["Barcelona", "AC Milan", "Inter Milan"],
     "Trivia", "Medium", "Beckham joined Real Madrid in 2003."),

    ("Which player scored the winning goal for Real Madrid in the 2014 Champions League final?",
     "Gareth Bale", ["Cristiano Ronaldo", "Sergio Ramos", "Ángel Di María"],
     "Trivia", "Hard", "Bale scored Real Madrid's second goal in extra time."),

    ("Which country did England defeat in the 1966 World Cup final?",
     "West Germany", ["Argentina", "Brazil", "Portugal"],
     "Trivia", "Medium", "England won 4-2 after extra time at Wembley.")
]


# ============================================================
# GAME SETTINGS
# ============================================================

QUESTIONS_PER_GAME = 10
POINTS_PER_CORRECT_ANSWER = 10
STREAK_BONUS = 5


def show_line():
    print("=" * 64)


def get_choice(prompt, valid_choices):
    """Validate a user's menu or answer selection."""
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Try again.")


def choose_difficulty():
    show_line()
    print("SELECT DIFFICULTY")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Mixed")

    choice = get_choice("Your choice: ", ["1", "2", "3", "4"])

    difficulty_map = {
        "1": "Easy",
        "2": "Medium",
        "3": "Hard",
        "4": "Mixed"
    }

    return difficulty_map[choice]


def select_questions(difficulty):
    """Select ten different questions from the bank."""
    if difficulty == "Mixed":
        pool = QUESTIONS[:]
    else:
        pool = [q for q in QUESTIONS if q[4] == difficulty]

    # If a difficulty has fewer than ten questions,
    # fill the selection from the entire bank.
    if len(pool) < QUESTIONS_PER_GAME:
        print("\nNot enough questions at that difficulty.")
        print("Filling the game with questions from all levels.")
        pool = QUESTIONS[:]

    return r.sample(pool, QUESTIONS_PER_GAME)


def ask_question(question_data, number, total):
    """
    Every question follows the same structure:
    question, answer, wrong options, category, difficulty, explanation
    """
    question, answer, wrong_answers, category, difficulty, explanation = (
        question_data
    )

    # Make a fresh list for this question.
    # Never change the original question bank.
    options = list(wrong_answers) + [answer]
    r.shuffle(options)

    show_line()
    print(f"QUESTION {number}/{total}")
    print(f"Category: {category} | Difficulty: {difficulty}")
    print("-" * 64)
    print(question)
    print()

    for index, option in enumerate(options):
        print(f"  {chr(65 + index)}. {option}")

    choice = get_choice(
        "\nYour answer (A/B/C/D): ",
        ["a", "b", "c", "d"]
    )

    chosen_answer = options[ord(choice) - ord("a")]

    if chosen_answer == answer:
        print("\nCorrect! +10 points")
        points = POINTS_PER_CORRECT_ANSWER
        correct = True
    else:
        print(f"\nIncorrect! The correct answer is: {answer}")
        points = 0
        correct = False

    print(f"Explanation: {explanation}")

    return points, correct


def show_results(name, score, correct_count, best_streak, results):
    show_line()
    print(f"QUIZ COMPLETE, {name.upper()}!")
    show_line()

    accuracy = (correct_count / QUESTIONS_PER_GAME) * 100

    print(f"Correct answers : {correct_count}/{QUESTIONS_PER_GAME}")
    print(f"Accuracy        : {accuracy:.0f}%")
    print(f"Final score     : {score}")
    print(f"Best streak     : {best_streak}")
    print()

    if correct_count == QUESTIONS_PER_GAME:
        print("PERFECT SCORE! You're a football encyclopedia!")
    elif accuracy >= 80:
        print("Outstanding! You really know your football.")
    elif accuracy >= 60:
        print("Good performance! Keep sharpening your knowledge.")
    elif accuracy >= 40:
        print("Not bad! Keep practising.")
    else:
        print("Keep playing. Every football expert starts somewhere!")

    print("\nANSWER REVIEW")
    show_line()

    for index, (question, correct, answer) in enumerate(results, start=1):
        status = "CORRECT" if correct else "INCORRECT"
        print(f"{index}. [{status}] {question}")

        if not correct:
            print(f"   Correct answer: {answer}")

    show_line()


def play_game():
    show_line()
    print("             FOOTBALL QUIZ ARENA")
    show_line()

    print(f"Questions in bank: {len(QUESTIONS)}")
    print(f"Questions per game: {QUESTIONS_PER_GAME}")
    print("\nCategories include:")
    print("World Cup, Players, Clubs, Rules, Gaming, Tactics and Trivia.")

    name = input("\nEnter your name: ").strip()

    if not name:
        name = "Football Fan"

    difficulty = choose_difficulty()
    selected_questions = select_questions(difficulty)

    score = 0
    correct_count = 0
    streak = 0
    best_streak = 0
    results = []

    show_line()
    print(f"Welcome, {name}!")
    print("Your game begins in...")

    for countdown in [3, 2, 1]:
        print(countdown)
        time.sleep(0.5)

    print("KICK-OFF!")
    time.sleep(0.5)

    for number, question_data in enumerate(selected_questions, start=1):
        points, correct = ask_question(
            question_data,
            number,
            QUESTIONS_PER_GAME
        )

        if correct:
            streak += 1
            correct_count += 1
            best_streak = max(best_streak, streak)

            if streak >= 3:
                points += STREAK_BONUS
                print(f"Streak bonus! +{STREAK_BONUS} points")
        else:
            streak = 0

        score += points

        question = question_data[0]
        answer = question_data[1]

        results.append((question, correct, answer))

        print(f"\nCurrent score: {score}")
        print(f"Correct answers: {correct_count}/{number}")

        if number < QUESTIONS_PER_GAME:
            input("\nPress ENTER for the next question...")
        else:
            input("\nPress ENTER to see your final results...")

    show_results(name, score, correct_count, best_streak, results)


def main():
    while True:
        play_game()

        print("\nWould you like another round?")
        choice = get_choice(
            "Enter Y to play again or N to exit: ",
            ["y", "n"]
        )

        if choice == "n":
            print("\nThanks for playing Football Quiz Arena!")
            print("See you next time. Goodbye!")
            break

        print("\nStarting a fresh game...")
        time.sleep(1)

main()
