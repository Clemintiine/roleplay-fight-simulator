import random

def group_fight(group_1, group_2):
    # Sum group stats
    group1_strength = sum(c['fighting'] + c['stamina'] for c in group_1)
    group2_strength = sum(c['fighting'] + c['stamina'] for c in group_2)

    # Agility and size
    group1_agility = sum(c['agility'] for c in group_1)
    group2_agility = sum(c['agility'] for c in group_2)

    # Compare overall group power
    if group1_strength + group1_agility > group2_strength + group2_agility:
        return "Group 1 wins with minor injuries."
    elif group1_strength + group1_agility < group2_strength + group2_agility:
        return "Group 2 wins, with Group 1 suffering casualties."
    else:
        return "The fight ends in a draw with significant injuries on both sides."
