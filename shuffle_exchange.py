import networkx as nx
def shuffle_exchange(n):
  import collections
  def reverse_last_bit(b):
    my_b = list(b)
    if b[0]=='0':
      my_b[0] = '1'
      return ''.join(my_b)
    else:
      my_b[0] = '0'
      return ''.join(my_b)
  
  def left_shift(b):
    x  = collections.deque(list(b))
    x.rotate(-1)
    return ''.join(x)

  def right_shift(b):
    x  = collections.deque(list(b))
    x.rotate(1)
    return ''.join(x)


  getbinary = lambda x, n: format(x, 'b').zfill(n)
  G = nx.Graph()
  for i in range(2**n):
    node = int(str(getbinary(i,n)),2)
    swap = int(str(reverse_last_bit(getbinary(i,n))),2)
    left = int(left_shift(getbinary(i,n)),2)
    right = int(left_shift(getbinary(i,n)),2)
    G.add_edge(node,swap)
    G.add_edge(node,left)
    G.add_edge(node,right)
  return G
