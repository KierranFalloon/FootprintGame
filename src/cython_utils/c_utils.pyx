def read_stats():
    cdef int w, t
    cdef float r
    try:
        with open("stats.txt", "r") as stats:
            wins = int(stats.readline().strip())
            tries = int(stats.readline().strip())
            ratio = float(stats.readline().strip())
        
        return wins, tries, ratio
    except:
        w, t, r = 0, 0, 0
        with open("stats.txt", "w") as stats:
            stats.write(str(w)+"\n"+str(t)+"\n"+str(r))

        return w, t, r

def add_stats(w, t):
    cdef float ratio
    ratio = float((int(w) / int(t)) * 100)
    with open("stats.txt", "w") as stats:
        stats.write(str(w)+"\n"+str(t)+"\n"+str(ratio))
