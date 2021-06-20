
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

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def update_member(self, member):
        # fill this method and update the return
        member['last_name']=self.last_name               
        
        for member_del in self._members:
            if member['id'] == member_del['id']:            
                self._members.remove(member_del)
                 
                if not member.get('id'):                    
                    member['id'] = self._generateId()
                self._members.append(member)
                return self._members
        return
            
    def add_member(self, member):
        # fill this method and update the return
        member['last_name']=self.last_name
        if not member.get('id'):                    
            member['id'] = self._generateId()
        self._members.append(member)
        
    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if id == member['id']:            
                self._members.remove(member)
                return self._members
        

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if id == member['id']:
                return member        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
