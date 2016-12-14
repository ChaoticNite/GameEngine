# GlobalConstants.py
# Thorin Schmidt
# 12/05/2016

'''project-wide constants'''

TITLE_FONT = ("Helvetica", 20, "bold")
HEADING1_FONT = ("Helvetica", 16, "bold")
TABLE_FONT = ("Arial", 14, "bold")
INSTRUCTION_FONT = ("Helvetica", 14, "bold")
SIMPLE_MESSAGE = "The user is asked which stat(str, dex, con, int, wis, cha) "+\
                "is most important, and which is least.  most important gets "+\
                "a value of 17, least gets a 9, and the rest get 12. This " +\
                "method is suitable for a 20-point character build using " +\
                "Pathfinder d20 rules.  This method has only a few choices, " +\
                "and results in moderate satisfaction for the user."
HARDCORE_MESSAGE = "Results are generated randomly using the 3d6 method, "+\
                   "in standard stat block sequence: (str, dex, con, int, "+\
                   "wis, cha). If none of the stats are over 12, then the "+\
                   "entire set is re-rolled until it does. The user has no "+\
                   "control over ability scores. This method is the "+\
                   "easiest, but usually has the least satisfaction for the "+\
                   "user."
FOUR_D_6_MESSAGE = "Keep best three, arrange to suit - 6 sets of 4d6 are "+\
                   "rolled, in each set, the top three dice are kept and "+\
                   "added together. Then these scores are assigned by the "+\
                   "user. This method usually has the highest satisfaction "+\
                   "for the player, but is also the most complicated, due "+\
                   "to the many choices required."
