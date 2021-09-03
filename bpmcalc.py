import sys, time, qdarkgraystyle
from PyQt5 import QtWidgets, QtGui, QtCore, uic, QtMultimedia

from util import Clock

class Window(QtWidgets.QMainWindow):
    timeStart = 0.0

    tapStart = 0.0
    tapTaps = 0

    metroIsPlaying = False
    metroNext = 0.0
    metroSPT = 0.0
    metroTap = 0
    metroSig = 0 # how many tocks per tick
    metroBar = 0 # how many tocks per full bar

    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("resources/ui/form.ui", self)

        self.timeStart = time.time()

        # BPM Tap

        self.actionExit.triggered.connect(lambda: self.close())
        self.actionTapT.triggered.connect(self.tap)
        self.actionTapZ.triggered.connect(self.tap)
        self.actionTapX.triggered.connect(self.tap)
        self.actionTapReset.triggered.connect(self.tapReset)

        self.tapButtonTap.clicked.connect(self.tap)
        self.tapButtonReset.clicked.connect(self.tapReset)

        self.tapSpinboxAmount.valueChanged.connect(lambda: self.tapReset())

        self.tapLCD.display("0.0")

        # BPM Calculator

        self.actionGo.triggered.connect(self.calc)

        self.calcButtonGo.clicked.connect(self.calc)
        self.calcRadio1.clicked.connect(self.calc)
        self.calcRadio2.clicked.connect(self.calc)
        self.calcRadio3.clicked.connect(self.calc)
        self.calcRadio4.clicked.connect(self.calc)
        self.calcSpinboxValue.valueChanged.connect(self.calc)
        self.calcComboboxValue.currentIndexChanged.connect(self.calc)

        # BPM Metronome

        self.actionStart.triggered.connect(self.metro)

        self.metroButtonStart.clicked.connect(self.metro)
        self.metroSliderVolume.valueChanged.connect(lambda: (
            self.tick.setVolume(self.metroSliderVolume.value() / 100),
            self.tock.setVolume(self.metroSliderVolume.value() / 100)
        ))

        self.tick = QtMultimedia.QSoundEffect()
        self.tick.setSource(QtCore.QUrl("file:resources/snd/tick.wav"))
        self.tick.setVolume(self.metroSliderVolume.value() / 100)
        self.tock = QtMultimedia.QSoundEffect()
        self.tock.setSource(QtCore.QUrl("file:resources/snd/tock.wav"))
        self.tock.setVolume(self.metroSliderVolume.value() / 200)
    
    # BPM Tap
    
    def tap(self):
        self.tapSpinboxAmount.setReadOnly(True)

        maxTaps = int(self.tapSpinboxAmount.text())

        if maxTaps > 0 and self.tapTaps >= maxTaps:
            self.tapSpinboxAmount.setReadOnly(False)
            return
        
        if self.tapStart == 0:
            self.tapStart = time.time()
            self.tapLabelDetails.setText("Tap one more time...")
            return
        else:
            self.tapTaps = self.tapTaps + 1

        timeElapsed = time.time() - self.tapStart

        if timeElapsed == 0: return

        timeSignature = 1/1

        if   self.tapRadio1.isChecked(): timeSignature = 1/1
        elif self.tapRadio2.isChecked(): timeSignature = 1/2
        elif self.tapRadio3.isChecked(): timeSignature = 1/3
        elif self.tapRadio4.isChecked(): timeSignature = 1/4

        tapsPerSecond = self.tapTaps / timeElapsed
        secondsPerTap = timeElapsed / self.tapTaps
        bpm = tapsPerSecond * 60 * timeSignature

        self.tapLCD.display("{:.1f}".format(bpm))

        self.tapLabelDetails.setText(
            str(self.tapTaps) + " taps, " +
            str("{:.2f}".format(bpm)) + " bpm, " +
            str("{:.2f}".format(tapsPerSecond)) + " taps/second, " +
            str("{:.2f}".format(secondsPerTap * 1000)) + " ms/tap")
    
    def tapReset(self):
        self.tapStart = 0
        self.tapTaps = 0
        self.tapLCD.display("0.0")
        
        self.tapSpinboxAmount.setReadOnly(False)
        
        self.tapLabelDetails.setText("Waiting for taps...")

    # BPM Calculator
    
    def calcFromBpm(self, bpm, sig):
        tps = bpm / 60.0 / sig
        mspt = 1.0 / tps * 1000.0

        return [bpm, mspt, tps]
    
    def calcFromMspt(self, mspt, sig):
        tps = 1000.0 / mspt
        bpm = 60.0 * tps * sig

        return [bpm, mspt, tps]
    
    def calcFromTps(self, tps, sig):
        mspt = 1.0 / tps * 1000.0
        bpm = 60.0 * tps * sig

        return [bpm, mspt, tps]
        
    def calc(self):
        sig = 1/1

        if   self.calcRadio1.isChecked(): sig = 1/1
        elif self.calcRadio2.isChecked(): sig = 1/2
        elif self.calcRadio3.isChecked(): sig = 1/3
        elif self.calcRadio4.isChecked(): sig = 1/4

        baseValue = self.calcSpinboxValue.value()
        baseType = self.calcComboboxValue.currentText()

        [bpm, mspt, tps] = [0.0, 0.0, 0.0]

        if baseType == "BPM":
            [bpm, mspt, tps] = self.calcFromBpm(baseValue, sig)
        elif baseType == "ms/tap":
            [bpm, mspt, tps] = self.calcFromMspt(baseValue, sig)
        elif baseType == "taps/s":
            [bpm, mspt, tps] = self.calcFromTps(baseValue, sig)

        [to2, a, a] = self.calcFromTps(tps, 1/2)
        [to3, a, a] = self.calcFromTps(tps, 1/3)
        [to4, a, a] = self.calcFromTps(tps, 1/4)
        
        self.calcTextResult.setText(
            "<pre>" +
            "Result:\n" +
            "{:.2f}".format(bpm) + " bpm, " +
            "{:.2f}".format(mspt) + " ms/tap, " +
            "{:.2f}".format(tps) + " taps/s" +
            "\n--------------------------------------\n" +
            "{:.2f}".format(tps) + " taps/s = " + "{:.2f}".format(to2) + " bpm 1/2\n" +
            "{:.2f}".format(tps) + " taps/s = " + "{:.2f}".format(to3) + " bpm 1/3\n" +
            "{:.2f}".format(tps) + " taps/s = " + "{:.2f}".format(to4) + " bpm 1/4" +
            "</pre>"
        )
    
    # BPM Metronome
    
    def metro(self):
        if self.metroIsPlaying:
            self.metroIsPlaying = False
        else:
            sig = 1/1

            if   self.metroRadio1.isChecked(): sig = 1/1
            elif self.metroRadio2.isChecked(): sig = 1/2
            elif self.metroRadio3.isChecked(): sig = 1/3
            elif self.metroRadio4.isChecked(): sig = 1/4

            self.metroIsPlaying = True
            [bpm, mspt, tps] = self.calcFromBpm(self.metroSpinboxBPM.value(), sig)
            self.metroSPT = mspt / 1000
            self.metroNext = time.time() + mspt / 1000

            self.metroTap = 0
            self.metroSig = int(1 / sig)
            self.metroBar = int(self.metroComboboxSignature.currentText()[0]) * self.metroSig

            print(
                "tap: " + str(self.metroTap) +
                "\nsig: " + str(self.metroSig) +
                "\nbar: " + str(self.metroBar)
            )

            self.tick.play()
            self.metroProgressbar.setValue(0)

    def step(self, delta):
        self.metroLabelFPS.setText("{:.2f}".format(delta * 1000) + " ms/t, " + "{:.2f}".format(1 / delta) + " tps")

        if self.metroIsPlaying and time.time() > self.metroNext:
            if self.metroCheckboxSimulate.isChecked(): self.tap()
            self.metroNext = self.metroNext + self.metroSPT
            self.metroTap = self.metroTap + 1

            if self.metroTap >= self.metroBar:
                self.metroTap = 0

            if self.metroTap == 0 or (self.metroTap % self.metroSig == 0 and self.metroSig != 1):
                self.tick.play()
            else:
                self.tock.play()

            self.metroProgressbar.setValue(int(self.metroTap / (self.metroBar - 1) * 1000))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet("")
    app.setStyle("Fusion")
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    
    window = Window()
    window.show()

    clock = Clock()
    clock.tickDelta.connect(window.step)
    clock.start()

    app.exec()