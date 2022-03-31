'''
Create a function that takes a dictionary of objects like 
{ "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects 
like { "name": "John", "top_note": 5 }.'''


class MyDicts:
    def __init__(self, name, notes) -> None:
        self.name = name
        self.notes = notes
        self.higher = 0
        self.dict = {'name': name, 'notes': notes}

    def top_note(self):
        print(self.dict['name'], self.dict['notes'])
        for i in self.dict['notes']:
            if i > self.higher: self.higher = i
        
        return self.higher


a = MyDicts('Josh', [1, 2, 3])
print(a.top_note())