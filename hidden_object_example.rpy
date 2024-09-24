# Define some point and click objects
# default classroom_apple = pnco(
#     "Apple",
#     "hidden object/classroom/apple.png",
#     (69, 727),
#     items = ["Apple"]
#     )
default classroom_book = pnco(
    "Book",
    "images/book.png",
    (799, 806),
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
# default classroom_lube = pnco(
#     "Lube",
#     "hidden object/classroom/lube.png",
#     (1182, 649),
#     items = ["Lube"]
#     )
default classroom_note = pnco(
    "Note",
    "images/note.png",
    (1022, 513),
    items = ["Note"]
    )
# default classroom_scissors = pnco(
#     "Scissors",
#     "hidden object/classroom/scissors.png",
#     (158, 961),
#     items = ["Scissors"]
#     )

# Define a point and click location
default hidden_object = pncs(
    "Classroom",
    [
        # classroom_apple,
        classroom_book,
        # classroom_knife,
        # classroom_kobe,
        # classroom_lube,
        classroom_note,
        # classroom_scissors,
    ],
    darkness = "darkness"
    
)


label hidden_object_example:
    show bg classroom
    call screen pnc(p = None, g=hidden_object)
    if _return:
        "Sepertinya udah semua, mari kita cepat-cepata keluar dari sini"
        jump library
    else:
        e"Sepertinya ada yang kurang"
        e"Kamu yakin udh ngecek semuanya?"
    jump hidden_object_example