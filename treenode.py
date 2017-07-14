class treeNode():

    def __init__(self, name, node_function, *children, node_type='np', frac=1):
        self.name = name
        self.node_function = node_function
        self.node_type = node_type
        self.running = True
        self.frac = frac
        self.children = children
        self.total_runtime = 0
        self.total_repairtime = 0

    def update_node_status(self):
        if self.node_function == 'AND':
            not_running = 0
            for child in self.children:
                if child.running == False:
                    not_running += 1
            if not_running > 0:
                self.running = False
            else:
                self.running = True
        elif self.node_function == 'OR':
            running = 0
            for child in self.children:
                if child.running == True:
                    running += 1
            if running > 0:
                self.running = True

            else:
                self.running = False
        elif self.node_function == 'XofY':
            running = 0
            for child in self.children:
                if child.running == True:
                    running += 1
            if running/len(self.children) >= self.frac:
                self.running = True
            else:
                self.running = False

    def print_child_qty(self):
        print(len(self.children))

    def shutdown_node(self):
        for child in self.children:
            child.running = False

    def startup_node(self):
        for child in self.children:
            child.running = True

    def get_availability(self):
        return self.total_runtime/(self.total_runtime+self.total_repairtime)
