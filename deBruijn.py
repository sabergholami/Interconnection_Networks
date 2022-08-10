import networkx as nx
def DeBruijn(n):
  import collections
  def reverse_first_bit(b):
    my_b = list(b)
    if b[-1]=='0':
      my_b[-1] = '1'
      return ''.join(my_b)
    else:
      my_b[-1] = '0'
      return ''.join(my_b)
  
  def left_shift(b):
    x  = collections.deque(list(b))
    x.rotate(-1)
    return ''.join(x)



  getbinary = lambda x, n: format(x, 'b').zfill(n)
  G = nx.Graph()
  for i in range(2**n):
    node = int(str(getbinary(i,n)),2)
    left = int(left_shift(getbinary(i,n)),2)
    left_swap = int(reverse_first_bit(left_shift(getbinary(i,n))),2)
    
    if node!= left: #no self-loop
      G.add_edge(node,left)
    G.add_edge(node,left_swap)
  return G
