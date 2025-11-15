#Intro + penjelasan bareng Doni, cabang opsional
label chapter_1:
    stop music
    d "H-Halo..?"
    u "Halo, Dika, udah siap berangkat belum?"
    u "Kamu gak lupa kan kalau pagi ini kamu ada kelas?"
    d "Enggak kok, gak lupa, cuman sedikit begadang aja semalam"
    u "Yaudah,buruan, katanya kamu ada kelas pagi"
    d "Iya, iya, ini lagi siap-siap"

    play music "Blithe.ogg"
    scene bg campus with dissolve
    d "Aduh gimana ya, udah berapa kali aku ngirim proposal ke 3 dosen ditolak semua apa gak ada cara lain?"
    u "Yaelah, kamu juga asal bikin proposal gimana mau diterima kalau bikinnya asal-asalan"
    d "Enggak kok, justru ini bikinnya paling serius"
    u "Yaudah aku tanya sini, proposal kamu tentang geometri kan"
    u "Kamu tahu gak geometri itu apa?"
    menu:
        "Geometri itu cabang matematika yang ngulik bentuk, ukuran, dan posisi benda di ruang":
            jump benar_1

        "Geometri itu cabang matematika yang fokusnya cuma hitung-hitungan angka tanpa bentuk visual":
            jump salah_1
        "Geometri adalah ilmu yang khusus mempelajari bilangan prima dan faktorisasi":
            jump salah_1
        "Geometri itu...gak tahu":
            jump salah_1
        
            label benar_1:
                u "Hmm, ya bolehlah, kebangetan sih kalau pertanyaan itu saja kamu gak bisa jawab"
                jump chapter_1_1

            label salah_1:
                u "Tuh kan bener, kamu masih asal-asalan"
                u "Geometri itu cabang matematika yang ngulik bentuk, ukuran, dan posisi benda di ruang"
                jump chapter_1_1

label chapter_1_1:
    u "Terus, gimana dengan proposal yang kamu ajuin baru-baru ini?"
    d "Owh itu, itu proposal yang aku ajuin ke pak Adib, katanya sih dia mau ngabarin setelah kelas dia pagi ini, doain ya"
    u "Okee, semangat!"
    d "Astaga, 5 menit lagi kelas mau dimulai, kalau gitu aku tutup dulu ya telponnya, dadah"
    u "Eh tunggu Di-"

    #sfx tabrakan dengan erika
    show erika base with dissolve
    show erika base at shake
    "*Takkkk*"
    
    u "Aduhh"
    "Sesaat setelah menutup telefon dengan tergesa, aku menabrak seorang perempuan asing"
    "Kertasnya kulihat berhamburan kemana-mana"
    menu:
        "Maaf aku gak sengaja, salahku kertasmu jadi berhamburan dimana-dimana, sini aku bantu":
            jump bantu_1
        "Maaf, apa kau tak apa?":
            jump bantu_1
    label bantu_1:
    default goodies = ""
    menu:
        "Ambil Kalung yang terjatuh":
            $ goodies = "kalung"
            jump bantu_3
        "Beritahu kalungnya terjatuh":
            jump bantu_2
    label bantu_2:
        d "Ini kalungnya jatuh"
        e "Oh iya, makasih ya udah ngingetin"
        jump bantu_3

label bantu_3:
    u "Maaf itu salahku juga jalan tidak lihat-lihat, terima kasih ya sudah bantu."
    menu:
    u "Iya, maaf itu salahku juga jalan tidak lihat-lihat, terima kasih ya sudah bantu."
    # u "Iya, maaf itu salahku juga jalan tidak lihat-lihat, terima kasih ya sudah bantu."
    d "Iya sama-sama, kalau begitu aku duluan, ya"

    hide erika with dissolve
    scene bg campus_interrior with dissolve

    d "Akhirnya kelasnya selesai juga, untung saja tadi dateng tepat waktu"
    show doni base
    r "Syukurlah kalau begitu. Ngomong-ngomong kenapa tadi lu hampir telat?"
    d "Itu anu, tadi ada-"
    hide doni 
    show adib base
    p "Baik, sekian dari perkuliahan kita hari ini, sebelum saya pergi, saya ingin bertanya-"
    p "Apakah ada Andika Adyatama disini ?"
    d "Hadir Pak"
    show adib happy
    p "Setelah ini keruangan saya, ya. Ada yang mau saya diskusikan"
    d "Baik, Pak"
    hide adib
    show doni sus
    r "Ada apa ini, abis ngapain lu, Dika?"
    r "Jarang-jarang pak Adib manggil mahasiswa keruangannya"
    d "Ah enggak kok, gua cuman mengajukan proposal saja ke Pak Adib"
    show doni base
    r "Secepat itu? skripsi tentang apa emang lu ngajuinnya?"
    d "Anu, itu tentang Geometri Analitik Bidang, tapi mungkin ada perubahan terkait isi penelitiannya karena agak bingung mau fokus ke sub materi yang mana"
    r "Hah Geometri Analitik apa tuh"
    d "Serius lu udah gak tahu?"
    d "Baru juga semester kemaren kita belajar"
    menu:
        "Geometri analitik bidang itu cabang matematika yang ngegabungin aljabar sama geometri pakai sistem koordinat (x, y)":
            jump bener_2
        "Geometri analitik bidang itu ilmu yang cuma fokus ke bangun ruang tiga dimensi":
            jump salah_2
        "Geometri analitik bidang adalah teknik menggambar grafik fungsi trigonometri tanpa koordinat":
            jump salah_2
        
            label salah_2:
                show doni sus
                r "Hah? Gak salah tuh?"
                r "Bukannya geometri analitik bidang itu cabang matematika yang ngegabungin aljabar sama geometri pakai sistem koordinat (x, y)"
                show doni happy
                r "Haduh Dika, masa topik skripsi sendiri gak tahu, haha"
                jump chapter_1_2

            label bener_2:
                show doni happy
                r "Oalahh, iya gua inget sekarang"
                jump chapter_1_2

label chapter_1_2:
    show doni sus
    image kartesius satu = im.Scale("images/Materi/karte.png", 1100, 500)
    v "Tapi jujur gua gak terlalu paham sih tentang itu"
    d "Serius gak paham? garis lurus? kartesius"
    v "Kartesius? apa itu kartesius"
    show doni sus at left
    show kartesius satu at truecenter
    d "Jadi gini, bayangkan sebuah bidang datar yang luas dan hening..."
    d "Di tengah bidang itu, terbentang dua garis, satu mendatar, satu lagi tegak lurus padanya."
    d "Yang mendatar disebut garis X'OX, dan yang tegak disebut Y'OY."
    d "Keduanya bersilangan tepat di satu titik pusat, yang disebut O, titik asal segalanya."

    d "Kini, bayangkan sebuah titik sembarang di bidang itu. Namanya P."
    d "Dari titik P, ditarik dua garis lurus, satu menuju garis X'X, satu lagi menuju garis Y'Y, dan keduanya tegak lurus."
    d "Garis itu menyentuh titik-titik tertentu pada M di garis X'X dan N di garis Y'Y."

    d "Jarak dari titik O ke titik M disebut x. Inilah yang disebut absis."
    d "Sedangkan jarak dari titik O ke titik N disebut y. Inilah yang dinamakan ordinat."

    d "Ketika kita tahu nilai x dan y, kita tahu di mana P berada."
    d "Dan saat itulah titik P dikenal sebagai koordinat Kartesius, yaitu (x, y)."

    d "Sederhana... namun dari sinilah semua bentuk dan arah dimulai."
    d "Sampai sini apa kamu paham, Don?"
    v "Owh iya aku sedikit ingat, kalau tidak salah ini ada bagian kuadran-kuadran gitu gak sih?"
    image kuadran satu = im.Scale("images/Materi/kuad.png", 1100, 500)
    d "Ya benar sekali"
    show kuadran satu at truecenter
    d "Sumbu koordinat membagi bidang datar menjadi empat bagian"
    d "Masing-masing bagiannya sendiri memiliki nilai plus dan minus untuk masing-masing nilai x dan y yang berada pada kuadran itu sendiri"
    v "Oh gitu..."
    v "Dika, menurutku, kamu pasti bisa untuk topik ini"
    v "Penjelasan kamu mudah banget untuk dipahami"
    v "Makasih ya, Dika, semoga beruntung nanti"
    hide kuadran satu
    menu:
        "Sampai Jumpa":
            jump chapter_2