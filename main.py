import pychrono

timer = pychrono.Timer()
timer.start()

pychrono.delay(2000)

print(timer.elapsed())