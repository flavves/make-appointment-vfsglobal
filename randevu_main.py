# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:03:53 2022

@author: okmen
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
from selenium.webdriver.chrome.options import Options

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from anasayfa_python import Ui_Widget

import glob


class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_Widget()
            self.ui.setupUi(self)
            
            
            self.ui.KayitEkle.clicked.connect(self.kayitEkle)
            self.ui.KrediKartiEkle.clicked.connect(self.KrediKartiEkle)
            self.ui.Kategori.currentTextChanged.connect(self.Kategori)
            self.ui.AltKategori.currentTextChanged.connect(self.AltKategori)
            self.ui.KrediKartiCheck.stateChanged.connect(self.KrediKartiCheck)
            self.ui.Baslat.clicked.connect(self.Baslat)
            #self.ui.Kayitlar_list.itemSelectionChanged.connect(self.listedegisti)
            self.ui.Kayitlar_list.itemDoubleClicked.connect(self.listedegisti)
            self.ui.yenile.clicked.connect(self.yenile)
            
        
            #kayitlari güncelleme
            
            #kayıtları listede güncelleme
            kayitlar = glob.glob('kayitlar/*.txt')
            
            self.ui.Kayitlar_list.clear()       
            for ekle in kayitlar:
                    kullanici=(ekle.split("\\")[1].split(".txt")[0])
                    dosya=open("kayitlar/"+kullanici+".txt", 'r')
                    kullanici=dosya.readline()
                    dosya.close()
                    kullanici=kullanici.split(";")
                    kullanici.pop(-1)
                    if kullanici[-1]=="0":
                        self.ui.Kayitlar_list.addItem(ekle.split("\\")[1].split(".txt")[0])
                
            
            global secilen_kategori,secilen_alt_kategori,secilen_bolge
            
            
            secilen_bolge=str(self.ui.Bolge.currentIndex())
            secilen_kategori=str(self.ui.Kategori.currentIndex())
            secilen_alt_kategori=str(self.ui.AltKategori.currentIndex())
            
            
            dosyasaat=open("saaticin.txt", 'w')
            dosyasaat.write("1")
            dosyasaat.close()
        
        
        
        
        
        
        
        
        
        
        def Baslat(self):
            global secilen_kategori,secilen_alt_kategori,secilen_bolge,driver
            
            
            
            
            def girisyap(kullanicimail,kullanicisifre):
                global driver
                options = Options()
                options.add_argument("--start-maximized")
                driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
                driver.maximize_window()


                driver.get("https://visa.vfsglobal.com/tur/tr/pol/login")

                time.sleep(2)
                try:
                     element = WebDriverWait(driver, 10).until(
                         EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-input-0"]'))
                     )
                except:
                    pass


                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="mat-input-0"]').click()
                driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(kullanicimail)
                driver.find_element_by_xpath('//*[@id="mat-input-1"]').click()
                driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(kullanicisifre)
                while 1:
                        
                    try:
                         element = WebDriverWait(driver, 0.1).until(
                             EC.element_to_be_clickable((By.CLASS_NAME, 'ngx-overlay'))
                         )
                    except:
                        break
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/app-root/div/app-login/section/div/div/mat-card/form/button').click()
                time.sleep(2)
                while 1:
                        
                    try:
                         element = WebDriverWait(driver, 0.1).until(
                             EC.element_to_be_clickable((By.CLASS_NAME, 'ngx-overlay'))
                         )
                    except:
                        break
                driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
                time.sleep(2)
                while 1:
                        
                    try:
                         element = WebDriverWait(driver, 0.1).until(
                             EC.element_to_be_clickable((By.CLASS_NAME, 'ngx-overlay'))
                         )
                    except:
                        break

                time.sleep(2)
                try:
                    
                    driver.find_element_by_xpath('/html/body/app-root/div/app-dashboard/section/div/div[2]/button/span[1]').click()
                except:
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/app-root/div/app-dashboard/section/div/div[2]/button/span[1]').click()

                
            
            
            
            
            
            #İstanbul Trabzon İzmir Gaziantep kırmızı bölge Ankara Antalya beyaz bölge
            xpath_merkez="/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div"
            xpath_merkez_degisken="/html/body/div[4]/div[2]/div/div/div/mat-option[%s]/span"
            xpath_kategori="/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div"
            xpath_kategori_degisken="/html/body/div[4]/div[2]/div/div/div/mat-option[%s]/span"
            xpath_alt_kategori="/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div"
            xpath_alt_kategori_degisken="/html/body/div[4]/div[2]/div/div/div/mat-option[%s]/span"


            #(xpath_merkez)%2
            
            def bekleme():
                
                while 1:
                        
                    try:
                         element = WebDriverWait(driver, 0.1).until(
                             EC.element_to_be_clickable((By.CLASS_NAME, 'ngx-overlay'))
                         )
                    except:
                        break 
                
            def kategoribeklemekoruma(kategorisecimi):
                try:
                     element = WebDriverWait(driver, 10).until(
                         EC.element_to_be_clickable((By.XPATH, (xpath_kategori_degisken)%kategorisecimi))
                     )
                except:
                    pass

            def merkezbeklemekoruma(merkezsecimi):
                global driver
                try:
                     element = WebDriverWait(driver, 10).until(
                         EC.element_to_be_clickable((By.XPATH, (xpath_merkez_degisken)%merkezsecimi))
                     )
                except:
                    pass

            def altkategoribeklemekoruma(altkategorisecimi):
                try:
                     element = WebDriverWait(driver, 10).until(
                         EC.element_to_be_clickable((By.XPATH, (xpath_alt_kategori_degisken)%altkategorisecimi))
                     )
                except:
                    pass

            def merkezsecimi_dongu(merkezsecimi):
                global driver
                driver.find_element_by_xpath(xpath_merkez).click()
                merkezbeklemekoruma(merkezsecimi)
                driver.find_element_by_xpath((xpath_merkez_degisken)%merkezsecimi).click()
                bekleme()
                
            def kategorisecimi_dongu(kategorisecimi):
                driver.find_element_by_xpath(xpath_kategori).click()
                kategoribeklemekoruma(kategorisecimi)
                driver.find_element_by_xpath((xpath_kategori_degisken)%kategorisecimi).click()
                bekleme()
            
            def altkategorisecimi_dongu(altkategorisecimi):
                driver.find_element_by_xpath(xpath_alt_kategori).click()
                altkategoribeklemekoruma(altkategorisecimi)
                driver.find_element_by_xpath((xpath_alt_kategori_degisken)%altkategorisecimi).click()
                bekleme()
            
            def ilicindongulusecimarama():
                
                if (str(secilen_kategori)=="0"):
                    kategorisecimi=1
                    kategorisecimi_dongu(kategorisecimi)
                    
                    #burayı döngüye almak zorundayım çünkü alt kategoride bir ileri bir geri yapacak
                    bak=True                   
                    while 1:
                        if bak == True:
                                
                            if (str(secilen_alt_kategori)=="0"):
                                altkategorisecimi=1
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            elif (str(secilen_alt_kategori)=="1"):
                                altkategorisecimi=2
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="2"):                        
                                altkategorisecimi=3
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            bekleme()    
                            randevu_durumu=driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').get_attribute('disabled')
                                
                            if (randevu_durumu != "true") and (bak == True):
                               
                            
                                bekleme()
                                driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').click()
                                break    
                            else:
                                bak=False
                        else:
                            
                            if (str(secilen_alt_kategori)=="0"):
                                altkategorisecimi=2
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            elif (str(secilen_alt_kategori)=="1"):
                                altkategorisecimi=3
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="2"):                        
                                altkategorisecimi=1
                                altkategorisecimi_dongu(altkategorisecimi)
                            bak=True
                                
                        
                        
                        
                elif (str(secilen_kategori)=="1"):
                    kategorisecimi=2
                    kategorisecimi_dongu(kategorisecimi)
                    
                    bak=True                   
                    while 1:
                        if bak == True:
                                
                            if (str(secilen_alt_kategori)=="0"):
                                altkategorisecimi=1
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            elif (str(secilen_alt_kategori)=="1"):
                                altkategorisecimi=2
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="2"):                        
                                altkategorisecimi=3
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="3"):                        
                                altkategorisecimi=4
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            bekleme()    
                            randevu_durumu=driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').get_attribute('disabled')
                                
                            if (randevu_durumu != "true") and (bak == True):
                            
                            
                                bekleme()
                                driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').click()
                                break    
                            else:
                                bak=False
                        else:
                            
                            if (str(secilen_alt_kategori)=="0"):
                                altkategorisecimi=2
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            elif (str(secilen_alt_kategori)=="1"):
                                altkategorisecimi=3
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="2"):                        
                                altkategorisecimi=4
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="3"):                        
                                altkategorisecimi=1
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            bak=True
                    
            
            def ilsecimi():
              
                if (str(secilen_bolge)=="2"):
                    merkezsecimi_dongu(1)         
                    ilicindongulusecimarama() 
                elif (str(secilen_bolge)=="3"):
                    merkezsecimi_dongu(2)         
                    ilicindongulusecimarama()
                elif (str(secilen_bolge)=="4"):
                    merkezsecimi_dongu(3)         
                    ilicindongulusecimarama()
                elif (str(secilen_bolge)=="5"):
                    merkezsecimi_dongu(4)         
                    ilicindongulusecimarama()
                elif (str(secilen_bolge)=="6"):
                    merkezsecimi_dongu(5)         
                    ilicindongulusecimarama()
                elif (str(secilen_bolge)=="7"):
                    merkezsecimi_dongu(6)         
                    ilicindongulusecimarama()


            def beyazbolge():
                global driver
            
                merkezsecimi=1
                while 1:
                    merkezsecimi_dongu(merkezsecimi)
           
                    if (str(secilen_kategori)=="0"):
                        kategorisecimi=1
                        kategorisecimi_dongu(kategorisecimi)
                        
                        if (str(secilen_alt_kategori)=="0"):
                            altkategorisecimi=1
                            altkategorisecimi_dongu(altkategorisecimi)
                            
                        elif (str(secilen_alt_kategori)=="1"):
                            altkategorisecimi=2
                            altkategorisecimi_dongu(altkategorisecimi)
                        elif (str(secilen_alt_kategori)=="2"):                        
                            altkategorisecimi=3
                            altkategorisecimi_dongu(altkategorisecimi)
                            
                        bekleme()    
                        randevu_durumu=driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').get_attribute('disabled')
                            
                        if randevu_durumu != "true":
                            
                        
                            bekleme()
                            driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').click()
                            break
                            
                    elif (str(secilen_kategori)=="1"):
                        kategorisecimi=2
                        kategorisecimi_dongu(kategorisecimi)
                        
                        if (str(secilen_alt_kategori)=="0"):
                            altkategorisecimi=1
                            altkategorisecimi_dongu(altkategorisecimi)
                            
                        elif (str(secilen_alt_kategori)=="1"):
                            altkategorisecimi=2
                            altkategorisecimi_dongu(altkategorisecimi)
                        elif (str(secilen_alt_kategori)=="2"):
                            altkategorisecimi=3
                            altkategorisecimi_dongu(altkategorisecimi)
                        elif (str(secilen_alt_kategori)=="3"):
                            altkategorisecimi=4
                            altkategorisecimi_dongu(altkategorisecimi)
                            
                        bekleme()    
                        randevu_durumu=driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').get_attribute('disabled')
                            
                        if randevu_durumu != "true":
                         
                            
                            bekleme()
                            driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').click()
                            break
                        
                    merkezsecimi=merkezsecimi+1
                    if merkezsecimi==3:
                        merkezsecimi=1
                
            def kirmizibolge():
               
                merkezsecimi=3
                while 1:
                        merkezsecimi_dongu(merkezsecimi)
                        if (str(secilen_kategori)=="0"):
                            kategorisecimi=1
                            kategorisecimi_dongu(kategorisecimi)
                            
                            if (str(secilen_alt_kategori)=="0"):
                                altkategorisecimi=1
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            elif (str(secilen_alt_kategori)=="1"):
                                altkategorisecimi=2
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="2"):                        
                                altkategorisecimi=3
                                altkategorisecimi_dongu(altkategorisecimi)
                            
                            bekleme()    
                            randevu_durumu=driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').get_attribute('disabled')
                                
                            if randevu_durumu != "true":
                             
                            
                                bekleme()
                                driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').click()
                                break
                                
                        elif (str(secilen_kategori)=="1"):
                            kategorisecimi=2
                            kategorisecimi_dongu(kategorisecimi)
                            
                            if (str(secilen_alt_kategori)=="0"):
                                altkategorisecimi=1
                                altkategorisecimi_dongu(altkategorisecimi)
                                
                            elif (str(secilen_alt_kategori)=="1"):
                                altkategorisecimi=2
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="2"):
                                altkategorisecimi=3
                                altkategorisecimi_dongu(altkategorisecimi)
                            elif (str(secilen_alt_kategori)=="3"):
                                altkategorisecimi=4
                                altkategorisecimi_dongu(altkategorisecimi)
                            
                            bekleme()    
                            randevu_durumu=driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').get_attribute('disabled')
                                
                            if randevu_durumu != "true":
                               
                            
                                bekleme()
                                driver.find_element_by_xpath('/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button').click()
                                break
                            
                        merkezsecimi=merkezsecimi+1
                        if merkezsecimi==7:
                            merkezsecimi=3
                        
                        
                        
            def bilgileridoldur(kullanici):
                
                 Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
                 kullanici[0].lower().translate(Tr2Eng)
                 
                 
                 bekleme()
                 driver.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(kullanici[0].lower().translate(Tr2Eng))
                 #soyad
                 
                 driver.find_element_by_xpath('//*[@id="mat-input-3"]').send_keys(kullanici[1].lower().translate(Tr2Eng))
                 bekleme()
                 #cinsiyet tıklama ardından seçme
                 driver.find_element_by_xpath('//*[@id="mat-select-value-7"]').click()
                 bekleme()
                 if (kullanici[2].lower())=="kadın":
                     
                     driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/mat-option[1]/span').click()
                     
                 else:
                     driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/mat-option[2]/span').click()
                     
                     
                 #dgko tarihi
                 driver.find_element_by_xpath('//*[@id="dateOfBirth"]').send_keys(kullanici[3])
                 
                 #uyruk seçme
                 driver.find_element_by_xpath('/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[5]/div/div/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]').click()
                 #dogru uyruk bulma
                 bekleme()
                 for i in range(1,237):
                     
                     durum=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/mat-option['+str(i)+']').text==kullanici[4].upper()
                     if durum==True:
                         
                         driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/mat-option['+str(i)+']').click()
                         break
                 
                 #pasaport no
                 driver.find_element_by_xpath('//*[@id="mat-input-4"]').send_keys(kullanici[5])
                 #pasaport tarih
                 
                 driver.find_element_by_xpath('//*[@id="passportExpirtyDate"]').send_keys(kullanici[6])

                 #tel no alan
                 
                 driver.find_element_by_xpath('//*[@id="mat-input-5"]').send_keys(kullanici[7])
                 #tel no
                 
                 driver.find_element_by_xpath('//*[@id="mat-input-6"]').send_keys(kullanici[8])
                 #email
                 
                 driver.find_element_by_xpath('//*[@id="mat-input-7"]').send_keys(kullanici[9])
                 
                 driver.find_element_by_xpath('/html/body/app-root/div/app-applicant-details/section/mat-card[2]/app-dynamic-form/div/div/app-dynamic-control/div/div/div[2]/button/span[1]').click()
                 bekleme()
            def basvuruyap():
                # basvuru onayla butonu
                bekleme()
                driver.find_element_by_xpath('/html/body/app-root/div/app-applicant-details/section/mat-card[2]/div[2]/div[2]/button').click()
                bekleme()

                #gün seçiyoruz 
                driver.find_element_by_class_name("fc-daygrid-day.fc-day.fc-day-mon.fc-day-future.date-availiable").click()
                bekleme()
                #saat sorununu cozmek icin
                
                dosyasaat=open("saaticin.txt", 'r')
                saat_icin=dosyasaat.readline()
                dosyasaat.close()
                saat_icin=str(saat_icin)
                
                
                def saattiklama(veri):
                    #saat
                    
                    try:driver.find_element_by_xpath('//*[@id="STRadio'+str(veri)+'"]').click()
                    except:
                        try:driver.find_element_by_xpath('//*[@id="STRadio'+str(veri+1)+'"]').click()
                        except:
                            try:driver.find_element_by_xpath('//*[@id="STRadio'+str(veri+2)+'"]').click()
                            except:
                                try:driver.find_element_by_xpath('//*[@id="STRadio'+str(veri+3)+'"]').click()
                                except:pass
                                
                if saat_icin=="1":
                    saattiklama(1)
                    
                    dosyasaat=open("saaticin.txt", 'w')
                    dosyasaat.write("2")
                    dosyasaat.close()
                    
                elif saat_icin=="2":
                    saattiklama(2)
                    dosyasaat=open("saaticin.txt", 'w')
                    dosyasaat.write("3")
                    dosyasaat.close()
                    
                elif saat_icin=="3":
                    saattiklama(3)
                    dosyasaat=open("saaticin.txt", 'w')
                    dosyasaat.write("4")
                    dosyasaat.close()
                
                elif saat_icin=="4":
                    saattiklama(4)
                    dosyasaat=open("saaticin.txt", 'w')
                    dosyasaat.write("5")
                    dosyasaat.close()
                    
                
                
                
                
                
                bekleme()
                #onayla
                driver.find_element_by_xpath('/html/body/app-root/div/app-book-appointment/section/mat-card[2]/div/div[2]/button/span[1]').click()
                bekleme()
                #check boxlar
                
                driver.find_element_by_xpath('/html/body/app-root/div/app-review-and-payment/section/form/mat-card[1]/div[8]/div/mat-checkbox/label/span[1]').click()
                driver.find_element_by_xpath('/html/body/app-root/div/app-review-and-payment/section/form/mat-card[1]/div[9]/mat-checkbox/label/span[1]').click()
            
                #onayla
                bekleme()
                driver.find_element_by_xpath('/html/body/app-root/div/app-review-and-payment/section/form/mat-card[2]/div/div[2]/button/span[1]').click()
                
            
            def kartbilgilerigir(kredikarti):
                #bekle
                try:
                     element = WebDriverWait(driver, 60).until(
                         EC.element_to_be_clickable((By.XPATH, '/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[1]/td[3]/input'))
                     )
                except:
                    pass
  
                #kart kısmı

                #numara
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[1]/td[3]/input').send_keys(kredikarti[0])
                #ay          
                ay=str(int(kredikarti[1]))     
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/select[1]/option['+ay+']').click()            
                #yıl          
                yıl=kredikarti[2]               
                yıl=str(int(yıl)-21) 
 
                
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/select[2]/option['+yıl+']').click()
                #cvv
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[3]/td[3]/input').send_keys(kredikarti[3])
                #ad soyad
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[7]/td[3]/input').send_keys(kredikarti[4])
                #adres
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[8]/td[3]/input').send_keys(kredikarti[5])
                #sehir postakodu
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[9]/td[3]/input').send_keys(kredikarti[6])
                #aynıysa tıkla check box
                driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[11]/td[3]/input').click()
                #gönder
                driver.find_element_by_xpath('//*[@id="btnSbmt"]').click()
                
                
            #veri alma yeri
            
            try:
                    
                kayitlar = glob.glob('kayitlar/*.txt')
                
                for ekle in kayitlar:
                    kullanici=(ekle.split("\\")[1].split(".txt")[0])
                    
                
                    dosya=open("kayitlar/"+kullanici+".txt", 'r')
                    kullanici=dosya.readline()
                    dosya.close()
                    kullanici=kullanici.split(";")
                    kullanici.pop(-1)
                    
                    
                    
                    if kullanici[-1]=="0":
                        
                        girisyap(kullanici[10],kullanici[11])
                        
                        bekleme()
                        
                        if (str(secilen_bolge)=="0"):
                            beyazbolge()
                        elif (str(secilen_bolge)=="1"):
                            kirmizibolge()
        
                        bekleme()
                        bilgileridoldur(kullanici)
                        basvuruyap()
                        
                        dosya=open("kredikarti/kredikarti.txt", 'r')
                        kredikarti=dosya.readline()
                        dosya.close()
                        kredikarti=kredikarti.split(";")
                        kredikarti.pop(-1)
                        time.sleep(1)
                        kartbilgilerigir(kredikarti)
                        
                        
                        
                        winsound.PlaySound('uyari.wav', winsound.SND_FILENAME) 
                        
                        print("Ödeme YAPABİLDİYSENİZ ise 1 tusuna basıp enter tusuna basınız.")
                        
                        secim=input("lütfen seçimizi yapın siz seçim yapana kadar program hazırda bekleyecek: ")
                        
                        if secim=="1":
                            
                            kullanici[-1]="1"
                            kullanici_txt=(ekle.split("\\")[1].split(".txt")[0])
                            
                            dosya=open("kayitlar/"+kullanici_txt+".txt", 'w')
                            for guncelle in kullanici:
                                guncelle=str(guncelle)
                                dosya.write(guncelle+";")
                            dosya.close()
                       
                            
                        driver.close()
                        
            except Exception as e:
                self.ui.HataKodu.setText(str(e))

                

        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def KrediKartiCheck(self):
           
            if self.ui.KrediKartiCheck.isChecked()==True:
                    
                #kayıtları listede güncelleme
                self.ui.KrediKartiList.clear()
                dosya=open("kredikarti/kredikarti.txt", 'r')
                okudum=dosya.readline()
                dosya.close()
                okudum=okudum.split(";")             
                okudum.pop(-1)
                self.ui.KrediKartiList.addItem("Kart No:"+okudum[0])
                self.ui.KrediKartiList.addItem("Ay:"+okudum[1])
                self.ui.KrediKartiList.addItem("Yıl:"+okudum[2])
                self.ui.KrediKartiList.addItem("Kod:"+okudum[3])
                self.ui.KrediKartiList.addItem("Ad::"+okudum[4])
                self.ui.KrediKartiList.addItem("Adres:"+okudum[5])
                self.ui.KrediKartiList.addItem("Posta:"+okudum[6])
            else:
                self.ui.KrediKartiList.clear()
                
            
            
        def AltKategori(self):
            
            global secilen_kategori,secilen_alt_kategori,secilen_bolge
            
            
            secilen_bolge=str(self.ui.Bolge.currentIndex())
            secilen_kategori=str(self.ui.Kategori.currentIndex())
            secilen_alt_kategori=str(self.ui.AltKategori.currentIndex())
            
      
            
        #####################################################3
        def Kategori(self):
            
            global secilen_kategori,secilen_alt_kategori,secilen_bolge
            
            secilenIndex = self.ui.Kategori.currentIndex()
            
            secilen_bolge=str(self.ui.Bolge.currentIndex())
            secilen_kategori=str(self.ui.Kategori.currentIndex())
            secilen_alt_kategori=str(self.ui.AltKategori.currentIndex())
            
            
            if secilenIndex==0:
                self.ui.AltKategori.clear()
                self.ui.AltKategori.addItem("Yuksek Öğrenim")
                self.ui.AltKategori.addItem("Çalışma İzni")
                self.ui.AltKategori.addItem("Diğer Uzun Dönem")
            if secilenIndex==1:
                self.ui.AltKategori.clear()
                self.ui.AltKategori.addItem("İş Seyehati")
                self.ui.AltKategori.addItem("Turistlik")
                self.ui.AltKategori.addItem("Tir Soforu")
                self.ui.AltKategori.addItem("Diğer Kısa Dönem")
            
            

        #######################################################################
        def KrediKartiEkle(self):
            
            
            kartno=str(self.ui.kartno.text())
            ay=str(self.ui.ay.text())
            yil=str(self.ui.yil.text())
            kod=str(self.ui.kod.text())
            adisoyadi=str(self.ui.adisoyadi.text())
            adres=str(self.ui.adres.text())
            postakodu=str(self.ui.postakodu.text())
            
            dosya=open("kredikarti/kredikarti.txt", 'w')
            
            dosya.write(kartno+";"+ay+";"+yil+";"+kod+";"+adisoyadi+";"+adres+";"+postakodu+";")
            dosya.close()
            QMessageBox.about(self, "Kayit", "Basarili")
        
            #kayıtları listede güncelleme
            if self.ui.KrediKartiCheck.isChecked()==True:
                dosya=open("kredikarti/kredikarti.txt", 'r')
                okudum=dosya.readline()
                dosya.close()
                okudum=okudum.split(";")             
                okudum.pop(-1)
                self.ui.KrediKartiList.addItem("Kart No:"+okudum[0])
                self.ui.KrediKartiList.addItem("Ay:"+okudum[1])
                self.ui.KrediKartiList.addItem("Yıl:"+okudum[2])
                self.ui.KrediKartiList.addItem("Kod:"+okudum[3])
                self.ui.KrediKartiList.addItem("Ad::"+okudum[4])
                self.ui.KrediKartiList.addItem("Adres:"+okudum[5])
                self.ui.KrediKartiList.addItem("Posta:"+okudum[6])
        
        #######################################################################
        def kayitEkle(self):
            isim=str(self.ui.giris1.text())
            soyad=str(self.ui.giris2.text())
            cinsiyet=str(self.ui.giris3.text())
            dogumtarihi=str(self.ui.giris4.text())
            uyruk=str(self.ui.giris5.text())
            pasaportno=str(self.ui.giris6.text())
            pasaporttarih=str(self.ui.giris7.text())
            telalankodu=str(self.ui.giris8.text())
            telno=str(self.ui.giris9.text())
            email=str(self.ui.giris10.text())
            mail_txt=str(self.ui.vfsmail.text())
            sifre_txt=str(self.ui.vfssifre.text())
            kayitonay="0"
            
            
            
            dosya=open("kayitlar/"+isim+soyad+".txt", 'w')
            dosya.write(isim+";"+soyad+";"+cinsiyet+";"+dogumtarihi+";"+uyruk+";"+pasaportno+";"+pasaporttarih+";"+telalankodu+";"+telno+";"+email+";"+mail_txt+";"+sifre_txt+";"+kayitonay+";")
            dosya.close()
            QMessageBox.about(self, "Kayit", "Basarili")
            
            #kayıtları listede güncelleme
            kayitlar = glob.glob('kayitlar/*.txt')
            
            self.ui.Kayitlar_list.clear()       
            for ekle in kayitlar:
                    kullanici=(ekle.split("\\")[1].split(".txt")[0])
                    dosya=open("kayitlar/"+kullanici+".txt", 'r')
                    kullanici=dosya.readline()
                    dosya.close()
                    kullanici=kullanici.split(";")
                    kullanici.pop(-1)
                    if kullanici[-1]=="0":
                        self.ui.Kayitlar_list.addItem(ekle.split("\\")[1].split(".txt")[0])
            
            
            
        def yenile(self):
            
            #kayıtları listede güncelleme
            kayitlar = glob.glob('kayitlar/*.txt')
            
            self.ui.Kayitlar_list.clear()       
            for ekle in kayitlar:
                    kullanici=(ekle.split("\\")[1].split(".txt")[0])
                    dosya=open("kayitlar/"+kullanici+".txt", 'r')
                    kullanici=dosya.readline()
                    dosya.close()
                    kullanici=kullanici.split(";")
                    kullanici.pop(-1)
                    if kullanici[-1]=="0":
                        self.ui.Kayitlar_list.addItem(ekle.split("\\")[1].split(".txt")[0])
            
        
        
        def listedegisti(self,item):
            guncelleme=str(item.text())
            
            dosya2=open("kayitlar/"+guncelleme+".txt", 'r')
            okudum_gece=dosya2.readline()
            okudum_gece=okudum_gece.split(";")
            
            self.ui.giris1.setText(okudum_gece[0])
            self.ui.giris2.setText(okudum_gece[1])
            self.ui.giris3.setText(okudum_gece[2])
            self.ui.giris4.setText(okudum_gece[3])
            self.ui.giris5.setText(okudum_gece[4])
            self.ui.giris6.setText(okudum_gece[5])
            self.ui.giris7.setText(okudum_gece[6])
            self.ui.giris8.setText(okudum_gece[7])
            self.ui.giris9.setText(okudum_gece[8])    
            self.ui.giris10.setText(okudum_gece[9])  
            self.ui.vfsmail.setText(okudum_gece[10])
            self.ui.vfssifre.setText(okudum_gece[11])

            
            
            
            
            
            
        #######################################################################



if __name__ == "__main__":
        app = QApplication(sys.argv)
    
        window = MainWindow()
        window.setWindowTitle("Randevu Alma Programı")
        window.show()
    
        sys.exit(app.exec_())























