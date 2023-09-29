"""
This example uses AnimationsSequence to display multiple animations in sequence, at a five second
interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.
"""
import board
import neopixel
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.color import PURPLE, AMBER, JADE, PINK, MAGENTA, ORANGE, TEAL, GREEN

pixel_pin = board.D2
pixel_num = 30

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

blink = Blink(pixels, speed=0.05, color=ORANGE)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
chase = Chase(pixels, speed=0.05, size=2, spacing=4, color=ORANGE)
solid = Solid(pixels, color=MAGENTA)
colorcycle = ColorCycle(pixels, 0.5, colors=[PURPLE, ORANGE, GREEN, MAGENTA])
pulse = Pulse(pixels, speed=0.05, color=ORANGE, period=3)
sparkle = Sparkle(pixels, speed=0.05, color=GREEN, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=MAGENTA)
#rainbow = Rainbow(pixels, speed=0.05, period=1, precompute_rainbow = True)
#rainbow_chase = RainbowChase(pixels, speed=0.05, size=5, spacing=3, step = 3)
#rainbow_comet = RainbowComet(pixels, speed=0.05, tail_length=7, bounce=True, colorwheel_offset = 85)
#rainbow_sparkle = RainbowSparkle(pixels, speed=0.07, num_sparkles=15)


animations = AnimationSequence(pulse, sparkle, solid, blink, comet, chase, sparkle_pulse, colorcycle, advance_interval=6, auto_clear=True)

while True:
    animations.animate()
