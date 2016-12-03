# coding=utf-8
import sys
import re
from bilibili import *
sectionList = sys.argv[1].split(',')
keywordList = sys.argv[2].split(',')
startDate = sys.argv[3].split('-')
for i in startDate:
    i=int(i)
endDate = sys.argv[4].split('-')
for i in endDate:
    i=int(i)
pages = int(sys.argv[5])
for sectionId in sectionList:
    for pageNum in range(1,pages+1):
        failed = 0
        print('Searching section:'+sectionId+' page '+str(pageNum)+'...')
        try:
            videoList = GetPopularVideo(startDate,endDate,'hot',int(sectionId),pageNum)
        except Exception,e:
            print('Cannot get video list, skip')
            continue;
        for video in videoList:
            try:
                wordcount = " "
                match = False
                cid = GetCidOfVideo(video.aid)
                danmu = re.sub(r'<[^>]*>','',GetDanmuku(cid))
                danmu = danmu.decode('utf-8').encode(sys.getfilesystemencoding())
                #print(danmu)
                for keyword in keywordList:
                    num = len(GetRE(danmu,keyword))
                    wordcount += keyword+':'+str(num)+' '
                    if(num>0):
                        match = True
                if (match):
                    print(video.title.decode('utf-8').encode(sys.getfilesystemencoding())+' av'+str(video.aid)+' cid:'+str(cid)+wordcount )
            except Exception,e:
                print(e)
                failed += 1
                
