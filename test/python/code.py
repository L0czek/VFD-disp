from machine import *
import time
adc_f = ADC(2)
adc_hv = ADC(3)

disable_f = Pin(6, Pin.OUT, value=1)
disable_hv = Pin(9, Pin.OUT, value=1)
mosfet = Pin(8, Pin.OUT, value = 0)

spi = SPI(
    1,
    baudrate=100_000,
    polarity=0,
    phase=0,
    sck=Pin(19),
    mosi=Pin(18),
)

# also known as "strobe"
latch = Pin(21, Pin.OUT, value=0)
blanking = Pin(20, Pin.OUT, value=0)

def write_shift_register(value):
    if len(value) != 5:
        print("gowno dales")
    spi.write(bytes(value))
    latch.on()
    time.sleep_ms(1)
    latch.off()
    print("Wrote", value)

write_shift_register([0xAA]*5)

def print_voltages():
    print("HV: ", adc_hv.read_uv()*101.0/1000000)
    print("F: ", adc_f.read_uv()*101.0/1000000)


print_voltages()
time.sleep(1)
disable_f.value(0)
time.sleep(1)
print_voltages()
mosfet.on()
print("f_pwm on")
time.sleep(3)
disable_hv.value(0)
print("hv on")
time.sleep(5)


for i in range(100000):
    time.sleep(1)
    write_shift_register([i%256]*5)
    print_voltages()
