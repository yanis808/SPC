data = open("data.txt", "r")
lines = data.readlines()
length = (len(lines))
report = open("report.txt", "w")
data.close()
data = open("data.txt", "w")
for i in lines:
    if "," in i:
        i = i.replace(",", ".")
        data.write(i)
    else:
        data.write(i)
data.close()
data = open("data.txt", "r")
lines = data.readlines()


def average():
    """Calculate average"""
    sum = 0
    ave = 0
    for i in lines:
        i = i[:-1]
        i = float(i)
        sum = sum + i
        ave = sum / length
    global ave2
    ave2 = ave
    ave = round(ave, 2)
    print(ave)
    ave = str(ave)
    report.write("Average = ")
    report.write(ave)
    report.write("\n")


def mediana():
    """Calculate mediana"""
    lines.sort()
    x = int(length / 2)
    if length % 2 != 0:
        half = lines[x]
        print(half)
        report.write("Mediana = ")
        report.write(half)
        report.write("\n")
    else:
        x1 = lines[x]
        x1 = x1[:-1]
        x2 = lines[x - 1]
        x2 = x2[:-1]
        x1 = float(x1)
        x2 = float(x2)
        half = (x1 + x2) / 2
        print(half)
        half = str(half)
        report.write("Mediana = ")
        report.write(half)
        report.write("\n")


def rango():
    """Calculate range"""
    lines.sort()
    x1 = float(lines[0])
    x2 = float(lines[-1])
    ran = str(x2 - x1)
    report.write("Range = ")
    report.write(ran)
    report.write("\n")
    print(ran)


def std_dv():
    """Calculate standard deviation for Pp"""
    sum_n = 0
    k = (1 / (length - 1))
    for i in lines:
        i = float(i)
        brac = (i - ave2) ** 2
        sum_n += brac
    s = (k * sum_n) * (0.5)
    s = round(s, 3)
    print(s)
    s = str(s)
    report.write("Standard deviation = ")
    report.write(s)
    report.write("\n")


def main():
    average()
    mediana()
    rango()
    std_dv()


main()
