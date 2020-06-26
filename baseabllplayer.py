# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv

# ブラウザのオプションを格納する変数をもらってきます。
options = Options()
# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
options.set_headless(True)
# ブラウザを起動する
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(executable_path='/Users/sugamayuusuke/Documents/chromedriver')
#driver = webdriver.Chrome(executable_path = 'C:/Documents/chromedriver')

# ブラウザでアクセスする
url = 'https://www.nikkansports.com/baseball/professional/player/tigers/'
driver.get(url)
#読込が完了するまで待つ
time.sleep(10)
# HTMLを文字コードをUTF-8に変換してから取得します。
html = driver.page_source.encode('utf-8')
# BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(html, "html.parser")

#選手の取得URL生成
header = ['背番号','氏名','カナ','出身校','誕生日','年齢','血液型','身長','体重','所属履歴','キャリア','投打','ドラフト年度','ドラフト順位','公式戦初出場','年俸','昨季年俸','タイトル','家族','寸評']
playerUrl =[]
for player in soup.find_all("div", class_='playerBox'): #その領域内をすべて調べる
    for link in player.find_all('a'):
        playerUrl.append(url + link.get('href'))

# CSVファイルを開く。ファイルがなければ新規作成する。
f = open("output.csv", "w", encoding='UTF-8') 
writecsv = csv.writer(f, lineterminator='\n')
#ヘッダーを出力
writecsv.writerow(header)
for pUrl in playerUrl:
    #seleniumでアクセス
    driver.get(pUrl)
    #読込が完了するまで待つ
    time.sleep(3)
    # HTMLを文字コードをUTF-8に変換してから取得します。
    html = driver.page_source.encode('utf-8')
    # BeautifulSoupで扱えるようにパースします
    pSoup = BeautifulSoup(html, "html.parser")

    playerValue = []
    
    for player in pSoup.find_all("table", id='plyIndvData'):
        for value in player.find_all('td'):
            playerValue.append(value.getText().replace('\u3000', ' '))
    print(playerValue)
    # 出力
    writecsv.writerow(playerValue)
# CSVファイルを閉じる。
f.close()

#ブラウザを閉じる
driver.close()



