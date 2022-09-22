import tkinter as tk
import random
import itertools


class TableClass:

    """A class for the card table."""


    def __init__(self):
        self.cell_size = 30
        self.colum = 40
        self.row = 25
        self.threshold = 8
        self.money_pool = 0
        self.bet = 1
        self.count = 0
        self.card_dict = {"C": "♣", "H": "♥", "S":"♠", "D": "♦"}
        self.monster_money = 3 * self.bet
        self.good_money = 2 * self.bet
        self.decent_money = self.bet
        self.CreateWindow()
        self.CreateCanvas()
        self.hint_text = tk.StringVar()
        self.welcome_text = tk.StringVar()
        self.username = tk.StringVar()
        #self.draw_blank_board()
        self.draw_table_profile()
        self.welcome()


    def CreateWindow(self) -> None:
        """Create tkinter window."""
        self.master = tk.Tk()
        self.master.title("Texas Hold'em")
        self.master.resizable(0, 0)


    def CreateCanvas(self):
        """Create tkinter canvas."""
        self.canvas = tk.Canvas(self.master, width=self.colum * self.cell_size, height=self.row * self.cell_size,
                                bg="#CCCCCC")
        self.canvas.pack()


    def draw_blank_board(self):
        """Use to place objects on canvas conveniently."""
        for ri in range(self.row):
            for ci in range(self.colum):
                self.draw_cell(ci,ri)


    def draw_cell(self,c,r):
        """Help with placing items by making small cubes."""
        x0 = c * self.cell_size
        y0 = r * self.cell_size
        x1 = c * self.cell_size + self.cell_size
        y1 = r * self.cell_size + self.cell_size
        self.canvas.create_rectangle(x0,y0,x1,y1,fill = "#CCCCCC", outline= "white", width = 2)


    def draw_table_profile(self):
        """Draw table and all the player profile pictures."""
        profile_color = "#984f44"
        outline_color = "#833c31"
        #Game table
        self.canvas.create_oval(200, 150, 1000, 600, fill = "#1d892e", outline = "#044b10", width = 40)
        #Player profile pictures
        self.P1_pic = self.canvas.create_oval(8 * self.cell_size, 16 * self.cell_size, 11 * self.cell_size, 19 * self.cell_size,
                                fill=profile_color, outline=outline_color, width=5)
        self.P2_pic = self.canvas.create_oval(8 * self.cell_size, 6 * self.cell_size, 11 * self.cell_size, 9 * self.cell_size,
                                fill=profile_color, outline=outline_color, width=5)
        self.P3_pic = self.canvas.create_oval(18.5 * self.cell_size, 3.7 * self.cell_size, 21.5 * self.cell_size,
                                6.7 * self.cell_size, fill=profile_color, outline=outline_color, width=5)
        self.P4_pic = self.canvas.create_oval(29 * self.cell_size, 6 * self.cell_size, 32 * self.cell_size, 9 * self.cell_size,
                                fill=profile_color, outline=outline_color, width=5)
        self.P5_pic = self.canvas.create_oval(29 * self.cell_size, 16 * self.cell_size, 32 * self.cell_size, 19 * self.cell_size,
                                fill=profile_color, outline=outline_color, width=5)
        self.P6_pic = self.canvas.create_oval(18.5 * self.cell_size, 18.2 * self.cell_size, 21.5 * self.cell_size,
                                21.2 * self.cell_size, fill=profile_color, outline=outline_color, width=5)
        self.all_prof_pic = [self.P1_pic, self.P2_pic, self.P3_pic, self.P4_pic, self.P5_pic, self.P6_pic]
        #Player number
        self.P1 = self.canvas.create_text(9.5 * self.cell_size, 17.5 * self.cell_size, text="1",
                                          fill="white", font=('Times 30 bold'))
        self.P2 = self.canvas.create_text(9.5 * self.cell_size, 7.5 * self.cell_size, text="2",
                                          fill="white", font=('Times 30 bold'))
        self.P3 = self.canvas.create_text(20 * self.cell_size, 5.2 * self.cell_size, text="3",
                                          fill="white", font=('Times 30 bold'))
        self.P4 = self.canvas.create_text(30.5 * self.cell_size, 7.5 * self.cell_size, text="4",
                                          fill="white", font=('Times 30 bold'))
        self.P5 = self.canvas.create_text(30.5 * self.cell_size, 17.5 * self.cell_size, text="5",
                                          fill="white", font=('Times 30 bold'))
        self.P6 = self.canvas.create_text(20 * self.cell_size, 19.7 * self.cell_size, text="U",
                                          fill="white", font=('Times 30 bold'))
        self.all_player_prof = [self.P1, self.P2, self.P3, self.P4, self.P5, self.P6]


    def welcome(self):
        """Welcome game panel."""
        self.welcome_text.set("Welcome to Texas Hold'em (6-player)!\n\nPress start if you want to play :)")
        self.welcome_label = tk.Label(textvariable=self.welcome_text, font=('Times 25 bold'), bg="#1d892e",
                                      fg="#ffffff")
        self.welcome_label.place(x=13 * self.cell_size, y=10 * self.cell_size)
        self.start_button = tk.Button(self.master, text='Start', width=9, height=2, command=self.before_start)
        self.start_button.place(x=18.5 * self.cell_size, y=14 * self.cell_size)


    def before_start(self):
        """Prompt the user to input user name."""
        self.start_button.destroy()
        self.welcome_text.set(
            "   Before game starts....\n Please give yourself an awsome name\nNote:there are no limitations")
        self.name_entry = tk.Entry(self.master, textvariable=self.username)
        self.name_entry.place(x=14 * self.cell_size, y=14 * self.cell_size)
        self.submit_button = tk.Button(self.master, text='Submit', width=9, height=2, command=self.begin)
        self.submit_button.place(x=24 * self.cell_size, y=14 * self.cell_size)


    def begin(self):
        """Start the whole game."""
        self.name = self.name_entry.get()
        self.submit_button.destroy()
        self.welcome_label.destroy()
        self.name_entry.destroy()
        self.canvas.create_text(20 * self.cell_size, 9 * self.cell_size, text="Texas Hold'em 6-Player-Game",
                                fill="white", font=('Times 25 bold'))
        self.all_labels()
        self.Buttons()
        self.card_position()
        self.create_player_class()
        self.initialize()


    def all_labels(self):
        """Place all the needed labels on the table."""
        #Game round and winner information label
        self.hint_label = tk.Label(
            textvariable=self.hint_text, font=('Times 15'),
            bg="#1d892e", fg="#CCCCCC")
        self.hint_label.place(x=17.5 * self.cell_size, y=13 * self.cell_size)
        #All player actions display
        self.all_player_actions = [tk.Label(text="", font=('Times 18 bold'), fg="#ffffff", bg= "#1d892e") for i in range(6)]
        self.all_player_actions[0].place(x=10.3 * self.cell_size, y=15 * self.cell_size)
        self.all_player_actions[1].place(x=10.3 * self.cell_size, y=9 * self.cell_size)
        self.all_player_actions[2].place(x=18 * self.cell_size, y=7 * self.cell_size)
        self.all_player_actions[3].place(x=27.8 * self.cell_size, y=9 * self.cell_size)
        self.all_player_actions[4].place(x=27.8 * self.cell_size, y=15 * self.cell_size)
        self.all_player_actions[5].place(x=21.5 * self.cell_size, y=17.6 * self.cell_size)
        #All player moneys display
        self.all_player_money = [tk.Label(text="$10", font=('Times 18 bold'), fg="#000000", bg="#CCCCCC") for i in range(6)]
        self.all_player_money[0].place(x=6.2 * self.cell_size, y=18 * self.cell_size)
        self.all_player_money[1].place(x=6.2 * self.cell_size, y=6 * self.cell_size)
        self.all_player_money[2].place(x=22.5 * self.cell_size, y=3 * self.cell_size)
        self.all_player_money[3].place(x=32.2 * self.cell_size, y=6 * self.cell_size)
        self.all_player_money[4].place(x=32.2 * self.cell_size, y=18 * self.cell_size)
        self.all_player_money[5].place(x=16 * self.cell_size, y=21 * self.cell_size)


    def card_position(self):
        """Place all the cards in position."""
        self.all_player_cards = [tk.Label(text="", font=('Times 23 bold'), fg="#000000") for i in range(12)]
        # Player 1, left down
        self.canvas.create_rectangle(3.7 * self.cell_size, 19.3 * self.cell_size, 5.7 * self.cell_size,
                                     21.8 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[0].place(x=3.8 * self.cell_size, y=19.4 * self.cell_size)
        self.canvas.create_rectangle(6 * self.cell_size, 19.3 * self.cell_size, 8 * self.cell_size,
                                     21.8 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[1].place(x=6.1 * self.cell_size, y=19.4 * self.cell_size)
        # Player 2, left up
        self.canvas.create_rectangle(3.7 * self.cell_size, 3 * self.cell_size, 5.7 * self.cell_size,
                                     5.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[2].place(x=3.8 * self.cell_size, y=3.1 * self.cell_size)
        self.canvas.create_rectangle(6 * self.cell_size, 3 * self.cell_size, 8 * self.cell_size, 5.5 * self.cell_size,
                                     fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[3].place(x=6.1 * self.cell_size, y=3.1 * self.cell_size)
        # Player 3, top
        self.canvas.create_rectangle(17.8 * self.cell_size, 0.5 * self.cell_size, 19.8 * self.cell_size,
                                     3 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[4].place(x=17.9 * self.cell_size, y=0.6 * self.cell_size)
        self.canvas.create_rectangle(20.1 * self.cell_size, 0.5 * self.cell_size, 22.1 * self.cell_size,
                                     3 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[5].place(x=20.2 * self.cell_size, y=0.6 * self.cell_size)
        # Player 4, right up
        self.canvas.create_rectangle(32 * self.cell_size, 3 * self.cell_size, 34 * self.cell_size, 5.5 * self.cell_size,
                                     fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[6].place(x=32.1 * self.cell_size, y=3.1 * self.cell_size)
        self.canvas.create_rectangle(34.3 * self.cell_size, 3 * self.cell_size, 36.3 * self.cell_size,
                                     5.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[7].place(x=34.4 * self.cell_size, y=3.1 * self.cell_size)
        # Player 5, right down
        self.canvas.create_rectangle(32 * self.cell_size, 19.3 * self.cell_size, 34 * self.cell_size,
                                     21.8 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[8].place(x=32.1 * self.cell_size, y=19.4 * self.cell_size)
        self.canvas.create_rectangle(34.3 * self.cell_size, 19.3 * self.cell_size, 36.3 * self.cell_size,
                                     21.8 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[9].place(x=34.4 * self.cell_size, y=19.4 * self.cell_size)
        # User, bottom
        self.canvas.create_rectangle(17.8 * self.cell_size, 21.9 * self.cell_size, 19.8 * self.cell_size,
                                     24.4 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[10].place(x=17.9 * self.cell_size, y=22 * self.cell_size)
        self.canvas.create_rectangle(20.1 * self.cell_size, 21.9 * self.cell_size, 22.1 * self.cell_size,
                                     24.4 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.all_player_cards[11].place(x=20.4 * self.cell_size, y=22 * self.cell_size)
        #community card
        self.canvas.create_rectangle(13 * self.cell_size, 10 * self.cell_size, 15 * self.cell_size,
                                     12.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.canvas.create_rectangle(16 * self.cell_size, 10 * self.cell_size, 18 * self.cell_size,
                                     12.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.canvas.create_rectangle(19 * self.cell_size, 10 * self.cell_size, 21 * self.cell_size,
                                     12.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.canvas.create_rectangle(22 * self.cell_size, 10 * self.cell_size, 24 * self.cell_size,
                                     12.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.canvas.create_rectangle(25 * self.cell_size, 10 * self.cell_size, 27 * self.cell_size,
                                     12.5 * self.cell_size, fill="#ffffff", outline="gray", width=2)
        self.community_display = [tk.Label(text="", font=('Times 23 bold'),fg="#000000") for i in range(5)]
        self.community_display[0].place(x=13.5 * self.cell_size, y=10.2 * self.cell_size)
        self.community_display[1].place(x=16.5 * self.cell_size, y=10.2 * self.cell_size)
        self.community_display[2].place(x=19.5 * self.cell_size, y=10.2 * self.cell_size)
        self.community_display[3].place(x=22.5 * self.cell_size, y=10.2 * self.cell_size)
        self.community_display[4].place(x=25.4 * self.cell_size, y=10.2 * self.cell_size)



    def Buttons(self):
        """Place action buttons on the table."""
        self.action_button = [tk.Button(self.master, text='Fold', width=9, height=2, command=lambda:self.handle_action("Fold")),
                       tk.Button(self.master, text='Check', width=9, height=2, command=lambda:self.handle_action("Check")),
                       tk.Button(self.master, text='Bet', width=9, height=2, command=lambda:self.handle_action("Bet"))]
        self.action_button[0].place(x= 14.5 * self.cell_size, y=16 * self.cell_size)
        self.action_button[1].place(x=18.5 * self.cell_size, y=16 * self.cell_size)
        self.action_button[2].place(x=22.5 * self.cell_size, y=16 * self.cell_size)
        self.disable_button()


    def disable_button(self):
        """Disable buttons when finishing a round."""
        for button in self.action_button:
            button["state"] = "disabled"


    def enable_button(self):
        """Disable buttons when starting a round."""
        for button in self.action_button:
            button['state'] = 'normal'


    def handle_action(self, action):
        """Handle action when click on button."""
        self.disable_button()
        self.round += 1
        if action == "Fold":
            self.round_player_class.pop()
            self.canvas.itemconfig(self.all_prof_pic[-1],fill="#cd9090")
            self.player_still_play = False
            self.continue_game()
        elif action == "Bet":
            self.handle_bet()
        elif action == "Check":
            self.continue_game()


    def continue_game(self):
        """Check which round is next and then continue the game."""
        self.clear_action()
        if self.round == 1:
            self.Round_1()
        elif self.round == 2:
            self.check_player_number()
        else:
            self.player_get_best_comb()
            self.Result()


    def handle_bet(self):
        """Handle bet amount."""
        self.money_buttons = [
            tk.Button(self.master, text='$1', width=9, height=2, command=lambda: self.handle_money(1)),
            tk.Button(self.master, text='$2', width=9, height=2, command=lambda: self.handle_money(2)),
            tk.Button(self.master, text='$3', width=9, height=2, command=lambda: self.handle_money(3))]
        if self.user_class.money >= 3:
            self.money_buttons[2].place(x=22.5 * self.cell_size, y=14.5 * self.cell_size)
        if self.user_class.money >= 2:
            self.money_buttons[1].place(x=18.5 * self.cell_size, y=14.5 * self.cell_size)
        if self.user_class.money >= 1:
            self.money_buttons[0].place(x=14.5 * self.cell_size, y=14.5 * self.cell_size)


    def handle_money(self, val):
        """Handle bet amount."""
        self.user_class.money -= val
        self.money_pool += val
        self.all_player_money[5].config(text=f"${self.user_class.money} ")
        for button in self.money_buttons:
            button.destroy()
        self.continue_game()


    def create_player_class(self):
        """Create 6 players' classes."""
        self.all_player_class = []
        for x in range(5):
            self.all_player_class.append(PlayerClass(name="Player" + str(x + 1)))
        self.user_class = PlayerClass(name=self.name+"6") #add an additional class for user
        self.all_player_class.append(self.user_class)


    def initialize(self):
        """Initialize a game."""
        self.count += 1
        self.round = 0
        self.hint_text.set(f"Game{self.count} Initialize ")
        self.reset_whole_game()
        self.clear_action()
        self.display_user_cards()
        self.smart_bot_init()
        self.enable_button()
        self.action_button[1]["state"] = "disabled"


    def clear_action(self):
        """Clear all players' actions"""
        for action in self.all_player_actions:
            action.config(text = "         ")


    def reset_whole_game(self):
        """Reset and initialize everything."""
        self.reset_deck_cards()
        self.reset_community_card()
        self.reset_in_hand_cards()
        self.each_round_player_class()
        self.prof_pic_back()
        self.money_pool = 0
        self.player_still_play = True
        self.has_monster = False


    def prof_pic_back(self):
        """Put the folded player's profile picture back."""
        for player in self.round_player_class:
            self.canvas.itemconfig(self.all_prof_pic[int(player.name[-1]) - 1], fill="#984f44")


    def reset_deck_cards(self):
        """Create a deck of cards."""
        self.deck_cards = []
        for x in range(1, 14):
            self.deck_cards.append("S" + str(x))
            self.deck_cards.append("H" + str(x))
            self.deck_cards.append("D" + str(x))
            self.deck_cards.append("C" + str(x))


    def reset_community_card(self):
        """Reset community cards."""
        self.community_card = [self.random_card(), self.random_card(), self.random_card()]
        self.update_player_communityCards()
        for com in self.community_display:
            com.config(text="   \n   ")


    def display_community_cards(self):
        """Display community cards."""
        self.community_display[0].config(
            text=f"{self.card_dict[self.community_card[0][0]]}\n{self.community_card[0][1:]}")
        self.community_display[1].config(
            text=f"{self.card_dict[self.community_card[1][0]]}\n{self.community_card[1][1:]}")
        self.community_display[2].config(
            text=f"{self.card_dict[self.community_card[2][0]]}\n{self.community_card[2][1:]}")
        self.community_display[3].config(text="   \n   ")
        self.community_display[4].config(text="   \n   ")


    def update_player_communityCards(self):
        """Update community card to player end."""
        for player in self.all_player_class:
            player.community_card = self.community_card


    def reset_in_hand_cards(self):
        """Initialize the two in-hand cards for each player."""
        for player in self.all_player_class:
            player.own_card = [self.random_card(), self.random_card()]
        for card in self.all_player_cards:
            card.config(text="   \n   ")


    def random_card(self):
        """Randomly generate cards."""
        self.chosen_card = random.choice(self.deck_cards)
        self.deck_cards.remove(self.chosen_card)
        return self.chosen_card


    def each_round_player_class(self):
        """Get the player class for each round, convenient for removing the plyaer who fold."""
        self.round_player_class = self.all_player_class[:]


    def display_user_cards(self):
        """Display only user's in-hand cards."""
        self.all_player_cards[10].config(text=f"{self.card_dict[self.user_class.own_card[0][0]]}\n{self.user_class.own_card[0][1:]}")
        self.all_player_cards[11].config(
            text=f"{self.card_dict[self.user_class.own_card[1][0]]}\n{self.user_class.own_card[1][1:]}")


    def display_all_cards(self):
        """Display all unfolded players' cards when one game ends."""
        for i in range(len(self.round_player_class)):
            card_index = 2 * (int(self.round_player_class[i].name[-1])-1)
            self.all_player_cards[card_index].config(text=f"{self.card_dict[self.round_player_class[i].own_card[0][0]]}\n{self.round_player_class[i].own_card[0][1:]}")
            self.all_player_cards[card_index+1].config(
                text=f"{self.card_dict[self.round_player_class[i].own_card[1][0]]}\n{self.round_player_class[i].own_card[1][1:]}")


    def Round_1(self):
        """Start Round 1."""
        self.display_community_cards()
        self.clear_action()
        self.hint_text.set(f"Game {self.count} Round 1")
        self.players_init_rank()
        self.smart_bot()
        if self.player_still_play == True:
            self.botton_modify()
        else:
            self.check_player_number()


    def players_init_rank(self):
        """Get players' ranks for the first round."""
        for player in self.round_player_class:
            player.get_init_rank()


    def smart_bot_init(self):
        """Get smart bots' initial round's action."""
        self.bad_card_player = 0
        self.player_num = len(self.round_player_class)
        for player in self.round_player_class[:-1]:
            self.hand_number = set([int(num[1:]) for num in player.own_card])
            self.judge = self.judge_init()
            if self.judge is None:
                self.bad_card_player += 1
                if self.bad_card_player < int(self.player_num/2) or self.has_monster == True:
                    self.all_player_actions[int(player.name[-1])-1].config(text="Fold   ")
                    self.canvas.itemconfig(self.all_prof_pic[int(player.name[-1])-1], fill="#cd9090")
                    self.round_player_class.remove(player)
                elif self.bad_card_player == int(self.player_num/2):
                    self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${self.bet}  ")
                    player.money -= self.bet
                    self.all_player_money[int(player.name[-1]) - 1].config(text=f"${player.money}  ")
                    self.money_pool += self.bet
                else:
                    self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${self.monster_money}  ")
                    player.money -= self.monster_money
                    self.all_player_money[int(player.name[-1]) - 1].config(text=f"${player.money}  ")
                    self.money_pool += self.monster_money

            else:
                self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${self.judge}  ")
                player.money -= self.judge
                self.all_player_money[int(player.name[-1]) - 1].config(text=f"${player.money}  ")
                self.money_pool += self.judge


    def judge_init(self):
        """Judge how much money should a smart bot bet depending on the card they have."""
        if self.hand_number in [{1}, {1, 13}, {13}, {12}]:
            self.has_monster = True
            return self.monster_money
        elif self.hand_number in [{11}, {10}, {9}, {1, 12}, {1, 11}, {1, 10}, {13, 12}]:
            return self.good_money
        elif len(self.hand_number) == 1 or ({1} in self.hand_number) or (
                (sorted(list(self.hand_number))[1] - sorted(list(self.hand_number))[0]) == 1):
            return self.decent_money
        else:
            return None


    def smart_bot(self):
        """Display bot user's action about fold, check or bet."""
        self.bad_rank_player = 0
        if self.user_class in self.round_player_class:
            bots = self.round_player_class[:-1]
        else:
            bots = self.round_player_class
        for player in bots: # except user, which is the last index
            if player.rank == self.threshold or player.money < 1:
                self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Check  ")
                self.bad_rank_player += 1
            elif player.rank > self.threshold:
                self.bad_rank_player += 1
                if self.bad_rank_player < len(self.round_player_class) - 1:
                    self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Fold   ")
                    self.canvas.itemconfig(self.all_prof_pic[int(player.name[-1]) - 1], fill="#cd9090")
                    self.round_player_class.remove(player)
                else:
                    if player.money >= 2 * self.bet:
                        self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${2*self.bet}  ")
                        player.money -= 2 * self.bet
                        self.money_pool += 2 * self.bet
                    else:
                        self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${player.money}  ")
                        self.money_pool += player.money
                        player.money = 0
            else:
                if player.rank >= 5:
                    self.should_bet = self.bet
                elif player.rank >= 3:
                    self.should_bet = 2 * self.bet
                elif player.rank >= 1:
                    self.should_bet = 3 * self.bet
                if player.money >= self.should_bet:
                    self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${self.should_bet}")
                    player.money -= self.should_bet
                    self.money_pool += self.should_bet
                else:
                    self.all_player_actions[int(player.name[-1]) - 1].config(text=f"Bet ${self.should_bet}")
                    self.money_pool += player.money
                    player.money = 0
            self.all_player_money[int(player.name[-1]) - 1].config(text=f"${player.money}")


    def check_player_number(self):
        """Check how many player left."""
        if len(self.round_player_class) == 1:
            self.win_name = self.round_player_class[0].name
            self.game_over()
        else:
            self.Round_2()


    def game_over(self):
        """Ask the user whether keep on playing."""
        if len(self.all_player_class) == 1:
            self.stats = f"{self.user_class.name[:-1]}\nYou have defeated ALL the bots!\nCongrats and we'll see you next time :)"
        elif self.user_class.money < 1:
            self.stats = f"{self.user_class.name[:-1]}\nSorry but you are broke :( \nGo earn some more money!"
        else:
            self.stats = f"{self.user_class.name[:-1]}\nYou still have some money left\ndo you want to play again? :)"
            self.yes_button = tk.Button(self.master, text='Yes', width=9, height=2, command=self.yes)
            self.yes_button.place(x=23 * self.cell_size, y=23 * self.cell_size)
            self.no_button = tk.Button(self.master, text='No', width=9, height=2, command=self.master.destroy)
            self.no_button.place(x=26 * self.cell_size, y=23 * self.cell_size)
        self.report = tk.Label(text=self.stats, font=('Times 15 bold'), bg="gray", fg="#ffffff")
        self.report.place(x = 23 * self.cell_size, y = 20.7 * self.cell_size)


    def yes(self):
        """Handle player's response if it's yes."""
        self.yes_button.destroy()
        self.no_button.destroy()
        self.report.destroy()
        self.initialize()


    def Round_2(self):
        """Start Round 2."""
        self.hint_text.set(f"Game{self.count} Round 2")
        self.update_community_card()
        self.smart_bot()
        if self.player_still_play == True:
            self.botton_modify()
        else:
            self.player_get_best_comb()
            self.Result()


    def botton_modify(self):
        """Change the state of the button to disable if player money is not enough to bet."""
        self.enable_button()
        if self.user_class.money < 1:
                self.action_button[2]["state"] = "disabled"


    def update_community_card(self):
        """Add two additional community cards during round 2."""
        self.community_card.append(self.random_card())
        self.community_card.append(self.random_card())
        self.community_display[3].config(
            text=f"{self.card_dict[self.community_card[3][0]]}\n{self.community_card[3][1:]}")
        self.community_display[4].config(
            text=f"{self.card_dict[self.community_card[4][0]]}\n{self.community_card[4][1:]}")
        self.update_player_communityCards()


    def player_get_best_comb(self):
        """Get the best combination card for each player."""
        for player in self.round_player_class:
            player.get_update_data()


    def Result(self):
        """Display results."""
        self.all_player_data_round2()
        self.final_summary()
        self.display_all_cards()
        self.check_if_broke()
        self.game_over()


    def check_if_broke(self):
        """Check if any of the players don't have any more money to bet for the next round."""
        self.length_class = len(self.all_player_class)
        for player in self.all_player_class[:-1]:
            if player.money < 1:
                self.canvas.itemconfig(self.all_player_prof[int(player.name[-1]) - 1], text="X")
                self.all_player_money[int(player.name[-1])-1].config(text ="broke")
                self.canvas.itemconfig(self.all_prof_pic[int(player.name[-1]) - 1], fill="#CCCCCC")
                self.all_player_class.remove(player)


    def all_player_data_round2(self):
        """Get all players' data after second round for the final comparison."""
        self.all_cards = []
        self.numbers = []
        self.ranks = []
        for player in self.round_player_class:
            self.all_cards.append(player.organized_card)
            self.numbers.append(player.number)
            self.ranks.append(player.rank)
        self.final_rankclass = RankClass(self.all_cards, self.all_cards, self.numbers, self.ranks)
        self.final_win_index = self.final_rankclass.get_win_index()


    def final_summary(self):
        """Display winner name and user's result."""
        self.hint_text.set(f"End of Game{self.count}")
        self.winner_class = [self.round_player_class[index] for index in self.final_win_index]
        self.winner = ",".join([win.name for win in self.winner_class])
        if self.user_class in self.winner_class :
            if len(self.winner_class) == 1:
                self.hint_text.set(f"Congrats!\nYou are the winner!")
            else:
                self.winner_class.remove(self.user_class)
                self.hint_text.set(f"Congrats, you win!\nAlong with {','.join([win.name for win in self.winner_class])}")
        elif self.user_class in self.round_player_class:
            self.hint_text.set(f"Sorry but you lost!\nWinner:{self.winner}")
        else:
            self.hint_text.set(f"You fold in this round.\nWinner:{self.winner}")
        for player in self.round_player_class:
            if player in self.winner_class:
                self.split_money = int(self.money_pool / len(self.winner_class)) #The money after the decimal point will be removed
                player.money += self.split_money
                self.all_player_money[int(player.name[-1]) - 1].config(text=f"${player.money}")


class PlayerClass:

    """A class for each player."""


    def __init__(self, name: str = '', own_card: list = [], community_card: list = [], money: int = 10, rank=None):
        self.name = name
        self.own_card = own_card
        self.community_card = community_card
        self.money = money
        self.rank = rank
        self.organized_card = None


    def get_init_rank(self):
        """Get the rank for the first round"""
        self.init_card = self.own_card + self.community_card
        self.init_rankclass = RankClass(cards=self.init_card)
        self.init_rankclass.OrganizeData()
        self.init_rankclass.only_numbers()
        self.rank = self.init_rankclass.card_rank()



    def get_update_data(self):
        """Get the rank for the second round and the best combination card to pass on to the comparison."""
        self.all_cards = self.own_card + self.community_card
        self.all_combinations = list(itertools.combinations(self.all_cards, 5))
        self.combination_rankclass = RankClass(cards=self.all_combinations)
        self.combination_rankclass.separate_cards_combinations()
        self.combination_rankclass.get_best_combination()
        self.organized_card = self.combination_rankclass.best_card
        self.number = self.combination_rankclass.best_number
        self.rank = self.combination_rankclass.best_rank



class RankClass:

    """A class to determine the rank for each player's cards."""


    def __init__(self, cards: list = [], organized: list = [], numbers: list = [], ranks: list = []):
        self.cards = cards
        self.card = cards
        self.organized = organized
        self.numbers = numbers
        self.ranks = ranks


    def OrganizeData(self):
        """Organize the cards by the order of the number on the cards for each player."""
        if len(self.card[0]) == 1:
            self.card = self.card[1:] #for file mode, when the first index in the list is the player's number
        for i in range(len(self.card)):
            if self.card[i][1:] == '1':
                self.card[i] = self.card[i][0] + '14'  # change 1 to 14 to make sort easier
        self.card.sort(key=lambda x: int(x[1:]))# sort by the number in the cards


    def only_numbers(self):
        """Get only the number of each player's card."""
        self.OnlyNum = []
        for each_card in self.card:
            self.OnlyNum.append(int(each_card[1:]))


    def separate_cards_combinations(self):
        """Separate each combination and put them in list to get the best combination."""
        self.organized = []
        self.numbers = []
        self.ranks = []
        for card in self.cards:
            self.card = list(card)
            self.OrganizeData()
            self.only_numbers()
            self.organized.append(self.card)
            self.numbers.append(self.OnlyNum)
            self.ranks.append(self.card_rank())


    def get_best_combination(self):
        """Get the best combination."""
        self.best_index = self.get_win_index()
        self.best_card = self.organized[self.best_index[0]]
        self.best_number = self.numbers[self.best_index[0]]
        self.best_rank = self.ranks[self.best_index[0]]  # though it's very unlikely to have two sets of cards share the same rank, but use list just to be safe


    def card_rank(self):
        """Get the rank of the current card."""
        self.max_frequency = self.OnlyNum.count(
            max(self.OnlyNum, key=self.OnlyNum.count))  # check the highest frequency of a card appeared
        self.min_frequency = self.OnlyNum.count(
            min(self.OnlyNum, key=self.OnlyNum.count))  # check the lowest frequency of a card appeared
        if self.check_if_flush():
            if set(self.OnlyNum) == {10, 11, 12, 13, 14}:
                # Royal flush
                return 0
            elif self.OnlyNum[-1] - self.OnlyNum[0] == 4:
                # Since the number is in order and there will not be two same numbers share the same suit so if the last - the first = 4 then it's a straight flush
                return 1
            else:
                # Flush
                return 4
        else:
            if self.max_frequency == 4:
                # if there are four cards that share the same number, then it's four of a kind
                return 2
            elif self.max_frequency == 3:
                # if there are three cards that share the same number
                if self.min_frequency == 2:
                    # and if the other two also has the same number, then it's full house
                    return 3
                else:
                    # if the other two has different numbers, it's three of a kind
                    return 6
            elif self.max_frequency == 1 and self.OnlyNum[-1] - self.OnlyNum[0] == 4:
                # if every number is different and the difference between the first and last card is 4, then it's straight
                return 5
            elif self.OnlyNum.count(self.OnlyNum[1]) == 2 and self.OnlyNum.count(self.OnlyNum[3]) == 2:
                # no matter how to format the card, the second and the forth card is always double. Such as [2,2,3,4,4], [2,2,3,3,4],[2,3,3,4,4]
                # so if the second and forth card is double, then it's two pairs
                return 7
            elif self.max_frequency == 2:
                # Pairs
                return 8
            else:
                # Highcard
                return 9


    def check_if_flush(self):
        """Check if all the cards have the same suit."""
        if self.card[0][0] == self.card[1][0] == self.card[2][0] == self.card[3][0] == self.card[4][0]:
            return True


    def get_win_index(self):
        """Determine who has the smallest rank and highest number to be the winner."""
        self.winRank = min(self.ranks)  # find the lowest rank (highest score)
        self.PW_nums = []
        if self.ranks.count(self.winRank) == 1:  # if there is only one winner rank, there is only 1 winner
            return [self.ranks.index(self.winRank)]
        else:  # [0,1,2]
            self.P_Winners = [i for i, x in enumerate(self.ranks) if
                              x == self.winRank]  # the potential winner indexes, since index + 1 is the player id, so this is a list to store ids
            for P_Winner in self.P_Winners:  # P_Winner is the index (which is also id -1) of each potential winner
                self.ReorderNum = self.numbers[P_Winner]
                self.ReorderNum.reverse()
                # if the card is [2,2,3,4,4], it will become [4,4,3,2,2]
                self.ReorderNum = sorted(self.ReorderNum, key=self.ReorderNum.count, reverse=True)
                # sort the number by their count, the example above will become [4,4,2,2,3]
                self.PW_nums.append(self.ReorderNum)
            for i in range(5):  # each player has 5 cards, so the index is 0-4
                self.each_card = [x[i] for x in self.PW_nums]
                # compare each set of card from the biggest to the smallest, based on the sorted order of ReorderNum (compare the largest count's number first and then single number)
                if self.each_card.count(
                        max(self.each_card)) == 1:  # if one person have the largest number, then that player id is the winner
                    self.winners = self.P_Winners[self.each_card.index(max(self.each_card))]
                    return [self.P_Winners[self.each_card.index(max(self.each_card))]]
                else:  # if there are multiple sets of cards share the same largest number, we need to compare their second largest number, etc.
                    self.remove_index = []
                    for i in range(len(self.each_card)):
                        if self.each_card[i] != max(self.each_card):
                            self.remove_index.append(i)
                    self.PW_nums = [self.PW_nums[i] for i in range(len(self.PW_nums)) if i not in self.remove_index]
                    self.P_Winners = [self.P_Winners[i] for i in range(len(self.P_Winners)) if
                                      i not in self.remove_index]
        # if there are multiple player/cards that has the same cards' numbers, then they are tied
        return [index for index in self.P_Winners]


if __name__ == "__main__":
    t = TableClass()
    t.master.mainloop()
