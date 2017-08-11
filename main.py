#!/usr/bin/python

import sys
import os

def crawl_directory(dir_name):
    os.chdir(dir_name)
    # os.listdir(dirname)
    # for every file, lines_in_file
    # for every directory, crawl
    print("not yet impled")

def lines_in_file(filename):
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
    effort_years = 2.4* (line_count/1000)**1.05
    # person months
    effort_months = 12*effort_years
    schedule_years = 2.5*(effort_months ** 0.38)
    avg_num_developers = effort_years/schedule_years
    annual_salary = 56286
    overhead = 2.4 #?
    cost_of_development = effort_years * annual_salary
    print("Effort years: " + str(effort_years))
    print("Effort months: " + str(effort_months))
    print("Schedule years: " + str(schedule_years))
    print("num developers: " + str(avg_num_developers))
    print("cost to develop: " + str(cost_of_development))

def main():
    line_count = lines_in_file(sys.argv[1])
    print("Total Physical Source Lines of code: " + str(line_count))
    basic_COCOMO(line_count)


if __name__ == "__main__":
    main()
