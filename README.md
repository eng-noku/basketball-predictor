⚙How It Works

The prediction process follows four main steps:

Analyse Team Performance: The program reads previously recorded match statistics for each team, including baskets scored and baskets conceded.

Calculate Team Ratings: Each team's rating is calculated using the difference between its average baskets scored and average baskets conceded.

Team Rating = Average Baskets Scored - Average Baskets Conceded

Apply Home Advantage: The user selects the two competing teams and identifies the home team. The home team receives an additional 3 points.

Predict the Winner: The adjusted ratings are compared. The team with the higher rating is predicted to win.

🛠Technologies Used

Python

File retrieval

Lists and dictionaries

Functions

Conditional statements

Basic statistical calculations

📈Data

The predictor uses basketball match results from the current NBA season, with statistics recorded up to 11 November 2026.

Team performance data is stored in teams.txt.

👟How to Run

Clone or download this repository.

Make sure Python is installed.

Ensure predictor v2.py and teams.txt are in the same directory.

Run the program:

python "predictor v2.py"

Follow the prompts to enter the competing teams and identify the home team.

🔨Things I could improve:

Incorporating more advanced team performance metrics.

Testing prediction accuracy against actual match outcomes.

Updating team statistics automatically as new matches are played.

✍🏾Author

eng-noku

Developed as a personal Python project exploring sports statistics, data analysis and predictive modelling.