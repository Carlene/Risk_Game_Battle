
# coding: utf-8

# In[46]:


import random


# In[47]:


def welcome_screen():
    '''
    ASCII tank! http://www.ascii-art.de/ascii/t/tank.txt

    '''
    
    print("Welcome to Risk!")
    print("    .--._____,")
    print(" .-='=='==-, \"")
    print("(O_o_o_o_o_O) fsc")
    print("")


# In[64]:


def user_inputs(text):
    '''
    Forcing user input to be an integer and checking the values
    
    Arguments
    Text: Text that will be printed with the user input
    
    Outputs
    Units: the amount of units the player inputs
    '''
    while True:
        try:
            print(text)
            units = int(input())
        except ValueError:
            print("Please enter an integer.")
        else:
            return units


# In[62]:


def risk_start():
    '''
    Welcomes the players to the game and takes their unit counts.
    
    Outputs:
    attacking_units: number of attacking units
    defending_units: number of defending units
    units_willing_to_lose: number of units the attacker is willing to lose before they call off the attack 
                           (units_willing_to_lose must be less than or equal to attacking_units)
    '''
    #tank!
    welcome_screen()
    
    #user inputs for their starting amounts of units
    
    attacking_units = user_inputs("Enter the amount of attacking units: ")
    defending_units = user_inputs("Enter the amount of defending units: ")
    units_willing_to_lose = user_inputs("Enter the amount of units the attacker is willing to lose: ")
    
    return (attacking_units, defending_units, units_willing_to_lose)


# In[21]:


def roll_dice(units):
    '''
    Generates multiple dice rolls.
    
    Arguments
    Units: Amount of units in play
    
    Outputs
    Rolls: List of all rolls
    '''
    rolls = []
    
    for roll in range(units):
        #picking a random number from 1 - 6 for a die roll
        roll = random.randint(1,6)
        rolls.append(roll)
    return rolls


# In[22]:


def check_attacker_units(attacking_units):
    '''
    Checks how many dice the attacker will get for the battle
    
    Arguments
    attacking_units: Amount of attacking units in play
    
    Outputs 
    Amount of dice the attacker gains
    '''
    
    if attacking_units >= 3: 
        return roll_dice(3)
    elif attacking_units == 2: 
        return roll_dice(2)
    elif attacking_units == 1: 
        return roll_dice(1)
    else:
        return []


# In[23]:


def check_defender_units(defending_units):
    '''
    Checks how many dice the defender will get for the battle
    
    Arguments
    defending_units: Amount of defending units in play
    
    Outputs 
    Amount of dice the defender gains
    '''
    if defending_units >= 2: 
        return roll_dice(2)
    elif defending_units == 1: 
        return roll_dice(1)
    else:
        return []


# In[24]:


def risk_battle(attacking_units, defending_units):
    '''
    Simulates one "battle" of Risk. 
    (Battle is being used very loosely to mean one roll of x amount of dice from the attacker and the defender)
    
    Arguments
    attacking_units: number of attacking units
    defending_units: number of defending units
    
    Outputs:
    attacking_units: how many attacking units remain after the battle
    defending_units: how many defending units remain after the battle
    '''

# giving the attacker and defender the correct amount of dice per units they have
    attacker_dice = check_attacker_units(attacking_units)
    defender_dice = check_defender_units(defending_units)
    
            
#checking to see if both players have any dice     
    while len(attacker_dice) > 0 and len(defender_dice) > 0:
        # grabbing the highest roll from each player
        highest_attacker_roll = max(attacker_dice)
        highest_defender_roll = max(defender_dice)

#comparing the highest rolls of the attacker and defender, subtracting a unit from whichever side has the lower roll 
        if highest_defender_roll >= highest_attacker_roll:
            attacking_units -= 1
            defender_dice.remove(highest_defender_roll)
            attacker_dice.remove(highest_attacker_roll)
        else:
            defending_units -= 1
            attacker_dice.remove(highest_attacker_roll)
            defender_dice.remove(highest_defender_roll)
            
    return (attacking_units, defending_units)


# In[25]:


def results_of_risk_battle(attacking_units, defending_units):
    '''
    Prints current unit counts of attacker and defender
    
    Arguments
    attacking_units: number of attacking units
    defending_units: number of defending units
    '''
    
    print("")
    print(f"Attacker has {attacking_units} remaining units, Defender has {defending_units} remaining units!")
    print("")


# In[26]:


def attacker_gives_up():
    '''
    Checks to see if the attacker wants to continue the game
    
    Outputs:
    True or False
    '''
    
    give_up = input("Do you want to stop attacking? Y or N? ")
    give_up = give_up.upper()
    
    if give_up == "Y":
        return True
    elif give_up == "N":
        return False
    else:
        print("Please type Y for Yes or N for No.")
        attacker_gives_up()


# In[27]:


def attacker_wins(a_units):
    '''
    Win Screen for the Attacker
    
    Inputs: Amount of attacking units
    '''
    
    print("      /| ________________   ")
    print("O|===|* >________________>  ")
    print("      \|                    ")
    print("                            ") 
    print(f"The Attacker has won the game with {a_units} remaining units!")


# In[28]:


def defender_wins(d_units):
    '''
    Win Screen for the Defender
    
    Inputs: Amount of defending units
    '''
    
    print("     _..._     ")
    print(" .-'_.---._'-. ")
    print(" ||####|(__)|| ")
    print(" ((####|(**))) ")
    print("  '\###|_''/'  ")
    print("   \\()|##//   ")
    print("    \\ |#//    ")
    print("     .\_/.     ")
    print("      L.J      ")
    print("       \"      ")
    print(f"The Defender has successfully defended with {d_units} remaining units!")


# In[29]:


def risk_game():
    '''
    Simulates multiple "battles" in Risk and returns the overall winner.
    
    Outputs 
    Amount of dice the attacker gains
    '''
    
    start = risk_start()
    
    attacking_units = start[0]
    defending_units = start[1]
    units_willing_to_lose = start[2]
    remaining_attacker_units = attacking_units - units_willing_to_lose

    #checking if attacker hasn't lost more than they were willing to and that the defender has units left
    while attacking_units > remaining_attacker_units and defending_units != 0:
        battle = risk_battle(attacking_units, defending_units)
        
        #current units for attacker and defender after one "battle"
        attacking_units = battle[0]
        defending_units = battle[1]
        
        results_of_risk_battle(attacking_units, defending_units)
        
        if attacker_gives_up():
            return defender_wins(defending_units)
        
    if defending_units == 0:
        return attacker_wins(attacking_units)
    else:
        return defender_wins(defending_units)


# In[65]:


risk_game()

