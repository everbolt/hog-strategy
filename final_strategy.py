#coding=utf8
PLAYER_NAME='computer go brrrr'
m=[]
def final_strategy(s,o):
 global m
 w="""ABBGÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎÎ}BBLBBBBBBBBBBBBBBBnnnnnnABBu-BBBBBBBBBBBBBBBBBBBB}Ai8-MMMcccccccwnnnnnnnkM68s8#¿%!{fnØnnnnnnnnnnnØf677j-?{-?!A777BBnnnnnnnnn67}Ø#<$#?!$#7778BBBnnnnnjbcc7_B!#t!jni778BBCnnnnnjÏ,,,,,,,,,,,,,,,,,,,rrnnnÏ-}7\"77-777}i777777siinnnÒ/~L-.B~BLBBØnnnBBMMMunnnÒ/{$-@h$LØLknjnnnnnnnnnnnÒ/{!-?Ø-<nØnnqØnnnnnnnnnnÒ/{!-@,(BuntnnqnnnnnnnnnnÒ/|!++,;LOËØnnrnnnnnnnnnnÒ/}7-B7,BOO;cÏÁcnnnnnnnnnÒ/~C#CBLVE}`BECÁ1cccnnnnmÒ/~B-CBB<aEC~BEccccccccccÒ/~B-LJMBÁMFMMOccccccccccÒ/{B-BL-CNZXGRÀccccccccccÒ/~8-CBLBL}DWÊÀNXXcYccccbÒ/}L-AALCM:MMGMMM¿MMNXXXXÒ/}A-L9KAMBMM¿MMMMNXXNXMNÒ/}8-BBB98B2MMM¿MMMMMMMMMÒ/}8-BABAL9MxMFMMMMMMMMMMÒ/~8-BBBBLA}9dMMMMMMMMMMMÒ/}7-B8BBCB9MØMMM¿MMMMMMMÒ/}8-BLBBK~BB8kMMMMMMMMMMÒ/~8-BB-8B8B~BtC¿MMLMMMMLÒ/~B-BBBLBBx8B8aCM¿MCCBBBÒ/~7-BBABB87889<M<BBBBBBBÒ/~A-A78B7A7K777ZBBBBBBBBÒ/~7-777-7777777:777~8A77Ò/{7-A7-AK777-777U7777777Ò/{--A,,@677777-7:7}77777Ò/{,-|,,|,,|-,|77}K77}776Ò,{,-|,,,,,,,,,,,,(6(776,Ò/{+-|,,,,,,,,,,,,,F,,,,,Ò+{!-|\",,,,,,,,,,,,.,,,|,Ò/{!+{!+!!!!!!!!\"\",\"@,,,,Ò/{!+!!!!!!!!!!!!!!!#!{!!Ò/Ï!+{!!!!!!!!!!!!!!!5!!{Ò+{!+{!!{!!{!!{!!{!!{Ö!x!~/{{+{{Î{{!{{!{{!{{!{{({z~*{zÎzzÎzzÎzzÎzzÎzzÎzzÏ{z{/xz*xzÎxzÎxzÎxzÎxzÎxzÎxz{¿xzzxzzxzzxzzxzzxzzxzzxz{¿xzzxzyxzyxzzxzzxyyxyzxyyxxyxxyxxyxxyxxyxxyxxyxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""
 if len(m)==0:
  for b in w:
   b,f,s=ord(b),0,10
   if b>190:b-=64
   if b<100:f,s=b//10,b%10
   elif b<111:f,s=10,b%100
   elif b<120:f,s=b%10,10
   elif b<152:f,s=b//10-12,b%10
   m+=[f,s]
 return m[min(s,49)*50+min(o,49)]