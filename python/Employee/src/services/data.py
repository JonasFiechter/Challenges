class Data():
    def __init__(self) -> None:
        # Structure like -> (121, ('John', 'Analyst', 8812))
        self.database = set()

    def create(self, *args, **kwargs):
        if type(args[0]) != int:
            raise TypeError
        self.database.add((args[0], (args[1:])))

    def retrieve_by_id(self):
        ...
    
    def retrieve_all(self):
        return [item for item in self.database]

    def retrieve_range(self):
        ...
    
    def update(self):
        ...

    def delete(self):
        ...
