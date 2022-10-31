Alphabet = {"A": 0, "B": 0, "C": 0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}

#cele mai bune 5 caractere
char= ["A", "I", "E", "U", "R"]

#vectorul de pozitii optime
p= [0, 0, 0, 0, 0, 0]

#citim dictionarul si le punem in lines
with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

#frecventa fiecarei litere din fiecare cuvant
for cuvant in lines:
    cuvant = cuvant.strip("\n")
    for chr in cuvant:
        Alphabet[chr]+=1

 #sortare dupa literele cele mai frecvente
Alphabet2 = dict(sorted(Alphabet.items(), key=lambda item: item[1]))
print(Alphabet2)

#gasirea pozitiilor optime pentru ch cele mai frecvnte
for k in char:
	for cuv in lines:
		cuv = cuv.strip("\n")
		for i in range(len(cuv)):
			if cuv[i]==k:
				p[i]+=1
	print(f"Pentru {k}:") #R pentru pozitia 1; A pentru pozitia 2; U pentru pozitia 3; E pentru pozitia 4; I pentru pozitia 5    
    
#Trebuie gasit un cuvant valid optim, care sa aiba cat mai multe similaritati cu cuv RAUEI
	for i in range (0,5):
		print(f"pe pozitia {i+1} este {p[i]}")
		p[i]=0
	print(end="\n")

#gaseste primul cuv optim:
#for cuv in lines:
	#if cuv[1]=="A" and cuv[3]=="E" and cuv[4]=="I" and cuv[0]=="R":
		#print(cuv)
#deci,
cuv="RATEI"

#alege un cuv random + verificare dintre cuv ales si chosen
valid = [0] * 5

#seed
random.seed(5)

#vectorul valid e astfel: 2 e "green" 1 e "yellow" 0 e "No luck!"
#chosen e cuvantul ales de calculator
pozz=random.randrange(0,len(lines))
chosen=lines[pozz]

for i in range(5):
	if cuv[i]==chosen[i]:
		valid[i]=2
	else:
		for k in range(0,5):
			if cuv[i]==chosen[k]:
				valid[i]=1
				break
		else:
			valid[i]=0
print(chosen)
print(valid)

#Cautam cele mai mic nr de cuvinte astfel incat sa "acoperim" tot alfabetul SI sa maximizam cele mai probabile pozitii ale acestor litere
#Fiecare "if" este pentru fiecare pozitie si cu literele care se regasesc cel mai probabil pe acea pozitie
for cuv in lines:
	if cuv[3]=="S" or cuv[3]=="C" or cuv[3]=="M" or cuv[3]=="P" or cuv[3]=="D" or cuv[3]=="B" or cuv[3]=="G":
		if cuv[1]=="A" or cuv[1]=="U" or cuv[1]=="O":
			if cuv[2]=="Z" or cuv[2]=="X":
				if cuv[0]=="V" or cuv[0]=="F" or cuv[0]=="H" or cuv[0]=="J" or cuv[0]=="K" or cuv[0]=="W" or cuv[0]=="Q":
					if cuv[4]=="I" or cuv[4]=="E" or cuv[4]=="T" or cuv[4]=="Y":
						print(cuv)


#Din pacate, nu s-au gasit cuvinte cu Q si cu W, asa ca le-am luat separat, iar Q si W se gasesc aproape exclusiv pe pozitia 0, deoarece sunt putine cuvinte care contin aceste litere
for cuv in lines:
	if cuv.find("Q")!=-1:
		print(cuv)
for cuv in lines:
	if cuv.find("W")!=-1:
		print(cuv)

		
		
		

#Niste statistici: s e suma din vectorul valid pt fiecare cuvant "chosen", s2 ar trebui sa fie doar pentru cele care au litere care se repeta si nr numar de cuvinte care se repeta
s=0
nr=0
s2=0
for chosen in lines:
	valid=[0]*5
	cuv="QUICK"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k]:
					valid[k]=1
					break


	cuv="WALON"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k] and valid[k]==0: #comment ( daca valid[1] se transforma in 1 dupa ce litera J apare in cuvant si la urmatorul cuvant se transforma in 1 pentru litera A ? )
					valid[k]=1
					break

	cuv="JIDOV"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k] and valid[k]==0:
					valid[k]=1
					break

	cuv="HARSE"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k] and valid[k]==0:
					valid[k]=1
					break

	cuv="FIXEZ"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k] and valid[k]==0:
					valid[k]=1
					break

	cuv="IMPUT"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k] and valid[k]==0:
					valid[k]=1
					break
	cuv="RUGBY"
	for i in range(5):
		if cuv[i]==chosen[i]:
			valid[i]=2
		else:
			for k in range(0,5):
				if cuv[i]==chosen[k] and valid[k]==0:
					valid[k]=1
					break
	s3=0
	for i in range(5):
		s+=valid[i]
		s3+=valid[i]
	p=0
	if p in valid:
		print(chosen)
		nr+=1
		s2+=s3
	
		
print(s/11454)
print(s2/nr)

#varianta pentru calcularea validului
cuv=["QUICK", "WALON", "JIDOV", "HARHSE", "FIXEZ", "IMPUT", "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul
valid = [0] * 5
final = ["","","","",""]
letters=[]

#random value for testing the algorithm
random.seed(42) # seed pentru a avea acelas cuvant random
pozz=random.randrange(0,len(lines)) # o pozitie random intre 0 si len(lines)-1
chosen=lines[pozz]

for word in cuv:
	for i in range(5):
		if word[i]==chosen[i]: #varianta cand caracterul apare pe aceeasi pozitie ca in chosen
			valid[i]=2
			final[i] = word[i]
			if word[i] not in letters :  #Punem caracterul in letters
				letters += word[i]
		else:
			for k in range(5):
				if word[i]==chosen[k]: #varianta cand caracterul se afla in cuvanta si pe pozitia gresita
					valid[i]=1
					if word[i] not in letters : #punem caracterul in letters
						letters += word[i]
					break
			else:
				valid[i]=0 #varianta cand caracterul nu apare deloc in cuvant
	print(valid) #testing in terminal
	valid = [0] * 5 #resetam valid pentru a calcula trece prin urmatorul cuvant
print(f"letter choices are: {letters} ") #din ce litere este format cuvantul nostru
print(f"our first guess is : {final}") #final este cuvantul care il ghicim
print(f"the chosen word is : {chosen}") #testing in terminal (vedem care e cuvantul random)








#verficam cuvintele posibile ramase

nr=0
for word in lines:
	ok=1
	for i in range(len(word)-1):
		if word[i] not in letters:
			ok=0
		if final[i]!="":
			if word[i]!=final[i]:
				ok=0
	for i in range(len(letters)):
		if letters[i] not in word:
			ok=0
	if ok==1:
		print(word)
		nr+=1
print(nr)
