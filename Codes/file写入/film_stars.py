ffile = open("film_stars.txt")
line = ffile.readline()
first, *middle, last = line.split()
print(first, middle, last)
while line != "":
    line = ffile.readline().rstrip()
    first, *middle, last = line.split()
    print(first, middle, last)
ffile.close()