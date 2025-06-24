
# #Animasi Terguncang
# transform shake(rate=0.090):
#     linear rate xoffset 2 yoffset -6
#     linear rate xoffset -2.8 yoffset -2
#     linear rate xoffset 2.8 yoffset -2
#     linear rate xoffset -2 yoffset -6
#     linear rate xoffset +0 yoffset +0
#     repeat

transform shake:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset 0