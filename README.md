# codetable
This is my repository for a codetable class that manages information about lower bounds and constructions of linear codes. It uses Sagemath's coding theory module.

# current functionality
These methods search for linear codes with optimal linear distance. First add some sage codes to the codetable. Next the methods look for optimal codes obtained through: shortenings, lengthenings, truncations, juxtaposition and (u|u+v) construction of the input. The best attained distance is stored in a dict. It also stores a human readable log of the construction for each length and dimension [n,k].

Please see instructions.py for a demonstration of how to use this class.


