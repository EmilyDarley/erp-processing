import csv, re, sys, math, os.path

with open('output.csv','w') as outputfile:
    outputfile.write('Participant,Condition,Time,FP1,FP2,F7,F3,Fz,F4,F8,FC5,FC1,FC2,FC6,T7,\
C3,Cz,C4,T8,FCz,CP5,CP1,CP2,CP6,M2,P7,P3,Pz,P4,P8,PO9,O1,Oz,O2,PO10,M1\n')

for participant in range(1,33):

    print 'working on participant ' + str(participant)

    for segment in range(0,121):

        segmentname=str(segment)
        if len(segmentname)==1:
            segmentname='00'+segmentname
        elif len(segmentname)==2:
            segmentname='0'+segmentname

        print 'working on file ' + segmentname

        filename='p'+str(participant)+'-export.'+segmentname 
        if os.path.exists(filename):      
            with open(filename,'rb') as input:
                inputlist=csv.reader(input,delimiter=' ')
                inputlist=list(inputlist)

            for item in range(0,len(inputlist)):
                inputlist[item]=filter(None,inputlist[item]) #gets rid of empty ones due to excess whitespace

            if '91' in inputlist[0][6]:
                condition="TAP"
            elif '92' in inputlist[0][6]:
                condition="TAU"   
            elif '93' in inputlist[0][6]:
                condition="TNP"
            elif '94' in inputlist[0][6]:
                condition="TNU"
            elif '95' in inputlist[0][6]:
                condition="FAP"
            elif '96' in inputlist[0][6]:
                condition="FAU"
            elif '97' in inputlist[0][6]:
                condition="FNP"
            elif '98' in inputlist[0][6]:
                condition="FNU"

            currentline=3

            for time in range(-1,401):
                electrodevalues=''
                for electrode in range(0,33):
                    electrodevalues=electrodevalues+','+inputlist[currentline+time][electrode]
                with open('output.csv','a') as outputfile:
                    outputfile.write(str(participant)+','+condition+','+str(time)+electrodevalues+'\n')

