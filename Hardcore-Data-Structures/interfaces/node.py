'''
This file defines the interface that node has to implement.
'''

from abc import ABC, abstractmethod

class SimpleNodeABC(ABC):
    """
    This abstract class defines the methods that SimpleNode's implementation has to implement
    """
    
    @abstractmethod
    def has_next_node(self)->bool:
        """
        this method returns true if node is connected to another node.
        """
        raise NotImplementedError
    
    @abstractmethod
    def return_next_node(self) -> any:
        """
        this method returns the next node if present.
        """
        raise NotImplementedError
    

class TwoWayNodeABC(SimpleNodeABC):
    """
    This abstract class defines the methods that TwoWayNode's implementation has to implement
    """
    @abstractmethod
    def has_prev_node(self)->bool:
        """
        this method returns true if node was connected to another node.
        """
        raise NotImplementedError
    
    @abstractmethod 
    def return_prev_node(self):
        """
        this method returns the prev node if present.
        """
        raise NotImplementedError