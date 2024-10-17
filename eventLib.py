class event:
    def __init__(self, file) -> None:
        self.file = file
    
    def EventHandler(self, eventName):
        lines = []
        
        # Listen to txt file
        while lines == []:
            with open(self.file, "r") as file:
                for line in file:
                    lines.append(line)
        
        for line in lines:
            line = str(line)
            if line.startswith(eventName):
                parts = line.split(";-;")
                text = parts[1]
            
        with open(self.file, 'w') as file:
            file.write("")
        return text
    
    def TriggerEvent(self, eventName, *args):
        with open(self.file, "a") as file:
            print(args[0])
            file.write(eventName + ";-;" + args[0]+"\n")
        
