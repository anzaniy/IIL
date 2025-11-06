#Diskusi 2/ Revina dan Erika, bisa ditambahin opsional disini
label chapter_3:
"Chapter 3"
"Sesaat setelah pertemuan singkat itu, kami bertiga pergi menuju taman didepan jurusan"

scene bg campus with dissolve

show revina happy with dissolve
r "Sebelumnya, Terima kasih ya udah nyempetin waktu buat diskusi disini"
r "ngomong-ngomong sebelum kita diskusi lebih lanjut, kenalin namaku Revina, panggil aja Revi, salam kenal ya"
show erika base
e "Ohiya, kenalin, aku Erika, bisa dipanggil Eri"
e "ngomong-ngomong untuk tadi pagi makasih ya, anu..."
menu:
    "Namaku Andika Adyatama, panggil aja Dika, salam kenal":
        jump chapter_3_1
    "Dika, panggil aja aku Dika, mahasiswa paling tampan di seluruh universitas ini, yahahaha":
        jump lebay

        label lebay:
            show revina base at right
            show erika base at left
            revieri "....."
            show revina envy at right
            show erika envy at left
            revieri "Hah..?"
            "Gawat seharusnya aku gak ngelakuin itu, makin ilfeel sepertinya mereka"
            d "Intinya salam kenal ya semua"
            jump chapter_3_1

label chapter_3_1:
    show revina happy at right
    show erika happy at left
    revieri "Salam kenal juga dika"
    hide revina
    hide erika 
    show erika base at right
    e "Mohon kerja samanya ya teman-teman"
    show revina base
    r "Mohon kerjasamanya juga, semoga kita bisa menemukan titik P kita ya"
    e "Lagi-lagi itu, aku masih kurang paham dibagian itu"
    show revina sad
    e "Rasanya kepalaku ingin meledak"
    show revina happy
    r "Masa begitu aja kurang tahu, sini aku jelaskan"
    show revina base at left
    r "Jadi dalam penjelasan koordinat polar oleh pak Adib"
    r "Dalam geometri garis lurus, koordinat polar itu memiliki hubungan dengan koordinat kartesius"
    show hubungan satu at truecenter
    r "Misalkan titik P ada di bidang datar."
    r "Titik itu bisa kita lihat sebagai (x, y) berdasarkan sumbu X'OX dan Y'OY..."
    r "Atau sebagai (r, θ) jika kita mengacu pada kutub O dan garis awal OX."

    r "Nah, dari definisi fungsi lingkaran, kita bisa mulai menyusun hubungan antara koordinat Kartesius dan polar."

    r "Pertama, kita tahu bahwa x dibagi r adalah cos θ."
    r "Maka, x = r cos θ."

    r "Begitu juga untuk y. Kita tahu y = r sin θ."

    r "Dan kalau kita bagi y dengan x, kita dapatkan tan θ = y/x."

    r "Sederhana, bukan? Tapi dari hubungan inilah, kita bisa menghubungkan dua cara pandang antara sumbu dan sudut, antara arah dan jarak."
    r "Aku sebagai kartesius akan menopang dirimu Erika untuk dapat menemukan titik P kita"
    hide hubungan satu
    menu:
        "Lalu aku bagaimana?":
            jump chapter_3_2

label chapter_3_2:
    show revina base at left
    r "Eh, kamu ya, hmm apa ya, kamu ini sebagai...."
    r "Ah aku tahu"
    show revina happy
    r "Tukang hitung, hahaha"
    d "Emang kamu sendiri gak bisa ngitung, sampe nyuruh diriku buat ngitung"
    r "Bisa dong, justru GAB ini paling mudah"
    show erika base
    e "Kalo gitu gimana kita tes langsung saja"
    e "Dika coba kasih pertanyaan"
    d "Loh kok tiba-tiba banget saya"
    e "Hehe"
    d "Hmm coba kupikirkan sebentar"
    e "Oh aku ada. Revina, dimana koordinat polar dari titik kartesius dari (-√3, 1)"
    show revina base
    r "Iya, itu gampang"
    r "Kita punya sebuah titik dengan koordinat Kartesius: (-√3, 1)."
    r "Tugas kita sekarang adalah mencari bentuk koordinat polarnya."

    r "Ingat, dalam sistem polar, kita pakai dua komponen: radius r dan sudut θ."

    r "Dari definisi koordinat polar, kita tahu:"
    r "r cos θ = -√3"
    r "r sin θ = 1"

    r "Kita ingin r bernilai positif, dan karena x-nya negatif serta y-nya positif..."
    r "Berarti titik ini berada di kuadran kedua."

    r "Sekarang kita hitung nilai tan θ:"
    r "tan θ = y / x = 1 / (-√3) = -1/√3"

    r "Tanpa ragu, kita tahu bahwa sudut θ dengan nilai tangen -1/√3 di kuadran kedua adalah:"
    r "θ = 5π/6"

    r "Sekarang cari r:"
    r "r² = (-√3)² + (1)² = 3 + 1 = 4"
    r "Jadi, r = √4 = 2"

    r "Kesimpulannya?"
    r "Koordinat polar dari titik (-√3, 1) adalah: (2, 5π/6)"
    r "Simple kan"
    r "Sekarang gantian, aku yang tanya"
    r "Coba cari koordinat polar dari (√3,√3)"
    menu:
        "(√6, π/4)":
            jump benar_3_1
        "(6, π/4)":
            jump salah_3_1
        "(√3, 5π/4)":
            jump salah_3_1
 
            label benar_3_1:
                show revina happy
                r "Yap benar, gampang kan berarti"
                jump chapter_3_3

            label salah_3_1:
                show revina envy
                r "Kamu nyimak gak sih penjelasan aku?"
                jump chapter_3_3

label chapter_3_3:
    show revina base
    r "Gak kerasa banget, sudah mau malem aja kita diskusi disini"
    show erika base
    e "*Melihat jam tangan"
    show erika sad
    e "Wah iya, gak kerasa banget"
    show revina base
    r "Kalau gitu kita sudahi dulu ya pertemuan ini"
    r "Inget nanti kita diskusi lagi"
    r "Pastiin proposal kalian sudah dibikin dengan mateng ya"
    show revina happy
    r "Kalau gitu sampai jumpa"
    hide erika 
    hide revina
    menu:
        "Sampai Jumpa":
            jump chapter_4




