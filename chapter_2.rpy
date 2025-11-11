#Ketemu pak adib, tapi cuman penjelasan simple, no opsional(?)
label chapter_2:
    scene bg lecturer room with dissolve
    "Setelah kegiatan perkuliahan, aku langsung berjalan menuju ruangan Pak Adib"
    #sfx ketuk pintu
    p "Silahkan masuk"
    show erika base at left
    show revina base at right
    "Didalam ruangan aku melihat 2 wanita yang berdiri didepan Pak Adib"
    "Sesaat setelah mereka melihatku kedua wanita itu langsung bergeser dan memberiku posisi diantara mereka berdua."
    hide erika with dissolve
    hide revina with dissolve
    show adib base with dissolve
    p "Baik terima kasih sudah hadir"
    p "Apa kalian tahu kenapa saya mengumpulkan kalian bertiga disini?"
    d "Apakah terkait pengajuan proposal skripsi, Pak?"
    p "Ya, Benar"
    show adib sus
    p "Terkait pengajuan judul yang kalian ajukan tempo hari yang lalu"
    p "Kebetulan judul kalian bertiga ini memiliki kemiripan, yaitu sama-sama membahas Geometri Analitik Bidang"
    p "Seperti yang kita tahu, dalam pengambilan GAB itu sendiri"
    p "Dalam pembahasan topik garis, terdapat koordinat kartesius dan polar"
    p "Dika, kamu tahu gak, koordinat polar itu apa?"
    menu:   
        "Koordinat polar itu sistem posisi titik yang ditentukan pakai jarak dari pusat (radius) dan sudut terhadap garis awal":
            jump benar_3
        "Koordinat polar itu sistem yang cuma pakai sumbu x dan y tanpa sudut":
            jump salah_3
        "Koordinat polar adalah metode untuk menghitung luas bangun datar pakai rumus keliling":
            jump salah_3

            label benar_3:
                show adib happy
                p "Ya, benar sekali"
                jump chapter_2_1
            
            label salah_3:
                show adib happy
                p "Belajar lagi ya, Dika"
                jump chapter_2_1

label chapter_2_1:
    image polar satu  = im.Scale("images/Materi/koor_polar.png", 1100, 500)
    show adib base at left
    show polar satu at truecenter
    p "Coba kalian bayangkan, ada sebuah garis dari titik O ke titik A. Itu garis awal."
    p "Lalu, titik P itu ya seperti kalian sekarang, masih belum jelas posisinya."
    p "Garis dari O ke P membentuk sudut θ, dan panjangnya kita sebut r."
    p "Kalau r dan θ-nya sudah jelas, barulah kita tahu di mana letak titik P itu."

    p "Nah, proposal kalian juga begitu."
    p "Kalau arah penelitiannya masih belum pasti, dan isinya masih belum kuat, ya titiknya nggak akan ketemu."
    p "Cari sudut yang pas, bangun radius yang jelas, baru nanti, posisinya bisa disebut lengkap dalam koordinat polar."
    p "Ingat, (r, θ) itu sederhana, tapi hanya kalau kalian tahu kalian sedang mengarah ke mana."

    show adib happy
    p "maka dari itu saya ingin kalian bertiga berdiskusi lagi dan tentukan topik skripsi kalian dengan lebih spesifik lagi, oke? saya tunggu minggu depan"
    show adib base
    p "Sampai sini apakah ada pertanyaan?"

    both_1 "Tidak pak"
    hide adib with dissolve
    hide polar satu with dissolve
    jump chapter_3
