#spesial chapter with erika, bisa ditambahin cutscene bonus 1 or 2 di akhir
#bikin cabang dengan waktu yang sama dengan Revina
label chapter_4:
    "Chapter 4"
    scene bg night city
    show erika base
    e "Dika, kamu pulang kearah mana?"
    d "Kosanku ada di jalan Aiko, depan sana"
    d "Emangnya kenapa ?"
    e "Kebetulan aku juga lewat sana"
    e "Untung saja kamu searah denganku"
    d "Emang kamu gabisa pulang malem-malem kah"
    e "Bisa sih, tapi pulang sendiri itu yang bikin susah, kamu kan tahu juga aku perempuan"
    e "Jujur, aku suka banget geometri"
    e "Bahkan semua hal itu kalo dikaitin sama matematika itu menurutku asik banget"
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
    show erika base at left
    image jarak satu  = im.Scale("images/Materi/jarak_1.png", 1100, 500)
    show jarak satu at truecenter
    e "Bayangkan A dan B itu dua orang, mungkin kamu dan temanmu."
    e "Kalian berdiri di tempat yang berbeda di peta kota, dengan koordinat masing-masing: A di (x₁, y₁), dan B di (x₂, y₂)."

    e "Sekarang kamu ingin tahu, seberapa jauh sih jarakmu dari dia?"
    e "Itu kita sebut r yang merupakan jarak langsung dari titik A ke B."

    e "Tapi bukan cuma soal jarak."
    e "Bayangkan kamu berjalan dari A ke B, dan kamu lihat arah langkahmu membentuk sudut θ terhadap arah timur."
    e "Sudut ini kita sebut sudut inklinasi — arah perjalananmu."

    e "Kalau kamu pecah perjalananmu jadi arah kanan-kiri dan atas-bawah..."
    e "Bagian ke kanan adalah r cos θ, yang sama dengan x₂ - x₁."
    e "Dan bagian ke atas adalah r sin θ, yaitu y₂ - y₁."

    e "Nah, kayak kamu naik tangga — kamu tahu tinggi dan panjang langkahmu, tapi ingin tahu berapa panjang miringnya."
    e "Maka kamu pakai rumus Pythagoras."

    e "r² = (x₂ - x₁)² + (y₂ - y₁)²"

    e "Dan karena cos² θ + sin² θ = 1, hasil akhirnya tetap r²."

    e "Jadi, untuk tahu jarakmu ke seseorang... kamu cukup tahu posisi kalian berdua."

    e "Hidup juga gitu, kan?"
    e "Kadang kita gak tahu seberapa jauh kita dari tujuan, tapi kalau kita tahu posisi kita sekarang dan tahu arah, kita bisa hitung sendiri jaraknya."

    show erika happy at left
    e "Dan itulah gunanya koordinat."
    e "Jadi kalau misalnya ditanya carilah jarak antara titik (-2,1) dan (4,9)"
    e "Gampang kan tinggal dimasukin aja jadi =√36+64"
    e "Dapetlah 10"
    hide jarak satu
    hide erika
    show erika sad
    e "Aduh, maaf ya aku kebanyakan ngoceh dijalan"
    e "Pasti gedek juga dengerin aku ngomongin garis setelah kita pusing dengerin materi garis yang lain"
    show erika base
    e "Ah, kosan aku belok sini"
    show erika happy
    e "makasih ya udh nemenin. sampai jumpa besok, Dika"
    menu:
        "Sampai jumpa Erika":
            jump chapter_5