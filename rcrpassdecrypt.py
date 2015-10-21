#!/usr/bin/env python

# River City Ransom password decoder
# v0.0 - 09.10.2004
# author: Jerry McMahan Jr. (jerry@ensomnya.net)
#
# This program is freely redistributable and freely modifyable, provided
# any derivative works are also made freely redistributable and 
# freely modifyable.

import cgi, cgitb, string

def bcd2dec(num):
	""" converts BCD to decimal"""
	return (num / 16)*10 + num % 16

def dec2bcd(num):
    """converts decimal to BCD"""
    return num % 10 + (num/10)*16

keystring = (13,  5, 24,  7, 11, 17, 29, 16, 21, 19, 23, 
              9, 15, 25, 31, 12, 20,  5,  3, 22,  6, 12, 
	     18,  7, 10, 11, 27, 18, 14, 13, 12, 24, 17)

textval_reverse = {
255:"B'",
254:"A'",
253:"9",
252:"8",
251:"7",
250:"6",
249:"5",
248:"4",
247:"3",
246:"2",
245:"1",
244:"0",
243:"z",
242:"y",
241:"x",
240:"w",
239:"v",
238:"u",
237:"t",
236:"s",
235:"r",
234:"q",
233:"p",
232:"o",
231:"n",
230:"m",
229:"l",
228:"k",
227:"j",
226:"i",
225:"h",
224:"g",
223:"f",
222:"e",
221:"d",
220:"c",
219:"b",
218:"a",
217:"Z",
216:"Y",
215:"X",
214:"W",
213:"V",
212:"U",
211:"T",
210:"S",
209:"R",
208:"Q",
207:"P",
206:"O",
205:"N",
204:"M",
203:"L",
202:"K",
201:"J",
200:"I",
199:"H",
198:"G",
197:"F",
196:"E",
195:"D",
194:"C",
193:"B",
192:"A" }


textval = {
"B'":255,
"#":255, # same as B'
"A'":254,
"@":254, # same as A'
"9":253,
"8":252,
"7":251,
"6":250,
"5":249,
"4":248,
"3":247,
"2":246,
"1":245,
"0":244,
"z":243,
"y":242,
"x":241,
"w":240,
"v":239,
"u":238,
"t":237,
"s":236,
"r":235,
"q":234,
"p":233,
"o":232,
"n":231,
"m":230,
"l":229,
"k":228,
"j":227,
"i":226,
"h":225,
"g":224,
"f":223,
"e":222,
"d":221,
"c":220,
"b":219,
"a":218,
"Z":217,
"Y":216,
"X":215,
"W":214,
"V":213,
"U":212,
"T":211,
"S":210,
"R":209,
"Q":208,
"P":207,
"O":206,
"N":205,
"M":204,
"L":203,
"K":202,
"J":201,
"I":200,
"H":199,
"G":198,
"F":197,
"E":196,
"D":195,
"C":194,
"B":193,
"A":192 }



inventory = {
0 :'NOTHING',
1 :'DONUT',
2 :'MUFFIN',
3 :'BAGEL',
4 :'HONEY BUN',
5 :'CROISSANT',
6 :'SUGAR',
7 :'TOLL HOUSE',
8 :'MAPLE PECAN',
9 :'OATMEAL',
10 :'BROWNIE',
11 :'MINT GUM',
12 :'LOLLY POP',
13 :'JAW BREAKER',
14 :'ROCK CANDY',
15 :'FUDGE BAR',
16 :'SALAD PARIS',
17 :'ONION SOUP',
18 :'CORNISH HEN',
19 :'VEAL WALLE',
20 :'VITA-MINTS',
21 :'DIGESTOL',
22 :'RECHARGE!',
23 :'KARMA JOLT',
24 :'OMNI ELIXER',
25 :'DATE SAVER',
26 :'LOVE POTION',
27 :'ANTEDOTE 12',
28 :'R & B',
29 :'ROCK',
30 :'POP',
31 :'SOUL',
32 :'CLASSICAL',
33 :'SNEAKERS',
34 :'BOAT SHOES',
35 :'LOAFERS',
36 :'ARMY BOOTS',
37 :'TEXAS BOOTS',
38 :'SLIPPERS',
39 :'THONGS',
40 :'SANDALS',
41 :'MOD BOOTS',
42 :'INSOLES',
43 :'MAZE CRAZE',
44 :'DECATHLETE',
45 :'HYPER BALL',
46 :'TECHNO BELT',
47 :'TEDDY BEAR',
48 :'STONE HANDS',
49 :'DRAGON FEET',
50 :'GRAND SLAM',
51 :'ACRO CIRCUS',
52 :'JAVELIN MAN',
53 :'FATAL STEPS',
54 :'SCANDAL RAG',
55 :'COMIC TIMES',
56 :'MYSTIC SEER',
57 :'NUCLEAR SPY',
58 :'INDIAN LORE',
59 :'EXCALIBER',
60 :'ZEUS WAND',
61 :'RODAN WING',
62 :'GOLD MEDAL',
63 :'ISIS SCROLL',
64 :'SIRLOIN',
65 :'RIB-EYE',
66 :'T-BONE',
67 :'LAMB LEG',
68 :'MERV BURGER',
69 :'CHEESE MERV',
70 :'FISH MERV',
71 :'MONDO MERV',
72 :'MILK',
73 :'ICED TEA',
74 :'SODA',
75 :'MERV MALT',
76 :'MERV FRIES',
77 :'MERV RINGS',
78 :'APPLE PIES',
79 :'SPICY CHILI',
80 :'SMILE',
81 :'CHICKWICH',
82 :'DARK MEAT',
83 :'WHITE MEAT',
84 :'COMBINATION',
85 :'LEMONADE',
86 :'GRAVY',
87 :'BISCUITS',
88 :'CORN COBBER',
89 :'COLE SLAW',
90 :'COFFEE',
91 :'TEA',
92 :'HOT COCOA',
93 :'PANCAKES',
94 :'WAFFLES',
95 :'ICE CREAM',
96 :'ROMAN SHAKE',
97 :'COLA FLOAT',
98 :'NERO PIZZA',
99 :'LASAGNA',
100 :'FRESH JUICE',
101 :'LEMON TEA',
102 :'HERBAL TEA',
103 :'CARROT CAKE',
104 :'POUND CAKE',
105 :'EGG',
106 :'OCTOPUS',
107 :'SQUID',
108 :'CONGER EEL',
109 :'PRAWN',
110 :'SALMON',
111 :'ARK SHELL',
112 :'SEA URCHIN',
113 :'HALIBUT',
114 :'SWORDFISH',
115 :'SALAD ROLL',
116 :'TUNA ROLL',
117 :'SHRIMP ROLL',
118 :'MIXED ROLL',
119 :'EGG ROLL',
120 :'FRIED RICE',
121 :'GARLIC PORK',
122 :'PEPPER BEEF',
123 :'CHOW MEIN',
124 :'SAUNA',
125 :'NO THANKS',
126 :'NOTHING (ALT)',
127 :'MAIN MENU'}


password_invalid = False
password_error = "Password Valid"

# enable cgi debugging
# cgitb.enable()

# read cgi data
form = cgi.FieldStorage()
password_text = form.getvalue("password")

# eliminate white space and find occurences of "A'" and "B'"

password_split = password_text.split()
password_strip = ""
for excerpt in password_split:
	password_strip += excerpt

i_max = len(password_strip)

password_chars = []
for i in range(i_max-1):
	if password_strip[i] == "'":
		continue

	if (password_strip[i+1] == "'"):
		if (password_strip[i] == 'A' or password_strip[i] == 'B'):
			password_chars.append(password_strip[i]+"'")
		else:
			password_invalid = True
			password_error = "' used on invalid character"
	else:
		password_chars.append(password_strip[i])

if (password_strip[i_max-1] != "'"):
	password_chars.append(password_strip[i_max-1])


# check for errors

for i in range(33 - len(password_chars)):
	password_chars.append("A")
	if not password_invalid:
		password_invalid = True
		password_error = "Password too short"


password_clear = []
i=0
if textval.has_key(password_chars[32]):
	key = textval[password_chars[32]] - 192
else:
	key = 0
	if not password_invalid:
		password_invalid = True
		password_error = "Invalid character for password key"

if key >= 32:
	key = 0
	if not password_invalid:
		password_invalid = True
		password_error = "Bad key value for password"


# decode password info

i=0
for char in password_chars:
	if i >= 33:
		if not password_invalid:
			password_invalid = True
			password_error = "Password too long"
		break
	if not textval.has_key(char):
		password_clear.append(0)
		if not password_invalid:
			password_invalid = True
			password_error = "Invalid character entered"
	else:
		val = (textval[char]-192)^(keystring[i]+key)

		password_clear.append(val)
	i += 1


# extract data from password_clear

punch = password_clear[0] & 0x3f
kick = password_clear[1] & 0x3f
weapon = password_clear[2] & 0x3f
throwing = password_clear[3] & 0x3f
agility = password_clear[4] & 0x3f
defense = password_clear[5] & 0x3f
strength = password_clear[6] & 0x3f
will = password_clear[7] & 0x3f
stamina = ((password_clear[8]&0x3f) + ((password_clear[10] >> 2) & 0x3)*64)&0x7f
maxpwr = ((password_clear[9]&0x3f) + (password_clear[10] & 0x3)*64)&0x7f
skills = password_clear[11] & 0x3f
cents = (password_clear[12]&0x3f) + ((password_clear[15] >> 4) & 0x3)*64
ones = (password_clear[13]&0x3f) + ((password_clear[15] >> 2) & 0x3)*64
hundreds = (password_clear[14]&0x3f) + (password_clear[15] & 0x3)*64
inv1 = (password_clear[16]&0x3f) + ((password_clear[18] >> 2) & 0x3)*64
inv2 = (password_clear[17]&0x3f) + ((password_clear[18] ) & 0x3)*64
inv3 = (password_clear[19]&0x3f) + ((password_clear[21] >> 2) & 0x3)*64
inv4 = (password_clear[20]&0x3f) + ((password_clear[21] ) & 0x3)*64
inv5 = (password_clear[22]&0x3f) + ((password_clear[24] >> 2) & 0x3)*64
inv6 = (password_clear[23]&0x3f) + ((password_clear[24] ) & 0x3)*64
inv7 = (password_clear[25]&0x3f) + ((password_clear[27] >> 2) & 0x3)*64
inv8 = (password_clear[26]&0x3f) + ((password_clear[27] ) & 0x3)*64
boss1 = password_clear[28] & 0x3f
boss2 = password_clear[29] & 0x3f
boss3 = password_clear[30] & 0x3f
csum = password_clear[31] & 0x3f

dollars = bcd2dec(ones) + bcd2dec(hundreds) * 100
cents = bcd2dec(cents)
money = dollars + cents * .010


# calculate checksum and see if it matches the gathered checksum

csum_calc = 0
for i in range(31):
	csum_calc += (password_clear[i] & 0x3f)

csum_calc &= 0x3f
csum_calc_char = textval_reverse[((key + keystring[31]) ^ csum_calc) + 192]

if csum_calc != csum:
	if not password_invalid:
		password_invalid = True
		password_error = "Invalid checksum. <br>The game would reject this. The second to last letter should be " + '"' + csum_calc_char + '"' + '.'


# display html output

print "Content-type: text/html"
print

htmlfile1 = open('../projects/rcr_password/begin.html')
htmlfile2 = open('../projects/rcr_password/end.html')

html_begin = htmlfile1.read()
html_end = htmlfile2.read()

htmlfile1.close()
htmlfile2.close()

print html_begin

print "<b>Password Results</b><br><br>"
print "Password Possibly Invalid? :"
if password_invalid:
	print "Yes<br>"
	print "Error reported: " + password_error
	print "<br><br>"
	print "Parsed Input Data: <br>"
	i = 0
	for char in password_chars:
		print char, 
		if (i+1) % 11 == 0:
			print "<br>"
		i += 1
	print "<br><br>"

else:
	print "No<br><br>"


print """
<table width=50%>
<tr>
<td width=50%>
"""

print "Punch:"
print "</td><td>"
print punch
print "</td></tr><tr><td>"

print "Kick:"
print "</td><td>"
print kick
print "</td></tr><tr><td>"

print "Weapon:"
print "</td><td>"
print weapon
print "</td></tr><tr><td>"

print "Throwing:"
print "</td><td>"
print throwing
print "</td></tr><tr><td>"

print "Agility:"
print "</td><td>"
print agility
print "</td></tr><tr><td>"

print "Defense:"
print "</td><td>"
print defense
print "</td></tr><tr><td>"

print "Strength:"
print "</td><td>"
print strength
print "</td></tr><tr><td>"

print "Will Power:"
print "</td><td>"
print will
print "</td></tr><tr><td>"

print "Stamina:"
print "</td><td>"
print stamina
print "</td></tr><tr><td>"

print "Max Power:"
print "</td><td>"
print maxpwr
print "</td></tr><tr><td>"

print "Money:"
print "</td><td>"
print '$%3.2f'% money
print '</td></tr><tr><td>'

print "&nbsp;<br>"
print '</td></tr><tr><td valign="top">'


print "Skills:"
print "</td><td>"
if skills & 1:
	print "Stone Hands<br>"
if skills & 2:
	print "Dragon Feet<br>"
if skills & 4:
	print "Grand Slam<br>"
if skills & 8:
	print "Acro Circus<br>"
if skills & 16:
	print "Javelin Man<br>"
if skills & 32:
	print "Fatal Steps<br>"

print "</td></tr><tr><td>"

print "&nbsp;<br>"
print '</td></tr><tr><td>'

equip = ''
if inv1 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 1:"
print "</td><td>"
print equip + inventory[inv1&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv2 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 2:"
print "</td><td>"
print equip + inventory[inv2&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv3 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 3:"
print "</td><td>"
print equip + inventory[inv3&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv4 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 4:"
print "</td><td>"
print equip + inventory[inv4&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv5 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 5:"
print "</td><td>"
print equip + inventory[inv5&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv6 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 6:"
print "</td><td>"
print equip + inventory[inv6&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv7 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 7:"
print "</td><td>"
print equip + inventory[inv7&0x3f]
print '</td></tr><tr><td>'

equip = ''
if inv8 & 128:
	equip = '#'
else:
	equip = ''
print "Inventory Slot 8:"
print "</td><td>"
print equip + inventory[inv8&0x3f]
print '</td></tr><tr><td>'



print "&nbsp;<br>"
print '</td></tr><tr><td valign="top">'


print "Bosses Defeated:"
print "</td><td>"
if boss2 & 8:
	print "Moose<br>"
if boss2 & 1:
	print "Roxy<br>"
if boss1 & 2:
	print "Benny<br>"
if boss1 & 1:
	print "Clyde<br>"
if boss3 & 1:
	print "Rocko<br>"
if boss3 & 2:
	print "Blade<br>"
if boss2 & 32:
	print "Turk<br>"
if boss2 & 16:
	print "Mojo<br>"
if boss1 & 4:
	print "Thor<br>"
if boss1 & 16:
	print "Ivan<br>"
if boss1 & 8:
	print "Otis<br>"
if boss1 & 32:
	print "Tex<br>"
if boss3 & 4:
	print "Randy<br>"
if boss3 & 8:
	print "Andy<br>"
if boss2 & 4:
	print "Cyndi<br>"

print "</td></tr><tr><td>"

print "&nbsp;<br>"
print '</td></tr><tr><td>'

print "Entered Checksum:"
print "</td><td>"
print csum, "(" + csum_calc_char + ")"
print "</td></tr><tr><td>"

print "Calculated Checksum:"
print "</td><td>"
print csum_calc, "(" + password_chars[31]  + ")"
print "</td></tr><tr><td>"

print "Key:"
print "</td><td>"
print '%d (%s)' % (key, password_chars[-1])
print "</td></tr><tr><td>"



print "&nbsp;<br>"

print "</td></tr></table>"
print "<br>"
print html_end

