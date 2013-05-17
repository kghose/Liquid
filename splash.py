"""This module implements fun visualizations of the echo state/liquid state machine."""
import pylab
from matplotlib import animation

def plot_network(lsm, max_width=10):
  """Passes a liquid state machine show it as a ."""
  nodes = lsm.nodes
  N = lsm.node_count


def animate_network(lsm, buffer_len):
  def animate(frame):
    lsm.update()
    buffer[:,:-1] = buffer[:,1:]
    buffer[:,-1] = lsm.nodes
    im.set_array(buffer)
    return im, fig.suptitle(frame)

  buffer = pylab.zeros((lsm.node_count,buffer_len))

  fig = pylab.figure()
  im = pylab.imshow(buffer, vmin=0, vmax=1, cmap=pylab.cm.gray, interpolation='none')

  anim = animation.FuncAnimation(fig, animate,
                                 frames=500, interval=20, repeat=False, blit=True)
  return anim

