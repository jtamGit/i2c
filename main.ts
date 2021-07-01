let sensor = 0
pins.i2cWriteNumber(
32,
255,
NumberFormat.UInt8BE,
false
)
serial.redirectToUSB()
serial.setBaudRate(BaudRate.BaudRate115200)
let enter = 10
basic.forever(function () {
    sensor = pins.i2cReadNumber(32, NumberFormat.UInt8BE, false)
    serial.writeNumber(sensor)
    serial.writeLine("")
    basic.pause(200)
})
