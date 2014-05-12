from sys import exit

def S_room(note, NE_found, NW_found):	#entrance
	print note
				
	a = """\n\t       
\t  \|/
\t --|-- 
\t  /|\\
\t   S   """
	b = """\n\t     NE
\t  \|/
\t --|-- 
\t  /|\\
\t   S   """
	c = """\n\tNW     
\t  \|/
\t --|-- 
\t  /|\\
\t   S   """
	d = """\n\tNW   NE
\t  \|/
\t --|-- 
\t  /|\\
\t   S   """
	
	while not NE_found and not NW_found:
		print a
		next = raw_input("> ")
		
		if next == "S" or next == "s" or next == "leave":
			print "\nyou turn around and leave; never to come back!"
			exit(0)
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "use flint" or next == "strike flint":
			print "\nyou strike the flint and a spark jumps\nthe room brightens up for a fraction of a second\nyou notice something"
			print "\nnorth-east door found"
			NE_found = True
			
		elif next == "flint":
			print "\nwhat do you want to do with the flint?"
		elif "door" in next:
			print "\nwhat door?"
		elif next == "help" or next == "clue":
			print "\nyou have some flint"
		else:
			print "\nconfused?"
			
	while NE_found and not NW_found:
		print b
		next = raw_input("> ")
		
		if next == "S" or next == "s" or next == "leave":
			print "\nyou turn around and leave; never to come back!"
			exit(0)	
		elif next == "NE" or next == "ne" or next == "NE door" or next == "ne door":
			print "\nyou use the north-east door"
			SE_room("""\n\tTile Room:
\t\tYou enter the room to the north east.
\t\tYou can see in here.
\t\tThere seems to be a layout of numbered tiles
\t\ton the floor in rows of four:\n
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#:24:#:23:#:22:#:21:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#:17:#:18:#:19:#:20:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#:16:#:15:#:14:#:13:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#: 9:#:10:#:11:#:12:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#: 8:#: 7:#: 6:#: 5:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#: 1:#: 2:#: 3:#: 4:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################\n
\t\tWhat tile will you step on?
\t\tThere is also an engraving next to you on the wall.""", True, False, False, False, False, False, False, False, False, False, False)
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "use flint" or next == "strike flint":
			print "\nyou strike the flint and a spark jumps\nthe room brightens up for a fraction of a second\nyou notice something"
			print "\nnorth-west door found"
			NW_found = True
			
		elif next == "flint":
			print "\nwhat do you want to do with the flint?"
		elif "door" in next and (not next == "NE door" or not next == "ne door") :
			print "\nwhat door?"
		elif next == "help" or next == "clue":
			print "\nwhy don't you try going somewhere"
		else:
			print "\nconfused?"
			
	while not NE_found and NW_found:
		print c
		next = raw_input("> ")
		
		if next == "S" or next == "s" or next == "leave":
			print "\nyou turn around and leave; never to come back!"
			exit(0)
		elif next == "NW" or next == "nw" or next == "NW door" or next == "nw door":
			print "\nyou use the north-east door"
			SW_room()
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "use flint" or next == "strike flint":
			print "\nnorth-east door found"
			NE_found = True
			
		elif next == "flint":
			print "\nwhat do you want to do with the flint?"
		elif "door" in next and (not next == "NW door" or not next == "nw door"):
			print "\nwhat door?"
		elif next == "help" or next == "clue":
			print "\nwhy don't you try going somewhere"
		else:
			print "\nconfused?"	
	
	while NE_found and NW_found:
		print d
		next = raw_input("> ")
	
		if next == "S" or next == "s" or next == "leave":
			print "\nyou turn around and leave; never to come back!"
			exit(0)
		elif next == "NE" or next == "ne" or next == "NE door" or next == "ne door":
			print "\nyou use the north-east door"
			SE_room("""\n\tTile Room:
\t\tYou enter the room to the north east.
\t\tYou can see in here.
\t\tThere seems to be a layout of numbered tiles
\t\ton the floor in rows of four:\n
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#:24:#:23:#:22:#:21:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#:17:#:18:#:19:#:20:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#:16:#:15:#:14:#:13:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#: 9:#:10:#:11:#:12:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#: 8:#: 7:#: 6:#: 5:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#: 1:#: 2:#: 3:#: 4:#
\t\t\t\t#::::#::::#::::#::::#
\t\t\t\t#####################\n
\t\tWhat tile will you step on?\n
\t\tThere is also an engraving next to you on the wall.""", True, False, False, False, False, False, False, False, False, False, False)
		elif next == "NW" or next == "nw" or next == "NW door" or next == "nw door":
			print "\nyou use the north-west door"
			SW_room()
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"

		elif next == "use flint" or next == "strike flint":
			print "\nyou see nothing else here to be found"			
		elif next == "flint":
			print "\nwhat do you want to do with the flint?"
		elif "door" in next and (not next == "NE door" or not next == "ne door" or not next == "NW door" or not next == "nw door"):
			print "\nwhat door?"
		elif next == "help" or next == "clue":
			print "\nwhy don't you try going somewhere"
		else:
			print "\nconfused?"
			
def SE_room(note, sw, ne, t2, t3, t5, t7, t11, t13, t17, t19, t23):	#tile room
	print note
	a = """\n\t       
\t  \|/
\t --|-- 
\t  /|\\
\tSW     """
	b = """\n\t       
\t  \|/
\t --|-- 
\t  /|\\
\t       """
	c = """\n\t     NE
\t  \|/
\t --|-- 
\t  /|\\
\t        """
	
	while sw and not (ne and t2 and t3 and t5 and t7 and t11 and t13 and t17 and t19 and t23):
		print a
		print "\n\tYou see the first row of numbered tiles."
		print """\n\t#####################
\t#::::#::::#::::#::::#
\t#: 1:#: 2:#: 3:#: 4:#
\t#::::#::::#::::#::::#
\t#####################"""
	
		next = raw_input("> ")
		
		if next == "SW" or next == "sw" or next == "SW door" or next == "sw door":
			S_room("""\n\tEntrance:
\t\tYou re-enter the dark passage.
\t\tYou can see some light at the south entrance,
\t\tbut nothing else is visible to you.
\t\tYou remember the direction you came from.\n						
\t\tYou may leave the passage,
\t\treturn where you came from,
\t\tor find a way to see where you are going.
\t\tYou have some flint.""", True, False)
	
		elif next == "read engraving":
			print """\t\tYOUR PRIME TASK IS
\t\tTO MAKE IT OUT OF
\t\tBLEDROEGYWERA
\t\tBY THE NORTH EXIT"""
		elif next == "1" or next == "4":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "2":
			SE_room("""\n\tTile 2""", False, False, True, False, False, False, False, False, False, False, False)
		elif next == "3":
			SE_room("""\n\tTile 3""", False, False, False, True, False, False, False, False, False, False, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\ndid you read the engraving?\nwill you step on a tile?\nis there anywhere else you can go?"
		else:
			print "\nconfused?"
			
	while ne and not (sw and t2 and t3 and t5 and t7 and t11 and t13 and t17 and t19 and t23):
		print c
		print "\n\tYou see the last row of numbered tiles."
		print """\n\t#####################
\t#::::#::::#::::#::::#
\t#:24:#:23:#:22:#:21:#
\t#::::#::::#::::#::::#
\t#####################"""
	
		next = raw_input("> ")
		
		if next == "NE" or next == "ne" or next == "NE door" or next == "ne door":
			E_room()
	
		elif next == "read engraving":
			print """\t\tYOU HAVE SOLVED THIS PUZZEL\n
\t\tBE WARNED!
\t\tONCE YOU PASS THROUGH THIS DOOR
\t\tTHERE IS NO TURNING BACK!!!"""
		elif next == "21" or next == "22" or next == "24":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "23":
			SE_room("""\n\tTile 23""", False, False, False, False, False, False, False, False, False, False, True)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\ndid you read the engraving?\nwill you step on a tile?\nis there anywhere else you can go?"
		else:
			print "\nconfused?"
	
	while t2 and not (sw and ne and t3 and t5 and t7 and t11 and t13 and t17 and t19 and t23):
		print a
		print """\n\t################
\t#::::#::::#::::#
\t#: 8:#: 7:#: 6:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#: 1:#: X:#: 3:#
\t#::::#::::#::::#
\t################"""
	
		next = raw_input("> ")
		
		if next == "SW" or next == "sw" or next == "SW door" or next == "sw door":
			S_room("""\n\tEntrance:
\t\tYou re-enter the dark passage.
\t\tYou can see some light at the south entrance,
\t\tbut nothing else is visible to you.
\t\tYou remember the direction you came from.\n						
\t\tYou may leave the passage,
\t\treturn where you came from,
\t\tor find a way to see where you are going.
\t\tYou have some flint.""", True, False)
	
		elif next == "read engraving":
			print """\t\tYOUR PRIME TASK IS
\t\tTO MAKE IT OUT OF
\t\tBLEDROEGYWERA
\t\tBY THE NORTH EXIT"""
		elif next == "1" or next == "6" or next == "8":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "2":
			print "\nthat's the tile you're standing on"
		elif next == "3":
			SE_room("""\n\tTile 3""", False, False, False, True, False, False, False, False, False, False, False)
		elif next == "7":
			SE_room("""\n\tTile 7""", False, False, False, False, False, True, False, False, False, False, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\ndid you read the engraving?\nwill you step on a tile?\nis there anywhere else you can go?"
		else:
			print "\nconfused?"
			
	while t3 and not (sw and ne and t2 and t5 and t7 and t11 and t13 and t17 and t19 and t23):
		print a
		print """\n\t################
\t#::::#::::#::::#
\t#: 7:#: 6:#: 5:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#: 2:#: X:#: 4:#
\t#::::#::::#::::#
\t################"""
	
		next = raw_input("> ")
		
		if next == "SW" or next == "sw" or next == "SW door" or next == "sw door":
			S_room("""\n\tEntrance:
\t\tYou re-enter the dark passage.
\t\tYou can see some light at the south entrance,
\t\tbut nothing else is visible to you.
\t\tYou remember the direction you came from.\n						
\t\tYou may leave the passage,
\t\treturn where you came from,
\t\tor find a way to see where you are going.
\t\tYou have some flint.""", True, False)
	
		elif next == "read engraving":
			print """\t\tYOUR PRIME TASK IS
\t\tTO MAKE IT OUT OF
\t\tBLEDROEGYWERA
\t\tBY THE NORTH EXIT"""
		elif next == "4" or next == "6":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "3":
			print "\nthat's the tile you're standing on"
		elif next == "2":
			SE_room("""\n\tTile 2""", False, False, True, False, False, False, False, False, False, False, False)
		elif next == "5":
			SE_room("""\n\tTile 5""", False, False, False, False, True, False, False, False, False, False, False)
		elif next == "7":
			SE_room("""\n\tTile 7""", False, False, False, False, False, True, False, False, False, False, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\ndid you read the engraving?\nwill you step on a tile?\nis there anywhere else you can go?"
		else:
			print "\nconfused?"
			
	while t5 and not (sw and ne and t2 and t3 and t7 and t11 and t13 and t17 and t19 and t23):
		print b
		print """\n\t###########
\t#::::#::::#
\t#:11:#:12:#
\t#::::#::::#
\t###########
\t#::::#::::#
\t#: 6:#: X:#
\t#::::#::::#
\t###########
\t#::::#::::#
\t#: 3:#: 4:#
\t#::::#::::#
\t###########"""
	
		next = raw_input("> ")
	
		if next == "4" or next == "6" or next == "12":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "5":
			print "\nthat's the tile you're standing on"
		elif next == "3":
			SE_room("""\n\tTile 3""", False, False, False, True, False, False, False, False, False, False, False)
		elif next == "11":
			SE_room("""\n\tTile 11""", False, False, False, False, False, False, True, False, False, False, False)
			
		elif next == "help" or next == "clue":
			print "\nwill you step on a tile?"
		else:
			print "\nconfused?"
			
	while t7 and not (sw and ne and t2 and t3 and t5 and t11 and t13 and t17 and t19 and t23):
		print b
		print """\n\t################
\t#::::#::::#::::#
\t#: 9:#:10:#:11:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#: 8:#: X:#: 6:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#: 1:#: 2:#: 3:#
\t#::::#::::#::::#
\t################"""
	
		next = raw_input("> ")
	
		if next == "1" or next == "6" or next == "8" or next == "9" or next == "10":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "7":
			print "\nthat's the tile you're standing on"
		elif next == "2":
			SE_room("""\n\tTile 2""", False, False, True, False, False, False, False, False, False, False, False)
		elif next == "3":
			SE_room("""\n\tTile 3""", False, False, False, True, False, False, False, False, False, False, False)
		elif next == "11":
			SE_room("""\n\tTile 11""", False, False, False, False, False, False, True, False, False, False, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\nwill you step on a tile?"
		else:
			print "\nconfused?"
			
	while t11 and not (sw and ne and t2 and t3 and t5 and t7 and t13 and t17 and t19 and t23):
		print b
		print """\n\t################
\t#::::#::::#::::#
\t#:15:#:14:#:13:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#:10:#: X:#:12:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#: 7:#: 6:#: 5:#
\t#::::#::::#::::#
\t################"""
	
		next = raw_input("> ")
	
		if next == "6" or next == "10" or next == "12" or next == "14" or next == "15":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "11":
			print "\nthat's the tile you're standing on"
		elif next == "5":
			SE_room("""\n\tTile 5""", False, False, False, False, True, False, False, False, False, False, False)
		elif next == "7":
			SE_room("""\n\tTile 7""", False, False, False, False, False, True, False, False, False, False, False)
		elif next == "13":
			SE_room("""\n\tTile 13""", False, False, False, False, False, False, False, True, False, False, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\nwill you step on a tile?"
		else:
			print "\nconfused?"
			
	while t13 and not (sw and ne and t2 and t3 and t5 and t7 and t11 and t17 and t19 and t23):
		print b
		print """\n\t###########
\t#::::#::::#
\t#:19:#:20:#
\t#::::#::::#
\t###########
\t#::::#::::#
\t#:14:#: X:#
\t#::::#::::#
\t###########
\t#::::#::::#
\t#:11:#:12:#
\t#::::#::::#
\t###########"""
	
		next = raw_input("> ")
	
		if next == "12" or next == "14" or next == "20":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "13":
			print "\nthat's the tile you're standing on"
		elif next == "11":
			SE_room("""\n\tTile 11""", False, False, False, False, False, False, True, False, False, False, False)
		elif next == "19":
			SE_room("""\n\tTile 19""", False, False, False, False, False, False, False, False, False, True, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\nwill you step on a tile?"
		else:
			print "\nconfused?"
			
	while t17 and not (sw and ne and t2 and t3 and t5 and t7 and t11 and t13 and t19 and t23):
		print b
		print """\n\t###########
\t#::::#::::#
\t#:24:#:23:#
\t#::::#::::#
\t###########
\t#::::#::::#
\t#: X:#:18:#
\t#::::#::::#
\t###########
\t#::::#::::#
\t#:16:#:15:#
\t#::::#::::#
\t###########"""
	
		next = raw_input("> ")
	
		if next == "15" or next == "16" or next == "18" or next == "24":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "17":
			print "\nthat's the tile you're standing on"
		elif next == "23":
			SE_room("""\n\tTile 23""", False, False, False, False, False, False, False, False, False, False, True)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\nwill you step on a tile?"
		else:
			print "\nconfused?"
			
	while t19 and not (sw and ne and t2 and t3 and t5 and t7 and t11 and t13 and t17 and t23):
		print b
		print """\n\t################
\t#::::#::::#::::#
\t#:23:#:22:#:21:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#:18:#: X:#:20:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#:15:#:14:#:13:#
\t#::::#::::#::::#
\t################"""
	
		next = raw_input("> ")
	
		if next == "14" or next == "15" or next == "18" or next == "20" or next == "21" or next == "22":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "19":
			print "\nthat's the tile you're standing on"
		elif next == "13":
			SE_room("""\n\tTile 13""", False, False, False, False, False, False, False, True, False, False, False)
		elif next == "23":
			SE_room("""\n\tTile 23""", False, False, False, False, False, False, False, False, False, False, True)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\nwill you step on a tile?"
		else:
			print "\nconfused?"
			
	while t23 and not (sw and ne and t2 and t3 and t5 and t7 and t11 and t13 and t17 and t19):
		print c
		print "You have made it to the far side!\nYou see a door and another engraving."
		print """\n\t################
\t#::::#::::#::::#
\t#:24:#: X:#:22:#
\t#::::#::::#::::#
\t################
\t#::::#::::#::::#
\t#:17:#:18:#:19:#
\t#::::#::::#::::#
\t################"""
	
		next = raw_input("> ")
		
		if next == "NE" or next == "ne" or next == "NE door" or next == "ne door":
			E_room()
	
		elif next == "read engraving":
			print """\t\tYOU HAVE SOLVED THIS PUZZEL\n
\t\tBE WARNED!
\t\tONCE YOU PASS THROUGH THIS DOOR
\t\tTHERE IS NO TURNING BACK!!!"""
		elif next == "18" or next == "22" or next == "24":
			dead("\nThe tile crumbles beneath your feat! You fall through the ground!")
		elif next == "23":
			print "\nthat's the tile you're standing on"
		elif next == "17":
			SE_room("""\n\tTile 17""", False, False, False, False, False, False, False, False, True, False, False)
		elif next == "19":
			SE_room("""\n\tTile 19""", False, False, False, False, False, False, False, False, False, True, False)
			
		elif next == "exit" or next == "quit":
			print "\nAre you sure? y/n"
			quit = raw_input("> exit: ")
			if quit == "n" or quit == "N":
				continue
			elif quit == "y" or quit == "Y":
				exit(0)
			else:
				print "\n???"
			
		elif next == "help" or next == "clue":
			print "\ndid you read the engraving?\nwill you step on a tile?\nis there anywhere else you can go?"
		else:
			print "\nconfused?"
			
def E_room(note):
	print note
	a = """\n\t       
\t  \|/
\t --|-- 
\t  /|\\
\t       """
	b = """\n\t       
\t  \|/
\tW--|-- 
\t  /|\\
\t       """
	c = """\n\t   N   
\t  \|/
\t --|-- 
\t  /|\\
\t       """
	
	while True:
		next = raw_input("> ")
	
		if next == "N":
			NE_room()
		elif next == "W":
			ME_room()
		elif next == "S":
			SE_room()
		else:
			print "Pardon?	N---W---S"
			
def NE_room():
	print "NE room"
	print "NW---SE"
	
	while True:
		next = raw_input("> ")
	
		if next == "NW":
			N_room()
		elif next == "SE":
			E_room()
		else:
			print "Pardon?	NW---SE"
			
def N_room():
	print "N room"
	print "Finished!"
	print "N---SW---SE"
	
	while True:
		next = raw_input("> ")
		
		if next == "N":
			exit(0)
		if next == "SW":
			NW_room()
		if next == "SE":
			NE_room()
	
def ME_room():
	print "ME room"
	print "E---W"
	
	while True:
		next = raw_input("> ")
	
		if next == "E":
			E_room()
		elif next == "W":
			MW_room()
		else:
			print "Pardon?	E---W"
			
def MW_room():
	print "MW room"
	print "W---E"
	
	while True:
		next = raw_input("> ")
	
		if next == "W":
			W_room()
		elif next == "E":
			ME_room()
		else:
			print "Pardon?	W---E"
			
def W_room():
	print "W room"
	print "SE---E---NE"
	
	while True:
		next = raw_input("> ")
	
		if next == "SE":
			SW_room()
		elif next == "E":
			MW_room()
		elif next == "NE":
			NW_room()
		else:
			print "Pardon?	SE---NE"
			
def NW_room():
	print "NW room"
	print "SW---NE"
	
	while True:
		next = raw_input("> ")
	
		if next == "SW":
			W_room()
		elif next == "NE":
			N_room()
		else:
			print "Pardon?	SW---NE"
			
def SW_room():
	print "SW room"
	print "SE---NW"
	
	while True:
		next = raw_input("> ")
	
		if next == "SE":
			S_room("""\n\tEntrance:
\t\tYou re-enter the dark passage.
\t\tYou can see some light at the south entrance,
\t\tbut nothing else is visible to you.
\t\tYou remember the direction you came from.\n						
\t\tYou may leave the passage,
\t\treturn where you came from,
\t\tor find a way to see where you are going.
\t\tYou have some flint.""", False, True)
		elif next == "NW":
			W_room()
		else:
			print "Pardon?	SE---NW"
			
def dead(why):
	print why, "You are dead!"
	exit(0)

def start():	
	print """\n\tYour name is Aledu. You have come to Hell Water Mountains pursuing
\tan old friend. Your purpose is to seek answers, and revenge! Your
\tdestination is Black Heart Mountain. There lies a great tower known
\tas Mergawyth, and it is in that tower where your answers lie.\n
\tYou have come from a small village called Lwetherye, journying
\tfor three months. Finally, you have arrived at the foot of Hell's
\tBack. This is a huge red mountain that towers into the clouds. Half
\tway up the mountain is Blood Rock Pass, a passage through the
\tmountain. This leads to Rethenuisuf (in the old language), a
\tcollection of mountains, vallies and volcanoes. Rethenuisuf (more
\tcommonly known as The Red Way) has a bitter climate of ash storms,
\trivers of lava, smokey red skies and an immense heat. At the far
\tside of The Red Way is Black Heart Mountain (or Ysigorumflegeth).
\tAlmost completely surrounded by swamp, the only known possible
\tpassage into The Red Way is through Blood Rock Pass.\n
\tYou make your way up Hell's Back until you you come to Blood Rock
\tPass. Before the entrance to the passage lies a box with items
\tinside. You look and find two pieces of flint and silver paint.
\tYou decide to take these items, believing it was intended that
\tyou should."""
	S_room("""\n\tEntrance:
\t\tYou enter, from the south, into a dark passage.
\t\tIt is so dark that you can't see anything.
\t\tFor fear where you might step,
\t\tyou are afraid to go any further.\n
\t\tYou may turn around and leave,
\t\tor find a way to see where you are going.""", False, False)

start()