# Texas-Hold-em-GUI
Texas-Hold-em-GUI is a Texas Hold'em poker card game with interactive features. It allows everyone to play Texas Hold'em in a graphical user interfaces with 6 bot players.

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have installed the latest version of Python 3, or at least Python 3.8.2.
* Make sure you are familiar with the game Texas Hold'em. If not, see the instructions below.

## Using Texas-Hold-em-GUI
To play Texas-Hold-em-GUI using user mode, run the program through command line below:
Python Texas-Hold-em-GUI.py

## Instructions
* Hand Values
Rank	Name		Description	
9	Highcard		Simple value of the card. Lowest: 2 – Highest: Ace
8	Pair		Two cards with the same value
7	Two pairs	Two times two cards with the same value
6	Three of a kind	Three cards with the same value
5	Straight		Sequence of 5 cards in increasing value
4	Flush		5 cards of the same suit
3	Full house	Combination of three of a kind and a pair
2	Four of a kind	Four cards of the same value
1	Straight flush	Straight of the same suit
Reference: https://en.wikipedia.org/wiki/Texas_hold_%27em

* Game start
	* Game Start Screen: press start to start the game
	* User Name Input Screen: input your username then press submit (there are no limitations)
	* Game Table:
		* In each round, the bot players have made their moves and are displayed on the table, you are the last player to take the action.
		* Initialize phase:
			* Bot player actions:
				* The system will first judge if the bot player has monster, good, or decent card. 
					* If the bot has monster card(such as two As, A&13, two 13s or two 12s), it will bet 3 times the bet amount
					* If the bot has good card(such as two 11s, two 10s, two 9s, 1&12, 1&11, 1&10 or 13&12), it will bet 2 times the bet amount
					* If the bot has decent card(such as a pair or two cards are consecutive), it will bet the normal bet amount
					* Else the bot is considered as bad card player.
				* If the bad card player amount is less than half of the player total number or there is no monster card player appear, the bot player "Fold"
				* Elif the bad card player amount is equal to half of the player total number, the bot player "Check"
				* Else the bot player bet the monster card amount of money to trick other players as if the bot has really great card.
			* Human player actions:
				* Player can only choose to bet or fold in this round.
				* If the player fold, the game ends on player end. The player will get the final result about who won and the money display for other bot players after the game ends.
				* If the player choose to bet, move on to round 1.
		* Round 1:
			* Bot player actions:
				* If the bot player's rank is equal to the threshold or player money is less than 1, the bot player "Check"
				* If the bot player's rank is larger than threshold, the bot player "Fold". If the fold player's amount is larger than the total player's amount -1, then the player will bet 2 times the bet amount to trick the other players. If the bot don't have that much money, it will all in to trick other players as if the bot's card is super good.
				* If the bot player's rank is smaller than the threshold, the player will bet 3 times bet amount if the player's rank is 1 or 2. The player will bet 2 times bet amount if the player's rank is 3 or 4. the player will bet the normal bet amount if the player's rank is 5 or above. 
		* Round 2 repeat Round 1.
		* If the bot is broke, remove the bot from the game.
		* The game will end if the human player don't have enough money to continue. Or all the bots are broke. Or the player choose not to continue.
		* If the user want to play another round, press yes. If not, press no.
		* Game ends.

## Note
I created a lot of cubes to help me find the positions to place each element, if you want to make adjustments, you can uncomment the line 28 and use function draw_blank_board and draw_cell to help you locate.

## Contact
If you want to contact me you can reach me at jingjw23@uci.edu.

## Sample
https://user-images.githubusercontent.com/104955830/191812814-5b2c8770-45bc-400b-a54c-a5d2e4bc62a3.mp4
