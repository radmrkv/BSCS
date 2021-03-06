# BSCS: Blood Sword Combat Simulator
This is a simple utility that semi-automates combat encounters for the [Blood Sword gamebooks](https://en.wikipedia.org/wiki/Blood_Sword_(gamebook_series)).


## Features
* Attack roll simulation; weapon attacks and blasting spells
* Different attacks with different attack dice and damage outputs (e.g. the Sage's Quarterstaff Technique)
* Battlefields: sets of actors (players or enemies) that facilitate simple attacking logic
* Maintaining actor states across rounds (HP tracking)
* Custom statement logging (useful for leaving yourself notes)
* All spells supported (blasting & psychic)
* Perks and status effects can be added or removed manually at any time.

## TODO:
* Track turns and initiative orders, plus automatic adding and removal of effects like Nighthowl)
* An "undo" function?
* Pretty "help" screen that lists commands and aliases -- right now it's there but not informative
* Tab-completion when selecting attacks or filling in actor names.