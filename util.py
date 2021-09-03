from PyQt5 import QtCore
import time

RATE = 120

class Clock(QtCore.QThread):
    tick = QtCore.pyqtSignal()
    tickDelta = QtCore.pyqtSignal(float)

    def run(self):
        ticks = 0
        timeLast = time.time()

        while True:
            time.sleep(1.0 / RATE)
            ticks = ticks + 1

            timeCurrent = time.time()

            self.tick.emit()
            self.tickDelta.emit(timeCurrent - timeLast)

            timeLast = timeCurrent