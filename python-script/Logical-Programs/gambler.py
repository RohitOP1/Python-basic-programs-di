import random

def gambler_simulation(stake, goal, trials):
    """
    Simulates a gambler playing until they reach the goal or go broke.
    
    Args:
        stake (int): Starting amount of money.
        goal (int): Target amount of money to win.
        trials (int): Number of times to run the simulation.
    
    Returns:
        tuple: (win_count, avg_bets) - number of wins and average bets per game.
    """
    win_count = 0
    total_bets = 0
    
    for _ in range(trials):
        money = stake
        bets = 0
        while money > 0 and money < goal:
            if random.random() < 0.5:  # 50% chance of winning
                money += 1
            else:
                money -= 1
            bets += 1
        
        if money == goal:
            win_count += 1
        total_bets += bets
    
    avg_bets = total_bets / trials
    return win_count, avg_bets

# Taking user input
stake = int(input("Enter your starting stake: "))
goal = int(input("Enter your goal amount: "))
trials = int(input("Enter the number of trials: "))

# Running the simulation
wins, avg_bets = gambler_simulation(stake, goal, trials)

# Displaying results
print(f"\nNumber of wins: {wins}")
print(f"Average bets per game: {avg_bets:.2f}")
print(f"Win percentage: { (wins / trials) * 100:.2f}%")
