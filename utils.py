# -*- coding: utf-8 -*-
def update_time(self,event):
        self.subject.set_time(self.time.get())
        ...

def set_time(time) :
        self.time=time
        if self.signal :
            self.signal=self.signal[0:(len(signal)/self.time) + 1]
            self.signal=map(lambda (x, y): (x*self.time, y), self.signal)
            self.notify()
        return self.signal
