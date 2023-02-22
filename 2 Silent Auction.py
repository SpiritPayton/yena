"""Program to run a silent auction
"""

user_bids = {}
bidding_end = False


def high_bidder(bidding_log):
    high_bid = 0
    won = ""
    for bidder in bidding_log:
        user_bids = bidding_log[bidder]
        if user_bids > high_bid:
            high_bid = user_bids
            won = bidder
    print("------------------------------------------------------")
    print(f"the highest bidder is {won} with a bid of ${high_bid}!!!!!")


while not bidding_end:
    print("welcome to Lady Ningguang's silent auction!! today we are bidding on the Jade Chamber.")
    name = input("GIVE ME your name!!!: ")
    bid = int(input("how much would you like to bid?\n> $"))
    user_bids[name] = bid
    add_bidders = input("any other bidders, y or n?!?!?!?: ").lower()
    if add_bidders == "n":
        bidding_finished = True
        high_bidder(user_bids)
        break
    elif add_bidders == "y":

