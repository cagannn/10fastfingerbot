import cv2
import pytesseract as tes
import numpy as np
import pyautogui
import time as tm

kelime=" "
yedek=''
sayac=0
Boz=True
while Boz:
    im1=pyautogui.screenshot(region=(446,240, 975,85))  #10fastfinger sitesindeki yazıların olduğu pixelerin kordinatlarını ekran görüntüsü alıyoruz
    im1.save("C:\\Users\\....")  #Aldığımız ekran görüntüsünü hangi dizine kayıt edeceğimizi seçiyoruz
    screenshot="C:\\Users\\...." #Aldığımız ekran görüntüsünün yolunu bir değişkene atıyoruz üsteki ile aynı olmalı
    tes.pytesseract.tesseract_cmd="C:\\Users\\kullaniciadin\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe" #tesseract.exe'nin bulunduğu dizini belirtiyoruz
    resim=cv2.imread(screenshot)       #Opencv ile ekran görüntüsünü değişkene atıyoruz
    metin=tes.image_to_string(resim)   #Tesseract kütüphanesi ile çekilen ekran görüntüsünüdeki yazıları stringe çeviriyoruz
    tm.sleep(0.5)                      
    for i in metin:
        yedek=i                                 #Oluşturduğumu stringin içindeki kelimeleri ayırıp 
        kelime=kelime+yedek                     #teker teker yazması için for döngüsü oluşturuyoruz
        yedek=''
        if i == '\n': #10fastfinger sitesi 2 satırlı olduğu için üst satırı yazıp enter'a basınca kelimeler kayıyor
            i=' '      #bu nedenle enter gördüğümüz yeri boşluğa çeviriyoruz
        if i==' ':
            pyautogui.typewrite(kelime) #Kelimemizi yazıyoruz
            print(kelime)
            kelime=" "       #Baştaki kelimeyi tekrar tekrar yazmaması içim kelime değişkenini boş hale getiriyoruz.
    sayac=sayac+1           #While döngüsünü sonlandırmak adına bir sayaç oluşturuyoruz
    pyautogui.hotkey('space') #Son kelimeden sonra space bastırıyoruz 
    if sayac==14:         #Sayaç 14'e ulaşınca döngüyü sonlandırıyoruz.
        Boz=False
 
