# Project Overview
## Problem Setup

The task is to generate a collision-free trajectory for a triangular mobile robot using reinforcement learning.

The robot starts from a predefined position and must reach the target while avoiding obstacles and achieving the desired final orientation.

## Simulation Environment

The environment contains the following components:

Triangular mobile robot
Static obstacle
Goal position
Goal orientation
Continuous action space




## Learning Objective

The agent learns a navigation policy by interacting with the environment. During training, the policy is updated continuously based on the reward received after each action.

The learned policy aims to satisfy the following objectives simultaneously:

Reach the target position
Avoid obstacle collision
Achieve the desired final orientation

Unlike traditional path planning methods, no predefined trajectory is provided to the robot during training.
