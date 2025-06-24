
default classroom_book = pnco(
    "Book",
    "images/book.png",
    (799, 806),
    items = ["Book"]
    )

default classroom_note = pnco(
    "Note",
    "images/note.png",
    (1022, 513),
    items = ["Note"]
    )

# Define a point and click location
default hidden_object = pncs(
    "Classroom",
    [   
        classroom_book,    
        classroom_note,
    ],
    darkness = "darkness"
    
)


label hidden_object_example:
    show bg classroom
    call screen pnc(p = None, g=hidden_object)
    if _return:
        "Sepertinya udah semua, mari kita cepat-cepat keluar dari sini"
        jump chapter_5_4
    else:
        e"Sepertinya ada yang kurang"
        e"Kamu yakin udh ngecek semuanya?"
    jump hidden_object_example