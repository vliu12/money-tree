class Tree:

    def __init__(self):
        self.size = "seedling"
        self.branch = 0;

    def grow(self):
        if self.size == "seedling":
            self.size = "sapling"
        elif self.size == "sapling":
            self.size = "mature"
        elif self.size == "mature":
            self.size = "old";
    
    def branch(self):
        self.branch += 1;


    def __str__(self):
        return str(self.value)