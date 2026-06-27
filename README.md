# SAC-Based-Robot-Motion-Planning
Soft Actor-Critic (SAC) based collision-free motion planning for a triangular robot with goal position and orientation control.
![Best Trajectory](images/best_trajectory.png)
## Project Overview

This project presents a reinforcement learning framework for collision-free motion planning using the Soft Actor-Critic (SAC) algorithm.

The objective is to navigate a triangular mobile robot from the start position to the target while avoiding obstacles and achieving the desired final orientation. Instead of relying on predefined trajectories, the agent learns an optimal navigation policy through interaction with the environment and a custom-designed reward function.
## Why Reinforcement Learning?

Traditional motion planning methods usually depend on handcrafted rules or predefined paths.

In contrast, reinforcement learning enables the robot to learn collision-free navigation directly from interaction with the environment, making the learned policy more flexible for different obstacle configurations.
## Project Highlights

- Collision-free trajectory generation
- Soft Actor-Critic (SAC) based continuous control
- Simultaneous position and orientation optimization
- Custom reward function for robot navigation
- Trajectory visualization and animation
- Goal-reaching behavior learned without predefined paths
## Final Result

| Metric | Result |
|---------|--------|
| Algorithm | Soft Actor-Critic (SAC) |
| Goal Reached | ✅ Yes |
| Distance Error | 9.89 mm |
| Orientation Error | 0.46° |
| Collision | No |
## Simulation Environment

![Simulation Environment](images/environment.png)
## Trajectory Animation

![Trajectory Animation](videos/trajectory_animation.gif)
## SAC Framework

![SAC Framework](images/sac_framework.png)
## Reward Function

![Reward Function](images/reward_design.png)
## Detailed Documentation

- [Project Overview](docs/project_overview.md)
- [System Pipeline](docs/system_pipeline.md)
- [Reward Function](docs/reward_function.md)
- [Results and Evaluation](docs/results_and_evaluation.md)
- [Limitations and Future Work](docs/limitations_and_future_work.md)
  ## Future Improvements

- Dynamic obstacle avoidance
- Multiple robot navigation
- Sim-to-real deployment
- Benchmarking with other reinforcement learning algorithms
