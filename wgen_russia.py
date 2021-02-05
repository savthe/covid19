#weighted gen
N = 22 #number of data columns
def app(out, fname, w):
	print("Append: ", fname, w)
	global N
	f = open(fname, 'r')
	lines = f.readlines()
	for i in range(0, len(lines)):
		line = lines[i]
		line.strip()
		line = line.replace(',', '.')
		line = line.replace('%', '')
		line = line.replace('+', '')
		if len(out) <= i: out.append(["0"]*N)
		a = out[i]
		b = line.split(';')

		if a[0] == '0': a[0] = b[0]
		for i in range(1, N):
			try:
				a[i] = str(round(float(a[i]) + w*float(b[i]), 5))
			except:
				pass

	f.close()

def dump(lst, fname):
	f = open(fname, 'w')
	for s in lst:
		f.write(' '.join(s))
		f.write('\n')
	f.close()
	print("\n")

def mean(lst, m):
	for line in lst:
		for i in range(1, len(line)):
			line[i] = str(round(float(line[i]) / m,5))

def weight(key, names):
	f = open("density.csv")
	lines = f.readlines()
	d = {}
	for s in lines:
		s.strip()
		(nm, ratio, p, a) = s.split()
		d[nm] = [ratio, p, a]
		#print(d[nm])
	sum = 0
	for nm in names:
		sum += float(d[nm][1])
	return float(d[key][1]) / sum

out = []
areapop = []
names = ["moscow"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region_moscow.txt")


out = []
names = ["moscow", "mosobl"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region0.txt")

out = []
names = ["nn", "ivanovsk", "mordov", "penza", "tambov", "volgograd", "ulyanovsk",
"kostroma", "chuvash", "mariy", "saratov"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region1.txt")

out = []
names = ["perm", "komi", "bashkortostan", "orenburg", "samara", "tatarstan", "kirov",
"nenetsk"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region2.txt")

out = []
names = ["tumen", "hanti", "kurgan", "sverdlovsk", "chelyabinsk"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region3.txt")

out = []
names = ["omsk", "tomsk", "yamalo", "novosib"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region4.txt")

out = []
names = ["krasnoyarsk", "irkutsk"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region5.txt")

out = []
names = ["habarovsk", "evreysk", "amursk", "primorsk"]
for s in names: app(out, s + ".csv", weight(s, names))
mean(out, len(names))
dump(out, "region6.txt")



