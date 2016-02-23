# Subject : notify (to observers), attach, detach (observers)
class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        print("notify",self.observers)
        for obs in self.observers:
            obs.update(self)
    def attach(self, obs):
        if not hasattr(obs,"update"):
            raise ValueError("Observer must have an update() method")
        self.observers.append(obs)
    def detach(self, obs):
        if obs in self.observers :
            self.observers.remove(obs)

# observer : update (observable state changes, change observable states)
class Observer:
    def update(self,subject):
        pass
