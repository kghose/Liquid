"""This module implements the basic liquid state machine class."""
import pylab
from collections import deque

class LSM:
  """
  nodes  - N x 1 (activation level)
  cm     - N x N x 2 (strength (signed), delay ([0,1]))
  axons  - N x N list of lists of deques (signal history) deque length determined from timestamps)

  """
  def __init__(self, N=100, cm=None, max_n=10):
    """A connection matrix of None will cause a completely random connection matrix to be initialized."""
    self.node_count = N
    self.nodes = pylab.zeros(N)
    if cm is not None:
      self.cm = cm
    else:
      self.random_cm()
    self.setup_axons(max_n)

  def random_cm(self):
    N = self.node_count
    self.cm = pylab.zeros((N,N,2))
    self.cm[:,:,0] = pylab.randn(N,N)-.2
    self.cm[:,:,1] = pylab.rand(N,N)+10

  def setup_axons(self, max_n=10):
    N = self.node_count
    L = self.cm[:,:,1]*max_n
    self.axons = [[deque([0]*L[r,c]) for c in xrange(N)] for r in xrange(N)]

  def update(self):
    """Run one step of the simulation."""
    N = self.node_count
    axons = self.axons
    nodes = self.nodes
    cm = self.cm

    #First go over each node, loading the current value of each node into the buffers
    #It's important to do this because axons that have zero delay have empty buffers: the buffers are unloaded right after they are loaded
    for r in xrange(N): #Source
      for c in xrange(N): #Destination
        axons[r][c].appendleft(nodes[r]*cm[r,c,0])

    #Now go over each node, updating the state based on the inputs
    for c in xrange(N): #Destination
      total_input = 0
      for r in xrange(N): #Source
        total_input += axons[r][c].pop()
      nodes[c] += total_input

    nodes[pylab.find(nodes > 1)] = 1
    nodes[pylab.find(nodes < 0)] = 0


