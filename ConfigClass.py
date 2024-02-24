import json
class Config():
    
    @staticmethod
    def getConf(Key):
        with open("config.json") as f:
            conf = json.load(f)
        for key, value in conf.items():
            if key == Key:
                return value
            
    @staticmethod
    def setConf(Key, Value):
        with open("config.json") as f:
            conf = json.load(f)
        for key, value in conf.items():
            if key == Key:
                conf[key] = Value
        with open("config.json","w") as f:
            json.dump(conf, f)