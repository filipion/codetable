# codetable
This is my repository for a codetable class that manages information about lower bounds and constructions of linear codes. It uses Sagemath's coding theory module.

# current functionality
These methods search for linear codes with optimal linear distance. First add some sage codes to the codetable. Next the methods look for optimal codes obtained through: shortenings, lengthenings, truncations, juxtaposition and (u|u+v) construction of the input. The best attained distance is stored in a dict. It also stores a human readable log of the construction for each length and dimension [n,k].

# instructions
Here is how it works so far. To start, pick a maximum length of codes you are considering and the base field (GF(2) is the default choice)

sage: TT = code_table(127,GF(2))

Use add() to let the table know about new constructions you have. For example to add sage BCHcodes of lengths 1,3,7,15,31,63,127:

sage:for pow in range(1,8):
         for designed_distance in range(1,2^pow):
             E = codes.BCHCode(GF(2),2^pow-1,designed_distance)
             TT.add(E,designed_distance)

add() does truncations and shortenings automatically. So now if you have a [15,5,7] BCH code you obtain:

sage:TT.lower_bounds[(15,5)] 
7
sage:TT.lower_bounds[(14,4)] 
7                           (from shortening)

Lastly, two more methods can be called to get the table to calculate combinations of more codes (juxtapose, u|u+v):

for r in range (1,127):
    TT.plotkin_update(r)
    
for k in range(1,127):
    TT.juxtapose_update(k)
(this part could take about a minute to execute as it is a little brute forcey)
    
After all this you are done and you can view the dicts:

sage: TT.lower_bounds[(42,13)]
10
sage: print TT._construction[(42,13)]
Truncation of
12 Plotkin sum of [22,10,6] and [22,3,12]     _ 

This tells you that to build a 42,13,10 code use u|u+v for those two codes. This produces a 44,13,12 code and truncation then produces a 42,13,10 code.


