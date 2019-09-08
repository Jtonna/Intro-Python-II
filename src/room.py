# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name="empty", description="empty", items=[]):
        self.name = name
        self.description = description
        self.items = []
    
    #Class functions would be added here
        
    def __str__(self):
	    return f"{self.name}"
