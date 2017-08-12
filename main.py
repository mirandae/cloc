#!/usr/bin/python

import os
import sys

ignore_dirs = [".git", ".vscode"]
ignore_files = [""]

def crawl_directory(dir_name):
    last = os.curdir
    os.chdir(dir_name)

    loc = 0
    for dirname, dirnames, filenames in os.walk("."):
        # dirnames.remove('.git')
        # dirnames.remove('.vscode')
        for filename in filenames:
            loc += lines_in_file(filename)

        for subdirname in dirnames:
            loc +=crawl_directory(subdirname)    
    os.chdir(last)
    return loc

def lines_in_file(filename):
    print(filename)
    loc = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if (line == "") | (line.startswith("//")):
                continue
            loc+=1

    f.close()
    return loc

# Organic: effort factor = 2.4, exponent = 1.05; schedule factor = 2.5, exponent = 0.38
# Effort Applied (E) = ab(KLOC)bb [ man-months ]
# Development Time (D) = cb(Effort Applied)db [months]
# People required (P) = Effort Applied / Development Time [count]
def basic_COCOMO(line_count):
    # person years
    person_years = 2.4* (line_count/1000)**1.05
    # person months
    person_months = 12*person_years
    schedule_years = 2.5*(person_months ** 0.38)
    avg_num_developers = person_years/schedule_years
    annual_salary = 56286
    overhead = 2.4 #?
    cost_of_development = person_years * annual_salary
    print("Effort years: " + str(person_years))
    print("Effort months: " + str(person_months))
    print("Schedule years: " + str(schedule_years))
    print("num developers: " + str(avg_num_developers))
    print("cost to develop: " + str(cost_of_development))

def main():
    root = sys.argv[1]
    line_count = -1
    if os.path.isfile(root):
        line_count = lines_in_file(root)
    else:
        line_count = crawl_directory(root)

    print("Total Physical Source Lines of code: " + str(line_count))
    basic_COCOMO(line_count)


if __name__ == "__main__":
    main()
