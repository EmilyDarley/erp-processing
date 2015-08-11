import csv, re, sys, math

for participant in range(1,33):

    filename='p'+str(participant)+'_new.evt'

    with open(filename,'rb') as original:
        originallist=csv.reader(original, delimiter='\t')
        originallist=list(originallist)


    print len(originallist)
    print 'p ' + str(participant)


    for currentrow in range(0,len(originallist)):
        if 'S91' in originallist[currentrow][3]:
            originallist[currentrow][2]='91'
        if 'S92' in originallist[currentrow][3]:
            originallist[currentrow][2]='92'
        if 'S93' in originallist[currentrow][3]:
            originallist[currentrow][2]='93'
        if 'S94' in originallist[currentrow][3]:
            originallist[currentrow][2]='94'
        if 'S95' in originallist[currentrow][3]:
            originallist[currentrow][2]='95'
        if 'S96' in originallist[currentrow][3]:
            originallist[currentrow][2]='96'
        if 'S97' in originallist[currentrow][3]:
            originallist[currentrow][2]='97'
        if 'S98' in originallist[currentrow][3]:
            originallist[currentrow][2]='98'

    outputfilename='p'+str(participant)+'_new2.evt'

    with open(outputfilename,'w') as outputfile:
        for i in originallist:
            for j in i:
                outputfile.write(j+'\t')
            outputfile.write('\n')
