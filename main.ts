input.onButtonPressed(Button.A, function () {
    led.unplot(posX, posY)
    posX += -1
    if (posX < 0) {
        posX = 4
        if (posY < 0) {
            posY = 4
        }
    }
})
input.onButtonPressed(Button.B, function () {
    led.unplot(posX, posY)
    posX += 1
    if (posX > 4) {
        posX = 0
        if (posY > 4) {
            posY = 0
        }
    }
})
let posY = 0
let posX = 0
posX = 2
posY = 4
basic.forever(function () {
    led.plot(posX, posY)
})
