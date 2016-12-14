#!/usr/bin/python 
import itertools


doc=["101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","121","122","124","126","127","128","129","133","134","140","141","142","143"]
query=["201","202","210","211","214","217","218","219"]
ctr=["367","467"]
personal=["601~1~n","602~1~n","603~1~n","604~1~n","605~1~n","606~1~n","607~1~n","608~1~n","611~1~n","612~1~n","613~1~n","614~1~n","615~1~n","616~1~n"]

bigFeaturefilter=['116','140','141','202','217','218','219']

for item1,item2 in itertools.combinations([doc,query,ctr],2):

    result=[]
    for fea1,fea2 in itertools.product(item1,item2):
        if fea1 in bigFeaturefilter:
            continue
        if fea2 in bigFeaturefilter:
            continue

        item=fea1+"*"+fea2
        result.append(item)
    print "--->item1",item1,"\nitem2:",item2
    print ",".join(result)



