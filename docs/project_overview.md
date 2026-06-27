# Project Overview

## Objective

The objective of this project is to generate a collision-free trajectory for a triangular mobile robot using reinforcement learning.

The robot starts from a predefined position and learns how to reach the target while avoiding obstacles and achieving the required final orientation.

---

## Problem Statement

Traditional motion planning methods usually require predefined paths or manually designed planning algorithms.

In this project, the robot learns the navigation policy directly through interaction with the environment using the Soft Actor-Critic (SAC) algorithm.

---

## Project Workflow

Start Position

↓

Observe Environment

↓

Select Action using SAC

↓

Move Robot

↓

Receive Reward

↓

Update Policy

↓

Repeat until Goal is Reached

---

## Environment

The simulation environment consists of:

- Triangular mobile robot
- Static obstacle
- Goal position
- Goal orientation
- Continuous action space

![Environment](../images/environment.png)

---

## Project Goal

The learning process aims to satisfy three objectives simultaneously:

- Reach the target position
- Avoid obstacle collision
- Achieve the desired final orientation
