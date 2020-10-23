#wisnuadipradana17@yahoo.com

import tweepy
import sqlite3
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from IPython.display import clear_output
import time 
import progressbar 

class sanbercode():
    def __init__ (self):
        pass
    
    def update_data(self, search_words, date_since, date_until, basisdata):
        tokens = pd.read_csv('API_keysecret.csv')

        consumer_key = tokens.iloc[0][1]
        consumer_secret = tokens.iloc[0][2]
        access_token = tokens.iloc[0][3]
        access_token_secret = tokens.iloc[0][4]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        
        new_search = search_words + " -filter:retweets"

        tweets_covid = tweepy.Cursor(api.search, 
                               q = new_search,
                               tweet_mode='extended',
                               lang='id',
                               since=date_since,
                               until=date_until,
                               result_type='recent',
                               include_entities=True,
                               monitor_rate_limit=True, 
                               wait_on_rate_limit=True).items()
        
        max_value=len([i.id for i in tweets_covid])
        bar = progressbar.ProgressBar(max_value, widgets=widgets).start() 
        
        Tanggal = []; Tweet = []; tweetid = []; username=[]
        for i,tweet in enumerate(tweets_covid):
            Tweet.append(tweet.full_text.strip())
            Tanggal.append(tweet.created_at) 
            tweetid.append(tweet.id)
            username.append(tweet.user.screen_name)
            time.sleep(0.1) 
            bar.update(i) 

        twit_prep = []
        for twit in Tweet:
            Twit=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                                  " ", twit).split())
            twit_prep.append(Twit.lower())
        
        sentiment = [-999 for i in range(len(Tanggal))] 
        input_list = list(zip(tweetid, Tanggal, username, twit_prep, sentiment))
        
        koneksi = sqlite3.connect(basisdata)
        query = '''create table if not exists twitter(
                        Tweet_id INTEGER PRIMARY KEY,
                        Tanggal TEXT,
                        Username TEXT,
                        Tweet TEXT,
                        Sentiment INTEGER);'''
        cursor = koneksi.cursor()
        cursor.execute(query)
        koneksi.commit()
        
        insert_query = '''insert or ignore into twitter(Tweet_id, 
                                        Tanggal, Username, Tweet, Sentiment) values (?,?,?,?,?);'''
        
        cursor.executemany(insert_query, input_list)
        koneksi.commit()
        cursor.close()
        return koneksi
    
    def get_tweetid(self, koneksi):
        query = 'select Tweet_id from twitter'
        cur = koneksi.cursor()
        cur.execute(query)
        tweetid = cur.fetchall()
        cur.close()
        return tweetid
    
    def get_sentiment(self, koneksi):
        query = 'select Sentiment from twitter'
        cur = koneksi.cursor()
        cur.execute(query)
        sentiment = cur.fetchall()
        cur.close()
        return sentiment
    
    def get_tweet(self, koneksi):
        query = 'select Tweet from twitter'
        cur = koneksi.cursor()
        cur.execute(query)
        tweet = cur.fetchall()
        cur.close()
        return tweet
    
    def get_akun(self, koneksi):
        query = 'select Username from twitter'
        cur = koneksi.cursor()
        cur.execute(query)
        username = cur.fetchall()
        cur.close()
        return username
    
    def get_tanggal(self, koneksi):
        query = 'select Tanggal from twitter'
        cur = koneksi.cursor()
        cur.execute(query)
        tanggal = cur.fetchall()
        cur.close()
        return tanggal
    
    def update_nilai_sentiment(self, basisdata):
        koneksi = sqlite3.connect(basisdata)
        
        tweetid = self.get_tweetid(koneksi)
        sentiment = self.get_sentiment(koneksi)
        twet_prep = self.get_tweet(koneksi)
        
        tweetid = [t[0] for t in tweetid]
        sentiment = [t[0] for t in sentiment]
        twet_prep = [t[0] for t in twet_prep]
        
#         nor_list = open("./normalisasi.txt","r")
#         nor_kata = nor_list.readlines()
        
#         list_nor = []
#         for i in nor_kata:
#             list_nor.append([i.split('\t')[0], i.split('\t')[1].strip('\n')])
# #         print(list_nor)
        

#         print(twet_prep[:10])
#         twet_nor = []
#         for twit in twet_prep:
# #             print(twit.split(' '))
#             for i, nor in enumerate(list_nor):
#                 if nor[0] in twit.split(' '): 
#                     twet_nor.append([isi.replace(nor[0],nor[1]) for isi in twit.split(' ')])
#                     print(i, '->', nor[0], '->', [isi.replace(nor[0],nor[1]) for isi in twit.split(' ')])
#             twet_nor.append(twit)
        
#         for i in twet_nor:
#             print(i) 
    
#         twet_normal = [i[0] for i in twet_nor]
#         if 'jgn' in twet_normal:
#             print('ya')
#         print(twet_normal)
        
        pos_list = open("./kata_positif.txt","r")
        pos_kata = pos_list.readlines()
        neg_list = open("./kata_negatif.txt","r")
        neg_kata = neg_list.readlines()
        
        bar = progressbar.ProgressBar(max_value=len(tweetid),widgets=widgets).start()  
        
        hasil_sentiment = []
        for i,item in enumerate(twet_prep):
            count_p = 0; count_n = 0
            for kata_pos in pos_kata:
                if kata_pos.strip() in item:
                    count_p +=1
            for kata_neg in neg_kata:
                if kata_neg.strip() in item:
                    count_n +=1
            hasil_sentiment.append(count_p-count_n)
            time.sleep(0.1) 
            bar.update(i)
        
        input_list = list(zip(hasil_sentiment, tweetid))
        
        query = 'update twitter set Sentiment = ? where Tweet_id = ?;'
        cur = koneksi.cursor()
        cur.executemany(query, input_list) 
        koneksi.commit()
        cur.close() 
    
    def lihat_data(self, basisdata, tanggal_awal, tanggal_akhir):
        koneksi = sqlite3.connect(basisdata)
        
        tanggal = self.get_tanggal(koneksi)
        akun = self.get_akun(koneksi)
        tweet = self.get_tweet(koneksi)
        
        akun = [t[0] for t in akun]
        tweet = [t[0] for t in tweet]
        
        tgl = [t[0].split(' ')[0] for t in tanggal] 
        
        indeks_awal = [i for i, Tgl in enumerate(tgl) if Tgl == tanggal_awal][0]
        indeks_akhir = [i for i, Tgl in enumerate(tgl) if Tgl == tanggal_akhir][0]
        
        entry_akun = [akun[k] for k in range(indeks_awal, indeks_akhir)]
        entry_tanggal = [tgl[k] for k in range(indeks_awal, indeks_akhir)]
        entry_tweet = [tweet[k] for k in range(indeks_awal, indeks_akhir)]
                
        df = pd.DataFrame({'nama akun':entry_akun, 'tanggal tweet':entry_tanggal, 
                           'Tweet':entry_tweet})
        display(df)
    
    def visualisasi(self, basisdata, tanggal_awal, tanggal_akhir):
        koneksi = sqlite3.connect(basisdata)
        
        tanggal = self.get_tanggal(koneksi)
        sentiment = self.get_sentiment(koneksi)
        sentiment = [t[0] for t in sentiment]
        
        tgl = [t[0].split(' ')[0] for t in tanggal] 

        indeks_awal = [i for i, Tgl in enumerate(tgl) if Tgl == tanggal_awal][0]
        indeks_akhir = [i for i, Tgl in enumerate(tgl) if Tgl == tanggal_akhir][0]
                
        entry_sentiment = [sentiment[k] for k in range(indeks_awal, indeks_akhir)]
        
        labels, counts = np.unique(entry_sentiment, return_counts=True)
        plt.subplots(figsize=(12,8), dpi=100)
        plt.bar(labels, counts, align='center')
        plt.gca().set_xticks(labels)
        plt.title('Analisis Sentimen vaksin covid dengan menggunakan media Twitter')

        print("Nilai rata-rata: "+str(np.mean(entry_sentiment)))
        print("Median: "+str(np.median(entry_sentiment)))
        print("Standar deviasi: "+str(np.std(entry_sentiment)))
        
        plt.show()

search_words = 'vaksin covid'
date_since = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
date_until = datetime.now().strftime('%Y-%m-%d')
basisdata = 'wisnuadipradana17.db'

widgets = [' [', progressbar.Timer(format= 'elapsed time: %(elapsed)s'),  '] ', 
           progressbar.Bar('*'),' (', 
           progressbar.ETA(), ') ', ] 

while True:
    print('Apa yang ingin Anda lakukan?')
    print('\t 1. Update Data')
    print('\t 2. Update Nilai Sentiment')
    print('\t 3. Lihat Data')
    print('\t 4. Visualisasi')
    print('\t 5. Keluar')
    a = input('\tInput Anda : ')
    Tugas_akhir = sanbercode()
    if int(a) == 1:
        Tugas_akhir.update_data(search_words, date_since, date_until, basisdata)
        print('\n database telah diupdate\n')
    elif int(a) == 2:
        Tugas_akhir.update_nilai_sentiment(basisdata)
        print('\n sentiment telah diupdate\n')
    elif int(a) == 3:
        tanggal_awal = input('tanggal awal  (format YYYY-MM-DD): ')
        tanggal_akhir = input('tanggal akhir (format YYYY-MM-DD): ')
        Tugas_akhir.lihat_data(basisdata, tanggal_awal, tanggal_akhir)
        print('\n')
    elif int(a) == 4:
        tanggal_awal = input('tanggal awal  (format YYYY-MM-DD): ')
        tanggal_akhir = input('tanggal akhir (format YYYY-MM-DD): ')
        Tugas_akhir.visualisasi(basisdata, tanggal_awal, tanggal_akhir)
        print('\n')
    elif int(a) == 5:
        clear_output(wait = True)
        print('Anda telah keluar dari aplikasi')
        break
    else:
        print('input tidak sesuai\n') 
        pass
