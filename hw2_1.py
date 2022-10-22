class VotingMachine:

    def __init__(self, orange_vote, purple_vote, yellow_vote):
        self.orange_vote = orange_vote
        self.purple_vote = purple_vote
        self.yellow_vote = yellow_vote
    
    def reset(self):
        self.orange_vote = 0
        self.purple_vote = 0
        self.yellow_vote = 0
    
    def voteOrange(self):
        self.orange_vote += 1
    
    def votePurple(self):
        self.purple_vote += 1
    
    def voteYellow(self):
        self.yellow_vote += 1
    
    def getVotes(self):
        votes_display = [self.orange_vote, self.purple_vote, self.yellow_vote]
        return tuple(votes_display)
    
obj = VotingMachine(0,0,0)


b = True
while b:
    print("----------- Election Voting Machine -----------")
    print("Please Select one of the below options to vote:")
    print("Option 1 - Orange Party")
    print("Option 2 - Purple Party")
    print("Option 3 - Yellow Party")
    print("Option 4 - Display votes")
    print("Option 5 - Reset Votes")
    print("Option 6 - Exit")
    print("Please type in 1, 2, 3, 4, 5 or 6 as per your choice to vote: ")
    choice = int(input("Please enter the option to vote:"))
    if choice == 1:
        obj.voteOrange()
    elif choice == 2:
        obj.votePurple()
    elif choice == 3:
        obj.voteYellow()
    elif choice == 4:
        display = obj.getVotes()
        print("Votes to Orange Party - ",display[0])
        print("Votes to Purple Party - ",display[1])
        print("Votes to Yellow Party - ",display[2])
    elif choice == 5:
        obj.reset()
        print('Votes Reseted')
        print(obj.getVotes())
    elif choice == 6:
        confirm = input("Are you sure you want to exit?, please type 'y' to exit else 'n' to continue: ").lower()
        if confirm == 'y':
            print("Thank You")
            print("Final Votes - ")
            display = obj.getVotes()
            print("Votes to Orange Party - ",display[0])
            print("Votes to Purple Party - ",display[1])
            print("Votes to Yellow Party - ",display[2])
            b = False
            break
        else:
            continue
    else:
        print("Choice number is wrong, please enter your option to vote again - ")
        continue