def on_button_pressed_a():
    global posX, posY
    led.unplot(posX, posY)
    posX += -1
    if posX < 0:
        posX = 4
        posY += -1
        if posY < 0:
            posY = 4
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global posX, posY
    led.unplot(posX, posY)
    posX += 1
    if posX > 4:
        posX = 0
        posY += 1
        if posY > 4:
            posY = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

posY = 0
posX = 0
posX = 2
posY = 2

def on_forever():
    led.plot(posX, posY)
basic.forever(on_forever)
