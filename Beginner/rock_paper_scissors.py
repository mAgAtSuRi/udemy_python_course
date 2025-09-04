import random

rps_list = ["rock", "paper", "scissors"]
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def rps_game():
    while True:
        pc_choice = random.choice(rps_list)
        player_choice = input("Choose rock paper or scissors\n")

        while player_choice not in rps_list:
            player_choice = input("Please type rock, paper, or scissors:\n")

        ascii_art = {"rock": rock, "paper": paper, "scissors": scissors}
        print(ascii_art[player_choice])
        print("VS")
        print(ascii_art[pc_choice])


        if (rps_list.index(player_choice) - rps_list.index(pc_choice)) % 3 == 1:
            print(f"{player_choice} vs {pc_choice}, you won!")
        elif (rps_list.index(pc_choice) - rps_list.index(player_choice)) % 3 == 1:
            print(f"{player_choice} vs {pc_choice}, you lost!")
        else:
            print(f"{player_choice} vs {pc_choice}, it's a draw!")

rps_game()