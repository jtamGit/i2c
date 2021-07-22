def on_data_received():
    basic.show_string(serial.read_until(serial.delimiters(Delimiters.NEW_LINE)))
serial.on_data_received(serial.delimiters(Delimiters.COMMA), on_data_received)

def on_button_pressed_a():
    global sensor
    serial.write_line(convert_to_text(input.temperature()))
    sensor = input.temperature()
input.on_button_pressed(Button.A, on_button_pressed_a)

sensor = 0
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
serial.redirect_to_usb()

def on_forever():
    pins.i2c_write_number(46, 107, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 111, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 110, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 110, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 110, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 105, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 116, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 105, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 119, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 97, NumberFormat.UINT8_BE, False)
    pins.i2c_write_number(46, 13, NumberFormat.UINT8_BE, False)
    basic.pause(1000)
    serial.write_string("a")
basic.forever(on_forever)
