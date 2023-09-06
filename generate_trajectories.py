import os
from creating import create_trajectories


path = "./data"
if not os.path.exists(path):
    os.makedirs(path)
create_trajectories(path)