class event:
    def __init__(self, file) -> None:
        self.file = file
        with open(self.file, "w") as txt:
            txt.write("")
    
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
                mainLine = line
        
        newLines = []

        for line in lines:
            line = str(line)
            if mainLine != line:
                newLines.append(line)


        with open(self.file, 'w') as file:
            for line in newLines:
                file.write(line + "\n")
        return text
    
    def TriggerEvent(self, eventName, *args):
        with open(self.file, "a") as file:
            print(args[0])
            file.write(eventName + ";-;" + args[0]+"\n")
        
