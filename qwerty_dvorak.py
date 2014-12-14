

"""This takes qwerty input and returns dvorak input"""
dic_qwerty_dvorak = { 
	'q':"'", 'w':',', 'e':'.', 'r':'p', 't':'y', 'y':'f', 'u':'g', 'i':'c', 'o':'r', 'p':'l', '[':'/', ']':'=',
	'a':'a', 's':'o', 'd':'e', 'f':'u', 'g':'i', 'h':'d', 'j':'h', 'k':'t', 'l':'n', ';':'s', "'":'-',
	'z':';', 'x':'q', 'c':'j', 'v':'k', 'b':'x', 'n':'b', 'm':'m', ',':'w', '.':'v', '.':'z',
	' ':' '
}

input_dvorak = str(raw_input("Enter your qwerty text: "))

if input_dvorak == '':
	print 'Error: no input'
print input_dvorak

dvorak = ''

for i in input_dvorak:
	if i in dic_qwerty_dvorak.keys():
		dvorak += dic_qwerty_dvorak[i]
	else:
		dvorak += i

print "Dvorak: " + dvorak