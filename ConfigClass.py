import json
class Config():
    def __init__(self) -> None:
        #self.path = "config.json" #debuge
        self.path = "_internal\config.json" #release
        self.Reopen()

    def Reopen(self):
        with open(self.path) as f:
            self.conf = json.load(f)

    def getConf(self, Key):
        for key, value in self.conf.items():
            if key == Key:
                return value
            

    def setConf(self, Key, Value):
        for key, value in self.conf.items():
            if key == Key:
                self.conf[key] = Value

    def ConfigSave(self):
        with open(self.path,"w") as f:
            json.dump(self.conf, f)