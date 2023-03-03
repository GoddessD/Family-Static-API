
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = [
             {
                "id": self._generateId(),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]
    def _generateId(self):
        return randint(0, 99999999)
    def add_family_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"]= self.last_name
        self.members.append(member)
        return self.members

    def get_all_members(self):
        return self.members

    def get_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                return member
        return False

    # def get_member(self, id):
    #     for member in self._members:
    #         if member['id'] == id:
    #             return {
    #             'first_name': member['first_name'],
    #             'id': member['id'],
    #             'age': member['age'],
    #             'lucky_numbers': member['lucky_numbers']
    #         }
    # return None
    

    def delete_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                self.members.remove(member)
                return {'done': True}
        return {"done": False}


    # this method is done, it returns a list with all the family members

