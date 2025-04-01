import machine
import hcsr04
import time

ultrasonic = hcsr04.HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)

led = machine.Pin(18, machine.Pin.OUT)
buzzer = machine.PWM(machine.Pin(14, machine.Pin.OUT))

buzzer.freq(4186)
buzzer.duty(0)

while True:
    distance = ultrasonic.distance_cm()
    print("Distance is: ", distance, "cm", "|", distance/2.54, "inch")
    if distance <= 10:
        buzzer.duty(512)
        led.on()
    else:
        buzzer.duty(0)
        led.off()
    time.sleep(0.3)