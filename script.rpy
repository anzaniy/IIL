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

    scene bg campus with dissolve

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


    
    
    return