import subprocess
destination = input()
hops = int(input())
def ping(destination,ttl):
    try:
        ping_output = subprocess.check_output(["ping","-c","3","-t",str(ttl),destination])
        
        m = ping_output.decode("utf-8")
        k = m.split()
        t = []
        for i in range(len(k)):
            if k[i][:5] == "time=" :
                p = k[i][5:]
                t.append(float(p))
            if k[i] == 'icmp_seq=1':
                x = k[i-1]
                y = k[i-2]
        return (t,x,1,ttl,y)
        
    except subprocess.CalledProcessError as e:
        m = e.output.decode('utf-8')
        k = m.split()
        return ([],k[8],0,ttl,k[9])

def traceroute(destination,hops):

    for i in range(1,hops+1):
        a = ping(destination,i)
        if a[2] == 0 :
            try:
                ping_output = subprocess.check_output(["ping","-c","3",a[1]])
                m = ping_output.decode("utf-8")
            
                k = m.split()
                t = []
                for j in range(len(k)):
                    if k[j][:5] == "time=" :
                        p = k[j][5:]
                        t.append(float(p))
                if k[1] == destination:
                    print(i,'*','*','*')
                else:
                     print(i,k[1],k[2],str(t[0])+'ms',str(t[1])+'ms',str(t[2])+'ms')
            except subprocess.CalledProcessError as e:
                m = e.output.decode('utf-8')
                k = m.split()
            
                print(i,k[1],k[2],'*','*','*')
        else:
            print(i,a[4],a[1],str(a[0][0])+'ms',str(a[0][1])+'ms',str(a[0][2])+'ms')
            break 


traceroute(destination,hops)
        

        



