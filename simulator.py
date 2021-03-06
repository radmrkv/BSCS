from util import *


##############################################################################################################
# Arguments have names listed to make it easier to remember. It's also more cluttered, but what can you do...
warrior = Actor("Sir Richard", fpr=9, awa=7, psy=6, armour=4, end=43, damage="3d6", attacks=[
    Attack("the Blood Sword", damage="5d6", fpr_bonus=3),
    Attack("his crossbow", damage="1d6"),
], perks=[
    Perk("Styx-touched", invulnerability_threshold=6),
    Perk("Myorg's Blessing", weapon_damage="1"),
    # Perk("Ankh of Life", resist_all=True),
])
trickster = Actor("Trickster", fpr=7, awa=9, psy=7, armour=3, end=43, damage="2d6+2", attacks=[
    Attack("his sword", damage="2d6+2"),
    Attack("his magic bow", damage="1d6", fpr_bonus=1),
    Attack("his magic bow and magic arrows", damage="1d6+3", fpr_bonus=1),
], perks=[
    Perk("Danger Sense", extra_dodge="1d6", fpr=1),
    #Perk("Dissembler", fpr=-1, awa=-1), 
    # Perk("Ankh of Life", resist_all=True),
])
sage = Actor("Mentok", fpr=9, awa=8, psy=9, armour=5, end=46, damage="2d6+2", attacks=[
    Attack("the Staff of Might", damage="2d6+3", fpr_bonus=1),
    Attack("his bow", to_hit="2d6", damage="1d6", attack_type="Weapon"),
    Attack("Quarterstaff Technique", to_hit="2d8", damage="3d6+3", fpr_bonus=1),
    Attack("Volcano Spray", to_hit="2d6", damage="1d6", target_value=10, attack_type="Blasting"), # From the Staff of Might
], perks=[
    #Perk("Dissembler", fpr=-1, awa=-1), 
    Perk("Styx-touched", invulnerability_threshold=6),
    # Perk("Ankh of Life", resist_all=True),
])
enchanter = Actor("Enchanter", fpr=4, awa=7, psy=12, armour=2, end=35, damage="2d6+1", attacks=[
    Attack("his sword"),
    Attack("Swordthrust", to_hit="1d6", damage="3d6+3", attack_type="Blasting", spell_level=2),
    Attack("Nemesis Bolt", "1d6", "7d6+7", "Blasting", 5),
    Attack("Sheet Lightning", "1d6", "2d6+2", "Blasting", 4),
], perks=[
    #Perk("Dissembler", fpr=-1, awa=-1), 
    Perk("Prepared Spells", psy=-1),  # Remember to update the number of prepared spells here!
    # Perk("Ankh of Life", resist_all=True),
])


battlefield = Battlefield([
    warrior, trickster, sage, enchanter,
    
    Actor("Karunaz", fpr=13, awa=11, psy=10, armour=0, end=100, damage="9d6"),
    Actor("Phantasm", fpr=8, awa=7, psy=7, armour=3, end=30, damage="3d6"),
    
    
    # Actor("Susurrien", fpr=8, awa=9, psy=10, armour=0, end=80, damage="4d6"),

    # Icon in Demon's Claw
    # Actor("Icon", fpr=9, awa=9, psy=9, armour=2, end=55, damage="5d6", attacks=[
        # Attack("his sword"),
        # Attack("Retributive Fire", to_hit="0", damage="1", attack_type="GuaranteedIgnoreArmour"),
    # ]),
    
    # Icon in Doomwalk
    # Actor("Icon", fpr=9, awa=9, psy=9, armour=0, end=55, damage="5d6", attacks=[
        # Attack("his sword"),
    # ], perks=[
        # Perk("Prepared Spells", psy=-1),
    # ]),
    
    Actor("Magus Tor", fpr=12, awa=12, psy=8, armour=3, end=100, damage="8d6", attacks=[
        Attack("a melee attack", to_hit="2d6", damage="8d6"),
        Attack("Mirage-Bolt", to_hit="1", damage="7d6", attack_type="Blasting"),
    ]),
    


])


##############################################################################################################


print("")
print("BLOOD SWORD COMBAT SIMULATOR")
print("(created by Lumos, 2018)")
print("Edit the script file to set up your battlefield with greater ease.")
battlefield.status()

# trickster.attack(warrior, "dagg")

interpreter = Interpreter()
interpreter.cmdloop()
