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
    pc_choice = random.choice(rps_list)
    player_choice = input("Choose rock paper or scissors")
    if player_choice not in rps_list:
        print("Please type rock paper or scissors")
        rps_game()
    if player_choice == pc_choice:
        print(f"{player_choice} vs {pc_choice}, it's a draw!")
    if rps_list[player_choice] == rps_list[pc_choice] + 1:
        print(f"{player_choice} vs {pc_choice}, you won!")
    elif rps_list[pc_choice] == rps_list[player_choice] + 1:
        print(f"{player_choice} vs {pc_choice}, you lost!")
