#	\TER-NIX/	\TER|NIX/

from Tkinter import *
from datetime import datetime

#	1 Terdat	=	3 Terputs	=	27 Terhuts	=	1 day
#	1 Terput	=	9 Terhuts					=	8 hours
#	1 Terhut	=	3 Terpins	=	81 Termins	=	160/3 minutes				~	53.33 minutes		~	55 minutes			~	1 hour
#	1 Terpin	=	27 Termins					=	160/9 minutes				~	17.78 minutes		~	20 minutes
#	1 Termin	=	3 Terpecs	=	81 Tersecs	=	3200/81 seconds				~	39.51 seconds		~	40 seconds			~	1 minute
#	1 Terpec	=	27 Tersecs					=	3200/243 seconds			~	13.17 seconds		~	15 seconds
#	1 Tersec									=	3200000/6561 milliseconds	~	487.73 milliseconds	~	500 milliseconds	~	1 second

root = Tk()
clock = Label(root, font=('times', 20, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
prevtime = ''

def dec_to_tern(n):
	n = int(n)
	r = 3
	l = []
	v = "0"
	a = b = n
	while a > 0:
		a = b / r
		l.append(b % r)
		b = a
	for i in range(len(l)):
		c = str(l[len(l) - (i + 1)])
		v = v + c
	return v
	
def ternix(input):
	nums = ('-', '/', '\\')
	string = []
	for j in list(input):
		string.append(nums[int(j)])
	result = ''.join(string)
	return result

def updateclock():
	global prevtime
	dt = datetime.now()
	s = dt.second + dt.microsecond / 1000000.0
	
	TH = dt.hour * (9.0 / 8.0)
	TM = dt.minute * (243.0 / 160.0)
	TS = s * (6561.0 / 3200.0)
	
	A = TH - float(int(TH))
	TH = int(TH)
	
	TM = TM + (81.0 * A)
	B = TM - float(int(TM))
	TM = int(TM)
	
	TS = TS + (81.0 * B)
	TS = int(TS)
	
	TM = TM + (TS / 81)
	TS = TS - ((TS / 81) * (81))
	TH = TH + (TM /81)
	TM = TM - ((TM / 81) * (81))
	
	TDp = TH / 9
	THp = TM / 27
	TMp = TS / 27
	
	TH = TH - (TDp * 9)
	TM = TM - (THp * 27)
	TS = TS - (TMp * 27)
	
	cTDp = dec_to_tern(int(TDp))
	cTH = dec_to_tern(int(TH))
	cTHp = dec_to_tern(int(THp))
	cTM = dec_to_tern(int(TM))
	cTMp = dec_to_tern(int(TMp))
	cTS = dec_to_tern(int(TS))		
	
	newtime = " " + ternix(str("%01i"%int(cTDp))) + ":   " + ternix(str("%01i"%int(cTHp))) + ":   " + ternix(str("%01i"%int(cTMp))) + ":\n" + ternix(str("%02i"%int(cTH))) + "  " + ternix(str("%03i"%int(cTM))) + "  " + ternix(str("%03i"%int(cTS)))
	
	#newtime = ternix(str("%01i"%int(cTDp))) + " " + ternix(str("%02i"%int(cTH))) + " " + ternix(str("%01i"%int(cTHp))) + " " + ternix(str("%03i"%int(cTM))) + " " + ternix(str("%01i"%int(cTMp))) + " " + ternix(str("%03i"%int(cTS)))
	
	#newtime = str("%01i"%int(cTDp)) + " " + str("%02i"%int(cTH)) + " " + str("%01i"%int(cTHp)) + " " + str("%03i"%int(cTM)) + " " + str("%01i"%int(cTMp)) + " " + str("%03i"%int(cTS))
	
	if prevtime != newtime:
		prevtime = newtime
		clock.configure(text=newtime)
	clock.after(10, updateclock)

updateclock()
root.mainloop()