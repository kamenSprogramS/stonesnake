from tkinter import *
import time
import random



game_width=500
game_height=500
snake_item=20
snake_color1="black"
snake_color2="orange"
virtual_game_x=game_width//snake_item
virtual_game_y=game_height//snake_item
snake_x=virtual_game_x//2
snake_y=virtual_game_y//2
snake_x_nav=0
snake_y_nav=0
snake_list=[]
snake_size=3



tk=Tk()
tk.title("stoneSnake")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=game_width,height=game_height,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

presents_color1="blue"
presents_color2="yellow"
presents_list=[]
presents_size=13
for i in range(presents_size):
    x=random.randrange(virtual_game_x)
    y=random.randrange(virtual_game_y)
    id1=canvas.create_oval(x*snake_item,y*snake_item,x*snake_item+snake_item,y*snake_item+snake_item,fill=presents_color2)
    id2=canvas.create_oval(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=presents_color2)
    
    presents_list.append([x,y,id1,id2])


def snake_paint_item(canvas,x,y):
    global snake_list
    id1=canvas.create_rectangle(x*snake_item,y*snake_item,x*snake_item+snake_item,y*snake_item+snake_item,fill=snake_color2)
    id2=canvas.create_rectangle(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=snake_color2)
    snake_list.append([x,y,id1,id2])
snake_paint_item(canvas,snake_x,snake_y)

def check_can_we_delete_snake_item():
    if len(snake_list)>=snake_size:
        temp_item=snake_list.pop(0)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])

def check_if_we_found_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0]==snake_x and presents_list[i][1]==snake_y:
            snake_size+=1
            canvas.delete(presents_list[i][2])
            canvas.delete(presents_list[i][3])

def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav
    if event.keysym=="Up":
        snake_x_nav=0
        snake_y_nav=-1
        check_can_we_delete_snake_item()
    elif event.keysym=="Down":
        snake_x_nav=0
        snake_y_nav=1
        check_can_we_delete_snake_item()
    elif event.keysym=="Left":
        snake_x_nav=-1
        snake_y_nav=0
        check_can_we_delete_snake_item()
    elif event.keysym=="Right":
        snake_x_nav=1
        snake_y_nav=0
        check_can_we_delete_snake_item()
    snake_x=snake_x+snake_x_nav
    snake_y=snake_y+snake_y_nav
    snake_paint_item(canvas,snake_x,snake_y)
    check_if_we_found_present()


canvas.bind_all("<KeyPress-Left>",snake_move)
canvas.bind_all("<KeyPress-Right>",snake_move)
canvas.bind_all("<KeyPress-Up>",snake_move)
canvas.bind_all("<KeyPress-Down>",snake_move)

def game_over():
    exit(1)

def check_if_borders():
    if snake_x > virtual_game_x or snake_x<0 or snake_y > virtual_game_y or snake_y<0:
        game_over()

def check_we_task_self(f_x,f_y):
    if not(snake_x_nav==0 and snake_y_nav==0):
        for i in range(len(snake_list)):
            if snake_list[i][0]==f_x and snake_list[i][1]==f_y:
                game_over()

while 1:
    check_can_we_delete_snake_item()
    check_if_we_found_present()
    check_if_borders()
    check_we_task_self(snake_x+snake_x_nav,snake_y+snake_y_nav)
    snake_x=snake_x+snake_x_nav
    snake_y=snake_y+snake_y_nav
    snake_paint_item(canvas,snake_x,snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.2)