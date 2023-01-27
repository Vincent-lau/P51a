from useful import ssh_cmd

def getdiff(exp,crsid):
    diff = []
    with open('/home/l51/'+crsid+'/P51aLab2/2.2/'+exp+'_0.txt') as f:
		lines1 = f.readlines()
    with open('/home/l51/'+crsid+'/P51aLab2/2.2/'+exp+'_1.txt') as f:
		lines2 = f.readlines()
    for i in range(100000):
        dif = float(lines1[i])-float(lines2[i])
        diff.append(dif*1000000)
    return diff


def gettimes(exp,crsid):
    fname = '/home/l51/'+crsid+'/P51aLab2/2.2/'+exp+'.txt'
    with open(fname) as f:
        times=f.readlines()  
    return times

def getrtt(fname,crsid):
    rt = []
    print crsid
    with open("/home/l51/"+crsid+"/P51aLab2/2.2/"+fname) as f:
        for i in range(10000):
            f.next()
            ts=f.next()
            rtt = ts[46:57]
            if (1<i<11):
                print rtt
            rt.append(float(rtt)*1000000)
    return rt
