#!/usr/bin/env python

# River City Ransom password generator
# v0.0 - 09.10.2004
# author: Jerry McMahan Jr. (jerry@ensomnya.net)
#
# This program is freely redistributable and freely modifyable, provided
# any derivative works are also made freely redistributable and 
# freely modifyable.

import cgi, cgitb

def dec2bcd(num):
	"""converts decimal to BCD"""
	return num % 10 + (num/10)*16


def get_high_bits(num):
	"""gets the high bits of a number for"""
	return (num & 0xc0) >> 6

keystring = (13,  5, 24,  7, 11, 17, 29, 16, 21, 19, 23, 
              9, 15, 25, 31, 12, 20,  5,  3, 22,  6, 12, 
	     18,  7, 10, 11, 27, 18, 14, 13, 12, 24, 17)

passkey = {
'0(A)':0,
'1(B)':1,
'2(C)':2,
'3(D)':3,
'4(E)':4,
'5(F)':5,
'6(G)':6,
'7(H)':7,
'8(I)':8,
'9(J)':9,
'10(K)':10,
'11(L)':11,
'12(M)':12,
'13(N)':13,
'14(O)':14,
'15(P)':15,
'16(Q)':16,
'17(R)':17,
'18(S)':18,
'19(T)':19,
'20(U)':20,
'21(V)':21,
'22(W)':22,
'23(X)':23,
'24(Y)':24,
'25(Z)':25,
'26(A)':26,
'27(B)':27,
'28(C)':28,
'29(D)':29,
'30(E)':30,
'31(F)':31}

textval = {
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

inventory = {
'NOTHING':0,
'DONUT':1,
'MUFFIN':2,
'BAGEL':3,
'HONEY BUN':4,
'CROISSANT':5,
'SUGAR':6,
'TOLL HOUSE':7,
'MAPLE PECAN':8,
'OATMEAL':9,
'BROWNIE':10,
'MINT GUM':11,
'LOLLY POP':12,
'JAW BREAKER':13,
'ROCK CANDY':14,
'FUDGE BAR':15,
'SALAD PARIS':16,
'ONION SOUP':17,
'CORNISH HEN':18,
'VEAL WALLE':19,
'VITA-MINTS':20,
'DIGESTOL':21,
'RECHARGE!':22,
'KARMA JOLT':23,
'OMNI ELIXER':24,
'DATE SAVER':25,
'LOVE POTION':26,
'ANTEDOTE 12':27,
'ANTEDOTE':27,
'R & B':28,
'ROCK':29,
'POP':30,
'SOUL':31,
'CLASSICAL':32,
'SNEAKERS':33,
'BOAT SHOES':34,
'LOAFERS':35,
'ARMY BOOTS':36,
'TEXAS BOOTS':37,
'SLIPPERS':38,
'THONGS':39,
'SANDALS':40,
'MOD BOOTS':41,
'INSOLES':42,
'MAZE CRAZE':43,
'DECATHLETE':44,
'HYPER BALL':45,
'TECHNO BELT':46,
'TEDDY BEAR':47,
'STONE HANDS':48,
'DRAGON FEET':49,
'GRAND SLAM':50,
'ACRO CIRCUS':51,
'JAVELIN MAN':52,
'FATAL STEPS':53,
'SCANDAL RAG':54,
'COMIC TIMES':55,
'MYSTIC SEER':56,
'NUCLEAR SPY':57,
'INDIAN LORE':58,
'EXCALIBER':59,
'ZEUS WAND':60,
'RODAN WING':61,
'GOLD MEDAL':62,
'ISIS SCROLL':63,
'SIRLOIN':64,
'RIB-EYE':65,
'T-BONE':66,
'LAMB LEG':67,
'MERV BURGER':68,
'CHEESE MERV':69,
'FISH MERV':70,
'MONDO MERV':71,
'MILK':72,
'ICED TEA':73,
'SODA':74,
'MERV MALT':75,
'MERV FRIES':76,
'MERV RINGS':77,
'APPLE PIES':78,
'SPICY CHILI':79,
'SMILE':80,
'CHICKWICH':81,
'DARK MEAT':82,
'WHITE MEAT':83,
'COMBINATION':84,
'LEMONADE':85,
'GRAVY':86,
'BISCUITS':87,
'CORN COBBER':88,
'COLE SLAW':89,
'COFFEE':90,
'TEA':91,
'HOT COCOA':92,
'PANCAKES':93,
'WAFFLES':94,
'ICE CREAM':95,
'ROMAN SHAKE':96,
'COLA FLOAT':97,
'NERO PIZZA':98,
'LASAGNA':99,
'FRESH JUICE':100,
'LEMON TEA':101,
'HERBAL TEA':102,
'CARROT CAKE':103,
'POUND CAKE':104,
'EGG':105,
'OCTOPUS':106,
'SQUID':107,
'CONGER EEL':108,
'PRAWN':109,
'SALMON':110,
'ARK SHELL':111,
'SEA URCHIN':112,
'HALIBUT':113,
'SWORDFISH':114,
'SALAD ROLL':115,
'TUNA ROLL':116,
'SHRIMP ROLL':117,
'MIXED ROLL':118,
'EGG ROLL':119,
'FRIED RICE':120,
'GARLIC PORK':121,
'PEPPER BEEF':122,
'CHOW MEIN':123,
'SAUNA':124,
'NO THANKS':125,
'NOTHING (ALT)':126,
'MAIN MENU':127 }


# enable cgi debugging
cgitb.enable()

# read cgi data
form = cgi.FieldStorage()

text_key = form.getvalue("key").upper()
punch = int(form.getvalue("punch").upper())
kick = int(form.getvalue("kick").upper())
weapon = int(form.getvalue("weapon").upper())
throwing = int(form.getvalue("throwing").upper())
agility = int(form.getvalue("agility").upper())
defense = int(form.getvalue("defense").upper())
strength = int(form.getvalue("strength").upper())
will = int(form.getvalue("will").upper())
stamina = int(form.getvalue("stamina").upper())
maxpwr = int(form.getvalue("maxpwr").upper())
dollars = int(form.getvalue("dollars").upper())
cents = int(form.getvalue("cents").upper())
skill = 0
inv1 = form.getvalue("inv1").upper()
inv2 = form.getvalue("inv2").upper()
inv3 = form.getvalue("inv3").upper()
inv4 = form.getvalue("inv4").upper()
inv5 = form.getvalue("inv5").upper()
inv6 = form.getvalue("inv6").upper()
inv7 = form.getvalue("inv7").upper()
inv8 = form.getvalue("inv8").upper()
inv1_val = inventory[inv1]
inv2_val = inventory[inv2]
inv3_val = inventory[inv3]
inv4_val = inventory[inv4]
inv5_val = inventory[inv5]
inv6_val = inventory[inv6]
inv7_val = inventory[inv7]
inv8_val = inventory[inv8]
boss1 = 0
boss2 = 0
boss3 = 0


# setup energy variables

stam_mpwr_hbits = (get_high_bits(stamina)<<2) + (get_high_bits(maxpwr))

# setup skill variables

if form.has_key("s_hands"):
	skill += 1
if form.has_key("d_feet"):
	skill += 2
if form.has_key("g_slam"):
	skill += 4
if form.has_key("a_circus"):
	skill += 8
if form.has_key("j_man"):
	skill += 16
if form.has_key("f_steps"):
	skill += 32

# setup money variables

hundreds = dollars / 100
dollars = dollars % 100

cents = dec2bcd(cents)
dollars = dec2bcd(dollars)
hundreds = dec2bcd(hundreds)

money_hbits = (get_high_bits(cents)<<4) + (get_high_bits(dollars)<<2) + get_high_bits(hundreds)

# setup inventory variables
 

if form.has_key("inv1_equip"):
	inv1_val += 128
if form.has_key("inv2_equip"):
	inv2_val += 128
if form.has_key("inv3_equip"):
	inv3_val += 128
if form.has_key("inv4_equip"):
	inv4_val += 128
if form.has_key("inv5_equip"):
	inv5_val += 128
if form.has_key("inv6_equip"):
	inv6_val += 128
if form.has_key("inv7_equip"):
	inv7_val += 128
if form.has_key("inv8_equip"):
	inv8_val += 128

inv12_hbits = (get_high_bits(inv1_val)<<2) + (get_high_bits(inv2_val))
inv34_hbits = (get_high_bits(inv3_val)<<2) + (get_high_bits(inv4_val))
inv56_hbits = (get_high_bits(inv5_val)<<2) + (get_high_bits(inv6_val))
inv78_hbits = (get_high_bits(inv7_val)<<2) + (get_high_bits(inv8_val))



# setup boss variables

if form.has_key("moose"):
	boss2 += 8
if form.has_key("roxy"):
	boss2 += 1
if form.has_key("benny"):
	boss1 += 2
if form.has_key("clyde"):
	boss1 += 1
if form.has_key("rocko"):
	boss3 += 1
if form.has_key("blade"):
	boss3 += 2
if form.has_key("turk"):
	boss2 += 32
if form.has_key("mojo"):
	boss2 += 16
if form.has_key("thor"):
	boss1 += 4
if form.has_key("ivan"):
	boss1 += 16
if form.has_key("otis"):
	boss1 += 8
if form.has_key("tex"):
	boss1 += 32
if form.has_key("randy"):
	boss3 += 4
if form.has_key("andy"):
	boss3 += 8
if form.has_key("cyndi"):
	boss2 += 4


# set checksum and password key
csum = 0
key = passkey[text_key]

# prepare password information

punch &= 0x3f
kick &=0x3f
weapon &=0x3f
throwing &=0x3f
agility &=0x3f
defense &=0x3f
strength &=0x3f
will &=0x3f
stamina &=0x3f
maxpwr &=0x3f
stam_mpwr_hbits &=0x3f
skill &=0x3f
cents &=0x3f
dollars &=0x3f
hundreds &=0x3f
money_hbits &=0x3f
inv1_val &=0x3f
inv2_val &=0x3f
inv12_hbits &=0x3f
inv3_val &=0x3f
inv4_val &=0x3f
inv34_hbits &=0x3f
inv5_val &=0x3f
inv6_val &=0x3f
inv56_hbits &=0x3f
inv7_val &=0x3f
inv8_val &=0x3f
inv78_hbits &=0x3f
boss1 &=0x3f
boss2 &=0x3f
boss3 &=0x3f
csum &=0x3f # pointless, but here for continuity's sake
key &=0x3f

stats = [
punch, kick, weapon,
throwing, agility, defense,
strength, will, stamina,
maxpwr, stam_mpwr_hbits, skill,
cents, dollars, hundreds,
money_hbits, inv1_val, inv2_val,
inv12_hbits, inv3_val, inv4_val,
inv34_hbits, inv5_val, inv6_val,
inv56_hbits, inv7_val, inv8_val,
inv78_hbits, boss1, boss2,
boss3]


# calculate the "checksum"

for stat in stats:
	csum = csum + stat

csum = csum & 0x3f


# tack the checksum and key to the password string

stats.append(csum)
stats.append(key)


# generate password

password = []
for i in range(32):
	val = ((key + keystring[i]) ^ stats[i]) + 192
	password.append(textval[val])

password.append(textval[192 + key])

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

i=0
for letter in password:
	i += 1
	print letter,
	if (i % 11) == 0:
		print "<br>"

print html_end
