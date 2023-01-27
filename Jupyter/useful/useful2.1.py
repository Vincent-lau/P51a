import re
def gettimes(exp,crsid):
    lines = ""
    fname = '/home/l51/'+crsid+'/P51aLab2/2.1/'+exp+'.txt'
    with open(fname) as f:
        while True:
            line=f.readline()
            if not line: break
            lines += line
    times = re.findall(r': (.*?) seconds',lines)
    return times

def getdiff(exp,crsid):
    if0_times= []
    if1_times= []
    f=open("/home/l51/"+crsid+"/P51aLab2/2.1/"+exp+".txt")
    for i in range(100000):
        intf = f.next()
        if ('0' in intf):
            if0_times.append(float(f.next()[42:53]))
            f.next()
            if1_times.append(float(f.next()[42:53]))
        elif ('1' in intf):
            if1_times.append(float(f.next()[42:53]))
            f.next()
            if0_times.append(float(f.next()[42:53]))
    f.close()

    diff = []
    for i in range(100000):
        dif = if0_times[i]-if1_times[i]
        diff.append(dif*1000000000)
    return diff
