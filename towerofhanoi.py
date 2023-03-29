import numpy as np
def showmove(positions):
	positions=np.asarray(positions)
	higheststack=int(np.max(np.unique(positions, return_counts=True)[1]))
	numdisks=len(positions)
	spaces=" "*numdisks
	for i in range(numdisks+1-higheststack):
		print(spaces+"|"+spaces+spaces+"|"+spaces+spaces+"|"+spaces)
	for i in reversed(range(higheststack)):
		widths=["|","|","|"]
		for tower in range(3):
			if tower in np.unique(positions, return_counts=True)[0]:
				if np.unique(positions, return_counts=True)[1][np.where(np.unique(positions, return_counts=True)[0]==tower)] > i:
					widths[tower]=np.nonzero([positions == tower])[1][-i-1]
		printstring=""
		for tower in range(3):
			if widths[tower]=="|":
				printstring+=" "*numdisks+"|"+" "*numdisks
			else:
				printstring+=" "*(numdisks-widths[tower])
				printstring+="―"*(1+2*widths[tower])
				printstring+=" "*(numdisks-widths[tower])
		print(printstring)
	print("‾"*numdisks*6+"‾"*3)

def solve(n, source, destination, intermediate,positions):
	if n==1:
		positions[0]=destination
		showmove(positions)
		return
	solve(n-1,source,intermediate,destination,positions)
	positions[n-1]=destination
	showmove(positions)
	solve(n-1,intermediate,destination,source,positions)

n=5
solve(5,0,2,1,np.zeros(5))