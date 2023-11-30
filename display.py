def draw_tbl(tbl):
    def drawline(w):
        for i in range(len(w)):
            print('+' + '-' * (w[i] + 2), end = '')
        print('+')
    def drawrow(l):
        for i in range(len(l)):
            print('| ' + (('%' + str(w[i]) + 's')%l[i]) + ' ', end = '')
        print('|')
    w = []
    for i in range(len(tbl[0])):
        templst = [len(str(tbl[j][i])) for j in range(len(tbl))]
        w.append(max(templst))
    for i in range(len(tbl)):
        drawline(w)
        drawrow(tbl[i])
    drawline(w)