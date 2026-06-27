# SAC-Based-Robot-Motion-Planning
Soft Actor-Critic (SAC) based collision-free motion planning for a triangular robot with goal position and orientation control.
## Project Overview

This project presents a collision-free motion planning framework for a triangular mobile robot using Soft Actor-Critic (SAC), a deep reinforcement learning algorithm.

The agent learns to navigate from the start position to the target while avoiding obstacles and achieving the desired final orientation. Instead of following a predefined path, the robot learns an optimal policy through continuous interaction with the environment and a carefully designed reward function.
## Project Demonstration
### Environment

![Environment](images/environment.png)
### Best Trajectory

![Best Trajectory](images/best_trajectory.png)
### Reward Design

![Reward Design](images/reward_design.png)
### Trajectory Animation

 **Video:** [trajectory_animation.mp4](videos/trajectory_animation.mp4)
 ## Features

- Collision-free robot navigation using Soft Actor-Critic (SAC)
- Continuous action space control
- Goal position and orientation optimization
- Custom reward function for navigation and obstacle avoidance
- Trajectory visualization and animation
- Easy-to-extend simulation environment

## System Pipeline

Environment

↓

State Observation

↓

SAC Agent

↓

Action Selection

↓

Robot Motion

↓

Reward Calculation

↓

Policy Update


## Final Results

| Metric | Value |
|---------|------:|
| Algorithm | Soft Actor-Critic (SAC) |
| Goal Reached | ✅ Yes |
| Distance Error | 9.89 mm |
| Orientation Error | 0.46° |
| Collision | No |

## Repository Structure

├── docs/
├── images/
├── models/
├── trajectories/
├── videos/
├── README.md
├── requirements.txt
├── train.py
├── evaluate.py
└── environment.py

## Installation

```bash
git clone https://github.com/yourusername/SAC-Based-Robot-Motion-Planning.git

cd SAC-Based-Robot-Motion-Planning

pip install -r requirements.txt
```

## Training

```bash
python train.py
```

## Future Improvements

- Dynamic obstacle avoidance
- Real robot implementation
- Multi-goal navigation
- Sim-to-real transfer
- Comparison with other reinforcement learning algorithms
## Acknowledgements

This project was developed as part of my internship on reinforcement learning for autonomous robot motion planning using Soft Actor-Critic (SAC).
