class Image:
    def __init__(i,img, folder, x_pos, y_pos):
        i.img = img
        i.folder = folder
        i.x_pos = x_pos
        i.y_pos = y_pos
class keyset:
    def __init__(id,i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, bk, sp, tb, esc, sh, enter):
        id.i0 = i0; id.i1 = i1; id.i2 = i2; id.i3 = i3; id.i4 = i4; id.i5 = i5; id.i6 = i6; id.i7 = i7; id.i8 = i8; id.i9 = i9; id.a = a; id.b = b; id.c = c; id.d = d; id.e = e; id.f = f; id.g = g; id.h = h; id.i = i; id.j = j; id.k = k; id.l = l; id.m = m; id.n = n; id.o = o; id.p = p; id.q = q; id.r = r; id.s = s; id.t = t; id.u = u; id.v = v; id.w = w; id.x = x; id.y = y; id.z = z; id.bk = bk; id.sp = sp; id.tb = tb; id.esc = esc; id.sh = sh; id.enter = enter
class mouseclass:
    def __init__(i,mouse1, mouse3, mouse2, mouse1t, mouse3t, mouse2t, mouse_x, mouse_y):
        i.o = mouse1; i.t = mouse3; i.w = mouse2; i.ot = mouse1t; i.tt = mouse3t; i.wt = mouse2t; i.x = mouse_x; i.y = mouse_y

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def message_display(screen, text, x, y, size, color):
    import pygame as pg
    largeText = pg.font.Font('Structure/helvetica.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.topleft = (x, y)
    screen.blit(TextSurf, TextRect)
    dimension = largeText.render(text, True, color).get_rect()
    return [x, y, dimension[2], dimension[3]]
def wrtmsg(text, x, y, size = 20, color = (255, 255, 255)):
    import pygame as pg
    localmsg_v = msg_v
    localmsg_v += 5
    message.update({localmsg_v: text})
    message.update({localmsg_v + 1: x})
    message.update({localmsg_v + 2: y})
    message.update({localmsg_v + 3: size})
    message.update({localmsg_v + 4: color})
    return localmsg_v
