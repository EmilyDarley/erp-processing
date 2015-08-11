import csv, re, sys, math

for participant in range(1,33):

    filename='p'+str(participant)+'.evt'

    with open(filename,'rb') as original:
        originallist=csv.reader(original, delimiter='\t')
        originallist=list(originallist)


    print len(originallist)
    print 'p ' + str(participant)

    tap=0
    tau=0
    tnp=0
    tnu=0
    fap=0
    fau=0
    fnp=0
    fnu=0

    for currentrow in range(0,len(originallist)):
        if '111' in originallist[currentrow][3]:
            originallist[currentrow][3]='S444'
        elif '112'in originallist[currentrow][3]:
            originallist[currentrow][3]='S445'
        elif '121'in originallist[currentrow][3]:
            originallist[currentrow][3]='S454'
        elif '122'in originallist[currentrow][3]:
            originallist[currentrow][3]='S455'
        elif '211'in originallist[currentrow][3]:
            originallist[currentrow][3]='S544'
        elif '212'in originallist[currentrow][3]:
            originallist[currentrow][3]='S545'
        elif '221'in originallist[currentrow][3]:
            originallist[currentrow][3]='S554'
        elif '222' in originallist[currentrow][3]:
            originallist[currentrow][3]='S555'

    for currentrow in range(0,len(originallist)):
        if '444' in originallist[currentrow][3]: #found tap
            if '21' in originallist[currentrow+5][3] or '21' in originallist[currentrow+6][3] or '21' in originallist[currentrow+7][3] or '21' in originallist[currentrow+8][3] or '21' in originallist[currentrow+9][3] or '21' in originallist[currentrow+10][3]: #correct answer
                if '8' in originallist[currentrow+2][3]:
                    originallist[currentrow+2][3]='S91'
                elif '8' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S91'
                elif '8' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S91'
                tap=tap+1
        elif '445' in originallist[currentrow][3]: #found tau
            if '21' in originallist[currentrow+5][3] or '21' in originallist[currentrow+6][3] or '21' in originallist[currentrow+7][3] or '21' in originallist[currentrow+8][3] or '21' in originallist[currentrow+9][3] or '21' in originallist[currentrow+10][3]: #correct answer
                if '8' in originallist[currentrow+2][3]:
                    originallist[currentrow+2][3]='S92'
                elif '8' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S92'
                elif '8' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S92'
                tau=tau+1
        elif '454' in originallist[currentrow][3]: #found tnp
            if '21' in originallist[currentrow+5][3] or '21' in originallist[currentrow+6][3] or '21' in originallist[currentrow+7][3] or '21' in originallist[currentrow+8][3] or '21' in originallist[currentrow+9][3] or '21' in originallist[currentrow+10][3]: #correct answer
                if '9' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S93'
                elif '9' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S93'
                elif '9' in originallist[currentrow+5][3]:
                    originallist[currentrow+5][3]='S93'
                tnp=tnp+1
        elif '455' in originallist[currentrow][3]: #found tnu
            if '21' in originallist[currentrow+5][3] or '21' in originallist[currentrow+6][3] or '21' in originallist[currentrow+7][3] or '21' in originallist[currentrow+8][3] or '21' in originallist[currentrow+9][3] or '21' in originallist[currentrow+10][3]: #correct answer
                if '9' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S94'
                elif '9' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S94'
                elif '9' in originallist[currentrow+5][3]:
                    originallist[currentrow+5][3]='S94'
                tnu=tnu+1
        elif '544' in originallist[currentrow][3]: #found fap
            if '22' in originallist[currentrow+5][3] or '22' in originallist[currentrow+6][3] or '22' in originallist[currentrow+7][3] or '22' in originallist[currentrow+8][3] or '22' in originallist[currentrow+9][3] or '22' in originallist[currentrow+10][3]: #correct answer
                if '8' in originallist[currentrow+2][3]:
                    originallist[currentrow+2][3]='S95'
                elif '8' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S95'
                elif '8' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S95'
                fap=fap+1
        elif '545' in originallist[currentrow][3]: #found fau
            if '22' in originallist[currentrow+5][3] or '22' in originallist[currentrow+6][3] or '22' in originallist[currentrow+7][3] or '22' in originallist[currentrow+8][3] or '22' in originallist[currentrow+9][3] or '22' in originallist[currentrow+10][3]: #correct answer
                if '8' in originallist[currentrow+2][3]:
                    originallist[currentrow+2][3]='S96'
                elif '8' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S96'
                elif '8' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S96'
                fau=fau+1
        elif '554' in originallist[currentrow][3]: #found fnp
            if '22' in originallist[currentrow+5][3] or '22' in originallist[currentrow+6][3] or '22' in originallist[currentrow+7][3] or '22' in originallist[currentrow+8][3] or '22' in originallist[currentrow+9][3] or '22' in originallist[currentrow+10][3]: #correct answer
                if '9' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S97'
                elif '9' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S97'
                elif '9' in originallist[currentrow+5][3]:
                    originallist[currentrow+5][3]='S97'
                fnp=fnp+1
        elif '555' in originallist[currentrow][3]: #found fnu
            if '22' in originallist[currentrow+5][3] or '22' in originallist[currentrow+6][3] or '22' in originallist[currentrow+7][3] or '22' in originallist[currentrow+8][3] or '22' in originallist[currentrow+9][3] or '22' in originallist[currentrow+10][3]: #correct answer
                if '9' in originallist[currentrow+3][3]:
                    originallist[currentrow+3][3]='S98'
                elif '9' in originallist[currentrow+4][3]:
                    originallist[currentrow+4][3]='S98'
                elif '9' in originallist[currentrow+5][3]:
                    originallist[currentrow+5][3]='S98'
                fnu=fnu+1

    print 'replaced tap ' + str(tap)
    print 'replaced tau ' + str(tau)
    print 'replaced tnp ' + str(tnp)
    print 'replaced tnu ' + str(tnu)
    print 'replaced fap ' + str(fap)
    print 'replaced fau ' + str(fau)
    print 'replaced fnp ' + str(fnp)
    print 'replaced fnu ' + str(fnu)

    outputfilename='p'+str(participant)+'_new.evt'

    with open(outputfilename,'w') as outputfile:
        for i in originallist:
            for j in i:
                outputfile.write(j+'\t')
            outputfile.write('\n')
