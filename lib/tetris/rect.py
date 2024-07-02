def draw_rect(x,y,width,heigh,screen,color_id):
    for i in range(x,x+width):
        for j in range(y,y+heigh):
            screen[i,j] = color_id