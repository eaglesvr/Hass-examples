def sfind(pcoll,pfind):
    foundsnr=None
    for ii in range (len(pcoll)):
        it=pcoll[ii]
        for i1 in range(1,len(it)):
            if (it[i1][0]==pfind):
                return [it[0],it[i1]]
    return None

snrs=[
['s1',['ad11','on',1],['ad12','off']],
['s2',['ad21','on',2],['ad22','off']],
['s3',['ad31','on',2],['ad32','off']],
['s4',['ad41','on',2]]
]
rems=[
['r1',['ad11','on',1],['ad12','off']],
['r2',['ad21','on',2],['ad22','off']],
['r3',['ad31','on',2],['ad32','off']],
['r4',['ad41','on',2]]
]
# create dict
d=dict()
d['ad11']= ['r1',['ad11','on',1],['ad12','off']]
print (d)



it = sfind(rems,'ad21')
if (it!=None):
    print (it)
else:
    print("Nothing found")

#   
#              break
#            else:
#                continue
#            break
#    if (foundsnr!=None):
#        print (foundsnr)
#    else:
#        print('**** Nothing found ******')








