# Define some point and click objects
default lounge_apple = pnco(
    "Apple",
    "images/apple.png",
    (69, 727),
    items = ["Apple"]
    )
default lounge_book = pnco(
    "Book",
    "images/book.png",
    (120, 200),
    items = ["Book"]
    )
# default classroom_knife = pnco(
#     "Knife",
#     "hidden object/classroom/knife.png",
#     (1788, 1003),
#     items = ["Knife"]
#     )
# default classroom_kobe = pnco(
#     "Kobe",
#     "hidden object/classroom/kobe.png",
#     (1317, 972),
#     items = ["Kobe"]
#     )
default lounge_lube = pnco(
    "Lube",
    "images/lube.png",
    (1182, 649),
    items = ["Lube"]
    )
default lounge_note = pnco(
    "Note",
    "images/note.png",
    (1022, 513),
    items = ["Note"]
    )
default lounge_scissors = pnco(
    "Scissors",
    "images/scissors.png",
    (1200, 961),
    items = ["Scissors"]
    )

# Define a point and click location
default bersih_bersih = pncs(
    "Lounge",
    [
        lounge_apple,
        lounge_book,
        # classroom_knife,
        # classroom_kobe,
        lounge_lube,
        lounge_note,
        lounge_scissors,
    ],
    darkness = "darkness"
    
)


label bersih_bersih:
    show bg lounge
    call screen pnc(p = None, g=bersih_bersih)
    if _return:
        "Sepertinya udah semua, mari kita cepat-cepat keluar dari sini"
        jump mtk
    else:
        e"Sepertinya ada yang kurang"
        e"Kamu yakin udh ngecek semuanya?"
    jump bersih_bersih