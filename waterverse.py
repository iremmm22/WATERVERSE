import sqlite3 as sql


with sql.connect('c:/users/iremmm/desktop/evsel su tüketimi tablosu.sqlite') as vt:
    im = vt.cursor()

    veriler = [('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04)]


    veriler2 = [('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04),
               ('Merkezefendi mahallesi', 5, 21.5, 20.25, 528.04)]


    im.execute("""CREATE TABLE IF NOT EXISTS Evsel Su Tüketimi
        (Mahalle adı, Hanedeki kişi sayısı, Aylık Su Tüketimi, İdeal Su Tüketim Mİktarı, Vergisiz Fatura Tutarı)""")


    for veri in veriler:
        im.execute("""INSERT INTO personel VALUES
            (?, ?, ?, ?, ?)""", veri)

    
    for veri in veriler2:
        im.execute("""INSERT INTO personel VALUES
            (?, ?, ?, ?, ?)""", veri2)

    vt.commit()


    for i in im:
        fatura(i)

    for j in im:
        sayac(j)


def fatura(x):
    im.execute("SELECT * FROM Evsel Su Tüketimi Where Mahalle adı = x")
    deger = im.fetchone()
    aşım_miktarı = deger[2] - deger[3]
    if aşım_miktarı > 0:
        tutar = aşım_miktarı*1.29
        fatura = tutar + deger[4]
        print("Ödenecek fatura tutarı: ",fatura)
    else:
        print("Ödencek fatura tutarı: ", deger[4])


def sayac(x):
    im.execute("SELECT * FROM Evsel Su Tüketimi WHERE Mahalle adı = x")
    deger2 = im.fetchone()
    ceza_miktarı = deger2[2] - deger2[3]
    if ceza_miktarı > 0:
        düşülecek_tutar = ceza_miktarı*1.29
        kullanılabilir_tutar = deger2[4] - düşülecek_tutar
        print("Kullanılabilecek sayaç TL tutarı: ", kullanılabilir_tutar)
    else:
        print("Kullanılabilecek sayaç TL tutaru: ", deger2[4])
