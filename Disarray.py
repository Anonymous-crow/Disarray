import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, json, random, pygame as pg
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

i0 = pg.K_0; i1 = pg.K_1; i2 = pg.K_2; i3 = pg.K_3; i4 = pg.K_4; i5 = pg.K_5; i6 = pg.K_6; i7 = pg.K_7; i8 = pg.K_8; i9 = pg.K_9; a = pg.K_a; b = pg.K_b; c = pg.K_c; d = pg.K_d; e = pg.K_e; f = pg.K_f; g = pg.K_g; h = pg.K_h; i = pg.K_i; j = pg.K_j; k = pg.K_k; l = pg.K_l; m = pg.K_m; n = pg.K_n; o = pg.K_o; p = pg.K_p; q = pg.K_q; r = pg.K_r; s = pg.K_s; t = pg.K_t; u = pg.K_u; v = pg.K_v; w = pg.K_w; x = pg.K_x; y = pg.K_y; z = pg.K_z; bk = pg.K_BACKSPACE; sp = pg.K_SPACE; tb = pg.K_TAB; esc = pg.K_ESCAPE; sh = pg.K_LSHIFT; enter = pg.K_RETURN; bq = pg.K_BACKQUOTE; min = pg.K_MINUS; plus = pg.K_EQUALS; lbra = pg.K_LEFTBRACKET; rbra = pg.K_RIGHTBRACKET; bckslsh = pg.K_BACKSLASH; semi = pg.K_SEMICOLON; quote = pg.K_QUOTE; comma = pg.K_COMMA; period = pg.K_PERIOD; slash = pg.K_SLASH
key = {i0:0, i1:0, i2:0, i3:0, i4:0, i5:0, i6:0, i7:0, i8:0, i9:0, a:0, b:0, c:0, d:0, e:0, f:0, g:0, h:0, i:0, j:0, k:0, l:0, m:0, n:0, o:0, p:0, q:0, r:0, s:0, t:0, u:0, v:0, w:0, x:0, y:0, z:0, bk:0, sp:0, tb:0, esc:0, sh:0, enter:0, bq:0, min:0, plus:0, lbra:0, rbra:0, bckslsh:0, semi:0, quote:0, comma:0, period:0, slash:0}
tkey = {i0:0, i1:0, i2:0, i3:0, i4:0, i5:0, i6:0, i7:0, i8:0, i9:0, a:0, b:0, c:0, d:0, e:0, f:0, g:0, h:0, i:0, j:0, k:0, l:0, m:0, n:0, o:0, p:0, q:0, r:0, s:0, t:0, u:0, v:0, w:0, x:0, y:0, z:0, bk:0, sp:0, tb:0, esc:0, sh:0, enter:0, bq:0, min:0, plus:0, lbra:0, rbra:0, bckslsh:0, semi:0, quote:0, comma:0, period:0, slash:0}
tkey_v = {i0:0, i1:0, i2:0, i3:0, i4:0, i5:0, i6:0, i7:0, i8:0, i9:0, a:0, b:0, c:0, d:0, e:0, f:0, g:0, h:0, i:0, j:0, k:0, l:0, m:0, n:0, o:0, p:0, q:0, r:0, s:0, t:0, u:0, v:0, w:0, x:0, y:0, z:0, bk:0, sp:0, tb:0, esc:0, sh:0, enter:0, bq:0, min:0, plus:0, lbra:0, rbra:0, bckslsh:0, semi:0, quote:0, comma:0, period:0, slash:0}
nkey = {i0:0, i1:0, i2:0, i3:0, i4:0, i5:0, i6:0, i7:0, i8:0, i9:0, a:0, b:0, c:0, d:0, e:0, f:0, g:0, h:0, i:0, j:0, k:0, l:0, m:0, n:0, o:0, p:0, q:0, r:0, s:0, t:0, u:0, v:0, w:0, x:0, y:0, z:0, bk:0, sp:0, tb:0, esc:0, sh:0, enter:0, bq:0, min:0, plus:0, lbra:0, rbra:0, bckslsh:0, semi:0, quote:0, comma:0, period:0, slash:0}

from Structure.Disarray_Classes import *
from Structure.Disarray_Modes import *

Unsorted_Images = []
for this in os.listdir():
    if this[-4:] == ".jpg" or this[-4:] == ".png":
        Unsorted_Images.append(this)

importables = {}
for this in importables:
    with open('Data/' + this + '.json', 'r') as file:
        importables[this].update(json.load(file))

mode_func_dict = {'Quit': Quit_func, 'Add_New': Add_New_func, 'Help': Help_func, 'Menu': pass_func2}

class keyset:
    def __init__(id,i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, bk, sp, tb, esc, sh, enter):
        id.i0 = i0; id.i1 = i1; id.i2 = i2; id.i3 = i3; id.i4 = i4; id.i5 = i5; id.i6 = i6; id.i7 = i7; id.i8 = i8; id.i9 = i9; id.a = a; id.b = b; id.c = c; id.d = d; id.e = e; id.f = f; id.g = g; id.h = h; id.i = i; id.j = j; id.k = k; id.l = l; id.m = m; id.n = n; id.o = o; id.p = p; id.q = q; id.r = r; id.s = s; id.t = t; id.u = u; id.v = v; id.w = w; id.x = x; id.y = y; id.z = z; id.bk = bk; id.sp = sp; id.tb = tb; id.esc = esc; id.sh = sh; id.enter = enter
class mouseclass:
    def __init__(i,mouse1, mouse3, mouse2, mouse1t, mouse3t, mouse2t, mouse_x, mouse_y):
        i.o = mouse1; i.t = mouse3; i.w = mouse2; i.ot = mouse1t; i.tt = mouse3t; i.wt = mouse2t; i.x = mouse_x; i.y = mouse_y

Toolbar_Assets_dict = {'Toolbar.png':[0, 0, 10], 'Question_Block.png':[15, 0, 10.1]}
Toolbar_Assets = []
for this in os.listdir('Toolbar/Toolbar_Assets/'):
    Toolbar_Asset = Image(this, 'Toolbar/Toolbar_Assets/', Toolbar_Assets_dict[this][0], Toolbar_Assets_dict[this][1]); Toolbar_Asset.Layer = Toolbar_Assets_dict[this][2]
    Toolbar_Assets.append(Toolbar_Asset)

Bgr = 0; Bgg = 0; Bgb = 0; mouse_visible = 1; mode = "Menu"; toolbar_show = 1; New_Image = Image(None, '', 0, 0); Images = []
running = 1
while running:
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse1, mouse3, mouse2 = pg.mouse.get_pressed()
    mouse1t = 0; mouse3t = 0; mouse2t = 0
    if mouse1 and not mouse1_v: mouse1t = 1; mouse1_v = 1
    if not mouse1: mouse1_v = 0
    if mouse3 and not mouse3_v: mouse3t = 1; mouse3_v = 1
    if not mouse3: mouse3_v = 0
    if mouse2 and not mouse2_v: mouse2t = 1; mouse2_v = 1
    if not mouse2: mouse2_v = 0
    mouse = mouseclass(mouse1, mouse3, mouse2, mouse1t, mouse3t, mouse2t, mouse_x, mouse_y)
    pg.mouse.set_visible(mouse_visible)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = 0
        if event.type == pg.KEYDOWN:
            for this in key:
                if this == event.key:
                    key[this] = 1
        if event.type == pg.KEYUP:
            for this in key:
                if this == event.key:
                    key[this] = 0
    keys = keyset(key[i0], key[i1], key[i2], key[i3], key[i4], key[i5], key[i6], key[i7], key[i8], key[i9], key[a], key[b], key[c], key[d], key[e], key[f], key[g], key[h], key[i], key[j], key[k], key[l], key[m], key[n], key[o], key[p], key[q], key[r], key[s], key[t], key[u], key[v], key[w], key[x], key[y], key[z], key[bk], key[sp], key[tb], key[esc], key[sh], key[enter])
    for this in tkey:
        tkey[this] = 0
        if key[this] and not tkey_v[this]:
            tkey[this] = 1
            tkey_v[this] = 1
        elif not key[this]:
            tkey_v[this] = 0
    tkeys = keyset(tkey[i0], tkey[i1], tkey[i2], tkey[i3], tkey[i4], tkey[i5], tkey[i6], tkey[i7], tkey[i8], tkey[i9], tkey[a], tkey[b], tkey[c], tkey[d], tkey[e], tkey[f], tkey[g], tkey[h], tkey[i], tkey[j], tkey[k], tkey[l], tkey[m], tkey[n], tkey[o], tkey[p], tkey[q], tkey[r], tkey[s], tkey[t], tkey[u], tkey[v], tkey[w], tkey[x], tkey[y], tkey[z], tkey[bk], tkey[sp], tkey[tb], tkey[esc], tkey[sh], tkey[enter])
    for this in nkey:
        nkey[this] = 1 - key[this]
    nkeys = keyset(nkey[i0], nkey[i1], nkey[i2], nkey[i3], nkey[i4], nkey[i5], nkey[i6], nkey[i7], nkey[i8], nkey[i9], nkey[a], nkey[b], nkey[c], nkey[d], nkey[e], nkey[f], nkey[g], nkey[h], nkey[i], nkey[j], nkey[k], nkey[l], nkey[m], nkey[n], nkey[o], nkey[p], nkey[q], nkey[r], nkey[s], nkey[t], nkey[u], nkey[v], nkey[w], nkey[x], nkey[y], nkey[z], nkey[bk], nkey[sp], nkey[tb], nkey[esc], nkey[sh], nkey[enter])

    if toolbar_show:
        for this in Toolbar_Assets:
            Images.append(this)
    Image_None_List = []
    Images_Sort = []
    for this in Images:
        Image_None_List.append(None)
        if not hasattr(this, 'Layer'):
            this.Layer = 0
        Images_Sort.append(this.Layer)
    Images_Sort = sorted(Images_Sort, key = float)
    for this in Images:
        Image_None_List[Images_Sort.index(this.Layer)] = this
    Images = Image_None_List
    for this in Images:
        if not hasattr(this, 'Surf'):
            this.Surf = pg.image.load(this.folder + this.img).convert_alpha()
            this.dimensions = str(this.Surf)[9:-8]
            for that in this.dimensions:
                if that == 'x': this.X_marks_the_spot = this.dimensions.index(that)
            this.x_len = this.dimensions[:this.X_marks_the_spot]; this.y_len = this.dimensions[this.X_marks_the_spot + 1:]; this.rect = this.Surf.get_rect()
        screen.blit(this.Surf, (this.x_pos, this.y_pos))
        if this.rect.collidepoint(mouse_x, mouse_y): this.mouse_over = 1
        elif not this.rect.collidepoint(mouse_x, mouse_y): this.mouse_over = 0
    for this in Toolbar_Assets:
        if this in Images:
            Images.remove(this)

    mode_dict = {key[sh]*key[esc]: Quit, nkey[sh]*key[q]: Add_New, nkey[sh]*key[h]: Help, nkey[sh]*key[esc]: Menu}
    mode_func_arg_dict = {'Quit': [None], 'Add_New': [Unsorted_Images, New_Image, tkeys, mouse], 'Help': [], 'Menu': [None]}
    mode_func_retn_dict = {'Quit': [running], 'Add_New': [New_Image], 'Help': []}
    for this in mode_dict:
        mode = {1: mode_dict[this], 0: pass_func}[this](mode)
    mode_func_retn_dict[mode] = mode_func_dict[mode](*mode_func_arg_dict[mode])

    if mode == 'Quit':
        if not mode_func_retn_dict['Quit'][0] == running:
            running = mode_func_retn_dict['Quit'][0]

    if mode == 'Add_New':
        if not mode_func_retn_dict['Add_New'][0] == New_Image:
            if New_Image in Images:
                Images.remove(New_Image)
            New_Image = mode_func_retn_dict['Add_New'][0]
            Images.append(New_Image)
    elif mode != 'Add_New':
        if New_Image in Images:
            Images.remove(New_Image)

    if mode == 'Menu':
        pass

    pg.time.wait(2)
    pg.display.flip()
    screen.fill((Bgr, Bgg, Bgb))
