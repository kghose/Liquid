Liquid is a simulator for liquid state machines (LSM). The emphasis is on developing intuitions about how these constructs work and visualizing the machine in operation.

A LSM in Liquid consists of N reservoir nodes connected to each other and M readout nodes that each combine the outputs of a subset of the reservoir nodes.

The nodes are specified by a N x k matrix, where each row is a node with k parameters

The connection matrix is an N x N x m matrix, where each connection has m parameters

The node state is a scalar continuous value that stays between -1 and +1 and is a linear function of the inputs.

The entire network runs in 'chunked time' each time step taking T seconds.


