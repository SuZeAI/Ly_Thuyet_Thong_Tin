f1 = open("in.txt", "r")
s = f1.read()
f1.close()
s = s.replace("\\right", "", -1)
s = s.replace("\\left", "", -1)
f = open("out.txt", "w")
f.write(s)
f.close()