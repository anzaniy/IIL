# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = im.Scale("images/Background/bg_1.jpg", 2400, 1200)
image bg bedroom dika = im.Scale("images/Background/dikas_bedroom.jpg", 2400, 1200)
image bg campus = im.Scale("images/Background/campus_1_anime.jpg", 2400, 1200)
image bg campus_interrior = im.Scale("images/Background/classroom.jpg", 2400, 1200)
image bg lecturer room = im.Scale("images/Background/room_1.jpg", 2400, 1200)
image bg night city = im.Scale("images/Background/night_city_1.jpg", 2400, 1200)
image bg library = im.Scale("images/Background/library.jpg", 2400, 1200)
image bg cafe = im.Scale("images/Background/cafe.jpg", 2400, 1200)
image bg lounge = im.Scale("images/Background/lounge.jpg", 2400, 1200)

image erika base = im.Scale("images//Character/erika_2.png", 500, 1100)
image aurellia base = im.Scale("images/Character/aurellia.png", 500, 1100)
image revina base = im.Scale("images/Character/revina.png", 500, 1100)


# Deklarasikan karakter yang digunakan di game.
define d = Character('Andika', color="#2920aa")
define e = Character('Erika', color="#c8ffc8")
define a = Character('Aurellia', color="#90cb10")
define u = Character('....', color="#ffffff")
define r = Character('Doni', color="#2aa80a")
define p = Character('Pak Adib', color="#eeff8d")
define v = Character('Revina', color="#c4158f")
define both_1 = Character('Dika, Erika, dan Revina', color="#ffffff")

# Game dimulai disini.
label start:

    d "Setiap manusia memiliki masing-masing satu garis kehidupan"
    d "Garis kehidupan inilah yang menjadi saksi atas setiap peristiwa yang dialami manusia"
    d "Garis kehidupan ini memang hanya satu tapi garis ini memiliki cabang yang tak terhingga jumlahnya"
    d "Orang-orang menyebut garis ini sebagai Jalinan Garis Tak Terhingga"
    d "Lalu, apa kalian tahu apa maksud dari itu"
    d "Dalam setiap kehidupan manusia, kita diberi pilihan atas kehendak kita yang dimana pilihan itu memiliki konsekuensiya sendiri"
    d "Dari kita"
    d "Untuk Kita"
    d "Dan demi kita lah kita memilih pilihan hidup itu"
    d "Itulah yang diajarkan kakekku saat aku kecil bahwa hidup kita hanya sekali dan kita harus hati-hati terhadap pilihan kita"
    d "Dan saat ini aku dihadapkan dengan pilihan yang sulit"
    d "Sebuah pilihan yang sangat sulit untuk seorang mahasiswa semester akhir di hari ini"
    d "Ya benar, ini adalah"
    d "SKRIPSI!"

    scene bg bedroom dika with dissolve
    play music "iphone.mp3" fadeout 2.0 fadein 2.0
menu:
    "Angkat Telefon":
        jump act_1

label act_1:
    stop music
    d "H-Halo..?"
    u "Halo, Dika, apakah kamu sudah siap berangkat, kamu tidak lupa kan kalau pagi ini kamu ada kelas?"
    d "Tidak kok, aku tidak lupa, cuman sedikit begadang aja semalam"
    u "Kalau gitu bergegaslah setengah jam lagi akan dimulai kelasnya"
    d "Iya, iya, ini aku lagi siap-siap"

    play music "Blithe.ogg"
    scene bg campus with dissolve
    d "Aduh bagaimana ya, sudah berapa kali aku mengirim proposal kepada 3 dosen berbeda dan semuanya ditolak apakah tidak ada cara lain?"
    u "Kamu juga asal bikin proposal gimana mau diterima jika kamu bikinnya asal-asalan"
    u "Lalu, bagaimana dengan proposal terakhir aku dengar kamu agak serius bikinnya"
    d "Owh itu, itu proposal yang aku ajukan pak Adib, ada kemungkinan dia akan mengabariku setelah kelas dia pagi ini, doain aku yang terbaik ya"
    u "Tentu saja"
    d "Gawat, 5 menit lagi kelas mau dimulai, kalau gitu aku tutup dulu ya telponnya"
    u "Okey"

    #sfx tabrakan dengan erika
    show erika base with dissolve
    u "Aduhh"
    d "Maaf aku gak sengaja, salahku kertasmu jadi berhamburan dimana-dimana" 
    u "Iya, maaf itu salahku juga jalan tidak lihat-lihat, terima kasih ya sudah bantu."
    d "Iya sama-sama, kalau begitu aku duluan, ya"

    hide erika with dissolve
    scene bg campus_interrior with dissolve

    d "Akhirnya kelasnya selesai juga, untung saja tadi aku tepat waktu"
    r "Syukurlah kalau begitu. Ngomong-ngomong kenapa tadi kamu hampir telat"
    d "Itu anu, tadi ada-"
    p "Baik, sekian dari perkuliahan kita hari ini, sebelum saya pergi, saya ingin bertanya-"
    p "Apakah ada Andika Adyatama disini ?"
    d "Hadir Pak"
    p "Setelah ini keruangan saya, ya. Ada yang mau saya diskusikan"
    d "Baik, Pak"
    r "Ada apa ini, apa kau sudah membuat pak Adib marah, Dik"
    r "Jarang-jarang pak Adib manggil mahasiswa keruangannya"
    d "Ah enggak kok, aku cuman mengajukan proposal skripsi ku saja ke Pak Adib"
    r "Secepat itu? skripsi tentang apa emang kamu ngajuinnya?"
    d "Proposal ku membahas tentang Geometri Analitik Bidang, tapi mungkin ada perubahan terkait isi penelitiannya karena aku agak bingung mau fokus ke sub materi yang mana"
    d "Mungkin aku akan sekalian tanyakan ke Pak Adib soal ini"
    d "Bagaimana denganmu, Don?"
    r "Aku masih bingung mau ngambil judul yang mana"
    r "Ada satu judul yang bikin ku tertarik, tapi dosennya susah ditemuin"
    r "sebaliknya dosen-dosen yang mudah ditemuin malah topik pembahasannya yang susah"
    r "Aku jadi bingung mau lebih prioritasin kemana, hadeh..."
    r "By the way, kelompok penelitianmu siapa saja ?"
    d "Apa yang kau maksud?"
    r "Kamu tidak tahu?, aku dengar mahasiswa bimbingan dia banyak yang dikerjakan selama berkompok, aku pikir kamu juga sudah ada beebrapa orang yang mengerjakan topik yang sama"
    d "Kalau itu aku kurang tau sih, aku mengajukannya juga sendiri"
    d "Lagipula, aku juga tidak berniat mengerjakan penelitian secara berkelompok"
    r "Emangnya kenapa ?"
    d "Menurutku kegiatan berkelompok itu melelahkan, terkadang kita malah asik bersenang-senang"
    d "Tidak menutup kemungkinan juga ada pertengkaran ditengah penelitian"
    d "Hal semacam itulah yang membuatku berfikir untuk mengerjakan sesuatu secara sendiri"
    d "Tenang saja, judul penelitianku lumayan susah kok, kecil kemungkinan ada yang sama, hahahaha"
    d "Kalau begitu, aku duluan ya, Don"
    r "Oh iya hati-hati"

    scene bg lecturer room with dissolve

    "Setelah kegiatan perkuliahan, aku langsung berjalan menuju ruangan Pak Adib"
    #sfx ketuk pintu
    p "Silahkan masuk"
    "Didalam ruangan aku melihat 2 wanita yang berdiri didepan Pak Adib"
    "Sesaat setelah mereka melihatku kedua wanita itu langsung bergeser dan memberiku posisi diantara mereka berdua."
    p "Baik terima kasih sudah hadir"
    p "Apa kalian tahu kenapa saya mengumpulkan kalian bertiga disini?"
    d "Apakah terkait pengajuan proposal skripsi, Pak?"
    p "Ya, Benar"
    p "Terkait pengajuan judul yang kalian ajukan tempo hari yang lalu"
    p "Kebetulan judul kalian bertiga ini memiliki kemiripan, yaitu sama-sama membahas Geometri Analitik Bidang"
    p "dan sayangnya judul kalian ini belum spesifik untuk dijadikan topik skripsi"
    p "maka dari itu saya ingin kalian bertiga berdiskusi lagi dan tentukan topik skripsi kalian dengan lebih spesifik lagi, oke? saya tunggu minggu depan"
    p "Sampai sini apakah ada pertanyaan?"

    both_1 "Tidak pak"
    
    "Sesaat setelah pertemuan singkat itu, kami bertiga pergi menuju taman didepan fakultas"

    scene bg campus with dissolve

    show revina base with dissolve
    v "Sebelumnya, Terima kasih ya udah nyempetin waktu buat diskusi disini, ngomong-ngomong sebelum kita diskusi lebih lanjut, kenalin namaku Revina semester 9 Matematika Terapan. panggil aja Revi, salam kenal ya"
   
menu:
    "Kenalin namaku Andika panggil aja Dika, salam kenal ya":
        jump intro 

    "Aku Dika salam kenal ya":
        jump intro
    
label intro:
    play music "good.ogg"
    hide revina with dissolve
    show erika base with dissolve
    
    e "Salam kenal semua namaku Erika Semester 7 Matematika Murni, panggil aja Eri"
    e "Ohiya Dika, terima kasih ya atas tadi pagi"
    d "Oh, iya, aku baru ingat kamu yang tadi pagi, apakah yang tadi pagi itu proposalmu?"
    e "Hehe iya, Untung saja aku mengumpulkannya tepat waktu, tau sendiri kan pak Adib bagaimana."
   
    hide erika with dissolve
    show revina base with dissolve
    
    v "Jadi, habis ini kita mau bagaimana?"
    v "Apakah ada ide?"
   
    hide revina with dissolve
    show erika base with dissolve
    
    e "Kalau kita lihat dari hasil percakapan dengan pak Adib, kita tidak mempunyai banyak waktu untuk melakukan revisi judul penelitian kita"
    e "Kita masing-masing cari judul alternatif kita, lal kita kumpul untuk review lagi hasil revisian kita, bagaimana ?"
    d "kapan ita akan berkumpul lagi?"

    hide erika with dissolve
    show revina base with dissolve

    v "Apakah tiga hari cukup ?"

    hide revina with dissolve
    show erika base with dissolve

    e "Aku sih tidak masalah, bagaimana dengan Dika?"
    d "Aku juga tidak masalah, tapi bukannya waktunya terlalu mepet?"

    hide erika with dissolve
    show revina base with dissolve

    v "Mau bagaimana lagi, kita cuma punya waktu seminggu, mau tidak mau kita harus bisa saling revisi dalam tiga hari kedepan, oke?"
    d "Okey"

    hide revina with dissolve
    scene bg night city with dissolve
    show erika base with dissolve

    e "Terima kasih ya udah menemani aku pulang, Dika"
    d "Jangan berlebihan gitu, kosan kita kan searah"
    d "ngomong-ngomong, kapan kamu mau memulai revisian judulmu?"
    e "Aku rencananya si mau nyari referensi di perpustakaan kota didepan nanti"
    e "Asal kamu tahu aja, aku gak begitu pintar soal geometri ini"
    d "kalau begitu, boleh aku ikut menemanimu, mungkin aku bisa sedikit membantu"
    e "Apa kamu yakin bisa membantuku belajar?"
    e "Pede sekali kamu hahaha"
    e "Yaudah, yuk"

    scene bg library with dissolve
    show erika base with dissolve
    #sfx naruh buku
    d "Baiklah, dari mana kita akan mulai"
    e "Hmmmmm, apa bisa mulai dari sini ?"
    "Erika menunjuk halaman pertama dari buku pemahaman geometri dasar"
    d "Dari situ !?"
    e "Kalau begitu kita mulai aja dari koordinat kartesius"

    image kartesius satu = im.Scale("images/Materi/kartesius_1.png", 1100, 500)
   
    hide erika with dissolve
    show kartesius satu at truecenter 

    e "Menurut penjelasan di buku ini, dimisalkan X'OX, dan Y'OY adalah garus yang saling tegak lurus dan P merupakan sembarang titik pada bidang datar"
    e "Sementara PM dan PN digambar tegak lurus ke X'X dan Y'Y"

    image kartesius dua = im.Scale("images/Materi/kartesius_2.png", 1100, 500)
    hide kartesius with dissolve
    show kartesius dua at truecenter

    e "Jika OM = x dan ON = y"
    image kartesius tiga = im.Scale("images/Materi/kartesius_3.png", 1100, 500)
    hide kartesius with dissolve
    show kartesius tiga at truecenter
    
    e "dan ON = y"
    e "Maka letak P terhadap X'X dan Y'Y dikenal ketika x dan y diketahui."
    e "x disebut sebagai absis, dan y sebagai ordinat"
    e "dan x,y sebagai koordinat kartesis dengan P menunjukan titik (x,y)"
    e "lalu apa yang disebut sebagai apa X'X dan Y'Y?"
    d "maka dapat kita simpulkan bahwa X'X merupakan sumbu x dan Y'Y disebut sumbu y"
    e "Yap, dengan O sebagai titik pusatnya"

    image kuadran satu = im.Scale("images/Materi/kuadran.png", 1100, 500)
    hide kartesius with dissolve
    show kuadran satu at truecenter

    e "selanjutnya berdasarkan sumber yang tertera dapat kita lihat bahwa"
    e "sumbu koordinat yang membagi bidang datar menjadi empat bagian yang disebut kuadran."

    image polar satu  = im.Scale("images/Materi/koordinat_polar.png", 1100, 500)
    hide kuadran with dissolve
    show polar satu at truecenter

    e "selanjutnya masuk ke koordinat polar"
    e "menurutmu, apa itu koordinat polar?"
    d "Koordinat polar adalah koordinat yang memiliki sumbu ke arah r dan theta."
    e "Oke jadi berdasarkan gambar yang tertera"
    e "Dimisalkan OA merupakan sebuah garis dan P sembarang titik pada bidang datar"

    image polar dua  = im.Scale("images/Materi/polar_1.png", 1100, 500)
    hide polar with dissolve
    show polar dua at truecenter

    e "Misal θ merupakan sudut yang bergerak berputar dari posisi OA ke posisi OP. Jika r adalah panjang OP, letak P diketahui saat r dan theta diketahui"
    e "Disini masalahnya aku masih bingung apa itu r dan theta. apa kau tahu sesuatu dika?"
    d "r merupakan radius sementara theta disebut dengan sudut"
    e "Owh jadi begitu, maka dari itu lah dapat kita simpulkan r dan theta merupakan koordinat polar dari titik P"
    e "Yang dimana OA disebut garis awal dan O sebagai kutubnya"

    e "Disini juga terdapat hubungan antara koordinat kartesius dan koordinat polar seperti pada gambar yang tertera"

    image hubungan satu  = im.Scale("images/Materi/hubungan_1.png", 1100, 500)
    hide polar with dissolve
    show hubungan satu at truecenter

    e "'Misal P adalah titik (x,y) yang mengacu pada sumbu X'OX"
    
    image hubungan dua  = im.Scale("images/Materi/hubungan_2.png", 1100, 500)
    hide hubungan with dissolve
    show hubungan dua at truecenter
    
    e "dan Y'OY"

    image hubungan tiga  = im.Scale("images/Materi/hubungan_3.png", 1100, 500)
    hide hubungan with dissolve
    show hubungan dua at truecenter
    
    e "dan titik (r,θ) yang mengacu pada kutub O dan garis awal OX"

    image hubungan empat  = im.Scale("images/Materi/hubungan_4.png", 1100, 500)
    hide hubungan with dissolve
    show hubungan empat at truecenter

    e "menurutmu dengan menggunakan definisi fungsi lingkaran, bagaimana cara mencari nilai x ?"

    image rumus satu  = im.Scale("images/Materi/rumus_1.png", 1100, 500)
    hide hubungan with dissolve
    show rumus satu at truecenter

    d "Untuk mencari x dapat menggunakan rumus r cos theta"
    d "Demikian juga y dapat menggunakan rumus r sin theta"

    hide rumus with dissolve
    show hubungan dua at truecenter

    e "maka dengan demikian, kita dapat menyimpulkan untuk mencari nikai tan theta dapat menggunakan rumus y/x"

    "Setelah itu kami menghabiskan waktu belajar di perpustakaan kota sampai perpustakaan tutup"
    
    scene bg night city
    show erika base with dissolve
    
    e "Terima kasih ya dika udh menemaniku mencari referensi"
    d "Sama-sama"
    e "Ohiya sepertinya aku sudah dapat judul yang sesuai"
    d "Apa itu?"
    e "Aku akan menganalisis Perbandingan Representasi Koordinat Kartesius dan Polar dalam Penggambaran Data Geometri"
    e "Gimana, bagus, kan?"
    d "Bagus-bagus"
    e "Kalau begitu aku duluan ya, kosanku disini"
    e "Dika jangan lupa revisianmu, ya terima kasih, bye bye"

    "Tiga Hari Kemudian"
    scene bg cafe with dissolve
    show revina base with dissolve

    v "Jadi, gimana, sudah ada pencerahan?"
    "suasana sempat hening, sesaat setelah itu Revina menoleh ke Erika yang sedang melamun"
    v "Erika?"

    show revina base at right
    show erika base at left

    e "Oh, iya, maaf kak aku sempat melamun tadi hehe"
    v "Tenang, jangan dipikirin"
    v "ngomong-ngomong, kalian cukup manggil aku revi aja selagi ini pertemuan nonformal"
    v "aku lebih nyaman dipanggil begitu"
    d "lalu bagaimana saaat pertemuan formal"
    v "yang manggil 'kak' lah"
    e "Baik, mungkin sebaiknya kita kembali ke topik diskusi kita ya revi, dika ?"
    v "Oh ya, maaf-maaf, aku  terlalu terbawa suasana tadi"
    e "Untuk topik utama penelitianku aku ingin membahas terkait representasi koordinat kartesius dan dan koordinat polar dalam penggambaran data geometri"
    v "kalau menurut revi gimana?"
    v "Menurutku sih tidak ada masalah terkait judulmu itu, tapi menurutku terdapat permasalahan dalam transformasi antara koordinat kartesian dan polar"
    v "karena dalam proses transformasi itu merupakan proses yang rumit terutama dalam konteks data yang kompleks atau dalam analisis yang memerlukan banyak transformasi koordinat"
    e "Ada benarnya si, namun pilihan antara koordinat kartesian dan polar tergantung pada sifat data yang akan direpresentasikan dan tujuan analisisnya"
    e "Dan juga, Dalam beberapa kasus, mungkin perlu menggunakan keduanya secara bersamaan atau menggabungkan elemen-elemen dari masing-masing sistem koordinat untuk mendapatkan representasi yang paling informatif dan relevan"
    e "Jadi menurutku, so far, tidak permasalahan serius dalam judul penelitianku ini"
    e "Bagaimana dengan mu, kak ?"
    
    #Pembahasan Jarak, Perbandingan, dan Gradien

    #Rumus Jarak
    v "Sebelumnya kita pahami bagaimana cara mengetahui rumus untuk mendapatkan jarak"
    image jarak satu  = im.Scale("images/Materi/jarak_1.png", 1100, 500)
    # hide polar with dissolve
    show jarak satu at truecenter
    v "Misalkan A dan B adalah titik X1,Y1 dan X2,Y2"
    v "r panjang AB dan θ sudut inklinasi dari AB ke OX"
    
    v "Maka dapat kita simpulkan"

    image jarak dua  = im.Scale("images/Materi/jarak_2.png", 1100, 500)
    hide jarak with dissolve
    show jarak dua at truecenter

    v "r cos θ = x2-x1"

    image jarak tiga  = im.Scale("images/Materi/jarak_3.png", 1100, 500)
    hide jarak with dissolve
    show jarak tiga at truecenter

    v "r sin θ = y2-y1"
    v "Dengan kedua rumus yang tadi kita sebutkan, maka untuk mendapatkan nilai dari r kita tinggal memasukkan 2 variabel yang kita sebutkan tadi"

    image jarak empat  = im.Scale("images/Materi/jarak_4.png", 1100, 500)
    hide jarak with dissolve
    show jarak empat at truecenter

    v "Didapatlah rumus sebagai berikut"

    image jarak lima  = im.Scale("images/Materi/jarak_5.png", 1100, 500)
    hide jarak with dissolve
    show jarak lima at truecenter

    v "Dalam kasus tertentu, r dapat diperoleh dengan cara berikut"

    image jarak enam  = im.Scale("images/Materi/jarak_6.png", 1100, 500)
    hide jarak with dissolve
    show jarak enam at truecenter

    v "Misalkan MA, NB (Gambar 1.8) adalah ordinat dari A (x_1,y_1), B (x_2,y_2)"

    image jarak tujuh  = im.Scale("images/Materi/jarak_7.png", 1100, 500)
    hide jarak with dissolve
    show jarak tujuh at truecenter

    v "Dan misalkan AC sejajar OX, memotong NB di C"
    
    image jarak delapan  = im.Scale("images/Materi/jarak_8.png", 1100, 500)
    hide jarak with dissolve
    show jarak delapan at truecenter

    v "Maka dapat disimpulkan untuk mencari nilai kuadrat dari jarak adalah dengan penjumlahan dari kuadrat AC dan kuadrat AB"
    v "Kita dapat memperoleh nilai r hanya jika nilai NC = MA"

    e "Selanjutnya kita masuk ke garis lurus"
    e "Apa kau tahu apa itu garis lurus ?"
    v "Garis yang berbentuk lurus?"
    e "Gak salah sih"
    e "Sekarang kita kan lebih fokus tentang persamaan garis lurusnya"
    e "Persamaan garis lurus dapat kita tulis dengan bentuk Ax + By + C = 0"
    e "Dengan A, B, C konstan menunjukkan persamaan garis"

    image rumus dua  = im.Scale("images/Materi/rumus_2.png", 1100, 500)
    hide jarak with dissolve
    show rumus dua at truecenter

    e "Jika B ≠ 0, kita tuliskan dengan bentuk berikut"
    e "Persamaan tersebut menunjukkan gradien -A/B dan melalui titik (0,-C/B)"
    e "Jika B=0, kita tuliskan x= -C/A"
    e "Persamaan tersebut menunjukkan garis sejajar sumbu-y"
    e "Oh iya, perlu diingat ya.."
    e "Jika A=0, maka y=-C/B menunjukkan persamaan garis sejajar sumbu-x"
    e "Jika C=0, maka y=-A/B x menunjukkan persamaan garis melalui titik pusat"
    e "Jika A = C = 0, maka y = 0 menunjukkan persamaan sumbu-x"
    e "Jika B = C = 0, maka x = 0 menunjukkan persamaan sumbu-y"

    v "ngomong-ngomong, apa kau tahu tempat kedudukan suatu titik?"
    v "Tempat kedudukan suatu titik adalah himpunan titik-titik yang anggotanya merupakan himpunan yang memiliki sifat yang sama"
    v "Sebagai contoh"

    image titik satu  = im.Scale("images/Materi/titik_1.png", 1100, 500)
    hide rumus with dissolve
    show titik satu at truecenter
    
    v "Jika P (x,y) adalah sembarang titik yang sama jauhnya dari A (1,4) dan B (3,2), maka didapatlah persamaan sebagai berikut"

    image rumus tiga  = im.Scale("images/Materi/rumus_3.png", 1100, 500)
    hide titik with dissolve
    show rumus tiga at truecenter

    v "Jika garis tersebut dijalankan, persamaan semula dapat menjadi 2x-2y=6"

    e "Selanjutknya bagaimana jika ada garis lurus dengan gradien (m) melalui satu titik"

    image gradien dua  = im.Scale("images/Materi/gradien_2.png", 1100, 500)
    hide rumus with dissolve
    show gradien dua at truecenter

    e "Dari garis yang melalui A dan B dapat diketahui gradien garis tersebut dengan rumus y-y1/x-x1"
    e "Gradien garis AB diketahui sama dengan m, sehingga y-y1 = m(x-x1)"

    # image garis lurus satu  = im.Scale("images/Materi/lurus_1.png", 1100, 500)
    # hide gradien with dissolve
    # show garis lurus satu at truecenter

    e "Jika tadi garis melalui satu titik, sekarang kita akan mencari bagaimana jika garis melalui dua titik"

    image sumbu satu  = im.Scale("images/Materi/sumbu_1.png", 1100, 500)
    hide gradien with dissolve
    show sumbu satu at truecenter

    e "Misalkan A, B adalah titik (x_1,y_1), (x_2,y_2) memotong sumbu-x dan sumbu-y, maka A (x_1,0), B (0,y_2)"
    e "Maka ketika kita masukkan variabelnya akan menjadi seperti berikut"

    hide erika base with dissolve
    hide revina base with dissolve

    
    jump act_2

label act_2 :
    scene bg lounge with dissolve
    play music "My Only Love.ogg"
    show aurellia base with dissolve
    #Skenario 1
    #Dika bangun tidur siap2 mau keluar dan diluar udh ditunggu sama Aurellia

    "Sesaat setelah ku keluar dari kosan, aku melihat seorang berdiri didepan pagar kosanku"
    "Oh, Halo, Dika"
    "Sudah berapa lama kita tidak bertemu"

    "Dia adalah Aurellia, temanku dari SD, aku sempat terkejut kenapa dia ada"
    a "Kenapa mukamu, seperti baru lihat hantu?"
    a "Apa kau lupa pesanku semalam"
    "Aku sempat terbingung dengan apa maksud dari perkaataan Aurel"
    "Karena pesan yang dia sampaikan itu bertepatan setelah kami menyelesaikan permasalahan Erika tentang garis lurus"
    "Yang menyebabkan aku sampai kelelahan dan hanya sempat membaca sekilas pesannya"
    a "So, shall we go now?"

    #Latar kompleks
    a "Jadi, gimana kuliahmu"
    #basa basi

    a "Lingkaran adalah tempat kedudukan titik-titik yang memiliki jarak yang sama terhadap titik tertentu"

    image lingkaran satu  = im.Scale("images/Materi/lingkaran_1.png", 1100, 500)
    hide aurellia base with dissolve
    show aurellia base at left
    # hide gradien with dissolve
    show lingkaran satu at truecenter

    a "Misalkan P sembarang titik (x,y) pada lingkaran, maka"

    image lingkaran dua  = im.Scale("images/Materi/lingkaran_2.png", 1100, 500)
    hide lingkaran with dissolve
    show lingkaran dua at truecenter

    a "Persamaan ini berlaku untuk setiap titik pada lingkaran dan menjadi persamaan lingkaran dengan pusat O. Persamaan polar lingkaran memenuhi a = r."
    a "Jika tadi persamaan lingkaran dengan pusat(0,0) selanjutnya kita membahas persamaan lingkaran dengan pusat (a,b)"

    image lingkaran tiga  = im.Scale("images/Materi/lingkaran_3.png", 1100, 500)
    hide lingkaran with dissolve
    show lingkaran tiga at truecenter

    a "Misalkan C adalah titik (a,b) yang merupakan titik pusat lingkaran dan misalkan P (x,y) titik pada lingkaran, maka"
    
    image lingkaran empat  = im.Scale("images/Materi/lingkaran_4.png", 1100, 500)
    hide lingkaran with dissolve
    show lingkaran empat at truecenter

    a "Persamaan diatas dapat diubah menjadi x^2+y^2-2ax-2by+(a^2+b^2-r^2)=0 atau x^2+y^2+Ax+By+C=0"
    a "yang disebut persamaan umum lingkaran. Dengan nilai A=-2a, B=-2b, C=a^2+b^2-r^2"

    image lingkaran lima  = im.Scale("images/Materi/lingkaran_5.png", 1100, 500)
    hide lingkaran with dissolve
    show lingkaran lima at truecenter

    a "Dengan demikian persamaan di atas menunjukkan titik pusat lingkaran (-1/2 A,-1/2 B) dan jari-jari √(1/4 A^2+1/4 B^2-C)"
    a "Memperhatikan jari-jari tersebut, terdapat beberapa kemungkinan"
    a "Jika 1/4 A^2+1/4 B^2-C>0, maka menyatakan lingkaran nyata"
    a "Jika 1/4 A^2+1/4 B^2-C=0, maka menyatakan lingkaran dengan jari-jari nol"
    a "Jika 1/4 A^2+1/4 B^2-C>0, maka menyatakan lingkaran imajiner"

    hide lingkaran with dissolve

    a "Selanjutnya bagaimana jika terdapat persamaan lingkaran melalui 3 titik"
    a "Misalkan terdapat titik P (x_1,y_1), Q (x_2,y_2), dan R (x_3,y_3) tak segaris. Akan dibentuk persamaan lingkaran melalui ketiga titik tersebut, maka diperoleh"

    image lingkaran enam  = im.Scale("images/Materi/lingkaran_6.png", 1100, 500)
    # hide lingkaran with dissolve
    show lingkaran enam at truecenter

    a "Dari persamaan-persamaan tersebut diperoleh sistem persamaan linier 3 variabel. Melalui eliminasi dan subtistusi diperoleh nilai A, B, dan C. Selanjutnya substitusi nilai-nilai tersebut ke persamaan umum lingkaran sehingga diperoleh persamaan lingkaran melalui tiga titik tak segaris."
    a "Cara lain yang dapat digunakan adalah menggunakan determinan"

    image lingkaran tujuh  = im.Scale("images/Materi/lingkaran_7.png", 1100, 500)
    hide lingkaran with dissolve
    show lingkaran tujuh at truecenter

    a "Misalkan terdapat titik P (x_1,y_1), Q (x_2,y_2), R (x_3,y_3), dan sembarang titik T (x,y) pada lingkaran sehingga diperoleh nilai sebagai berikut"

    image lingkaran delapan  = im.Scale("images/Materi/lingkaran_8.png", 1100, 500)
    hide lingkaran with dissolve
    show lingkaran delapan at truecenter

    a "Sistem persamaan tersebut akan memiliki penyelesaian jika determinan dari koefisien A, B, C, sebagai variabel dan konstantanya sama dengan nol"
    a "Karena T (x,y) adalah titik sebarang pada lingkaran, maka setiap titik pada lingkaran akan memenuhi persamaan determinan tersebut"

    hide lingkaran with dissolve
    a "ngomong-ngomong, apakah kamu tahu tentang garis singgung dan gariskutub lingkaran?"
    a "Garis singgung lingkaran adalah garis yang memotong atau bersinggungan dengan lingkaran hanya di sebuah titik. Selanjutnya titik tersebut disebut titik singgung"
    a "Dalam persamaan Garis Singgung Lingkaran di titik di Titik (x_1,y_1)"
    a "Jika P (x_1,y_1) dan Q (x_2,y_2).adalah dua titik pada lingkaran, persamaan garis PQ adalah y-y_1=(y_2-y_1)/(x_2-x_1 ) (x-x_1 )"
    a "Tapi x_1^2+y_1^2=r^2=x_2^2+y_2^2 dan y_2^2-y_1^2=-(x_2^2+x_1^2 )"
    a "Maka (y_2-y_1)/(x_2-x_1 )=-(x_2+x_1)/(y_2+y_1 )"
    a "Persamaan garis PQ menjadi y-y_1=-(x_2+x_1)/(y_2+y_1) (x-x_1)"
    a "Sekarang misalkan Q mendekati P, persamaan garis PQ maka menjadi"

    image singgung satu  = im.Scale("images/Materi/singgung_1.png", 1100, 500)
    # hide lingkaran with dissolve
    show singgung satu at truecenter

    a "Jika lingkaran tersebut memiliki titik pusat di (a,b) maka dengan cara yang sama dapat diperoleh persamaan garis singgungnya (x-a)(x_1-a)+(y-b)(y_1-b)=r^2"
    hide lingkaran with dissolve
    a "Selanjutnya ke persamaan Garis Singgung y=mx+c terhadap Lingkaran x^2+y^2=r^2"
    a "Saat garis y=mx+c menyinggung lingkaran x^2+y^2=r^2 maka persamaannya menjadi x^2+〖(mx+c)〗^2=r^2(1+m^2 )x^2+2mcx+(c^2-r^2 )=0"

    image singgung dua  = im.Scale("images/Materi/singgung_2.png", 1100, 500)
    hide singgung with dissolve
    show singgung dua at truecenter
    a "Karena keduanya memiliki titik yang sama (titik potong), maka persamaan di atas memiliki nilai diskriminan sama dengan nol"
    a "Sehingga persamaan garis singgungnya menjadi y=mx±r√(1+m^2 )."
    a "Jika lingkaran tersebut memiliki titik pusat di (a,b) maka dengan cara yang sama dapat diperoleh persamaan garis singgungnya y-b=m(x-a)±r√(1+m^2 )."

    hide singgung with dissolve

    a "Sudut antara dua lingkaran adalah sudut yang diapit oleh garis-garis singgung pada lingkaran di titik potong kedua lingkaran tersebut"

    image sudut satu  = im.Scale("images/Materi/sudut_1.png", 1100, 500)
    # hide singgung with dissolve
    show sudut satu at truecenter

    a "Sudut α pada Gambar 2.4 menunjukkan sudut antara dua lingkaran dengan titik pusat P_1 dan P_2."
    a "Langkah-langkah untuk menentukan besar α sebagai berikut:"
    a "Tentukan titik potong antara dua lingkaran dengan pusat P_1 dan P_2."
    a "Tentukan persamaan garis singgung pada salah satu titik potongnya"
    a "Tentukan sudut apit kedua garis singgung menggunakan tan⁡α=(m_1-m_2)/(1+m_1.m_2 )"

    a "Oke biar langsung paham kita masuk ke latihan saja yak"




    




    return