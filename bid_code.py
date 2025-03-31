import  pic_logo
print(pic_logo.LOGO)


bid_detail ={}
def bid_user(bid_name,bid_value):
    bid_detail[name]=bid_value

def highest_bidder(bid_dict):
    highest_bid =0
    winner=''
    for bidder in bid_dict:
        bid_value =bid_dict[bidder]
        if bid_value > highest_bid:
            highest_bid=bid_value
            winner= bidder

    print(f"Winner of biding is {winner} and amount bid {highest_bid} ")


bid_continue = True
while bid_continue:
    name = input("Enter the name...")
    bid_amount =int(input("bid amount "))
    bid_user(bid_name=name, bid_value=bid_amount)


    bid_continue = input("Anyone want to bid..(y/n)")
    if bid_continue =='n':
        bid_continue =False
        highest_bidder(bid_detail )
    elif bid_continue =="y":
        print("\n" *25)









