maxi=0
maxim=""
for chosen in lines:
	cuv=["QUICK", "WALON", "JIDOV", "HARHSE", "FIXEZ", "IMPUT", "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul
	valid = [0] * 5
	final = ["","","","",""]
	letters=[]

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
		#print(valid) #testing in terminal
		valid = [0] * 5 #resetam valid pentru a calcula trece prin urmatorul cuvant

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
			nr+=1
	if nr>maxi:
		maxi=nr
		maxim=chosen
	print(nr)

print(maxi)
print(maxim)
