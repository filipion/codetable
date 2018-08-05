#Here is how it works so far. To start, pick a maximum length of codes you are considering and the base field (GF(2) is the default choice)

TT = code_table(127,GF(2))


#Use add() to let the table know about new constructions you have. For example to add sage BCHcodes of lengths 1,3,7,15,31,63,127:

for pow in range(1,8):
     for designed_distance in range(1,2^pow):
         E = codes.BCHCode(GF(2),2^pow-1,designed_distance)
         TT.add(E,designed_distance)

#add() does truncations and shortenings automatically. So now if you have a [15,5,7] BCH code you obtain:

TT.lower_bounds[(15,5)] 
#7
TT.lower_bounds[(14,4)] 
#7(from shortening)


#Lastly, two more methods can be called to get the table to calculate combinations of more codes (juxtapose, u|u+v):

for r in range (1,127):
    TT.plotkin_update(r)
    
for k in range(1,127):
    TT.juxtapose_update(k)
    
#(this part could take about a minute to execute as it depends on some brute force)


#After all this you are done and you can view the dicts:

TT.lower_bounds[(42,13)]
#10
print TT._construction[(42,13)]
#Truncation of
#12 Plotkin sum of [22,10,6] and [22,3,12]     _ 

#This tells you that to build a 42,13,10 code use u|u+v for those two codes. This produces a 44,13,12 code and truncation then produces a 42,13,10 code.
