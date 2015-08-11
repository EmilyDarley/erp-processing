import csv, re, sys, math, os.path

with open('avg300to400.csv','w') as outputfile:
    outputfile.write('Participant,Condition,FP1,FP2,F7,F3,Fz,F4,F8,FC5,FC1,FC2,FC6,T7,\
C3,Cz,C4,T8,FCz,CP5,CP1,CP2,CP6,M2,P7,P3,Pz,P4,P8,PO9,O1,Oz,O2,PO10,M1\n')

with open('longformbins.csv','rb') as input:
    inputlist=csv.reader(input)
    inputlist=list(inputlist)

print len(inputlist)

#startingrow=1

electrodes=range(1,34)
avelectrodes=electrodes

for row in inputlist:
    if row[2] <> 'Time':
        print 'working on participant ' + row[0]
        if int(row[2])==300: #time is 300, start adding
            for electrode in range(0,len(electrodes)):
                electrodes[electrode]=0
            print electrodes
            for electrode in range(0,len(electrodes)):
                electrodes[electrode]=electrodes[electrode]+float(row[electrode+3])       
        elif int(row[2])>300 and int(row[2])<400: #add to sums
            for electrode in range(0,len(electrodes)):
                electrodes[electrode]=electrodes[electrode]+float(row[electrode+3])
        elif int(row[2])==400:
            for electrode in range(0,len(electrodes)):
                electrodes[electrode]=electrodes[electrode]+float(row[electrode+3])
            for avelectrode in range(0,len(avelectrodes)):
                avelectrodes[avelectrode]=electrodes[avelectrode]/100

            averages=''
            for avelectrode in range(0,len(avelectrodes)):
                averages=averages+','+str(avelectrodes[avelectrode])

            with open('avg300to400.csv','a') as outputfile:
                outputfile.write(row[0]+','+row[1]+averages+'\n')


