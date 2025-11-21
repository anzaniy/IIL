#spesial chapter with erika, bisa ditambahin cutscene bonus 1 or 2 di akhir
#bikin cabang dengan waktu yang sama dengan Revina
label chapter_4:
    "Chapter 4"
    scene bg night city
    show erika base
    e "Dika, kamu pulang kearah mana?"
    d "Kosanku ada di jalan Aiko, depan sana"
    menu:
        "Emangnya kenapa ?":
            jump erieri
        "Kalau gitu, aku duluan ya, hati-hati di jalan":
            jump chapter_5
label erieri:
    e "Kebetulan aku juga lewat sana"
    show erika happy
    e "Untung saja kamu searah denganku"
    menu:
        "Emang kamu gabisa pulang malem-malem kah ?":
            jump tanya_erika
        "Emangnya kenapa ?":
            jump tanya_erika
label tanya_erika:
    show erika base
    e "Bisa sih, tapi pulang sendiri itu yang bikin susah, kamu kan tahu juga aku perempuan"
    #scene jalan-jalan
    e "Jujur, aku suka banget geometri"
    e "Bahkan semua hal itu kalo dikaitin sama matematika itu menurutku asik banget"
    #bingung
    show erika happy
    e "Kayak misal contoh kamu tahu gak, rumus jarak dalam menghitung geometri dalam garis itu gimana"
    menu:
        "......":
            jump chapter_4_1
        "Lumayan panjang sih itu rumusnya":
            jump chapter_4_1
label chapter_4_1:
    show erika base
    e "Rumus matematika itu ya kalo diinget apalagi rumus yang panjang, itu belibet banget"
    e "Tapi kamu tahu gak sih klo rumus belibet itu bisa dipermudah mengingatnya kalau kita misalkan"
    e "Seperti contoh..."
    # show erika base at left
    hide erika
    image jarak satu  = im.Scale("images/Materi/jarak_1.png", 1100, 500)
    show jarak satu at truecenter
    e "Bayangkan A dan B itu dua orang, mungkin kamu dan temanmu."
    e "Kalian berdiri di tempat yang berbeda di peta kota, dengan koordinat masing-masing: A di (x₁, y₁), dan B di (x₂, y₂)."

    e "Sekarang kamu ingin tahu, seberapa jauh sih jarakmu dari dia?"
    e "Itu kita sebut r yang merupakan jarak langsung dari titik A ke B."

    e "Tapi bukan cuma soal jarak."
    e "Bayangkan kamu berjalan dari A ke B, dan kamu lihat arah langkahmu membentuk sudut θ terhadap arah timur."
    e "Sudut ini kita sebut {color=#00f}sudut inklinasi{/color} — arah perjalananmu."

    e "Kalau kamu pecah perjalananmu jadi arah kanan-kiri dan atas-bawah..."
    e "Bagian ke kanan adalah r cos θ, yang sama dengan x₂ - x₁."
    e "Dan bagian ke atas adalah r sin θ, yaitu y₂ - y₁."

    e "Nah, kayak kamu naik tangga — kamu tahu tinggi dan panjang langkahmu, tapi ingin tahu berapa panjang miringnya."
    e "Maka kamu pakai {color=#00f}rumus Pythagoras{/color}."

    e "r² = (x₂ - x₁)² + (y₂ - y₁)²"

    e "Dan karena cos² θ + sin² θ = 1, hasil akhirnya tetap r²."

    e "Jadi, untuk tahu jarakmu ke seseorang... kamu cukup tahu posisi kalian berdua."

    e "Hidup juga gitu, kan?"
    e "Kadang kita gak tahu seberapa jauh kita dari tujuan, tapi kalau kita tahu posisi kita sekarang dan tahu arah, kita bisa hitung sendiri jaraknya."

    show erika happy
    e "Dan itulah gunanya koordinat."
    show erika base
    e "Jadi kalau misalnya ditanya carilah jarak antara titik (-2,1) dan (4,9)"
    e "Gampang kan tinggal dimasukin aja jadi =√36+64"
    e "Dapetlah 10"
    hide jarak satu
    hide erika
    show erika sad
    e "Aduh, maaf ya aku kebanyakan ngoceh dijalan"
    e "Pasti gedek juga dengerin aku ngomongin garis setelah kita pusing dengerin materi garis yang lain"
    e "....."
    show erika base
    e "Anyway...abis ini kamu mau kemana ?"
    menu:
        "Aku sudah lelah hari ini, mau pulang dulu":
            jump pulang
        "Aku mau sedikit jalan-jalan sebentar di sekitar taman kota":
            jump jalan_1
    label jalan_1:
        d "Kamu mau ikut?"
        e "Eh, anu, boleh-boleh saja" #erika masang muka malu
        #ganti bg taman kota atau pinggiran kota
        e "Ngomong-ngomong, apa kamu sering ngelakuin ini setiap malam?"
        menu:
            "Iya, lumayan sering":
                jump jalan_2
            "Enggak, cuman lagi pengen aja malam ini":
                jump jalan_2
    
    label jalan_2:
        e "Oalah"
        show erika happy
        e "Dulu aku juga sering jalan-jalan kesini setiap malam"
        show erika base
        e "Tapi sekarang udah mulai jarang si"
        menu:
            "Kenapa kok mulai jarang?":
                jump jalan_3
            "Oh gitu":
                jump ngambek_1
        
        label ngambek_1:
            #Muka ngambek
            show erika envy
            e "Kamu kok gitu amat, gak pedulian banget"
            d "Eh, maaf-maaf"
            e "Yaudah deh kalo kamu gitu, aku pulang aja"
            e "BYE"
            jump chapter_5
    label jalan_3:
        e "Dulu tiap kali ada masalah aku itu kaburan anaknya"
        e "Dan ya, aku selalu kabur kesini dulu"
        e "Entah itu untuk jernihin pikiran"
        "aku menatap Erika dengan muka prihatin"
        show erika happy
        e "Gausah ngebayangin segitunya juga lah"
        e "Gak seburuk yang kamu pikirin kok"
        show erika base
        e "apalagi anak kecil, kan masalah kecil aja suka dibesar-besarin"
        menu:
            "Beneran bukan masalah besar?":
                jump jalan_4
            "Iyadeh aku percaya":
                jump jalan_4
    
    label jalan_4:
        menu:
            "Berikan kalung Erika" if goodies == "kalung":
                jump kalung
            "Erika....":
                jump pulang
        
        #CG Erika lihat pemandangan
        label kalung:
        e "Tunggu, inikan...?"
        e "Kamu nemu dimana?"
        show erika happy
        e "Aku dari kemariin nyariin gak ketemu-temu"
        show erika base
        e "Anyway, Dika, makasih ya udh nemuin"
        e "Kamu tahu gak sih seberapa berharganya kalung ini bagiku"
        e "Bagiku, segala kebahagiaanku berasal dari sini"
        e "Tak perlu banyak alasan untuk menikmati hidup"
        e "Selama ada kalung ini, sudah cukup buat mengisi alasanku untuk tetap kuat berada disini"
        e "Tapi, tidak semuanya kok butuh alasan"
        "Dari atas gunung, tempat kami berdiri, tertiup angin sangat kencang menghembus kearah kami"
        hide erika
        scene cg erika_sad with dissolve
        play music "remembrance.mp3" fadeout 2.0 fadein 2.0
        "Erika menepi di pagar taman sambil menatap pemandangan kota dari atas bukit"
        e "Lagipula, gak perlu banyak alasan juga udah cukup kok buat bisa nikmatin pemandangan ini"
        e "Meskipun hidup ini pahit"
        e "Kita mau gamau harus ngejalanin ini dengan lapang dada"
        e "Itu yang dikatakan oleh banyak orang"
        e "Tapi, gimana mau lapang dada"
        e "Kalau kita sendiri gak punya dada untuk dilapangkan"
        e "Apa aku benar, Dika?"
        d "......."
        jump pulang
        #ganti normal
    # label pulang:
    #     show erika base
    #     e "Anyway, yuk kita pulang"
    #     e "Udah mau tengah malem"
    
        # e "Oh, gitu.."
        # e "Yaudah, hati-hati ya"

    # hide erika   

# label jalan_4:
#     #CG Erika lihat pemandangan
#     "Erika menepi di pagar taman sambil menatap pemandangan kota dari atas bukit"
#     e "Lagipula, gak perlu banyak alasan juga udah cukup kok buat bisa nikmatin pemandangan ini"
#     e "Meskipun hidup ini pahit"
#     e "Kita mau gamau harus ngejalanin ini dengan lapang dada"
#     e "Itu yang dikatakan oleh banyak orang"
#     e "Tapi, gimana mau lapang dada"
#     e "Kalau kita sendiri gak punya dada untuk dilapangkan"
#     e "Apa aku benar, Dika?"
#     d "......."
#     #ganti normal
#     e "Anyway, yuk kita pulang"
#     e "Udah mau tengah malem"
    # hide cg erika_sad
    show erika happy
    scene bg night city
    e "makasih ya udh nemenin. sampai jumpa besok, Dika"
    menu:
        "Sampai jumpa Erika":
            jump chapter_5

label pulang:
    e "Oh, gitu.."
    e "Yaudah, hati-hati ya"
scene bg night city
show erika sad
menu:
    "Iya, selamat malam, Erika":
        jump chapter_5