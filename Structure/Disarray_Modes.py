def Quit(current_mode): return 'Quit'
def Add_New(current_mode): return 'Add_New'
def Menu(current_mode): return 'Menu'

def pass_func(current_mode): return current_mode
def pass_func2(null = None): pass

def Quit_func(running):
    loc_running = running
    loc_running = 0
    return [loc_running]

def Add_New_func(Unsorted_Images, Current_Image, tkey, mouse):
    import pygame as pg
    from Structure.Disarray_Classes import Image
    loc_Unsorted_Images = Unsorted_Images; loc_Current_Image = Current_Image.img; loc_Current_Image_dest = Current_Image.folder
    if not loc_Current_Image in loc_Unsorted_Images:
        loc_Current_Image = loc_Unsorted_Images[0]
    x = loc_Unsorted_Images.index(loc_Current_Image)
    if tkey.a and x > 0:
        x -= 1
    if tkey.d and x < len(loc_Unsorted_Images) - 1:
        x += 1
    loc_Current_Image = Image(loc_Unsorted_Images[x], loc_Current_Image_dest, mouse.x, mouse.y)
    return [loc_Current_Image]
