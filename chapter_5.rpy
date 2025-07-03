#Bisa dibikin cabang Revina, atau ditambah cabang Erika satu lagi juga bisa
#Chapter 4.1 dan 4.2 dan 5.1 dan 5.2
label chapter_5:
    "Chapter 5"
    scene lounge with dissolve
    "Esok hari setelah mengalami hari yang cukup melelahkan"
    "Sudah satu jam semenjak aku bangun, aku hanya berbaring di kasur"
    "memanfaatkan jam kosong sekaligus nyamannya beristirahat berbaring disini"
    "Niatnya sih mau rebahan aja sampai siang" 
    "namun terdengar nada dering panggilan yang mengganggu"
    play music "iphone.mp3" fadeout 2.0 fadein 2.0
    "Aku melihat ke layar ponselku, melihat ternyata Revina yang berusaha memanggilku"
    menu:
        "Angkat Telefon":
            jump chapter_5_1

label chapter_5_1:
    stop music
    r "Halo Dika, ini aku, Revina, harusnya kamu sudah save contact aku sih kemarin, tapi gak papa lah"
    d "Iya, aku save, ada apa kak?"
    r "Bisa tolong temenin aku gak ke perpusnas?"
    d "Bisa sampai jam 1 aku mungkin ada kelas"
    r "Okeh, kalau gitu aku tunggu ya sekarang"
    d "Hah"
    d "Tunggu, kak, seriusan lagi seka-"
    "Revina langsung menutup panggilan sebelum aku selesain kata-kata ku"
    "Gak ada pilihan lain juga..."

    scene bg library with dissolve
    "30 Menit kemudian"
    show revina envy
    r "Lama banget!"
    d "Ini aja udah paling cepet ya aku berangkat"
    d "Jadi, ada alasan apa kak kita kesini"
    show revina happy
    r "Temenin aku lah, kan kita satu topik, Erika lagi ada kelas, jadi aku ajak kamu dulu"
    "Dari sifatnya kemarin, walaupun kami baru bertemu sekali, aku bisa nebak kalau dia ini orang yang suka banyak omong"
    "Tentu saja orang yang banyak omong begini butuh seseorang buat denger omongannya"
    "Tapi aku mungkin pastiin dulu maksud dia itu bagaimana"
    d "Jadi, tujuan utamanya apa?"
    show revina base
    r "Owh, pinter juga kamu"
    r "Jelaslah buat denger pembahasanku"
    "Sudah kuduga"
    d "Jadi apa topik kita pagi ini?"
    r "Tentu saja"
    show revina happy
    r "Gradien"
    show revina base
    r "Kamu pernah jalan di tanjakan atau turunan waktu naik sepeda?"
    r "Semakin miring jalannya, semakin kerasa berat atau cepatnya, kan?"

    r "Nah, itu mirip dengan apa yang kita sebut gradien dalam matematika."
    r "Gradien adalah ukuran seberapa miring sebuah garis terhadap sumbu-x."

    r "Secara sederhana, kalau kita punya dua titik, misalnya A di (x₁, y₁) dan B di (x₂, y₂)..."
    image gradien satu  = im.Scale("images/Materi/gradien_1.png", 1100, 500)
    r "Gradien garis yang menghubungkan keduanya dihitung dengan rumus:"
    show revina base at left
    show gradien satu at truecenter
    r "m = (y₂ - y₁) / (x₂ - x₁)"

    r "Artinya, kita lihat seberapa besar perubahan naik atau turunnya, dibandingkan dengan seberapa jauh ke kanan atau kirinya."

    r "Sekarang bayangin ada tiga titik: A, B, dan C, berdiri di lapangan."
    r "Kalau mereka berada di satu garis lurus, berarti arah dari A ke B sama dengan arah dari B ke C."

    r "Dengan kata lain, gradien AB harus sama dengan gradien BC."

    r "Jadi, kamu bisa cek kesegarisannya dengan rumus sederhana:"
    r "Apakah (y₂ - y₁)/(x₂ - x₁) = (y₃ - y₂)/(x₃ - x₂)?"

    r "Kalau sama, ya mereka segaris."
    r "Sama seperti hidup, kalau arahnya sama, kemungkinan besar tujuannya juga satu jalur."

    hide gradien
    show revina base
    image rumus dua  = im.Scale("images/Materi/rumus_2.png", 1100, 500)

    r "Oke cukup, kita langsung ke soal aja"
    r "Jadi ceritanya, hari ini aku lagi bantu temanku, Raka, yang sedang merancang bentuk jalan setapak di taman kota."
    r "Dia pengen desainnya simetris dan menarik, jadi dia pakai bidang koordinat buat nentuin titik-titiknya."

    r "Dia menandai empat titik penting:"
    r "Titik A di (-1, 3)"
    r "Titik B di (1, 0)"
    r "Titik C di (4, 2)"
    r "Dan titik D di (0, 8)"

    r "Raka minta bantuanku buat memastikan dua hal..."
    r "Pertama, apakah jalur dari A ke B tegak lurus dengan jalur dari B ke C?"
    r "Dan kedua, apakah jalur dari A ke B sejajar dengan jalur dari D ke C?"

    r "Oke, kita mulai dari yang pertama."

    r "Gradien AB = (0 - 3)/(1 - (-1)) = -3/2"
    r "Gradien BC = (2 - 0)/(4 - 1) = 2/3"

    r "Kalau dua garis saling tegak lurus, hasil kali gradiennya harus -1."
    r "Dan memang, (-3/2) x (2/3) = -1"

    r "Berarti... garis AB tegak lurus dengan garis BC!"

    r "Sekarang kita cek yang kedua."

    r "Gradien AB tadi udah kita hitung, yaitu -3/2"
    r "Sekarang kita hitung gradien DC:"
    r "Gradien DC = (2 - 8)/(4  0) =-6/4 = -3/2"

    r "Karena gradiennya sama, berarti garis AB sejajar dengan garis DC."
    show revina happy
    r "Gradien mudah kan, cukup paham saja satu rumus itu"
    show revina base
    r "Hei Dika, kenapa kamu memilih topik ini"
    d "Topik GAB ?"
    r "Lebih spesifik lagi"
    d "Garis lurus?"
    r "Ya, benar, kepikiran gak sih, kena sebuah garis kita repot-repot buat menghitung"
    d "Karena memang semua aspek dibuat dengan penuh perhitungan bukan?"
    r "Mungkin, aku sendiri kurang tahu"
    r "Kamu sendiri tahu gak garis lurus itu apa?"
    menu:
        "Garis lurus dalam geometri analitik adalah himpunan titik-titik yang memenuhi persamaan linear":
            jump benar_5_1
        "Garis lurus adalah kurva yang membentuk lingkaran sempurna di bidang koordinat":
            jump salah_5_1
        "Garis lurus adalah garis yang selalu membentuk sudut 90° dengan sumbu-x di semua titiknya":
            jump salah_5_1

            label benar_5_1:
                show revina happy
                r "Tepat sekali"
                jump chapter_5_2

            label salah_5_1:
                show revina envy
                r "Hah? Kamu sudah cuci muka kan?"
                r "Cuci muka lagi aja sana"
                jump chapter_5_2

label chapter_5_2:
    show revina base
    r "Pernah lihat jalan lurus yang membelah persawahan atau jalur rel kereta api?"
    r "Jalur seperti itu bisa digambarkan dengan sebuah persamaan garis dalam geometri analitik."

    r "Bentuk umum dari garis itu adalah: Ax + By + C = 0"
    r "Di mana A, B, dan C adalah bilangan konstan."

    r "Kalau B tidak sama dengan nol, persamaan ini bisa diubah jadi:"
    hide revina 
    show revina base at left
    show rumus dua at truecenter
    r "y = -A/B * x - C/B"
    r "Artinya, gradien garis itu adalah -A/B, dan memotong sumbu-y di titik (0, -C/B)."

    r "Tapi kalau B-nya nol, maka persamaannya jadi x = -C/A"
    r "Itu menunjukkan garis yang tegak lurus — sejajar dengan sumbu-y."

    r "Lalu bagaimana kalau A-nya yang nol?"
    r "Persamaan tinggal jadi y = -C/B, garis datar yang sejajar sumbu-x."

    r "Sekarang, kalau C-nya nol, persamaan menjadi y = -A/B * x"
    r "Garis seperti ini selalu melalui titik asal atau pusat koordinat (0,0)."

    r "Ada juga kasus khusus..."
    r "Kalau A dan C sama-sama nol, persamaannya jadi y = 0 — artinya garis itu tepat berada di sumbu-x."

    r "Dan jika B dan C sama-sama nol, maka persamaan jadi x = 0, yaitu sumbu-y itu sendiri."

    r "Siapa sangka ya, dari sebuah rumus sederhana, bisa lahir begitu banyak jenis garis lurus dalam bidang datar."
    hide rumus dua
    hide revina
    show revina base at left
    r "Oke kita lanj-"
    "*Suara pintu terbuka"
    show erika sad at right
    e "Kak Revi, Dika, tolongin"
    menu:
        "Ada apa Erika?":
            jump chapter_5_3

label chapter_5_3:
    e "barang-barangku ketinggalan di ruang kelas"
    r "Tinggal ambil lah, kenapa repot-repot kesini"
    e "Masalahnya itu kelasnya lagi dipake acara sampai sore"
    e "Gimana dong"
    e "Didalamnya ada buku catatan aku soal topik yang mau kita bahas hari ini"
    d "Yaudah kita ambil saat sore nanti saja gimana"
    e "Tapi, satpamnya galak, tau sendiri kan gimana"
    d "Yang penting jangan ketahuan saja"
    d "Kalau gitu siap-siap ya nanti sore kita ambil"
    hide erika
    hide revina

    scene bg hall_1
    show revina envy at left
    r "Jaadi, kenapa aku juga ikut"
    show erika base at right
    e "Temenin juga lah kan kita satu tim"
    r "Satu tim dari hongkong"
    r "Gamau tahu kalo ketahuan salah Dika"
    d "Yaudah ayok buruan masuk"
    hide erika
    hide revina 
    e "Terakhir kuingat, aku meninggalkan bukuku di  meja, dan catatan kertas di papan ruang kelas"
    "Sesi Minigames"
    "Cukup klik barang Erika yang ketinggalan ketika objek ditemukan"
    "Jika sudah tekan tombol done di pojok kanan atas"
    jump hidden_object_example

label chapter_5_4:
    show erika base
    e "Akhirnya keluar juga"
    d "Jangan santai dulu, masih ada satpam disini"
    hide erika
    show revina envy
    r "Iyaa bener itu, keluar dulu baru lega"
    "Hey kamu disana!"
    show revina base
    r "Gawat kita dikejer"
    r "Buruan lari cepetan"
    jump chapter_6




