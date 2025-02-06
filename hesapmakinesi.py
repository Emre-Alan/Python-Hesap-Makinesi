# tkinter modülünden her şeyi içe aktarın 
from tkinter import *
 
# gelen_ifade değişkenini global olarak ayarlayın
gelen_ifade = "" 
 
# gelen_ifade  güncelleme fonksiyonu
def islem(sayi): 
    
    global gelen_ifade 
 
    # dize birleştirin 
    gelen_ifade = gelen_ifade + str(sayi) 
 
    # set metodunu kullanarak gelen_ifade yi güncelleyin 
    denklem.set(gelen_ifade) 
 
 
# Son ifadeyi değerlendirmek için fonksiyon 
def sonuc(): 
    #oluşabilecek hataları engelleyin.
    try: 
 
        global gelen_ifade 
 
        # eval fonksiyonu ifadeyi değerlendirir
        # ve str fonksiyonu sonucu dönüştürür
        total = str(eval(gelen_ifade)) 
 
        denklem.set(total) 
 
        # gelen_ifade içerisini boşaltalım
        gelen_ifade = "" 
 
    # eğer hata oluşursa, o zaman işlem yap
    except: 
 
        denklem.set(" Hata ") 
        gelen_ifade = "" 

# İçeriği temizleme işlevi
# metin giriş kutusu
def silmek(): 
    global gelen_ifade 
    gelen_ifade = "" 
    denklem.set("") 
 
 
# bir GUI penceresi oluşturun 
pencere = Tk() 
 
#GUI penceresinin arka plan rengini ayarlayın 
pencere.configure(background="gray90") 
 
# GUI penceresinin başlığını ayarlayın
pencere.title("Hesap Makinesi") 
 
# GUI penceresinin boyutunu ayarlayın
pencere.geometry("350x400") 

#Ekran Boyutunun ayarlanmasını kapatın
pencere.resizable(False, False) 
 
# StringVar() değişken sınıfıdır
denklem = StringVar() 
 
# ekran için metin giriş kutusu oluştur. 
#justify ,bu seçenek metnin nasıl hizalanacağını denetler: ORTA, SOL veya SAĞ.
ekran = Entry(pencere, textvariable=denklem,font="Arial 20",justify=RIGHT) 
 
# grid yöntemi, tablo benzeri bir yapıdır
# widget'ları ilgili pozisyonlara
# yerleştirmek için kullanılır.
ekran.grid(columnspan=3, ipadx=15)
 
# Bir Düğme oluşturun ve kök penceresinin belirli bir
# konumuna yerleştirin.
# Kullanıcı düğmeye bastığında, o düğmeye bağlı komut veya
# fonksiyon yürütülür.

#Birinci Satır
button1 = Button(pencere, text=' 1 ', fg='white', bg='gray50',command=lambda: islem(1), font= ('Helvetica 20 bold'),width=6) 
button1.grid(row=2, column=0) 

button2 = Button(pencere, text=' 2 ',fg='white', bg='gray50',command=lambda: islem(2), font= ('Helvetica 20 bold'),width=6) 
button2.grid(row=2, column=1) 
 
button3 = Button(pencere, text=' 3 ', fg='white', bg='gray50',command=lambda: islem(3),font= ('Helvetica 20 bold'),width=6) 
button3.grid(row=2, column=2)   
 
#ikinci satır
button4 = Button(pencere, text=' 4 ',fg='white', bg='gray50',command=lambda: islem(4), font= ('Helvetica 20 bold'),width=6) 
button4.grid(row=3, column=0) 
 
button5 = Button(pencere, text=' 5 ', fg='white', bg='gray50',command=lambda: islem(5), font= ('Helvetica 20 bold'),width=6) 
button5.grid(row=3, column=1) 
 
button6 = Button(pencere, text=' 6 ', fg='white', bg='gray50',command=lambda: islem(6), font= ('Helvetica 20 bold'),width=6) 
button6.grid(row=3, column=2)   
  
#Üçüncü satır
button7 = Button(pencere, text=' 7 ', fg='white', bg='gray50',command=lambda: islem(7), font= ('Helvetica 20 bold'),width=6) 
button7.grid(row=4, column=0) 
 
button8 = Button(pencere, text=' 8 ', fg='white', bg='gray50',command=lambda: islem(8), font= ('Helvetica 20 bold'),width=6) 
button8.grid(row=4, column=1) 
 
button9 = Button(pencere, text=' 9 ', fg='white', bg='gray50',command=lambda: islem(9), font= ('Helvetica 20 bold'),width=6) 
button9.grid(row=4, column=2) 
    
#Dördüncü satır 
button0 = Button(pencere, text=' 0 ', fg='white', bg='gray50',command=lambda: islem(0), font= ('Helvetica 20 bold'),width=6) 
button0.grid(row=5, column=0) 

plus = Button(pencere, text=' + ', fg='white', bg='gray25',command=lambda: islem("+"), font= ('Helvetica 20 bold'),width=6) 
plus.grid(row=5, column=1) 

divide = Button(pencere, text=' / ', fg='white', bg='gray25',command=lambda: islem("/"), font= ('Helvetica 20 bold'),width=6) 
divide.grid(row=5, column=2) 

#Beşinci satır 
Decimal= Button(pencere, text='.', fg='white', bg='gray25',command=lambda: islem('.'), font= ('Helvetica 20 bold'),width=6) 
Decimal.grid(row=6, column=0) 

minus = Button(pencere, text=' - ', fg='white', bg='gray25',command=lambda: islem("-"), font= ('Helvetica 20 bold'),width=6) 
minus.grid(row=6, column=1) 

multiply = Button(pencere, text=' * ', fg='white', bg='gray25',command=lambda: islem("*"), font= ('Helvetica 20 bold'),width=6) 
multiply.grid(row=6, column=2) 

#Altıncı satır
sil = Button(pencere, text='Sil', fg='white', bg='Orange red',command=silmek, font= ('Helvetica 20 bold'),width=6) 
sil.grid(row=7, column=0)
 
equal = Button(pencere, text=' = ', fg='white', bg='Orange red',command=sonuc, font= ('Helvetica 20 bold')) 
equal.grid(row=7, column=1,columnspan=2,ipadx=85)

# GUI'yi başlat
pencere.mainloop() 