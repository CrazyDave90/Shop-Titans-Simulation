from random import randint;

# This script will run 100,000 simulations of a dungeon
# and calculate an estimated win percentage based on your
# hero's stats and enemy's stats entered below.

# Hero Information.
# Currently, this only supports Dancers.
# Instead of defense, you must enter the amount of damage
# your hero takes on a normal attack and a critical attack
# under Enemy Information. Furthermore, this only takes into
# consideration the number of lizard spirits you have. Other
# spirits which have special effects are not currently supported.

hero_max_hp = 503;
hero_attack = 8346;
hero_evasion = 75;
hero_crit_chance = 20;
hero_crit_modifier = 4;
lizard_spirits = 6;

# Enemy Information.
# By default, this is for Haunted Castle Hard. Adjust the
# enemy's damage based on your hero's defense stat. To find this,
# enter a battle and see how much damage they take.

enemy_crit_rate = 10;
enemy_normal_damage = 59;
enemy_crit_damage = 177;
enemy_max_hp = 250000;

# Next, we simulate 100,000 battles and compute the win percentage.

wins = 0;
for battle in range(100000):
    current_hero_hp = hero_max_hp;
    current_enemy_hp = enemy_max_hp;

    while True:

        # Enemy's Turn. We first roll to see if the enemy lands a
        # critical hit, and then roll to see if the hero dodges
        # the attack. We then reduce the hero's current HP by this
        # amount and check if the hero is dead.
        
        if (randint(1,100) <= enemy_crit_rate):
            enemy_critical_hit = True;
        else:
            enemy_critical_hit = False;

        if (randint(1,100) <= hero_evasion):
            hero_dodge = True;
        else:
            hero_dodge = False;

        if (hero_dodge == False):
            if (enemy_critical_hit == True):
                current_hero_hp = current_hero_hp - enemy_crit_damage;
            else:
                current_hero_hp = current_hero_hp - enemy_normal_damage;

        if (current_hero_hp <= 0):
            break; # This ends the battle without adding a win.

        # Hero's Turn. We roll to see if the hero lands a critical hit.
        # If the hero dodged the last attack, the hero will automatically
        # land a critical hit even if the roll fails. We then reduce the
        # enemy's current HP by the hero's attack, which is multiplied
        # by the hero's critical hit modifier if the hero lands a critical
        # hit, and check if the enemy is dead.

        if (hero_dodge == True or randint(1,100) <= hero_crit_chance):
            current_enemy_hp = current_enemy_hp - hero_attack*hero_crit_modifier;
        else:
            current_enemy_hp = current_enemy_hp - hero_attack;

        if (current_enemy_hp <= 0):
            wins = wins + 1;
            break; # This ends the battle while adding a win.

        # Between rounds, the lizard spirits will recover the hero's hp.
        # This cannot recover more than the hero's maximum hp.
        
        current_hero_hp = min(hero_max_hp, current_hero_hp + 3*lizard_spirits);

        # This round of combat ends, and a new round begins.

print("Estimated win percentage: " + str(wins/100000*100) + "%");
