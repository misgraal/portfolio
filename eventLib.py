class event:
    def __init__(self, file) -> None:
        self.file = file
    
    def RegisterEvent(self, eventName):
        lines = []
        with open(self.file, "r") as file:
            for line in file:
                lines.append(line)
        
        for line in lines:
            line = str(line)
            if line.startswith(eventName):
                parts = line.split(":")
                text = parts[1]
                return text
        return 
