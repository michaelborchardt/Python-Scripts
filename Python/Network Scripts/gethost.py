#!/usr/bin/env python
import socket

# Print 'Calculating' formatted with dashes.
print(format('-','-<30'), 'Getting Host', format('-','->30'))
print('Host:', socket.gethostname())