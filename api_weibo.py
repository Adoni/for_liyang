# -*- coding:utf-8 -*-
# get user weibo

import os
import sys
import json
import time
from urllib2 import urlopen
from urllib import quote

access_token = "2.00_BHNxDlxpd6C5ca3a1adb9BUxXTD"


sleeptime = 1

def get_user_tag(uid):
    basicurl='https://api.weibo.com/2/users/show.json?'
    url = basicurl + 'access_token='+ access_token +'&'+ 'uids='+str(uid)
    try:
        raw_json = urlopen(url, timeout=20).read().decode('utf8')
    except Exception as e:
        print e
        time.sleep(sleeptime)
        try:
            raw_json = urlopen(url, timeout=20).read().decode('utf8')
        except Exception as e:
            print ('Fail')
            return ('Fail')
    json_data = json.loads(raw_json)
    return

def API_Weibo(uid,page):
    basicurl = "https://api.weibo.com/2/statuses/timeline_batch.json?"
    url = basicurl + 'access_token='+ access_token +'&'+ 'uids='+str(uid)+'&'+'page='+str(page)+'&'+'count='+'100'
    raw_json = ''
    try:
        raw_json = urlopen(url, timeout=20).read().decode('utf8')
    except Exception as e:
        print e
        time.sleep(sleeptime)
        try:
            raw_json = urlopen(url, timeout=20).read().decode('utf8')
        except Exception as e:
            print ('Fail')
            return ('Fail')
    json_data = json.loads(raw_json)
    #print (json_data)
    return json_data

def get_statuses(uid):
    statuses=[]
    page = 1
    while page <= 2:
        json_data = API_Weibo(uid,page)
        page += 1

        if json_data == "Fail":
            continue

        #print (json_data)
        for each in json_data["statuses"]:
            if 'retweeted_status' in each:
                print 'Retweeted'
                print each['text']
                each=each['retweeted_status']
                print each['text']
            try:
                statuses.append(str(each['mid'])+'\t'+each['text']+'\t'+each['created_at']+'\t'+each['source']+'\n')
            except Exception as e:
                print e
    return statuses

def main():
    fp = open('uid')
    #os.chdir('/home/deng/sa/weibo/Weibo')
    #gotuid = os.listdir('/home/deng/sa/weibo/Weibo')
    gotuid = os.listdir('./data')

    num = 0
    success=0
    for eachline in fp:
        uid = eachline.split('\t')[0]

        num += 1
        print (uid,num,success)

        if uid in gotuid:
            continue

        statuses=get_statuses(uid)
        if statuses==[]:
            continue
        fw = open('./data/'+uid,'w+')
        success+=1
        for line in statuses:
            fw.write(line.encode('utf8'))

if __name__ == "__main__":
    main()
    #uid='1831202675'
    #get_statuses(uid)
