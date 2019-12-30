import nmap
import csv

nmp = nmap.PortScanner()

f = open('host.csv', 'r')
read = csv.reader(f)
for line in read:
	if line[0] == 'name':
		pass
	else:
		nmp.scan(line[1], '22-443')


		for hst in nmp.all_hosts():
			print('----------------------------------------------------')
			print('Host: %s (%s)' % (hst, nmp[hst].hostname()))
			print('State: %s' % nmp[hst].state())
			for prtcl in nmp[hst].all_protocols():
				print('----------')
				print('Protocol : %s' % prtcl)
				lport = nmp[hst][prtcl].keys()
				lport.sort()
				for port in lport:
					print ('port : %s \t state : %s' % (port, nmp[hst][prtcl][port]['state']))
f.close()
