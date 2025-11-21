# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = im.Scale("images/Background/bg_1.jpg", 2400, 1200)
image bg bedroom dika = im.Scale("images/Background/dika_kamar.png", 2400, 1200)
image bg campus = im.Scale("images/Background/street.jpg", 2400, 1200)
image bg campus_interrior = im.Scale("images/Background/kelas.png", 2400, 1200)
image bg lecturer room = im.Scale("images/Background/ruang_dosen.png", 2400, 1200)
image bg night city = im.Scale("images/Background/night.jpg", 2400, 1200)
image bg night city dock= im.Scale("images/Background/night_city_1.jpg", 2400, 1200)
image bg library = im.Scale("images/Background/library.jpg", 2400, 1200)
image bg cafe = im.Scale("images/Background/cafe_1.png", 2400, 1200)
image bg lounge = im.Scale("images/Background/lounge.jpg", 2400, 1200)
image bg dark = im.Scale("images/darkness.webp", 2400, 1200)

image bg campus_1 = im.Scale("images/Background/campus_1.jpg", 2400, 1200)
image bg lib_1 = im.Scale("images/Background/lib_1.jpg", 2400, 1200)
image bg cafe_1 = im.Scale("images/Background/lib_2.jpg", 2400, 1200)
image bg hall_1 = im.Scale("images/Background/hall_1.jpg", 2400, 1200)
image bg park_1 = im.Scale("images/Background/park_1.jpg", 2400, 1200)

image illu lia = im.Scale("images/Illustration/illu_1.png", 1950, 1100)

#CG Event
image cg erika_view = "erika_view.png"
image cg revina_flowers = im.Scale("images/CG/revina_flowers.png", 1950, 1100)
image cg erika_sad = im.Scale("images/CG/erika_sad.png", 1950, 1100)

#Revina
image revina base = im.Scale("images/Character/revina_base.png", 1100, 1100)
image revina happy = im.Scale("images/Character/revina_happy.png", 1100, 1100)
image revina envy = im.Scale("images/Character/revina_envy.png", 1100, 1100)
image revina sad = im.Scale("images/Character/revina_sad.png", 1100, 1100)

# #Erika Versi Awal
image erika base = im.Scale("images//Character/erika_base.png", 1100, 1100)
image erika happy = im.Scale("images//Character/erika_happy.png", 1100, 1100)
image erika envy = im.Scale("images//Character/erika_envy.png", 1100, 1100)
image erika sad = im.Scale("images//Character/erika_sad.png", 1100, 1100)

# #Erika Versi Akhir
# image erika base = im.Scale("images//Character/Erika/erika_base.png", 1400, 1400)
# image erika happy = im.Scale("images//Character/Erika/erika_happy.png", 1100, 1100)
# image erika envy = im.Scale("images//Character/Erika/erika_envy.png", 1100, 1100)
# image erika sad = im.Scale("images//Character/Erika/erika_sad.png", 1100, 1100)

#Aurellia
# image aurellia base = im.Scale("images/Character/aurellia.png", 500, 1100)
image aurellia base satu = im.Scale("images/Character/lia_base.png", 1100, 1100)
image aurellia happy = im.Scale("images/Character/lia_happy.png", 1100, 1100)
image aurellia envy = im.Scale("images/Character/lia_envy.png", 1100, 1100)
image aurellia sad = im.Scale("images/Character/lia_sad.png", 1100, 1100)

#Doni
image doni base = im.Scale("images/Character/doni_base.png", 1100, 1100)
image doni happy = im.Scale("images/Character/doni_happy.png", 1100, 1100)
image doni sad = im.Scale("images/Character/doni_sad.png", 1100, 1100)
image doni sus = im.Scale("images/Character/doni_sus.png", 1100, 1100)

#Doni
image adib base = im.Scale("images/Character/adib_base.png", 1100, 1100)
image adib happy = im.Scale("images/Character/adib_happy.png", 1100, 1100)
image adib sus = im.Scale("images/Character/adib_sus.png", 1100, 1100)

# Deklarasikan karakter yang digunakan di game.
define d = Character('Andika', color="#2920aa")
define e = Character('Erika', color="#1b751b")
define a = Character('Aurellia', color="#90cb10")
define u = Character('....', color="#330505")
define v = Character('Doni', color="#2aa80a")
define p = Character('Pak Adib', color="#607004")
define r = Character('Revina', color="#c4158f")
# define both_1 = Character('Dika, Erika, dan Revina', color="#ffffff")
# define revieri = Character('Erika, dan Revina', color="#ffffff")
define both_1 = Character('Dika, Erika, dan Revina', color="#123c8a")
define revieri = Character('Erika, dan Revina', color="#6d1092")
define dikarevi = Character('Andika, dan Revina', color="#ffffff")

image hubungan satu  = im.Scale("images/Materi/relasi_1.png", 1100, 500)

# Game dimulai disini.
label start:

    d "Setiap manusia memiliki satu garis kehidupan, seperti satu garis lurus dalam ruang dimensi."
    d "Garis ini merekam setiap titik peristiwa yang kita lalui, bagaikan koordinat dalam sistem yang kompleks."
    d "Meski tampak satu arah, garis ini sebenarnya memiliki cabang tak terhingga, seperti garis-garis yang terbentuk dari setiap titik percabangan dalam ruang vektor."
    d "Orang-orang menyebutnya sebagai Jalinan Garis Tak Terhingga, karena setiap pilihan membentuk sudut baru dalam hidup kita."
    d "Apakah kau tahu apa maksudnya?"
    d "Dalam hidup, setiap keputusan yang kita buat seperti memilih satu vektor dari banyak vektor yang tersedia — dan masing-masing membawa arah serta magnitude-nya sendiri."

    d "Bagi kita, setiap keputusan adalah rotasi kecil dalam hidup kita."
    d "Dan demi kita pulalah, kita memilih untuk mengubah lintasan itu, membelokkan arah garis hidup kita."
    d "Itulah yang diajarkan kakekku saat aku kecil bahwa hidup ini seperti satu kurva peluang, dan kita harus berhati-hati dalam menentukan titik beloknya."
    d "Dan kini, aku berada di titik kritis itu."
    d "Sebuah persimpangan dari titik singular yang rumit dan sulit bagi seorang mahasiswa semester akhir seperti diriku, di hari ini."

    scene bg bedroom dika with dissolve
    play music "iphone.mp3" fadeout 2.0 fadein 2.0
menu:
    "Angkat Telefon":
        jump chapter_1

# label act_1:
#     stop music
#     d "H-Halo..?"
#     u "Halo, Dika, udah siap berangkat belum?"
#     u "Kamu gak lupa kan kalau pagi ini kamu ada kelas?"
#     d "Enggak kok, gak lupa, cuman sedikit begadang aja semalam"
#     u "Yaudah,buruan, katanya kamu ada kelas pagi"
#     d "Iya, iya, ini lagi siap-siap"

#     play music "Blithe.ogg"
#     scene bg campus with dissolve
#     d "Aduh bagaimana ya, sudah berapa kali aku mengirim proposal kepada 3 dosen berbeda dan semuanya ditolak apakah tidak ada cara lain?"
#     u "Kamu juga asal bikin proposal gimana mau diterima jika kamu bikinnya asal-asalan"
#     u "Lalu, bagaimana dengan proposal terakhir aku dengar kamu agak serius bikinnya"
#     d "Owh itu, itu proposal yang aku ajukan pak Adib, ada kemungkinan dia akan mengabariku setelah kelas dia pagi ini, doain aku yang terbaik ya"
#     u "Tentu saja"
#     d "Gawat, 5 menit lagi kelas mau dimulai, kalau gitu aku tutup dulu ya telponnya"
#     u "Okey"

#     #sfx tabrakan dengan erika
#     show erika base with dissolve
#     u "Aduhh"
#     d "Maaf aku gak sengaja, salahku kertasmu jadi berhamburan dimana-dimana" 
#     u "Iya, maaf itu salahku juga jalan tidak lihat-lihat, terima kasih ya sudah bantu."
#     d "Iya sama-sama, kalau begitu aku duluan, ya"

#     hide erika with dissolve
#     scene bg campus_interrior with dissolve

#     d "Akhirnya kelasnya selesai juga, untung saja tadi aku tepat waktu"
#     show doni base
#     r "Syukurlah kalau begitu. Ngomong-ngomong kenapa tadi kamu hampir telat"
#     d "Itu anu, tadi ada-"
#     hide doni 
#     show adib base
#     p "Baik, sekian dari perkuliahan kita hari ini, sebelum saya pergi, saya ingin bertanya-"
#     p "Apakah ada Andika Adyatama disini ?"
#     d "Hadir Pak"
#     show adib happy
#     p "Setelah ini keruangan saya, ya. Ada yang mau saya diskusikan"
#     d "Baik, Pak"
#     hide adib
#     show doni sus
#     r "Ada apa ini, apa kau sudah membuat pak Adib marah, Dik"
#     r "Jarang-jarang pak Adib manggil mahasiswa keruangannya"
#     d "Ah enggak kok, aku cuman mengajukan proposal skripsi ku saja ke Pak Adib"
#     show doni base
#     r "Secepat itu? skripsi tentang apa emang kamu ngajuinnya?"
#     d "Proposal ku membahas tentang Geometri Analitik Bidang, tapi mungkin ada perubahan terkait isi penelitiannya karena aku agak bingung mau fokus ke sub materi yang mana"
#     d "Mungkin aku akan sekalian tanyakan ke Pak Adib soal ini"
#     d "Bagaimana denganmu, Don?"
#     show doni sad
#     r "Aku masih bingung mau ngambil judul yang mana"
#     r "Ada satu judul yang bikin ku tertarik, tapi dosennya susah ditemuin"
#     r "sebaliknya dosen-dosen yang mudah ditemuin malah topik pembahasannya yang susah"
#     r "Aku jadi bingung mau lebih prioritasin kemana, hadeh..."
#     show doni happy
#     r "By the way, kelompok penelitianmu siapa saja ?"
#     d "Apa yang kau maksud?"
#     r "Kamu tidak tahu?, aku dengar mahasiswa bimbingan dia banyak yang dikerjakan selama berkompok, aku pikir kamu juga sudah ada beebrapa orang yang mengerjakan topik yang sama"
#     d "Kalau itu aku kurang tau sih, aku mengajukannya juga sendiri"
#     d "Lagipula, aku juga tidak berniat mengerjakan penelitian secara berkelompok"
#     show doni base
#     r "Emangnya kenapa ?"
#     d "Menurutku kegiatan berkelompok itu melelahkan, terkadang kita malah asik bersenang-senang"
#     d "Tidak menutup kemungkinan juga ada pertengkaran ditengah penelitian"
#     d "Hal semacam itulah yang membuatku berfikir untuk mengerjakan sesuatu secara sendiri"
#     show doni happy
#     d "Tenang saja, judul penelitianku lumayan susah kok, kecil kemungkinan ada yang sama, hahahaha"
#     d "Kalau begitu, aku duluan ya, Don"
#     r "Oh iya hati-hati"
#     hide doni with dissolve

#     scene bg lecturer room with dissolve

#     "Setelah kegiatan perkuliahan, aku langsung berjalan menuju ruangan Pak Adib"
#     #sfx ketuk pintu
#     p "Silahkan masuk"
#     show erika base at left
#     show revina base at right
#     "Didalam ruangan aku melihat 2 wanita yang berdiri didepan Pak Adib"
#     "Sesaat setelah mereka melihatku kedua wanita itu langsung bergeser dan memberiku posisi diantara mereka berdua."
#     hide erika with dissolve
#     hide revina with dissolve
#     show adib base with dissolve
#     p "Baik terima kasih sudah hadir"
#     p "Apa kalian tahu kenapa saya mengumpulkan kalian bertiga disini?"
#     d "Apakah terkait pengajuan proposal skripsi, Pak?"
#     p "Ya, Benar"
#     show adib sus
#     p "Terkait pengajuan judul yang kalian ajukan tempo hari yang lalu"
#     p "Kebetulan judul kalian bertiga ini memiliki kemiripan, yaitu sama-sama membahas Geometri Analitik Bidang"
#     p "dan sayangnya judul kalian ini belum spesifik untuk dijadikan topik skripsi"
#     show adib happy
#     p "maka dari itu saya ingin kalian bertiga berdiskusi lagi dan tentukan topik skripsi kalian dengan lebih spesifik lagi, oke? saya tunggu minggu depan"
#     show adib base
#     p "Sampai sini apakah ada pertanyaan?"

#     both_1 "Tidak pak"
#     hide adib with dissolve
    
#     "Sesaat setelah pertemuan singkat itu, kami bertiga pergi menuju taman didepan fakultas"

#     scene bg campus with dissolve

#     show revina happy with dissolve
#     v "Sebelumnya, Terima kasih ya udah nyempetin waktu buat diskusi disini, ngomong-ngomong sebelum kita diskusi lebih lanjut, kenalin namaku Revina semester 9 Matematika Terapan. panggil aja Revi, salam kenal ya"
   
# menu:
#     "Kenalin namaku Andika panggil aja Dika, salam kenal ya":
#         jump intro 

#     "Aku Dika salam kenal ya":
#         jump intro
    
# label intro:
#     play music "good.ogg"
#     hide revina with dissolve
#     show erika happy with dissolve
    
#     e "Salam kenal semua namaku Erika Semester 7 Matematika Murni, panggil aja Eri"
#     show erika happy
#     e "Ohiya Dika, terima kasih ya atas tadi pagi"
#     d "Oh, iya, aku baru ingat kamu yang tadi pagi, apakah yang tadi pagi itu proposalmu?"
#     e "Hehe iya, Untung saja aku mengumpulkannya tepat waktu, tau sendiri kan pak Adib bagaimana."
   
#     hide erika with dissolve
#     show revina envy with dissolve
    
#     v "Jadi, habis ini kita mau bagaimana?"
#     v "Apakah ada ide?"
   
#     hide revina with dissolve
#     show erika base with dissolve
    
#     e "Kalau kita lihat dari hasil percakapan dengan pak Adib, kita tidak mempunyai banyak waktu untuk melakukan revisi judul penelitian kita"
#     e "Kita masing-masing cari judul alternatif kita, lal kita kumpul untuk review lagi hasil revisian kita, bagaimana ?"
#     d "kapan ita akan berkumpul lagi?"

#     hide erika with dissolve
#     show revina base with dissolve

#     v "Apakah tiga hari cukup ?"

#     hide revina with dissolve
#     show erika base with dissolve

#     e "Aku sih tidak masalah, bagaimana dengan Dika?"
#     d "Aku juga tidak masalah, tapi bukannya waktunya terlalu mepet?"

#     hide erika with dissolve
#     show revina base with dissolve

#     v "Mau bagaimana lagi, kita cuma punya waktu seminggu, mau tidak mau kita harus bisa saling revisi dalam tiga hari kedepan, oke?"
#     d "Okey"

#     hide revina with dissolve
#     scene bg night city with dissolve
#     show erika base with dissolve

#     e "Terima kasih ya udah menemani aku pulang, Dika"
#     d "Jangan berlebihan gitu, kosan kita kan searah"
#     d "ngomong-ngomong, kapan kamu mau memulai revisian judulmu?"
#     e "Aku rencananya si mau nyari referensi di perpustakaan kota didepan nanti"
#     show erika envy
#     e "Asal kamu tahu aja, aku gak begitu pintar soal geometri ini"
#     d "kalau begitu, boleh aku ikut menemanimu, mungkin aku bisa sedikit membantu"
#     show erika sad
#     e "Apa kamu yakin bisa membantuku belajar?"
#     menu:
#         "Tentu saja,mari kita belajar bersama":
#             jump eri_1
    
#     label eri_1:
#     e "Baiklah kalau begitu, tapi sebelum itu.."
#     e "Apa kita bisa kembali kekampus?"
#     e "Sepertinya buku pelajaranku tertinggal dikelas tadi"
#     menu:
#         "Bukankah malam-malam begini kelas dikunci? bagaimana carak ita masuk?":
#             jump eri_2
    
#     label eri_2:
#     e "Iya sih, tapi aku dengar-dengar kelas umum sepertinya pintunya lagi rusak, mungkin kita bisa menyelinap masuk"
#     menu:
#         "Apa tidak bahaya kalau ketahuan satpam?":
#             jump eri_3
    
#     label eri_3:
#     show erika happy
#     e "Tenang saja, kalo ketahuan kita lari"
#     e "Ayo kita bergegas"
#     hide erika
#     jump hidden_object_example

#     label library:
#     scene bg library with dissolve
#     show erika base with dissolve
#     #sfx naruh buku
#     d "Baiklah, dari mana kita akan mulai"
#     e "Hmmmmm, apa bisa mulai dari sini ?"
#     "Erika menunjuk halaman pertama dari buku pemahaman geometri dasar"
#     d "Dari situ !?"
#     e "Kalau begitu kita mulai aja dari koordinat kartesius"

#     # image kartesius satu = im.Scale("images/Materi/kartesius_1.png", 1100, 500)
#     image kartesius satu = im.Scale("images/Materi/karte.png", 1100, 500)
   
#     hide erika with dissolve
#     show kartesius satu at truecenter 

#     e "Menurut penjelasan di buku ini, dimisalkan X'OX, dan Y'OY adalah garus yang saling tegak lurus dan P merupakan sembarang titik pada bidang datar"
#     e "Sementara PM dan PN digambar tegak lurus ke X'X dan Y'Y"

#     image kartesius dua = im.Scale("images/Materi/kartesius_2.png", 1100, 500)
#     hide kartesius with dissolve
#     show kartesius dua at truecenter

#     e "Jika OM = x dan ON = y"
#     image kartesius tiga = im.Scale("images/Materi/kartesius_3.png", 1100, 500)
#     hide kartesius with dissolve
#     show kartesius tiga at truecenter
    
#     e "dan ON = y"
#     e "Maka letak P terhadap X'X dan Y'Y dikenal ketika x dan y diketahui."
#     e "x disebut sebagai absis, dan y sebagai ordinat"
#     e "dan x,y sebagai koordinat kartesis dengan P menunjukan titik (x,y)"
#     e "lalu apa yang disebut sebagai apa X'X dan Y'Y?"
#     d "maka dapat kita simpulkan bahwa X'X merupakan sumbu x dan Y'Y disebut sumbu y"
#     e "Yap, dengan O sebagai titik pusatnya"

#     image kuadran satu = im.Scale("images/Materi/kuadran.png", 1100, 500)
#     hide kartesius with dissolve
#     show kuadran satu at truecenter

#     e "selanjutnya berdasarkan sumber yang tertera dapat kita lihat bahwa"
#     e "sumbu koordinat yang membagi bidang datar menjadi empat bagian yang disebut kuadran."

#     image polar satu  = im.Scale("images/Materi/koordinat_polar.png", 1100, 500)
#     hide kuadran with dissolve
#     show polar satu at truecenter

#     e "selanjutnya masuk ke koordinat polar"
#     e "menurutmu, apa itu koordinat polar?"
#     d "Koordinat polar adalah koordinat yang memiliki sumbu ke arah r dan θ."
#     e "Oke jadi berdasarkan gambar yang tertera"
#     e "Dimisalkan OA merupakan sebuah garis dan P sembarang titik pada bidang datar"

#     image polar dua  = im.Scale("images/Materi/polar_1.png", 1100, 500)
#     hide polar with dissolve
#     show polar dua at truecenter

#     e "Misal θ merupakan sudut yang bergerak berputar dari posisi OA ke posisi OP. Jika r adalah panjang OP, letak P diketahui saat r dan θ diketahui"
#     e "Disini masalahnya aku masih bingung apa itu r dan θ. apa kau tahu sesuatu dika?"
#     d "r merupakan radius sementara θ disebut dengan sudut"
#     e "Owh jadi begitu, maka dari itu lah dapat kita simpulkan r dan θ merupakan koordinat polar dari titik P"
#     e "Yang dimana OA disebut garis awal dan O sebagai kutubnya"

#     e "Disini juga terdapat hubungan antara koordinat kartesius dan koordinat polar seperti pada gambar yang tertera"

#     image hubungan satu  = im.Scale("images/Materi/hubungan_1.png", 1100, 500)
#     hide polar with dissolve
#     show hubungan satu at truecenter

#     e "'Misal P adalah titik (x,y) yang mengacu pada sumbu X'OX"
    
#     image hubungan dua  = im.Scale("images/Materi/hubungan_2.png", 1100, 500)
#     hide hubungan with dissolve
#     show hubungan dua at truecenter
    
#     e "dan Y'OY"

#     image hubungan tiga  = im.Scale("images/Materi/hubungan_3.png", 1100, 500)
#     hide hubungan with dissolve
#     show hubungan dua at truecenter
    
#     e "dan titik (r,θ) yang mengacu pada kutub O dan garis awal OX"

#     image hubungan empat  = im.Scale("images/Materi/hubungan_4.png", 1100, 500)
#     hide hubungan with dissolve
#     show hubungan empat at truecenter

#     e "menurutmu dengan menggunakan definisi fungsi lingkaran, bagaimana cara mencari nilai x ?"

#     image rumus satu  = im.Scale("images/Materi/rumus_1.png", 1100, 500)
#     hide hubungan with dissolve
#     show rumus satu at truecenter

#     d "Untuk mencari x dapat menggunakan rumus r cos θ"
#     d "Demikian juga y dapat menggunakan rumus r sin θ"

#     hide rumus with dissolve
#     show hubungan dua at truecenter

#     e "maka dengan demikian, kita dapat menyimpulkan untuk mencari nilai tan θ dapat menggunakan rumus y/x"

#     "Setelah itu kami menghabiskan waktu belajar di perpustakaan kota sampai perpustakaan tutup"
    
#     scene bg night city
#     show erika base with dissolve
    
#     e "Terima kasih ya dika udh menemaniku mencari referensi"
#     d "Sama-sama"
#     e "Ohiya sepertinya aku sudah dapat judul yang sesuai"
#     d "Apa itu?"
#     e "Aku akan menganalisis Perbandingan Representasi Koordinat Kartesius dan Polar dalam Penggambaran Data Geometri"
#     e "Gimana, bagus, kan?"
#     d "Bagus-bagus"
#     e "Kalau begitu aku duluan ya, kosanku disini"
#     e "Dika jangan lupa revisianmu, ya terima kasih, bye bye"

#     "Tiga Hari Kemudian"
#     scene bg cafe with dissolve
#     show revina base with dissolve

#     v "Jadi, gimana, sudah ada pencerahan?"
#     "suasana sempat hening, sesaat setelah itu Revina menoleh ke Erika yang sedang melamun"
#     v "Erika?"

#     show revina base at right
#     show erika happy at left

#     e "Oh, iya, maaf kak aku sempat melamun tadi hehe"
#     v "Tenang, jangan dipikirin"
#     show revina happy at right
#     v "ngomong-ngomong, kalian cukup manggil aku revi aja selagi ini pertemuan nonformal"
#     v "aku lebih nyaman dipanggil begitu"
#     show erika base at left
#     d "lalu bagaimana saaat pertemuan formal"
#     show revina envy at right
#     v "yang manggil 'kak' lah"
#     show revina base at right
#     e "Baik, mungkin sebaiknya kita kembali ke topik diskusi kita ya revi, dika ?"
#     v "Oh ya, maaf-maaf, aku  terlalu terbawa suasana tadi"
#     e "Untuk topik utama penelitianku aku ingin membahas terkait representasi koordinat kartesius dan dan koordinat polar dalam penggambaran data geometri"
#     v "kalau menurut revi gimana?"
#     v "Menurutku sih tidak ada masalah terkait judulmu itu, tapi menurutku terdapat permasalahan dalam transformasi antara koordinat kartesian dan polar"
#     v "karena dalam proses transformasi itu merupakan proses yang rumit terutama dalam konteks data yang kompleks atau dalam analisis yang memerlukan banyak transformasi koordinat"
#     e "Ada benarnya si, namun pilihan antara koordinat kartesian dan polar tergantung pada sifat data yang akan direpresentasikan dan tujuan analisisnya"
#     e "Dan juga, Dalam beberapa kasus, mungkin perlu menggunakan keduanya secara bersamaan atau menggabungkan elemen-elemen dari masing-masing sistem koordinat untuk mendapatkan representasi yang paling informatif dan relevan"
#     e "Jadi menurutku, so far, tidak permasalahan serius dalam judul penelitianku ini"
#     e "Bagaimana dengan mu, kak ?"
    
# #Pembahasan Jarak, Perbandingan, dan Gradien

#     #Rumus Jarak
#     v "Sebelumnya kita pahami bagaimana cara mengetahui rumus untuk mendapatkan jarak"
#     image jarak satu  = im.Scale("images/Materi/jarak_1.png", 1100, 500)
#     # hide polar with dissolve
#     show jarak satu at truecenter
#     v "Misalkan A dan B adalah titik X1,Y1 dan X2,Y2"
#     v "r panjang AB dan θ sudut inklinasi dari AB ke OX"
    
#     v "Maka dapat kita simpulkan"

#     image jarak dua  = im.Scale("images/Materi/jarak_2.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak dua at truecenter

#     v "r cos θ = x₂-x₁" 

#     image jarak tiga  = im.Scale("images/Materi/jarak_3.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak tiga at truecenter

#     v "r sin θ = y₂-y₁"
#     v "Dengan kedua rumus yang tadi kita sebutkan, maka untuk mendapatkan nilai dari r kita tinggal memasukkan 2 variabel yang kita sebutkan tadi"

#     image jarak empat  = im.Scale("images/Materi/jarak_4.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak empat at truecenter

#     v "Didapatlah rumus sebagai berikut"
#     v "Untuk memperoleh nilai r, kira dapat memanfaatkan sifat persamaan trigonometri dimana nilai jumlah dari cos dan sin kuadrat θ bernilai 1"

#     image jarak lima  = im.Scale("images/Materi/jarak_5.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak lima at truecenter

#     v "Dalam kasus tertentu, r dapat diperoleh dengan cara berikut"

#     image jarak enam  = im.Scale("images/Materi/jarak_6.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak enam at truecenter

#     v "Misalkan MA dan NB  adalah ordinat dari A (x₁,y₁), B (x₂,y₂)"

#     image jarak tujuh  = im.Scale("images/Materi/jarak_7.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak tujuh at truecenter

#     v "Dan misalkan AC sejajar OX, memotong NB di C"
    
#     image jarak delapan  = im.Scale("images/Materi/jarak_8.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak delapan at truecenter

#     v "Maka dapat disimpulkan untuk mencari nilai kuadrat dari jarak adalah dengan menggunakan rumus pythagoras yaitu penjumlahan dari kuadrat AC dan kuadrat CB"
#     v "Perlu diingat, rumus ini hanya berlaku jika nilai NC = MA"
#     v "Oke kalau gitu mari kita kerjakaan contoh soal"
#     v "Erika, Carilah jarak antara titik (-2,1) dan (4,9)"
#     e "Sebentar.."
#     "Erika langsung mengambil penanya dan mengerjakaan soal yang diberikan Revina di kertas kosong"
#     e "10, apakah benar?"
#     v "Ya benar sekali"
#     v "Oke, mari kita masuk ke pembahasan, kenapa bisa didapatkan nilai 10?" 

#     image soal satu  = im.Scale("images/Soal/soal_1.png", 1100, 500)
#     hide jarak with dissolve
#     show soal satu at truecenter

#     v "Seperti yang sudah dikerjakan erika, kita cukup memasukkan rumus √(x₂-x₁)²+(y₂-y₁)²"
#     v "Jangan lupa sebelum mengerjakan soal, kita pahami dulu apa saja yang diketahui"
#     v "Diketahui x₁ = -2, y₁ = 1"
#     v "Sementara x₂ = 4 dan y₂ = 9"
#     v "Dengan memasukkan rumus √(x₂-x₁)²+(y₂-y₁)²"
#     v "Maka didapatlah nilai √100 yaitu 10"

#     v "Untuk rumus selanjutnya ada rumus perbandingan jarak"

#     image jarak sembilan  = im.Scale("images/Materi/jarak_9.png", 1100, 500)
#     hide soal with dissolve
#     show jarak sembilan at truecenter
    

#     v "Misalkan A dan B adalah titik (x₁,y₁), (x₂,y₂) dan θ adalah sudut dari AB ke sumbu-x" 
#     v "Kita misalkan P (x,y) adalah titik pada AB sedemikian hingga AP:PB = K:L"

#     image jarak sepuluh  = im.Scale("images/Materi/jarak_10.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak sepuluh at truecenter

#     v "Maka dapat kita simpulkan bahwa untuk mencari nilai AP cos θ = x - x₁"
#     v "Dan untuk nilai PB cos θ = x₂ - x"
#     v "Dengan menggunakan perbandingan antara AP:PB, maka kita dapat membandingkan nilai x - x₁/x₂ - x"
#     v "Kita dapat mengkali silang nilai AP:PB dan K:L, maka didapatlah nilai kx₂ + lx₁ = (k + l)x"
#     v "Dengan itu, untuk mencari nilai x pada perbandingan jarak antar dua titik, kita dapat menggunakan rumus yang tertera"
#     v "Rumus ini juga berlaku jika kita juga ingin mencari nilai y"
#     hide jarak with dissolve
#     v "Oke, selanjutnya kita langsung bahas soal saja"
#     v "Dika, kali ini giliran kamu, ya"
#     v "Carilah koordinat P yang membagi garis A (-7,1) dan B (3,6) dengan rasio 3:2"
#     menu:
#         "P(-1,4)":
#             jump benar_satu
        
#         "P(4,-1)":
#             jump salah_satu
        
#         "P(1,-4)":
#             jump salah_satu
        
#         "P(1,4)":
#             jump salah_satu
    
#     label salah_satu:
#         show revina envy at right
#         v "Apa kamu memerhatikan penjelasanku tadi?"
#         v "Kau tidak tertidur kan?"
#         menu:
#             "Tentu saja tidak, apa jawabanku salah?":
#                 jump lanjut
#             "Hehe, maaf, apa jawabanku salah?":
#                 jump lanjut

#                 label lanjut:
#                     v "Tentu saja salah"
#                     jump penjelasan
    
#     label benar_satu:
#         show revina happy at right
#         v "Benar sekali, tidak sia-sia aku ngomong panjang lebar haha"
#         jump penjelasan
    
#     label penjelasan:
#         show revina happy at right
#         v "Oke, mari kita bahas bareng-bareng ya"
#         v "Erika silahkan.."
#         e "Oke, mari kita mulai lihat nilai yang diketahui dulu"
#         e "Diketahui x₁ = -7 dan y₁ = 1"
#         e "Sementara nilai x₂ = 3 dan y₂ = 6"
#         e "untuk rasionya bernilai 3:2, yang artinya nilai k = 3 dan l = 2"
        
#         image jarak sebelas  = im.Scale("images/Materi/jarak_11.png", 1100, 500)
#         # hide jarak with dissolve
#         show jarak sebelas at truecenter

#         e "Dengan memasukan rumus yang telah kita bahas barusan"

#         image soal dua  = im.Scale("images/Soal/soal_2.png", 1100, 500)
#         hide jarak with dissolve
#         show soal dua at truecenter

#         e "maka kita cukup masukkan saja semua nilai yang diketahui"
#         e "nilai x kita mendapat nilai -1, sementara untuk y bernilai 4"
#         e "oleh karena itu koordinat P yang tepat adalah P(-1,4)"

#         hide soal with dissolve
#         jump gradien
# label gradien:
#     e "Terakhir kita membahas gradien"
#     e "Gradien dari suatu garis didefinisikan sebagai garis singgung sudut yang dibuat oleh garis tersebut dengan arah positif dari sumbu-x"
#     image gradien satu  = im.Scale("images/Materi/gradien_1.png", 1100, 500)
#     # hide jarak with dissolve
#     show gradien satu at truecenter
#     e "Gradien garis melalui dua titik (x₁,y₁), (x₂,y₂) adalah y₂-y₁/x₂-x₁"
#     e "Kita langsung masuk ke contoh soal saja"
#     e "Diketahui A, B, C, D adalah titik (-1,3), (1,0), (4,2), (0,8). Tunjukkan bahwa AB⊥BC(Tegak Lurus) dan juga AB∥DC(Sejajar)"
#     e "Karena x dan y masing-masing titik sudah diketahui, kita cukup masukkan masing-masing nilai yang ada"
#     image soal tiga  = im.Scale("images/Soal/soal_3.png", 1100, 500)
#     hide gradien with dissolve
#     show soal tiga at truecenter
#     e "Kesimpulan yang kita dapat adalah titik AB⊥BC karena hasil kali gradiennya -1 dan  AB∥DC karena gradiennya sama"
#     e "Sampai sini mudahkan?"
#     e "Sebelum kita masuk ke materi selanjutnya, mari kita mengerjakan latihan"
#     v "Apa kau siap, Dika?"
#     hide soal with dissolve

#     menu:
#         "Tentu Saja":
#             jump soal

#             label soal:
#                 v "Okay, soal pertama.."
#                 v "Carilah jarak antar dua titik (0,4) dan (7,2)"
#                 menu:
#                     "√53":
#                         jump dua
#                     "√50":
#                         jump dua
#                     "√52":
#                         jump dua
            
#             label dua:
#                 v "Selanjutnya nomor 2"
#                 v "Carilah perbandingan AP:PB pada titik P (4,-2) terletak pada garis yang melalui A (7,-3) dan B (-5,1)"
#                 menu  :
#                     "2:4":
#                         jump tiga
#                     "1:3":
#                         jump tiga
#                     "1:5":
#                         jump tiga
            
#             label tiga:
#                 v "Hmmmmm....Tidak buruk"
#                 v "Terakhir ya"
#                 v "Carilahg gradien dari garis yang melalui titik C (4,3) dan D (-1,-1)"
#                 menu:
#                     "4/5":
#                         jump garis_lurus
#                     "5/4":
#                         jump garis_lurus
#                     "2/5":
#                         jump garis_lurus

# label garis_lurus:
#     e "Selanjutnya kita masuk ke garis lurus"
#     e "Apa kau tahu apa itu garis lurus ?"
#     v "Garis yang berbentuk lurus?"
#     e "Gak salah sih"
#     e "Sekarang kita kan lebih fokus tentang persamaan garis lurusnya"
#     e "Persamaan garis lurus dapat kita tulis dengan bentuk Ax + By + C = 0"
#     e "Dengan A, B, C konstan menunjukkan persamaan garis"

#     image rumus dua  = im.Scale("images/Materi/rumus_2.png", 1100, 500)
#     hide jarak with dissolve
#     show rumus dua at truecenter

#     e "Jika B ≠ 0, kita tuliskan dengan bentuk berikut"
#     e "Persamaan tersebut menunjukkan gradien -A/B dan melalui titik (0,-C/B)"
#     e "Jika B=0, kita tuliskan x= -C/A"
#     e "Persamaan tersebut menunjukkan garis sejajar sumbu-y"
#     e "Oh iya, perlu diingat ya.."
#     e "Jika A=0, maka y=-C/B menunjukkan persamaan garis sejajar sumbu-x"
#     e "Jika C=0, maka y=-A/B x menunjukkan persamaan garis melalui titik pusat"
#     e "Jika A = C = 0, maka y = 0 menunjukkan persamaan sumbu-x"
#     e "Jika B = C = 0, maka x = 0 menunjukkan persamaan sumbu-y"

#     v "ngomong-ngomong, apa kau tahu tempat kedudukan suatu titik?"
#     v "Tempat kedudukan suatu titik adalah himpunan titik-titik yang anggotanya merupakan himpunan yang memiliki sifat yang sama"
#     v "Sebagai contoh"

#     image titik satu  = im.Scale("images/Materi/titik_1.png", 1100, 500)
#     hide rumus with dissolve
#     show titik satu at truecenter
    
#     v "Jika P (x,y) adalah sembarang titik yang sama jauhnya dari A (1,4) dan B (3,2), maka.."

#     image rumus tiga  = im.Scale("images/Materi/rumus_3.png", 1100, 500)
#     hide titik with dissolve
#     show rumus tiga at truecenter

#     e "PA²=PB²"
#     e "Jika kita menggunakan rumus persamaan garis, maka didapat.."
#     e "(x-1)² + (y-4)² = (x-3)² + (y-2)²"
#     e "maka didapatlah persamaan x - y = 3"
#     e "Jika garis tersebut dijalankan, persamaan semula dapat menjadi 2x - 2y = 6" 
#     e "Selanjutnya bagaimana jika ada garis lurus dengan gradien (m) melalui satu titik"

#     image gradien dua  = im.Scale("images/Materi/gradien_2.png", 1100, 500)
#     hide rumus with dissolve
#     show gradien dua at truecenter

#     e "Dari garis yang melalui A dan B dapat diketahui gradien garis tersebut dengan rumus y-y₁/x-x₁" 
#     e "Gradien garis AB diketahui sama dengan m, sehingga y-y₁ = m(x-x₁)"
#     e "Langsung ke contoh soalnya ya"
#     e "Carilah persamaan garis yang memiliki gradien 3/4 dan melewati titik (2,1)"
#     menu:
#         "3x-4y-2 = 0":
#             jump lanjut_1
#         "4x-3y-1 = 0":
#             jump lanjut_1

#             label lanjut_1:
#                 e "Jawaban yang benar adalah 3x-4y-2 =0"
#                 e "jika sudah diketahui gradien danti titiknya, kita cukup masukkansa ja 3/4 sebagai m, dan 2,1s ebaya x₁ dany y₁"
#                 e "Maka didapatlah nilai y-1 = 3/4(x-2)"
#                 e "Jika disederhanakan maka hasilnya adalah 3x - 4y - 2 = 0"

#                 jump materi

#     # image garis lurus satu  = im.Scale("images/Materi/lurus_1.png", 1100, 500)
#     # hide gradien with dissolve
#     # show garis lurus satu at truecenter

# label materi:

#     e "Jika tadi garis melalui satu titik, sekarang kita akan mencari bagaimana jika garis melalui dua titik"

#     image sumbu satu  = im.Scale("images/Materi/sumbu_1.png", 1100, 500)
#     hide gradien with dissolve
#     show sumbu satu at truecenter

#     e "Dari gambar, diketahui gradien AB adalah y-y₁/x-x₁"
#     e "Gradien AB pada pembahasan sebelumnya adalah y₂-y₁/x₂-x₁" 

#     image sumbu dua  = im.Scale("images/Materi/sumbu_1.png", 1100, 500)
#     hide sumbu with dissolve
#     show sumbu dua at truecenter

#     e "Dari kedua persamaan sebelumnya, dapat diperoleh persamaan berikut..."
#     hide sumbu with dissolve
#     v "Sepertinya sudah cukup untuk hari ini"
#     v "Jujur kepalaku mumet sekali"
#     e "Eh iya, pantes saja kamu dari tadi diam saja"
#     e "Kalau begitu kita cukupkan ya pertemuan hari ini, jangan lupa rutin cek grup ya"
#     e "Terima kasih semuanya"

#     hide erika base with dissolve
#     hide revina base with dissolve

#     "Setelah menjalani hari yang melelahkan kami bertiga pulang ke tempat tinggal masing-masing"
#     "Tanpa mandi, makan, sesampai di kosan, aku langsung tidur terkapar di kamar"
#     "End of act 1"

#     stop music

#     play music "iphone.mp3" fadeout 2.0 fadein 2.0

#     menu:
#         "Angkat Telefon":
#             jump act_2  

# label act_2 :
#     scene bg lounge with dissolve
#     play music "My Only Love.ogg"
#     "Setelah hampir sebelas jam aku tidur"
#     "Aku bangun dalam keadaan terlentang jatuh dibawah kasur"
#     "Sepertinya aku tidak sadar kalau aku sudah terjatuh dalam tidurku"
#     "Aku membuka ponselku dan melihat jam menunjukan pukul 09.00 dengan notif Whatsapp dari seorang teman yang berkata dia sudah didepan kosanku"
#     "tunggu, DIDEPAN?"
#     "Aku kaget sehingga membuat mataku yang tadinya sangat mengantuk kembali menjadi segar"
#     "Dengan pakaian yang sama dipakai kemarin aku langsung keluar kedepan pintu dan melihat Aurel bersandar dengan wajah cemberut melihatku"
#     show aurellia envy with dissolve
#     a "...."
#     a "Minimal cuci muka dulu baru keluar, jam berapa semalem kamu pulang, setidaknya rawat dirimu dulu sebelum tidur"
#     menu:
#         "Maaf...":
#             jump aurellia
#         "Itu bukan urusanmu":
#             jump aurellia
#     label aurellia:
#     "Dia adalah Aurellia, temanku dari sd, dia juga yang dari kemarin membangunkanku lewat ponsel"
#     "Perawakannya agak jutek, dan pemarah, tapi sebenarnya dia baik"
#     a "Apa kau tidak baca pesanku semalam ?"
#     menu:
#         "Pesan apa?":
#             jump aurelia
#     label aurelia:
#     a "Sudah kuduga, pasti kamu langsung tidur semalam"
#     a "Aku ingin memintamu menemaniku menonton pertandingan basket di gor siang ini"
#     a "Astaga ruangan apa ini, apa kamu rajin membersihkan rumah?"
#     a "Kenapa bisa banyak barang berantakan disini"
#     a "Karena sekarang aku marah, kamu gaboleh nolak, ayo sini bersih-bersih"
#     "Mendengar perkataan Lia, aku tidak bisa membantah perkataan dia"
#     hide aurellia
#     jump bersih_bersih

#     #Skenario 1
#     #Dika bangun tidur siap2 mau keluar dan diluar udh ditunggu sama Aurellia

#     #Latar kompleks
#     label mtk:
#     show aurellia base satu
#     a "Jadi, gimana kuliahmu"
#     d "Pusing"
#     a "Sama, aku juga, apalagi di semester akhir ini"
#     a "Makanya aku ngajak kamu buat refreshing sedikit"
#     a "Sayang sekali ya kita beda fakultas, padahal kita dlu SMA sama-sama suka matematika"
#     a "Mempung waktu masih panjang, apa kau mau belajar matematika denganku? aku saat ini sedang memperdalam materi lingkaran buat skripsiku"
#     menu:
#         "Tidak Terima kasih":
#             jump ayo
#     label ayo:
#     a "Ayolaah sebentar saja, sudah lama kita tidak belajar bareng"
#     menu:
#         "Sepertinya aku tidak bisa menolak ini":
#             jump bljr 
#     label bljr:
#     a "Terima kasihh"
#     a "Ngomong-ngomong, apa kau tahu kenapa bola itu berbentuk lingkaran?"
#     a "Apakah agar ia bisa dimainkan? atau karena bentuknya simple dan mudah dibuat?"
#     a "Aku mikirnya karena dia bisa bebas untuk dimainkan, ada yang main sambil ditendang, ada juga yang dilempar"
#     #basa basi

#     a "Lingkaran adalah tempat kedudukan titik-titik yang memiliki jarak yang sama terhadap titik tertentu"

#     image lingkaran satu  = im.Scale("images/Materi/lingkaran_1.png", 1100, 500)
#     show aurellia base satu at left
#     # hide gradien with dissolve
#     show lingkaran satu at truecenter

#     a "Misalkan P sembarang titik (x,y) pada lingkaran, maka.."

#     image lingkaran dua  = im.Scale("images/Materi/lingkaran_2.png", 1100, 500)
#     hide lingkaran with dissolve
#     show lingkaran dua at truecenter
    
#     a "OP² = x² + y²"
#     a "Atau x² + y² = a²" 
#     a "Persamaan ini berlaku untuk setiap titik pada lingkaran dan menjadi persamaan lingkaran dengan pusat O. Persamaan polar lingkaran memenuhi a = r."
#     a "Jika tadi persamaan lingkaran dengan pusat(0,0) selanjutnya kita membahas persamaan lingkaran dengan pusat (a,b)"

#     image lingkaran tiga  = im.Scale("images/Materi/lingkaran_3.png", 1100, 500)
#     hide lingkaran with dissolve
#     show lingkaran tiga at truecenter

#     a "Misalkan C adalah titik (a,b) yang merupakan titik pusat lingkaran dan misalkan P (x,y) titik pada lingkaran, maka.."
#     a "CP² = (x-a)² + (y-b)² "
#     a "Atau (x-a)² + (y-b)² = r²"
    
#     image lingkaran empat  = im.Scale("images/Materi/lingkaran_4.png", 1100, 500)
#     hide lingkaran with dissolve
#     show lingkaran empat at truecenter

#     a "Persamaan diatas dapat diubah menjadi x² + y² - 2ax - 2by + (a² + b² - r²) = 0"
#     a "atau x²+y²+Ax+By+C=0 yang disebut persamaan umum lingkaran. Dengan nilai A = -2a, B = -2b, C = a²+b²-r²"

#     image lingkaran lima  = im.Scale("images/Materi/lingkaran_5.png", 1100, 500)
#     hide lingkaran with dissolve
#     show lingkaran lima at truecenter

#     a "Dengan demikian persamaan di atas menunjukkan titik pusat lingkaran (-1/2 A,-1/2 B) dan jari-jari √(1/4 A² + 1/4 B² - C)"
#     a "Memperhatikan jari-jari tersebut, terdapat beberapa kemungkinan"
#     a "Jika 1/4 A² + 1/4 B² - C>0, maka menyatakan lingkaran nyata"
#     a "Jika 1/4 A² + 1/4 B² - C=0, maka menyatakan lingkaran dengan jari-jari nol"
#     a "Jika 1/4 A² + 1/4 B² - C>0, maka menyatakan lingkaran imajiner"

#     hide lingkaran with dissolve

#     a "Selanjutnya bagaimana jika terdapat persamaan lingkaran melalui 3 titik"    
#     a "Misalkan terdapat titik P (x₁,y₁), Q (x₂,y₂), dan R (x₃,y₃) tak segaris. Akan dibentuk persamaan lingkaran melalui ketiga titik tersebut, maka diperoleh"

#     image lingkaran enam  = im.Scale("images/Materi/lingkaran_6.png", 1100, 500)
#     # hide lingkaran with dissolve
#     show lingkaran enam at truecenter

#     a "Dari persamaan-persamaan tersebut diperoleh sistem persamaan linier 3 variabel. Melalui eliminasi dan subtistusi diperoleh nilai A, B, dan C. Selanjutnya substitusi nilai-nilai tersebut ke persamaan umum lingkaran sehingga diperoleh persamaan lingkaran melalui tiga titik tak segaris."
#     a "Cara lain yang dapat digunakan adalah menggunakan determinan"

#     image lingkaran tujuh  = im.Scale("images/Materi/lingkaran_7.png", 1100, 500)
#     hide lingkaran with dissolve
#     show lingkaran tujuh at truecenter

#     a "Misalkan terdapat titik P (x₁,y₁), Q (x₂,y₂), R (x₃,y₃), dan sembarang titik T (x,y) pada lingkaran sehingga diperoleh nilai sebagai berikut"

#     image lingkaran delapan  = im.Scale("images/Materi/lingkaran_8.png", 1100, 500)
#     hide lingkaran with dissolve
#     show lingkaran delapan at truecenter

#     a "Sistem persamaan tersebut akan memiliki penyelesaian jika determinan dari koefisien A, B, C, sebagai variabel dan konstantanya sama dengan nol"
#     a "Karena T (x,y) adalah titik sebarang pada lingkaran, maka setiap titik pada lingkaran akan memenuhi persamaan determinan tersebut"

#     hide lingkaran with dissolve

#     a "ngomong-ngomong, apakah kamu tahu tentang garis singgung dan garis kutub lingkaran?"
#     a "Garis singgung lingkaran adalah garis yang memotong atau bersinggungan dengan lingkaran hanya di sebuah titik. Selanjutnya titik tersebut disebut titik singgung"
#     a "Dalam persamaan Garis Singgung Lingkaran di titik di Titik (x₁,y₁)"
#     a "Jika P (x₁,y₁) dan Q (x₂,y₂).adalah dua titik pada lingkaran, persamaan garis PQ adalah y-y₁=(y₂-y₁)/(x₂-x₁ ) (x-x₁ )" 
#     a "Tapi x₁²+y₁² = r² = x₂² + y₂² dan y₂²-y₁² = -(x₂²+x₁²)"
#     a "Maka (y₂-y₁)/(x₂-x₁) = -(x₂+x₁)/(y₂+y₁)"
#     a "Persamaan garis PQ menjadi y-y₁=-(x₂+x₁)/(y₂+y₁) (x-x₁)"
#     # a "Sekarang misalkan Q mendekati P, persamaan garis PQ maka menjadi seperti berikut"

#     image singgung satu  = im.Scale("images/Materi/singgung_1.png", 1100, 500)
#     # hide lingkaran with dissolve
#     # show singgung satu at truecenter

#     # a "Jika lingkaran tersebut memiliki titik pusat di (a,b) maka dengan cara yang sama dapat diperoleh persamaan garis singgungnya (x-a)(x₁-a) + (y-b)(y₁-b) = r²"
#     # hide lingkaran with dissolve
#     # a "Selanjutnya ke persamaan Garis Singgung y = mx+c terhadap Lingkaran x²+y² = r²"
#     # a "Saat garis y = mx+c menyinggung lingkaran x²+y²=r² maka persamaannya menjadi x + (mx+c)² = r²(1+m²)x² + 2mcx + (c²-r²)=0"

#     # image singgung dua  = im.Scale("images/Materi/singgung_2.png", 1100, 500)
#     # hide singgung with dissolve
#     # show singgung dua at truecenter

#     # a "Karena keduanya memiliki titik yang sama (titik potong), maka persamaan di atas memiliki nilai diskriminan sama dengan nol"
#     # a "Sehingga persamaan garis singgungnya menjadi y = mx ± r√(1+m²)."
#     # a "Jika lingkaran tersebut memiliki titik pusat di (a,b) maka dengan cara yang sama dapat diperoleh persamaan garis singgungnya y-b = m(x-a) ± r√(1+m²)."

#     # hide singgung with dissolve

#     # a "Sudut antara dua lingkaran adalah sudut yang diapit oleh garis-garis singgung pada lingkaran di titik potong kedua lingkaran tersebut"

#     # image sudut satu  = im.Scale("images/Materi/sudut_1.png", 1100, 500)
#     # # hide singgung with dissolve
#     # show sudut satu at truecenter

#     # a "Sudut α pada Gambar menunjukkan sudut antara dua lingkaran dengan titik pusat P₁ dan P₂."
#     # a "Langkah-langkah untuk menentukan besar α sebagai berikut:"
#     # a "Tentukan titik potong antara dua lingkaran dengan pusat P₁ dan P₂."
#     # a "Tentukan persamaan garis singgung pada salah satu titik potongnya"
#     # a "Tentukan sudut apit kedua garis singgung menggunakan tan ⁡α = (m₁-m₂)/(1 + m₁.m₂ )"

#     # a "Oke biar langsung paham kita masuk ke latihan saja yak"
#     # a "Tentukan sudut antara x²+y²-3y-19=0 dan x²+y²-6x-16=0"
#     # a "Penyelesaiannya jadi titik potong dari kedua lingkaran tersebut adalah (3,5) dan (-1,-3)."
#     # a "Misalkan titik potong yang digunakan adalah (3,5), maka garis singgung dari L1 adalah 6x+7y-53=0 dan garis singgung L2 adalah y = 5"
#     # a "Dari garis singgung tersebut diperoleh m₁=-6/7 dan m₂=0"

#     # image sudut dua  = im.Scale("images/Soal/sudut_2.png", 1100, 500)
#     # hide sudut with dissolve
#     # show sudut dua at truecenter

#     # a "Karena sudah diketahui beberapa nilai dan variabel, maka kita cukup masukkan saja dirumus, dan sudut yangter bentuk adalah seperti gambar tertera"
#     # hide sudut with dissolve
#     a "Sepertinya sudah cukup untuk pagi ini"
#     a "Dilihat dari wajamu saja udah keliatan banget pusing"
#     a "Kalau begitu, siap-siap dari sekarang kita mau berangkat" 
#     scene bg dark
#     menu:
#         "Lagian, ngapain bahas pelajaran di pagi-pagi libur gini":
#             jump ending
    
#     label ending:
#         a "Hehe, maaf"
#         a "Sekalian buang waktu aja, sudah saatnya kita berangkat, ayo berangkat"
#         a "Ngomong ngomong menurutmu bagaimana?"
#         menu:
#             "Bagaimana apanya?":
#                 jump tampilan
#         label tampilan:
#         scene illu lia with dissolve
#         a "Bagaimana penampilanku? cocok ?"
#         menu:
#             "Cocok":
#                 jump obrol
#             "Bagus, hari ini kamu tampil cantik":
#                 jump obrol
#         label obrol:
#             a "Benarkah"
#             a "Aku harap kamu lebih terkejut melihatku berpenampilan seperti ini"
#             a "Kamu tahukan dari dulu aku selalu berpenampilan tomboy"
#             a "Anywayy, yuk langsung berangkat"
#         hide aurellia base with dissolve
#         "Setelah mengalami pagi yang memusingkan akhirnya kami pergi untuk menonton pertandingan basket bersama"
#         "Aku tidak tahu pelajaran apalagi nanti yang akan dibahas dimasa mendatang, tapi yang jelas akhirnya aku bisa bersantai dengan leluasa.."


#     return

# # Game dimulai disini.
# label start:

#     d "Setiap manusia memiliki masing-masing satu garis kehidupan"
#     d "Garis kehidupan inilah yang menjadi saksi atas setiap peristiwa yang dialami manusia"
#     d "Garis kehidupan ini memang hanya satu tapi garis ini memiliki cabang yang tak terhingga jumlahnya"
#     d "Orang-orang menyebut garis ini sebagai jalinan Garis Tak Terhingga"
#     d "Lalu, apa kalian tahu apa maksud dari itu"
#     d "Dalam setiap kehidupan manusia, kita diberi pilihan atas kehendak kita yang dimana pilihan itu memiliki konsekuensiya sendiri"
#     d "Dari kita"
#     d "Untuk Kita"
#     d "Dan demi kita lah kita memilih pilihan hidup itu"
#     d "Itulah yang diajarkan kakekku saat aku kecil bahwa hidup kita hanya sekali dan kita harus hati-hati terhadap pilihan kita"
#     d "Dan saat ini aku dihadapkan dengan pilihan yang sulit"
#     d "Sebuah pilihan yang sangat sulit untuk seorang mahasiswa semester akhir di hari ini"
#     d "Ya benar, ini adalah"
#     d "SKRIPSI!"

#     scene bg bedroom dika with dissolve
#     play music "iphone.mp3" fadeout 2.0 fadein 2.0
# menu:
#     "Angkat Telefon":
#         jump act_1

# label act_1:
#     stop music
#     d "H-Halo..?"
#     u "Halo, Dika, Niku khadu lapah? niku lupa mawat, ki pagi so wat kelas? (Halo, dika, apakah kamu sudah berangkat?, kamu tidak lupa kan kalau pagi ini kamu ada kelas?)"
#     d "mak lupa, ikah begadang cutik sebingi so (tidak kok, aku tidak lupa, cuman sedikit begadang aja semalam)"
#     u "ki khanno gelukko setengah jam lagi kelas haga mulai(kalau gitu bergegaslah setengah jam lagi akan dimulai kelasnya)"
#     d "Iya, iya, ini aku lagi siap-siap"

#     play music "Blithe.ogg"
#     scene bg campus_1 with dissolve
#     d "nah khappa ya, khadu pikha kali nyak ngikhim proposal mit telu dosen sai bida unyin-unyinna ditolak, wat kudo cakha lain? (aduh bagaimana ya, sudah berapa kali aku menirim proposal kepada 3 dosen berbeda dan semuanya ditolak apakah tidak ada cara lain?)"
#     u "niku gila nyani proposal asal khaiya khappa hana haga di tekhima? (kamu juga asal bikin proposal gimana mau diteirma jika kamu bikinnya asal-asalan)"
#     u "khappa sai proposal terakhir sepenengisanku niku serius nihhan ngeguwaiko (lalu, bagaimana dengan proposal terakhir aku dengar kamu agak serius bikinnya)"
#     d "oh sai hinno, hinno proposal sai nyak ajuko mit pak Adib, wat kemungkinan ia (owh itu, itu proposal yang aku ajukan pak Adib, ada kemungkinan dia akan mengabariku setelah kelas dia pagi ini, doain aku yang terbaik ya)"
#     u "Tentu saja"
#     d "Gawat, 5 menit lagi kelas mau dimulai, kalau gitu aku tutup dulu ya telponnya"
#     u "Okey"

#     #sfx tabrakan dengan erika
#     show erika base with dissolve
#     u "Aduhh"
#     d "Maaf aku gak sengaja, salahku kertasmu jadi berhamburan dimana-dimana" 
#     u "Iya, maaf itu salahku juga jalan tidak lihat-lihat, terima kasih ya sudah bantu."
#     d "Iya sama-sama, kalau begitu aku duluan, ya"

#     hide erika with dissolve
#     scene bg campus_interrior with dissolve

#     d "Akhirnya kelasnya selesai juga, untung saja tadi aku tepat waktu"
#     show doni base
#     r "Syukurlah kalau begitu. Ngomong-ngomong kenapa tadi kamu hampir telat"
#     d "Itu anu, tadi ada-"
#     hide doni 
#     show adib base
#     p "Baik, sekian dari perkuliahan kita hari ini, sebelum saya pergi, saya ingin bertanya-"
#     p "Apakah ada Andika Adyatama disini ?"
#     d "Hadir Pak"
#     show adib happy
#     p "Setelah ini keruangan saya, ya. Ada yang mau saya diskusikan"
#     d "Baik, Pak"
#     hide adib
#     show doni sus
#     r "Ada apa ini, apa kau sudah membuat pak Adib marah, Dik"
#     r "Jarang-jarang pak Adib manggil mahasiswa keruangannya"
#     d "Ah enggak kok, aku cuman mengajukan proposal skripsi ku saja ke Pak Adib"
#     show doni base
#     r "Secepat itu? skripsi tentang apa emang kamu ngajuinnya?"
#     d "Proposal ku membahas tentang Geometri Analitik Bidang, tapi mungkin ada perubahan terkait isi penelitiannya karena aku agak bingung mau fokus ke sub materi yang mana"
#     d "Mungkin aku akan sekalian tanyakan ke Pak Adib soal ini"
#     d "Bagaimana denganmu, Don?"
#     show doni sad
#     r "Aku masih bingung mau ngambil judul yang mana"
#     r "Ada satu judul yang bikin ku tertarik, tapi dosennya susah ditemuin"
#     r "sebaliknya dosen-dosen yang mudah ditemuin malah topik pembahasannya yang susah"
#     r "Aku jadi bingung mau lebih prioritasin kemana, hadeh..."
#     show doni happy
#     r "By the way, kelompok penelitianmu siapa saja ?"
#     d "Apa yang kau maksud?"
#     r "Kamu tidak tahu?, aku dengar mahasiswa bimbingan dia banyak yang dikerjakan selama berkompok, aku pikir kamu juga sudah ada beberapa orang yang mengerjakan topik yang sama"
#     d "Kalau itu aku kurang tau sih, aku mengajukannya juga sendiri"
#     d "Lagipula, aku juga tidak berniat mengerjakan penelitian secara berkelompok"
#     show doni base
#     r "Emangnya kenapa ?"
#     d "Menurutku kegiatan berkelompok itu melelahkan, terkadang kita malah asik bersenang-senang"
#     d "Tidak menutup kemungkinan juga ada pertengkaran ditengah penelitian"
#     d "Hal semacam itulah yang membuatku berfikir untuk mengerjakan sesuatu secara sendiri"
#     show doni happy
#     d "Tenang saja, judul penelitianku lumayan susah kok, kecil kemungkinan ada yang sama, hahahaha"
#     d "Kalau begitu, aku duluan ya, Don"
#     r "Oh iya hati-hati"
#     hide doni with dissolve

#     scene bg lecturer room with dissolve

#     "Setelah kegiatan perkuliahan, aku langsung berjalan menuju ruangan Pak Adib"
#     #sfx ketuk pintu
#     p "Silahkan masuk"
#     show erika base at left
#     show revina base at right
#     "Didalam ruangan aku melihat 2 mahasiswi yang berdiri didepan Pak Adib"
#     "Sesaat setelah mereka melihatku kedua mahasiswi itu itu langsung-"
#     "bergeser dan memberiku posisi diantara mereka berdua."
#     hide erika with dissolve
#     hide revina with dissolve
#     show adib base with dissolve
#     p "Baik terima kasih sudah hadir"
#     p "Apa kalian tahu kenapa saya mengumpulkan kalian bertiga disini?"
#     d "Apakah terkait pengajuan proposal skripsi, Pak?"
#     p "Ya, Benar"
#     show adib sus
#     p "Terkait pengajuan judul yang kalian ajukan tempo hari yang lalu"
#     p "Kebetulan judul kalian bertiga ini memiliki kemiripan."
#     p "Kalian sama-sama membahas Geometri Analitik Bidang"
#     p "dan sayangnya judul kalian ini belum spesifik untuk dijadikan topik skripsi"
#     show adib happy
#     p "maka dari itu saya ingin kalian bertiga berdiskusi lagi dan tentukan topik skripsi kalian dengan lebih spesifik lagi, oke? saya tunggu minggu depan"
#     show adib base
#     p "Sampai sini apakah ada pertanyaan?"

#     both_1 "Tidak pak"
#     hide adib with dissolve
    
#     "Sesaat setelah pertemuan singkat itu, kami bertiga pergi menuju taman didepan fakultas"

#     scene bg hall_1 with dissolve

#     show revina happy with dissolve
#     v "semakungni tekhimakasih yu khadu ngeluangko waktumu dapok diskusi dija"
#     v "semakung kham ngelajuko diskusi kham jo,kenalko pai ngekhalku Revina.."
#     v "Semester siwa(9) Matematika terapan,salam kenal yu,ukhau gaoh nyak Revi."
   
# menu:
#     "Kenalin namaku Andika panggil aja Dika, salam kenal ya":
#         jump intro 

#     "Aku Dika salam kenal ya":
#         jump intro
    
# label intro:
#     play music "good.ogg"
#     hide revina with dissolve
#     show erika happy with dissolve
    
#     e "Kenalko munih seunyinni,nyak Erika,semestr 7 pendidikan Matematika, ukhau gaoh nya Eri"
#     show erika happy
#     e "O ya dika,nekhima nihan yaa jenno pagi"
#     d "oo yaa nyak ampai ngingok niku sai jeno pagi, api sai jeno proposal mu?."
#     e "he he iyyaa,untung gaoh nyak ngumpul tepat waktu,niku pandai gaohkan pak Adib kheppa"
   
#     hide erika with dissolve
#     show revina envy with dissolve
    
#     v "jadi kak khadu jak sinji kham haga kheppa? kintu bang wat ede mu?."
   
#     hide revina with dissolve
#     show erika base with dissolve
    
#     e "kingeliakko jak percakapan jama pak Adib,kham mawat ngedok waktu lamon pakai revisi judul penelitian kham"
#     e "Kham masing-masing Nyepok judul alternatif kham.tekhus kham ngumpul pakai riviu luot hasil ni revisi kham,kheppa kikhenno?"
#     d "Kapan kham kumpul luot"

#     hide erika with dissolve
#     show revina base with dissolve

#     v "Apikah 3 khani cukup"

#     hide revina with dissolve
#     show erika base with dissolve

#     e "kinyak mak ngedok sangkutan kidang kheppa jama Dika?"
#     d "nyak munih mak ngedok masalah,kidang apikah api waktuni mak terlalu mepet?"

#     hide erika with dissolve
#     show revina base with dissolve

#     v "Na haga tikheppako,kham ikah ngedok waktu seminggu,jadi haga mak haga kham harus saling merevia dilom waktu lima khadi saiyihadap.ok.."
#     d "Ok.."

#     hide revina with dissolve
#     scene bg night city with dissolve
#     show erika base with dissolve

#     e "Tekhimakasih yu khadu ngekhi'i nyak mulang, Dika"
#     d "dang kheno,kan kosan kham searah"
#     d "Kapan niku hga ngerevisi judul mu?"
#     e "nyak khencanani hga nyepok revisi diperpustakaan kota dihadap kanah"
#     show erika envy
#     e "Kidang asal niku pandai ya,nyak mawat kinalaomga tengtang giometri hijo"
#     d "kikhanno ngasi nyak nutuk ngekhi'i niku?kintu nyak dapok kipak cutik nulung niku"
#     show erika sad
#     e "api niku yakin dapok nulung nyak belajakh?"
#     menu:
#         "Tentu saja,mari kita belajar bersama":
#             jump eri_1
    
#     label eri_1:
#     e "payu kikhenno,kidang semakung ni,api khamdapok muloh mid kampus?"
#     e "ulih buku ku jeno ketinggalan dikelas.lainhak kidebingi kheji kelas tekunci,kheppa cakha kham kukhuk?"
#     menu:
#         "Bukankah malam-malam begini kelas dikunci? bagaimana cara kita masuk?":
#             jump eri_2
    
#     label eri_2:
#     e "iyya munih ya,kidang kudengis kls umum khangok ni lagi cadang"
#     menu:
#         "Apa tidak bahaya kalau ketahuan satpam?":
#             jump eri_3
    
#     label eri_3:
#     show erika happy
#     e "tenang gaoh,kikham kepandayan kham cekelang lijung"
#     hide erika
#     jump hidden_object_example

#     label library:
#     scene bg lib_1 with dissolve
#     show erika base with dissolve
#     #sfx naruh buku
#     d "Baiklah, dari mana kita akan mulai"
#     e "Hmmmmm, apa bisa mulai dari sini ?"
#     "Erika menunjuk halaman pertama dari buku pemahaman geometri dasar"
#     d "Dari situ !?"
#     e "Kalau begitu kita mulai aja dari koordinat kartesius"

#     # image kartesius satu = im.Scale("images/Materi/kartesius_1.png", 1100, 500)
#     image kartesius satu = im.Scale("images/Materi/karte.png", 1100, 500)
   
#     hide erika with dissolve
#     show kartesius satu at truecenter 

#     e "Menurut penjelasan di buku ini, dimisalkan X'OX, dan Y'OY adalah garis yang saling tegak lurus dan P merupakan sembarang titik pada bidang datar"
#     e "Sementara PM dan PN digambar tegak lurus ke X'X dan Y'Y"

#     image kartesius dua = im.Scale("images/Materi/karte_2.png", 1100, 500)
#     hide kartesius with dissolve
#     show kartesius dua at truecenter

#     e "Jika OM = x dan ON = y"
#     image kartesius tiga = im.Scale("images/Materi/karte_3.png", 1100, 500)
#     hide kartesius with dissolve
#     show kartesius tiga at truecenter
    
#     e "dan ON = y"
#     e "Maka letak P terhadap X'X dan Y'Y dikenal ketika x dan y diketahui."
#     e "x disebut sebagai absis, dan y sebagai ordinat"
#     e "dan x,y sebagai koordinat kartesis dengan P menunjukan titik (x,y)"
#     e "lalu apa yang disebut sebagai apa X'X dan Y'Y?"
#     d "maka dapat kita simpulkan bahwa X'X merupakan sumbu x dan Y'Y disebut sumbu y"
#     e "Yap, dengan O sebagai titik pusatnya"

#     image kuadran satu = im.Scale("images/Materi/kuad.png", 1100, 500)
#     hide kartesius with dissolve
#     show kuadran satu at truecenter

#     e "selanjutnya berdasarkan sumber yang tertera dapat kita lihat bahwa"
#     e "sumbu koordinat yang membagi bidang datar menjadi empat bagian yang disebut kuadran."

#     image polar satu  = im.Scale("images/Materi/koor_polar.png", 1100, 500)
#     hide kuadran with dissolve
#     show polar satu at truecenter

#     e "selanjutnya masuk ke koordinat polar"
#     e "menurutmu, apa itu koordinat polar?"
#     d "Koordinat polar adalah koordinat yang memiliki sumbu ke arah r dan θ."
#     e "Oke jadi berdasarkan gambar yang tertera"
#     e "Dimisalkan OA merupakan sebuah garis dan P sembarang titik pada bidang datar"

#     image polar dua  = im.Scale("images/Materi/theta.png", 1100, 500)
#     hide polar with dissolve
#     show polar dua at truecenter

#     e "Misal θ merupakan sudut yang bergerak berputar dari posisi OA ke posisi OP. Jika r adalah panjang OP, letak P diketahui saat r dan θ diketahui"
#     e "Disini masalahnya aku masih bingung apa itu r dan θ. apa kau tahu sesuatu dika?"
#     d "r merupakan radius sementara θ disebut dengan sudut"
#     e "Owh jadi begitu, maka dari itu lah dapat kita simpulkan r dan θ merupakan koordinat polar dari titik P"
#     e "Yang dimana OA disebut garis awal dan O sebagai kutubnya"

#     e "Disini juga terdapat hubungan antara koordinat kartesius dan koordinat polar seperti pada gambar yang tertera"

#     image hubungan satu  = im.Scale("images/Materi/relasi_1.png", 1100, 500)
#     hide polar with dissolve
#     show hubungan satu at truecenter

#     e "'Misal P adalah titik (x,y) yang mengacu pada sumbu X'OX"
    
#     image hubungan dua  = im.Scale("images/Materi/relasi_2.png", 1100, 500)
#     hide hubungan with dissolve
#     show hubungan dua at truecenter
    
#     e "dan Y'OY"

#     image hubungan tiga  = im.Scale("images/Materi/relasi_3.png", 1100, 500)
#     hide hubungan with dissolve
#     show hubungan dua at truecenter
    
#     e "dan titik (r,θ) yang mengacu pada kutub O dan garis awal OX"

#     image hubungan empat  = im.Scale("images/Materi/relasi_4.png", 1100, 500)
#     hide hubungan with dissolve
#     show hubungan empat at truecenter

#     e "menurutmu dengan menggunakan definisi fungsi lingkaran, bagaimana cara mencari nilai x ?"

#     image rumus satu  = im.Scale("images/Materi/rumus_1.png", 1100, 500)
#     hide hubungan with dissolve
#     show rumus satu at truecenter

#     d "Untuk mencari x dapat menggunakan rumus r cos θ"
#     d "Demikian juga y dapat menggunakan rumus r sin θ"

#     hide rumus with dissolve
#     show hubungan dua at truecenter

#     e "maka dengan demikian, kita dapat menyimpulkan untuk mencari nilai tan θ dapat menggunakan rumus y/x"

#     "Setelah itu kami menghabiskan waktu belajar di perpustakaan kota sampai perpustakaan tutup"
    
#     scene bg night city
#     show erika base with dissolve
    
#     e "Terima kasih ya dika udh menemaniku mencari referensi"
#     d "Sama-sama"
#     e "Ohiya sepertinya aku sudah dapat judul yang sesuai"
#     d "Apa itu?"
#     e "Aku akan menganalisis Perbandingan Representasi Koordinat Kartesius dan Polar dalam Penggambaran Data Geometri"
#     e "Gimana, bagus, kan?"
#     d "Bagus-bagus"
#     e "Kalau begitu aku duluan ya, kosanku disini"
#     e "Dika jangan lupa revisianmu, ya, terima kasih, bye bye"

#     "Tiga Hari Kemudian"
#     scene bg cafe_1 with dissolve
#     show revina base with dissolve

#     v "Jadi, gimana, sudah ada pencerahan?"
#     "suasana sempat hening, sesaat setelah itu Revina menoleh ke Erika yang sedang melamun"
#     v "Erika?"

#     show revina base at right
#     show erika happy at left

#     e "Oh, iya, maaf ya kak aku sempat melamun tadi hehe"
#     v "Tenang-tenang, jangan dipikirin"
#     show revina happy at right
#     v "ngomong-ngomong, kalian cukup manggil aku revi aja selagi ini pertemuan nonformal"
#     v "aku sih lebih nyaman dipanggil begitu"
#     show erika base at left
#     d "lalu bagaimana saaat pertemuan formal"
#     show revina envy at right
#     v "yang manggil 'kak' lah"
#     show revina base at right
#     e "Baik, mungkin sebaiknya kita kembali ke topik diskusi kita ya Revi, Dika ?"
#     v "Oh ya, maaf-maaf, aku  terlalu terbawa suasana tadi"
#     e "Untuk topik utama penelitianku aku ingin membahas terkait representasi koordinat kartesius dan dan koordinat polar dalam penggambaran data geometri"
#     v "kalau menurut revi gimana?"
#     v "Menurutku sih tidak ada masalah terkait judulmu itu, tapi menurutku terdapat permasalahan dalam transformasi antara koordinat kartesian dan polar"
#     v "karena dalam proses transformasi itu merupakan proses yang rumit terutama dalam konteks data yang kompleks atau dalam analisis yang memerlukan banyak transformasi koordinat"
#     e "Ada benarnya sih, namun pilihan antara koordinat kartesian dan polar tergantung pada sifat data yang akan direpresentasikan dan tujuan analisisnya"
#     e "Dan juga, dalam beberapa kasus, mungkin perlu menggunakan keduanya secara bersamaan atau menggabungkan elemen-elemen dari masing-masing sistem koordinat untuk mendapatkan representasi yang paling informatif dan relevan"
#     e "Jadi menurutku, so far, tidak permasalahan serius dalam judul penelitianku ini"
#     e "Bagaimana dengan mu, kak ?"
    
#     #Pembahasan Jarak, Perbandingan, dan Gradien

#     #Rumus Jarak
#     v "Sebelumnya kita pahami bagaimana cara mengetahui rumus untuk mendapatkan jarak"
#     image jarak satu  = im.Scale("images/Materi/jarak_1.png", 1100, 500)
#     # hide polar with dissolve
#     show jarak satu at truecenter
#     v "Misalkan A dan B adalah titik X1,Y1 dan X2,Y2"
#     v "r panjang AB dan θ sudut inklinasi dari AB ke OX"
    
#     v "Maka dapat kita simpulkan"

#     image jarak dua  = im.Scale("images/Materi/jarak_2.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak dua at truecenter

#     v "r cos θ = x₂-x₁" 

#     image jarak tiga  = im.Scale("images/Materi/jarak_3.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak tiga at truecenter

#     v "r sin θ = y₂-y₁"
#     v "Dengan kedua rumus yang tadi kita sebutkan, maka untuk mendapatkan nilai dari r kita tinggal memasukkan 2 variabel yang kita sebutkan tadi"

#     image jarak empat  = im.Scale("images/Materi/jarak_4.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak empat at truecenter

#     v "Didapatlah rumus sebagai berikut"
#     e "Panjang ya..."
#     v "Kamu diam.."
#     v "Untuk memperoleh nilai r, kira dapat memanfaatkan sifat persamaan trigonometri dimana nilai jumlah dari cos dan sin kuadrat θ bernilai 1 (satu)"

#     image jarak lima  = im.Scale("images/Materi/jarak_5.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak lima at truecenter

#     v "Dalam kasus tertentu, r dapat diperoleh dengan cara berikut"

#     image jarak enam  = im.Scale("images/Materi/jarak_6.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak enam at truecenter

#     v "Misalkan MA dan NB  adalah ordinat dari A (x₁,y₁), B (x₂,y₂)"

#     image jarak tujuh  = im.Scale("images/Materi/jarak_7.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak tujuh at truecenter

#     v "Dan misalkan AC sejajar OX, memotong NB di C"
    
#     image jarak delapan  = im.Scale("images/Materi/jarak_8.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak delapan at truecenter

#     v "Maka dapat disimpulkan untuk mencari nilai kuadrat dari jarak adalah dengan menggunakan rumus pythagoras yaitu penjumlahan dari kuadrat AC dan kuadrat CB"
#     v "Perlu diingat, rumus ini hanya berlaku jika nilai NC = MA"
#     v "Oke kalau gitu mari kita kerjakaan contoh soal"
#     v "Erika, Carilah jarak antara titik (-2,1) dan (4,9)"
#     e "Sebentar.."
#     "Erika langsung mengambil penanya dan mengerjakaan soal yang diberikan Revina di kertas kosong"
#     e "10, apakah benar?"
#     v "Ya benar sekali"
#     v "Oke, mari kita masuk ke pembahasan, kenapa bisa didapatkan nilai 10?" 

#     image soal satu  = im.Scale("images/Soal/soal_1.png", 1100, 500)
#     hide jarak with dissolve
#     show soal satu at truecenter

#     v "Seperti yang sudah dikerjakan erika, kita cukup memasukkan rumus √(x₂-x₁)²+(y₂-y₁)²"
#     v "Jangan lupa sebelum mengerjakan soal, kita pahami dulu apa saja yang diketahui"
#     v "Diketahui x₁ = -2, y₁ = 1"
#     v "Sementara x₂ = 4 dan y₂ = 9"
#     v "Dengan memasukkan rumus √(x₂-x₁)²+(y₂-y₁)²"
#     v "Maka didapatlah nilai √100 yaitu 10"

#     v "Untuk rumus selanjutnya ada rumus perbandingan jarak"

#     image jarak sembilan  = im.Scale("images/Materi/jarak_9.png", 1100, 500)
#     hide soal with dissolve
#     show jarak sembilan at truecenter
    

#     v "Misalkan A dan B adalah titik (x₁,y₁), (x₂,y₂) dan θ adalah sudut dari AB ke sumbu-x" 
#     v "Kita misalkan P (x,y) adalah titik pada AB sedemikian hingga AP:PB = K:L"

#     image jarak sepuluh  = im.Scale("images/Materi/jarak_10.png", 1100, 500)
#     hide jarak with dissolve
#     show jarak sepuluh at truecenter

#     v "Maka dapat kita simpulkan bahwa untuk mencari nilai AP cos θ = x - x₁"
#     v "Dan untuk nilai PB cos θ = x₂ - x"
#     v "Dengan menggunakan perbandingan antara AP:PB, maka kita dapat membandingkan nilai (x - x₁)/(x₂ - x)"
#     v "Kita dapat mengkali silang nilai AP:PB dan K:L, maka didapatlah nilai kx₂ + lx₁ = (k + l)x"
#     v "Dengan itu, untuk mencari nilai x pada perbandingan jarak antar dua titik, kita dapat menggunakan rumus yang tertera"
#     v "Rumus ini juga berlaku jika kita juga ingin mencari nilai y"
#     hide jarak with dissolve
#     v "Oke, selanjutnya kita langsung bahas soal saja"
#     v "Dika, kali ini giliran kamu, ya"
#     v "Carilah koordinat P yang membagi garis A (-7,1) dan B (3,6) dengan rasio 3:2"
#     menu:
#         "P(-1,4)":
#             jump benar_satu
        
#         "P(4,-1)":
#             jump salah_satu
        
#         "P(1,-4)":
#             jump salah_satu
        
#         "P(1,4)":
#             jump salah_satu
    
#     label salah_satu:
#         show revina envy at right
#         v "Apa kamu memerhatikan penjelasanku tadi?"
#         v "Kau tidak tertidur kan?"
#         menu:
#             "Tentu saja tidak, apa jawabanku salah?":
#                 jump lanjut
#             "Hehe, maaf, apa jawabanku salah?":
#                 jump lanjut

#                 label lanjut:
#                     v "Tentu saja salah"
#                     jump penjelasan
    
#     label benar_satu:
#         show revina happy at right
#         v "Benar sekali, tidak sia-sia aku ngomong panjang lebar haha"
#         jump penjelasan
    
#     label penjelasan:
#         show revina happy at right
#         v "Oke, mari kita bahas bareng-bareng ya"
#         v "Erika silahkan.."
#         e "Oke, mari kita mulai lihat nilai yang diketahui dulu"
#         e "Diketahui x₁ = -7 dan y₁ = 1"
#         e "Sementara nilai x₂ = 3 dan y₂ = 6"
#         e "untuk rasionya bernilai 3:2, yang artinya nilai k = 3 dan l = 2"
        
#         image jarak sebelas  = im.Scale("images/Materi/jarak_11.png", 1100, 500)
#         # hide jarak with dissolve
#         # show jarak sebelas at truecenter

#         e "Dengan memasukan rumus yang telah kita bahas barusan"

#         image soal dua  = im.Scale("images/Soal/soal_2.png", 1100, 500)
#         # hide jarak with dissolve
#         show soal dua at truecenter

#         e "maka kita cukup masukkan saja semua nilai yang diketahui"
#         e "nilai x kita mendapat nilai -1, sementara untuk y bernilai 4"
#         e "oleh karena itu koordinat P yang tepat adalah P(-1,4)"

#         hide soal with dissolve
#         jump gradien
# label gradien:
#     e "Terakhir kita membahas gradien"
#     e "Gradien dari suatu garis didefinisikan sebagai garis singgung sudut yang dibuat oleh garis tersebut dengan arah positif dari sumbu-x"
#     image gradien satu  = im.Scale("images/Materi/gradien_1.png", 1100, 500)
#     # hide jarak with dissolve
#     show gradien satu at truecenter
#     e "Gradien garis melalui dua titik (x₁,y₁), (x₂,y₂) adalah y₂-y₁/x₂-x₁"
#     e "Kita langsung masuk ke contoh soal saja"
#     e "Diketahui A, B, C, D adalah titik (-1,3), (1,0), (4,2), (0,8). Tunjukkan bahwa AB⊥BC(Tegak Lurus) dan juga AB∥DC(Sejajar)"
#     e "Karena x dan y masing-masing titik sudah diketahui, kita cukup masukkan masing-masing nilai yang ada"
#     image soal tiga  = im.Scale("images/Soal/soal_3.png", 1100, 500)
#     hide gradien with dissolve
#     show soal tiga at truecenter
#     e "Kesimpulan yang kita dapat adalah titik AB⊥BC karena hasil kali gradiennya -1 dan  AB∥DC karena gradiennya sama"
#     e "Sampai sini mudahkan?"
#     e "Sebelum kita masuk ke materi selanjutnya, mari kita mengerjakan latihan"
#     v "Apa kau siap, Dika?"
#     hide soal with dissolve

#     menu:
#         "Tentu Saja":
#             jump soal

#             label soal:
#                 v "Okay, soal pertama.."
#                 v "Carilah jarak antar dua titik (0,4) dan (7,2)"
#                 menu:
#                     "√53":
#                         jump dua
#                     "√50":
#                         jump dua
#                     "√52":
#                         jump dua
            
#             label dua:
#                 v "Selanjutnya nomor 2"
#                 v "Carilah perbandingan AP:PB pada titik P (4,-2) terletak pada garis yang melalui A (7,-3) dan B (-5,1)"
#                 menu  :
#                     "2:4":
#                         jump tiga
#                     "1:3":
#                         jump tiga
#                     "1:5":
#                         jump tiga
            
#             label tiga:
#                 v "Hmmmmm....Tidak buruk"
#                 v "Terakhir ya"
#                 v "Carilah gradien dari garis yang melalui titik C (4,3) dan D (-1,-1)"
#                 menu:
#                     "4/5":
#                         jump garis_lurus
#                     "5/4":
#                         jump garis_lurus
#                     "2/5":
#                         jump garis_lurus

# label garis_lurus:
#     e "Selanjutnya kita masuk ke garis lurus"
#     e "Apa kau tahu apa itu garis lurus ?"
#     v "Garis yang berbentuk lurus?"
#     e "Gak salah sih"
#     e "Sekarang kita kan lebih fokus tentang persamaan garis lurusnya"
#     e "Persamaan garis lurus dapat kita tulis dengan bentuk Ax + By + C = 0"
#     e "Dengan A, B, C konstan menunjukkan persamaan garis"

#     image rumus dua  = im.Scale("images/Materi/rumus_2.png", 1100, 500)
#     hide jarak with dissolve
#     show rumus dua at truecenter

#     e "Jika B ≠ 0, kita tuliskan dengan bentuk berikut"
#     e "Persamaan tersebut menunjukkan gradien -A/B dan melalui titik (0,-C/B)"
#     e "Jika B=0, kita tuliskan x= -C/A"
#     e "Persamaan tersebut menunjukkan garis sejajar sumbu-y"
#     e "Oh iya, perlu diingat ya.."
#     e "Jika A=0, maka y=-C/B menunjukkan persamaan garis sejajar sumbu-x"
#     e "Jika C=0, maka y=-A/B x menunjukkan persamaan garis melalui titik pusat"
#     e "Jika A = C = 0, maka y = 0 menunjukkan persamaan sumbu-x"
#     e "Jika B = C = 0, maka x = 0 menunjukkan persamaan sumbu-y"

#     v "ngomong-ngomong, apa kau tahu tempat kedudukan suatu titik?"
#     v "Tempat kedudukan suatu titik adalah himpunan titik-titik yang anggotanya merupakan himpunan yang memiliki sifat yang sama"
#     v "Sebagai contoh"

#     image titik satu  = im.Scale("images/Materi/titik_1.png", 1100, 500)
#     hide rumus with dissolve
#     show titik satu at truecenter
    
#     v "Jika P (x,y) adalah sembarang titik yang sama jauhnya dari A (1,4) dan B (3,2), maka.."

#     image rumus tiga  = im.Scale("images/Materi/rumus_3.png", 1100, 500)
#     hide titik with dissolve
#     show rumus tiga at truecenter

#     e "PA²=PB²"
#     e "Jika kita menggunakan rumus persamaan garis, maka didapat.."
#     e "(x-1)² + (y-4)² = (x-3)² + (y-2)²"
#     e "maka didapatlah persamaan x - y = 3"
#     e "Jika garis tersebut dijalankan, persamaan semula dapat menjadi 2x - 2y = 6" 
#     e "Selanjutnya bagaimana jika ada garis lurus dengan gradien (m) melalui satu titik"

#     image gradien dua  = im.Scale("images/Materi/gradien_2.png", 1100, 500)
#     hide rumus with dissolve
#     show gradien dua at truecenter

#     e "Dari garis yang melalui A dan B dapat diketahui gradien garis tersebut dengan rumus (y-y₁)/(x-x₁)" 
#     e "Gradien garis AB diketahui sama dengan m, sehingga y-y₁ = m(x-x₁)"
#     e "Langsung ke contoh soalnya ya"
#     e "Carilah persamaan garis yang memiliki gradien 3/4 dan melewati titik (2,1)"
#     hide gradien
#     menu:
#         "3x-4y-2 = 0":
#             jump lanjut_1
#         "4x-3y-1 = 0":
#             jump lanjut_1

#             label lanjut_1:
#                 e "Jawaban yang benar adalah 3x-4y-2 = 0"
#                 e "jika sudah diketahui gradien dan titiknya, kita cukup masukkan saja 3/4 sebagai m, dan 2,1 sebagai x₁ dan y₁"
#                 e "Maka didapatlah nilai y-1 = 3/4(x-2)"
#                 e "Jika disederhanakan maka hasilnya adalah 3x - 4y - 2 = 0"

#                 jump materi

#     # image garis lurus satu  = im.Scale("images/Materi/lurus_1.png", 1100, 500)
#     # hide gradien with dissolve
#     # show garis lurus satu at truecenter

# label materi:

#     e "Jika tadi garis melalui satu titik, sekarang kita akan mencari bagaimana jika garis melalui dua titik"

#     image sumbu satu  = im.Scale("images/Materi/sumbu_1.png", 1100, 500)
#     hide gradien with dissolve
#     show sumbu satu at truecenter

#     e "Dari gambar, diketahui gradien AB adalah y-y₁/x-x₁"
#     e "Gradien AB pada pembahasan sebelumnya adalah y₂-y₁/x₂-x₁" 

#     image sumbu dua  = im.Scale("images/Materi/sumbu_1.png", 1100, 500)
#     hide sumbu with dissolve
#     show sumbu dua at truecenter

#     e "Dari kedua persamaan sebelumnya, dapat diperoleh persamaan berikut..."
#     hide sumbu with dissolve
#     v "Sepertinya sudah cukup untuk hari ini"
#     v "Jujur kepalaku mumet sekali"
#     e "Eh iya, pantes saja kamu dari tadi diam saja"
#     e "Kalau begitu kita cukupkan ya pertemuan hari ini, jangan lupa rutin cek grup ya"
#     e "Terima kasih semuanya"

#     hide erika base with dissolve
#     hide revina base with dissolve

#     "Setelah menjalani hari yang melelahkan kami bertiga pulang ke tempat tinggal masing-masing"
#     "Tanpa mandi, makan, sesampai di kosan, aku langsung tidur terkapar di kamar"
#     "End of act 1"

#     stop music

#     play music "iphone.mp3" fadeout 2.0 fadein 2.0

#     menu:
#         "Angkat Telefon":
#             jump act_2  

# label act_2 :
    # scene bg lounge with dissolve
    # play music "My Only Love.ogg"
    # "Setelah hampir sebelas jam aku tidur"
    # "Aku bangun dalam keadaan terlentang jatuh dibawah kasur"
    # "Sepertinya aku tidak sadar kalau aku sudah terjatuh dalam tidurku"
    # "Aku membuka ponselku dan melihat jam menunjukan pukul 09.00 dengan notif Whatsapp dari seorang teman yang berkata dia sudah didepan kosanku"
    # "tunggu, DIDEPAN?"
    # "Aku kaget sehingga membuat mataku yang tadinya sangat mengantuk kembali menjadi segar"
    # "Dengan pakaian yang sama dipakai kemarin aku langsung keluar kedepan pintu dan melihat Aurel bersandar dengan wajah cemberut melihatku"
    # show aurellia envy with dissolve
    # a "...."
    # a "Minimal cuci muka dulu baru keluar, jam berapa semalem kamu pulang, setidaknya rawat dirimu dulu sebelum tidur"
    # menu:
    #     "Maaf...":
    #         jump aurellia
    #     "Itu bukan urusanmu":
    #         jump aurellia
    # label aurellia:
    # "Dia adalah Aurellia, temanku dari sd, dia juga yang dari kemarin membangunkanku lewat ponsel"
    # "Perawakannya agak jutek, dan pemarah, tapi sebenarnya dia baik"
    # a "Apa kau tidak baca pesanku semalam ?"
    # menu:
    #     "Pesan apa?":
    #         jump aurelia
    # label aurelia:
    # a "Sudah kuduga, pasti kamu langsung tidur semalam"
    # a "Aku ingin memintamu menemaniku menonton pertandingan basket di gor siang ini"
    # a "Astaga ruangan apa ini, apa kamu rajin membersihkan rumah?"
    # a "Kenapa bisa banyak barang berantakan disini"
    # a "Karena sekarang aku marah, kamu gaboleh nolak, ayo sini bersih-bersih"
    # "Mendengar perkataan Lia, aku tidak bisa membantah perkataan dia"
    # hide aurellia
    # jump bersih_bersih

    # #Skenario 1
    # #Dika bangun tidur siap2 mau keluar dan diluar udh ditunggu sama Aurellia

    # #Latar kompleks
    # label mtk:
    # show aurellia base satu
    # a "Jadi, gimana kuliahmu"
    # d "Pusing"
    # a "Sama, aku juga, apalagi di semester akhir ini"
    # a "Makanya aku ngajak kamu buat refreshing sedikit"
    # a "Sayang sekali ya kita beda fakultas, padahal kita dlu SMA sama-sama suka matematika"
    # a "Mempung waktu masih panjang, apa kau mau belajar matematika denganku? aku saat ini sedang memperdalam materi lingkaran buat skripsiku"
    # menu:
    #     "Tidak Terima kasih":
    #         jump ayo
    # label ayo:
    # a "Ayolaah sebentar saja, sudah lama kita tidak belajar bareng"
    # menu:
    #     "Sepertinya aku tidak bisa menolak ini":
    #         jump bljr 
    # label bljr:
    # a "Terima kasihh"
    # a "Ngomong-ngomong, apa kau tahu kenapa bola itu berbentuk lingkaran?"
    # a "Apakah agar ia bisa dimainkan? atau karena bentuknya simple dan mudah dibuat?"
    # a "Aku mikirnya karena dia bisa bebas untuk dimainkan, ada yang main sambil ditendang, ada juga yang dilempar"
    # #basa basi

    # a "Lingkaran adalah tempat kedudukan titik-titik yang memiliki jarak yang sama terhadap titik tertentu"

    # image lingkaran satu  = im.Scale("images/Materi/lingkaran_1.png", 1100, 500)
    # show aurellia base satu at left
    # # hide gradien with dissolve
    # show lingkaran satu at truecenter

    # a "Misalkan P sembarang titik (x,y) pada lingkaran, maka.."

    # image lingkaran dua  = im.Scale("images/Materi/lingkaran_2.png", 1100, 500)
    # hide lingkaran with dissolve
    # show lingkaran dua at truecenter
    
    # a "OP² = x² + y²"
    # a "Atau x² + y² = a²" 
    # a "Persamaan ini berlaku untuk setiap titik pada lingkaran dan menjadi persamaan lingkaran dengan pusat O. Persamaan polar lingkaran memenuhi a = r."
    # a "Jika tadi persamaan lingkaran dengan pusat(0,0) selanjutnya kita membahas persamaan lingkaran dengan pusat (a,b)"

    # image lingkaran tiga  = im.Scale("images/Materi/lingkaran_3.png", 1100, 500)
    # hide lingkaran with dissolve
    # show lingkaran tiga at truecenter

    # a "Misalkan C adalah titik (a,b) yang merupakan titik pusat lingkaran dan misalkan P (x,y) titik pada lingkaran, maka.."
    # a "CP² = (x-a)² + (y-b)² "
    # a "Atau (x-a)² + (y-b)² = r²"
    
    # image lingkaran empat  = im.Scale("images/Materi/lingkaran_4.png", 1100, 500)
    # hide lingkaran with dissolve
    # show lingkaran empat at truecenter

    # a "Persamaan diatas dapat diubah menjadi x² + y² - 2ax - 2by + (a² + b² - r²) = 0"
    # a "atau x²+y²+Ax+By+C=0 yang disebut persamaan umum lingkaran. Dengan nilai A = -2a, B = -2b, C = a²+b²-r²"

    # image lingkaran lima  = im.Scale("images/Materi/lingkaran_5.png", 1100, 500)
    # hide lingkaran with dissolve
    # show lingkaran lima at truecenter

    # a "Dengan demikian persamaan di atas menunjukkan titik pusat lingkaran (-1/2 A,-1/2 B) dan jari-jari √(1/4 A² + 1/4 B² - C)"
    # a "Memperhatikan jari-jari tersebut, terdapat beberapa kemungkinan"
    # a "Jika 1/4 A² + 1/4 B² - C>0, maka menyatakan lingkaran nyata"
    # a "Jika 1/4 A² + 1/4 B² - C=0, maka menyatakan lingkaran dengan jari-jari nol"
    # a "Jika 1/4 A² + 1/4 B² - C>0, maka menyatakan lingkaran imajiner"

    # hide lingkaran with dissolve

    # a "Selanjutnya bagaimana jika terdapat persamaan lingkaran melalui 3 titik"    
    # a "Misalkan terdapat titik P (x₁,y₁), Q (x₂,y₂), dan R (x₃,y₃) tak segaris. Akan dibentuk persamaan lingkaran melalui ketiga titik tersebut, maka diperoleh"

    # image lingkaran enam  = im.Scale("images/Materi/lingkaran_6.png", 1100, 500)
    # # hide lingkaran with dissolve
    # show lingkaran enam at truecenter

    # a "Dari persamaan-persamaan tersebut diperoleh sistem persamaan linier 3 variabel. Melalui eliminasi dan subtistusi diperoleh nilai A, B, dan C. Selanjutnya substitusi nilai-nilai tersebut ke persamaan umum lingkaran sehingga diperoleh persamaan lingkaran melalui tiga titik tak segaris."
    # a "Cara lain yang dapat digunakan adalah menggunakan determinan"

    # image lingkaran tujuh  = im.Scale("images/Materi/lingkaran_7.png", 1100, 500)
    # hide lingkaran with dissolve
    # show lingkaran tujuh at truecenter

    # a "Misalkan terdapat titik P (x₁,y₁), Q (x₂,y₂), R (x₃,y₃), dan sembarang titik T (x,y) pada lingkaran sehingga diperoleh nilai sebagai berikut"

    # image lingkaran delapan  = im.Scale("images/Materi/lingkaran_8.png", 1100, 500)
    # hide lingkaran with dissolve
    # show lingkaran delapan at truecenter

    # a "Sistem persamaan tersebut akan memiliki penyelesaian jika determinan dari koefisien A, B, C, sebagai variabel dan konstantanya sama dengan nol"
    # a "Karena T (x,y) adalah titik sebarang pada lingkaran, maka setiap titik pada lingkaran akan memenuhi persamaan determinan tersebut"

    # hide lingkaran with dissolve

    # a "ngomong-ngomong, apakah kamu tahu tentang garis singgung dan garis kutub lingkaran?"
    # a "Garis singgung lingkaran adalah garis yang memotong atau bersinggungan dengan lingkaran hanya di sebuah titik. Selanjutnya titik tersebut disebut titik singgung"
    # a "Dalam persamaan Garis Singgung Lingkaran x² + y² = r² di titik (x₁,y₁)"
    # a "Jika P (x₁,y₁) dan Q (x₂,y₂).adalah dua titik pada lingkaran, persamaan garis PQ adalah y-y₁=(y₂-y₁)/(x₂-x₁ ) (x-x₁ )" 
    # a "Tapi x₁²+y₁² = r² = x₂² + y₂² dan y₂²-y₁² = -(x₂²+x₁²)"
    # a "Maka (y₂-y₁)/(x₂-x₁) = -(x₂+x₁)/(y₂+y₁)"
    # a "Persamaan garis PQ menjadi y-y₁=-(x₂+x₁)/(y₂+y₁) (x-x₁)"
    # # a "Sekarang misalkan Q mendekati P, persamaan garis PQ maka menjadi seperti berikut"

    # image singgung satu  = im.Scale("images/Materi/singgung_1.png", 1100, 500)
    # hide lingkaran with dissolve
    # show singgung satu at truecenter

    # a "Jika lingkaran tersebut memiliki titik pusat di (a,b) maka dengan cara yang sama dapat diperoleh persamaan garis singgungnya (x-a)(x₁-a) + (y-b)(y₁-b) = r²"
    # hide lingkaran with dissolve
    # a "Selanjutnya ke persamaan Garis Singgung y = mx+c terhadap Lingkaran x²+y² = r²"
    # a "Saat garis y = mx+c menyinggung lingkaran x²+y²=r² maka persamaannya menjadi x + (mx+c)² = r²(1+m²)x² + 2mcx + (c²-r²)=0"

    # image singgung dua  = im.Scale("images/Materi/singgung_2.png", 1100, 500)
    # hide singgung with dissolve
    # show singgung dua at truecenter

    # a "Karena keduanya memiliki titik yang sama (titik potong), maka persamaan di atas memiliki nilai diskriminan sama dengan nol"
    # a "Sehingga persamaan garis singgungnya menjadi y = mx ± r√(1+m²)."
    # a "Jika lingkaran tersebut memiliki titik pusat di (a,b) maka dengan cara yang sama dapat diperoleh persamaan garis singgungnya y-b = m(x-a) ± r√(1+m²)."

    # hide singgung with dissolve

    # a "Sudut antara dua lingkaran adalah sudut yang diapit oleh garis-garis singgung pada lingkaran di titik potong kedua lingkaran tersebut"

    # image sudut satu  = im.Scale("images/Materi/sudut_1.png", 1100, 500)
    # # hide singgung with dissolve
    # show sudut satu at truecenter

    # a "Sudut α pada Gambar menunjukkan sudut antara dua lingkaran dengan titik pusat P₁ dan P₂."
    # a "Langkah-langkah untuk menentukan besar α sebagai berikut:"
    # a "Tentukan titik potong antara dua lingkaran dengan pusat P₁ dan P₂."
    # a "Tentukan persamaan garis singgung pada salah satu titik potongnya"
    # a "Tentukan sudut apit kedua garis singgung menggunakan tan ⁡α = (m₁-m₂)/(1 + m₁.m₂ )"

    # a "Oke biar langsung paham kita masuk ke latihan saja yak"
    # a "Tentukan sudut antara x²+y²-3y-19=0 dan x²+y²-6x-16=0"
    # a "Penyelesaiannya jadi titik potong dari kedua lingkaran tersebut adalah (3,5) dan (-1,-3)."
    # a "Misalkan titik potong yang digunakan adalah (3,5), maka garis singgung dari L1 adalah 6x+7y-53=0 dan garis singgung L2 adalah y = 5"
    # a "Dari garis singgung tersebut diperoleh m₁=-6/7 dan m₂=0"

    # image sudut dua  = im.Scale("images/Soal/sudut_2.png", 1100, 500)
    # hide sudut with dissolve
    # show sudut dua at truecenter

    # a "Karena sudah diketahui beberapa nilai dan variabel, maka kita cukup masukkan saja dirumus, dan sudut yangter bentuk adalah seperti gambar tertera"
    # hide sudut with dissolve
    # a "Sepertinya sudah cukup untuk pagi ini"
    # a "Dilihat dari wajamu saja udah keliatan banget pusing"
    # a "Kalau begitu, siap-siap dari sekarang kita mau berangkat" 
    # scene bg dark
    # menu:
    #     "Lagian, ngapain bahas pelajaran di pagi-pagi libur gini":
    #         jump ending
    
    # label ending:
    #     a "Hehe, maaf"
    #     a "Sekalian buang waktu aja, sudah saatnya kita berangkat, ayo berangkat"
    #     a "Ngomong ngomong menurutmu bagaimana?"
    #     menu:
    #         "Bagaimana apanya?":
    #             jump tampilan
    #     label tampilan:
    #     # scene illu lia with dissolve

    #         jump soal_lingkaran

    # label soal_lingkaran:
    #     scene bg park_1
    #     show aurellia happy with dissolve
    #     # a "Akhirnya kita keluar juga"
    #     a "Bagaimana penampilanku? cocok ?"
    #     menu:
    #         "Cocok":
    #             jump obrol
    #         "Bagus, hari ini kamu tampil cantik":
    #             jump obrol
    #     label obrol:
    #         a "Benarkah"
    #         a "Aku harap kamu lebih terkejut melihatku berpenampilan seperti ini"
    #         a "Kamu tahukan dari dulu aku selalu berpenampilan tomboy"
    #         # a "Anywayy, yuk langsung berangkat"
    #     show aurellia envy
    #     a "Jujur aku gakuat tadi pertama kali masuk, liat ruangan berantakan banget"
    #     a "Untung saja ada aku, kalau gak, gak bakal diberesin tuh"
    #     show aurellia base satu
    #     a "Anywayyy, kamu tau gak, Dik"
    #     a "Tadi, sebelum aku ketempatmu, aku tadi lihat bu Putri, kamu masih inget bu Putri, gak?"
    #     a "Bu Putri yang bikin kue segubal itu..."
    #     a "Denger-denger dia nerima pesenan sampe 1000 kue segubal,tahu.."
    #     menu :
    #         "Emang kue sebanyak itu, buat apaan?":
    #             jump kue
    #         "Bukannya itu udh gak normal pesenannya, banyak benget":
    #             jump kue
        
    #     label kue:
    #         a "Yah diliat dari tanggal sekarang si, kayaknya mau dibuat untuk lebaran minggu depan, wajar sih"
    #         a "Ngomongin kue segubal nih..."
        
    #     menu:
    #         "Ah jangan lagi..":
    #             jump soal_22
    #         "Pasti pertanyaan lagi":
    #             jump soal_22
        
    #     label soal_22:
    #         a "Hehe..."
    #         a "Menurutmu, dari obrolan ku tadi, misal nih ya, Bu Putri bikin 2 macam ukuran masing-masing diameter segubalnya 4cm dan 5cm..."
    #         a "Apa kamu bisa menentukan persamaan lingkaran yang melalui titik (0,0) pada kue tersebut?"
    #     show aurellia base satu at left
    #     image kue  = im.Scale("images/Materi/kue.png", 1100, 500)
    #     # hide titik with dissolve
    #     show kue at truecenter
    #     a "Ayo aku beri kamu waktu mikir dulu"
    #     a "Tapi jangan lama-lama ya, hehe.."
    #     hide kue
    #     jump choice

    #     label choice:
    #         show aurellia base satu
    #         a "Gimana berapa persamaan untuk masing-masing diameter 4cm dan 5cm?"
    #         menu:
    #             "x² + y² = 2² dan x² + y² = 2,5²":
    #                 jump benarr
    #             "2x² + 4y² = 3² dan 3x² + y² = 2,5²":
    #                 jump slhh
    #             "x² + y² = 2² dan 5x² + y² = 5²":
    #                 jump slhh
            
    #         label slhh:
    #             show aurellia envy
    #             a "Salahhh, mikir yang bener.."
    #             jump choice
            
    #     label benarr:
    #         a "Yap, benar, karena titik pusatnya sudah (0,0) cukup masukkan aja nilai jari-jarinya"
    #         a "Gawat, sudah jam segini, ayo kita bergegas"




        
    #     hide aurellia base with dissolve
    #     "Setelah mengalami pagi yang memusingkan akhirnya kami pergi untuk menonton pertandingan basket bersama"
    #     "Aku tidak tahu pelajaran apalagi nanti yang akan dibahas dimasa mendatang, tapi yang jelas akhirnya aku bisa bersantai dengan leluasa.."


    # return