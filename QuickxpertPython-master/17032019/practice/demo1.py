year = [1904, 1908, 1912, 1916, 1920, 1924, 1928,
        1932, 1936, 1940, 1944, 1948, 1952, 1956,
        1960, 1964, 1968, 1972, 1976, 1980, 1984,
        1988, 1992, 1996, 2000, 2004, 2008, 2012,
        2016, 2020, 2003]
for x in year:
    if(x % 4 == 0 or (x % 100 == 0 and x % 400 == 0)):
        print(" %d is a leap year " %x)
    else:
        print(" %d is not a leap year" %x)