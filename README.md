# Multi-agent Option Discovery based on Kronecker Product

## How to config the environments:
- python 3.6
- pytorch 1.6
- tensorboard 2.5
- matplotlib
- pandas
- numpy
- tqdm
- networkx
- ...

## How to run the experiments
- On Ubuntu 18.04
- Run experiments on n-agent Maze/Room tasks using Centralized Q-Learning + Force, please go to folder 'MAOD_n_agent_force'.
- Run experiments on n-agent Maze/Room tasks using Distributed Q-Learning, please go to folder 'MAOD_n_agents'.
- Run experiments on Maze/Room tasks with subtask grouping using Centralized Q-Learning + Force, please go to folder 'MAOD_pairwise_force_group'.
- Run experiments on Maze/Room tasks with subtask grouping using Distributed Q-Learning, please go to folder 'MAOD_pairwise_group'.
- Run experiments on Maze/Room tasks with random grouping using Centralized Q-Learning + Force, please go to folder 'MAOD_pairwise_force'.
- Run experiments on Maze/Room tasks with random grouping using Distributed Q-Learning, please go to folder 'MAOD_pairwise'.
- Run experiments on Maze/Room tasks with random grouping and dynamic influence using Centralized Q-Learning + Force, please go to folder 'MAOD_pairwise_force_influence'.
- In each folder, please first input:
```bash
cd options/experiments
```
and then:
```bash
python rl_experiments.py
```
Probably you will need a python IDE, like PyCharm, to run this file properly.

- When testing on the Room tasks, please add:
```bash
--use_median=True
```
  Otherwise, please add:
```bash
--use_median=False
```
- To change the test environment, please add:  
```bash
--task='grid_roomX'
```  
  Or:
```bash
--task='grid_mazeX'
```
where 'X' needs to be replaced with a number that represents the number of agents in the test environment. Please refer to the 'tasks' subfoloder in each folder mentioned above to check the available test environments.

- To produce the results of the MARL baselines on the 6-agent Grid Maze task, please go to the 'MARL_baselines' folder.  
  Fisrt, the parameter setup is available in 'common/arguments'.
  To run algorithm X which can be any of ['qmix', 'cwqmix', 'owqmix', 'coma', 'msac', 'maven'] with seed Y, please run:
  ```bash
  python main.py --alg=X --seed=Y
  ```