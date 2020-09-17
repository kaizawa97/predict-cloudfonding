import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import nagisa
import time
import random


file = '../makecsv/makuakedata.csv'
base_url = 'https://api.makuake.com/v2/projects?page={number}&per_page=15&type=most-funded'
for pagenumber in range(1):
    pagenumber += 1
    url = base_url.format(number = pagenumber)
    request = requests.get(url,url)
    urlhtml = request.json()

    for idnumber in range(15):
        url = urlhtml['projects'][idnumber]['url']
        idnumber += 1
# ここのコメントでURL内のHTMLを取得
        request = requests.get(url)
        print(url)
        soup = BeautifulSoup(request.text, 'html.parser')  # レスポンスのHTMLからオブジェクトを作成

        tagtitle = soup.find_all('span', {'class': 'tagName'})  # spanタグのタグを取得
        resection = soup.find_all('section', {'class': 'return-section'})  # sectionタグのパッケージ数取得
        projecttag = soup.find_all('a', {'class': 'projectTag'})  # aタグのカテゴリー取得
        moneygoal = soup.find_all('p', {'class': 'stMoneyGoal'})  # pタグの目標金額取得
        packagemoney = soup.find_all('h4', {'class': 'lefth4Right'})  # h4タグの文章取得
        listtag = []
        listpack = [] #moneypackageのリスト


# 文章が分割されていたため二つで取得
        projectdetail = soup.find_all('div', {'class': 'leftText project-content'})
        riskandchallenge = soup.find_all(
            'p', {'class': 'riskAndChallenge_body leftText'})

        imgdetail = soup.find_all('div', {'class': 'leftText project-content'})  # imgタグのイメージ数取得
        for imgdet in imgdetail:
            lenimg = imgdet.select('img')
        print("image-number:",len(lenimg))  # detail-image何個出てくるか数えている
        print("package-number:",len(resection))  # 提供パッケージ数

        for tagname in tagtitle: #タグを取得
            tag = tagname.text
            listtag.append(tag)
        print("tag name:",tag)

        for i in listtag:
            print(i)

        for protag in projecttag:
            pro = protag.text
        pro = pro.strip()
        print("category:",pro)  # カテゴリー取得

        for prodetail in projectdetail:
            prode = prodetail.text
        prode = prode.strip() #プロダクトの説明文
        words = nagisa.filter(prode,filter_postags=["助詞","助動詞"])
        wordsList = words.words #リスト型で単語ごとに分けられている
        wordsListpro = len(wordsList) #単語の数を数えている
        print("product-words-count:",wordsListpro)


        if riskandchallenge == []:
            wordsListric = 0
        else:
            for riskchallenge in riskandchallenge: #リスク＆チャレンジの説明文
                richa = riskchallenge.text
            words = nagisa.filter(richa,filter_postags=["助詞","助動詞"])
            wordsList = words.words #リスト型で単語ごとに分けられている
            wordsListric = len(wordsList) #単語の数を数えている
            print("riskandchallenge-words-count:",wordsListric)

        for mogoal in moneygoal:
            mogo = mogoal.text
        mogo = mogo.replace('目標金額 ', '')
        mogo = mogo.replace('円', '')
        mogo = mogo.replace(',', '')
        intmogo = int(mogo) #数字にキャストした
        print("goal-money:",intmogo)  # 目標金額 int型になった

        goalpercent = urlhtml['projects'][idnumber]['percent']
        if goalpercent >= 100: #目標金額に到達したかどうか
            goalflag = 1
        else:
            goalflag = 0
        print(goalflag)

        for packmoney in packagemoney:
            pack = packmoney.text
            pack = pack.replace('(税込)', '')
            pack = pack.replace('円', '')
            pack = pack.replace(',', '')
            intpack = int(pack)
            listpack.append(intpack)

        print("-----------------------------------------------------------------")

        data = [['tagname','moneygoal','image','projectdetail','riskchallengedetail','numberofpackage','moneypackeage','successorfail','category'], #最初の行の書き込みに使用
               [listtag,intmogo,len(lenimg),wordsListpro,wordsListric,len(resection),listpack,goalflag,pro]] #最初の行の書き込みに使用

        # data = [listtag,intmogo,len(lenimg),wordsListpro,wordsListric,len(resection),listpack,goalflag,pro] #２回目以降

        with open(file,'w',encoding="utf_8_sig",newline='') as f:
            csv_writer = csv.writer(f) #最初の書き込みモード
            csv_writer.writerows(data)

        # with open(file,'a',encoding="utf_8_sig",newline='') as f:
        #     csv_writer = csv.writer(f) #２回目以降
        #     csv_writer.writerow(data)
        
        timerandom = random.uniform(3,7) #秒数をランダムに設定しています
        time.sleep(timerandom) #Sleeptimeをしています