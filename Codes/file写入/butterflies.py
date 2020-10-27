# This program counts and prints all
# of the lines in an input file.
BUTTERFLY_FILE = \
    "Trends_in_UK_butterflies.csv"
HEADER_LINES = 2

def main():
    with open(BUTTERFLY_FILE) as file:
        line_count = 0
        butterflyName = ""
        shortTermChange = ""
        trend = 0
        
        for line in file:
            if line_count >= HEADER_LINES:
                line = line.rstrip()
                if line_count % 2 == 0:
                    butterflyName, *extra, shortTermChange, trend = line.split(',')
                else:
                    latinName = line.strip(',')
                    print("{} {}:\t {}, {}".format(butterflyName.capitalize(), latinName, shortTermChange.rstrip('*'), trend))
            line_count += 1
        print("\nLine count:", line_count)

main()