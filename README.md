# Beyond-Dynamics-Rolos-Demo

### This repository contains notebooks demonstrating the algorithm developed during the summer practice in Rolos as well as all files supporting these notebooks.

## Abstract

The discovery of conservation principles is crucial for understanding the underlying behavior of physical systems and has applications across various domains. In this paper, we propose a novel method that combines representation learning and topological analysis to uncover the topology of conservation law spaces. Our approach is robust, as it does not rely on expert-selected values of hyperparameters, making it accessible to researchers from different disciplines. We demonstrate the method's effectiveness on a set of physical simulations, showcasing its potential for uncovering previously unknown conservation principles and fostering interdisciplinary research. Ultimately, this work emphasizes the power of data-driven techniques in advancing our understanding of fundamental principles governing physical systems and beyond.

## Methods

### Data

In our work we learn to determine the number of conserved quantities in dynamical system using the data from trajectories of this system. For a given model we consider a dataset of $N_traj$ trajectories, where each trajectory is represented by $traj_len$ points in the phase space. Initial conditions for the trajectories are drawn randomly from the phase space. Our algorithm only works under the assumption that the time of sampling is sufficiently large, such that any two trajectories with equal conserved quantities will draw from a single distribution which depend only on the values of the conserved quantities and not on the specific initial condition. The property of the system to have such sufficiently large time is called ergodicyty, so we consider only ergodic systems.

### Algorithm

We start the algorithm with normalizing the data to have the zero mean and unit variance along each individual coordinate of the phase space. To the resulting rescaled trajectories we apply the Wasserstein distance to compute pairwise distances between trajectories. These pairwise distances approximate the metric sctructure of the manifold $\mathcal{C}$ consisting of all possible trajectories of the system. Then we construct a series of embeddings in spaces with different dimensions using the UMAP algorithm. For each embedding we compute a score measuring how different the metric structure in the embedding differs from the metric structure given by the Wasserstein distances. The minimal dimension where the score is low corresponds to the dimensionality of the manifold $\mathcal{C}$. Moreover, $\mathcal{C}$ can be parametrised by the values of conserved quantities, so its dimensionality equals to the number of conserved quantities. Therefore, our algorithm is able to find the number of conserved quantities in the system.

## Instructions for running the example

All nessecary packages can be installed by running "pip install -r requirements.txt" in terminal.
To simulate the generation of the data you should run the create_trajectories.py file, e.g. run "python3 create_trajectories.py" in terminal.
After these steps you are ready to run the notebook Beyond_Dynamics.ipynb.
