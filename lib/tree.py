class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
     # To define a recursive function for depth-first search
    def dfs(node):
       # If the node is None, return None (base case for recursion)
      if node is None:
        return None
       # If the current node matches the id, return the node
      if node['id'] == id:
        return node
      
       # Incase the node has children, iterate through each child
      for child in node['children']:
        result = dfs(child)
        # If the child or any of its descendants is a match, return the node
        if result is not None:
          return result
       # If no match was found in this branch, return None  
      return None
     # Start the search from the root
    return dfs(self.root)  
  pass
