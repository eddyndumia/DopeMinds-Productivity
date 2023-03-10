

class task:
    def __init__(self) -> None:
        self.taskID = None
        self.progress = 0
        self.name = None
        self.weight = None
        
    def increase_progress(self):
        self.progress += 1
        
task1 = task()

task1.name = input("What task do you have today?:")       
print(task1.name)

task1.increase_progress()
print(task1.progress)


# put it down on paper first

