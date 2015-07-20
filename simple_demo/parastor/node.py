#-*-coding=utf8 -*-
"""This is a demo of how to define parastor node."""

class Node(object):
    """Base Node"""

    def __init__(self, nodetype, nodeid):
        self.nodetype = nodetype
        self.nodeid = nodeid
        
    def get_node_type(self):
        return self.nodetype

    def get_node_id(self):
        return self.nodeid

    def get_desc(self):
        return "This is base node."


class MGRNode(Node):
    """MGR Node"""    
  
    def __init__(self, nodetype, nodeid):
        super(MGRNode, self).__init__(nodetype, nodeid)

    def get_desc(self):
        return "This is MGR node."



    

    
    
    


