from os import remove

import art
import random
def card_dealer():
    list_0f_card = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(list_0f_card)
    return card


def calc_card(lists_card):
    if sum(lists_card) == 21 and len(lists_card) == 2:
        return 0

    if 11 in lists_card and sum(lists_card) > 21:
        lists_card.remove(11)
        lists_card.append(1)

    return sum(lists_card)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "lose , opponent has blackjack"
    elif u_score == 0 :
        return "win has black jack"
    elif u_score > 21:
        return "lose went over 21"
    elif c_score> 21:
        return  "lose"
    elif u_score > c_score:
        return "user win"
    else:
        return "computer win"
def play_game():
    print(art.logo)
    player_list =[]
    computer_card =[]
    computer_score =-1
    user_score =-1
    for _ in range(2):
        new_card = card_dealer()
        player_list.append(new_card)
        computer_card.append(card_dealer())
    is_game_over = False


    while not is_game_over:
        user_score=calc_card(player_list)
        computer_score = calc_card(computer_card)

        print(f"{player_list},{user_score} ")
        print(computer_card[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_sh = input("type y to take another card n not").lower()
            if user_sh == 'y':
                player_list.append(card_dealer())
            else:
                is_game_over = True

    while computer_score!= 0 and computer_score >17:
        computer_card.append(card_dealer())
        computer_score = calc_card(computer_card)
    print(compare(user_score,computer_score))

while input(" WANT NEW GAME Y \ N ") == "y":
    print("\n" * 20)
    play_game()