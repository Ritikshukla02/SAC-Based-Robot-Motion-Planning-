# Implementation Details

## Environment

The simulation environment consists of a triangular mobile robot, a static obstacle, a predefined start position, and a target position with a desired final orientation.

The robot interacts with the environment through continuous actions and receives rewards based on its navigation performance.

---

## State Representation

At each step, the agent receives the current state of the environment, which includes:

- Robot position (x, y)
- Robot orientation (θ)
- Goal position
- Relative distance to the goal
- Orientation error

These observations allow the agent to understand its current situation and decide the next action.

---

## Action Space

The Soft Actor-Critic (SAC) agent outputs continuous actions that control the robot's motion.

The actions determine:

- Linear movement
- Rotational movement

Continuous control enables smoother and more realistic robot navigation.

---

## Training Process

The training process follows an interaction-based learning approach.

1. Observe the current state.
2. Predict the next action using the SAC policy.
3. Execute the action in the environment.
4. Receive a reward.
5. Update the policy.
6. Repeat until the goal is reached or the episode ends.

![SAC Framework](../images/sac_framework.png)

---

## Model Configuration

The agent was trained using the Soft Actor-Critic (SAC) algorithm with a continuous action space.

The policy was gradually improved through multiple training episodes by maximizing the cumulative reward while learning safe and efficient navigation behaviour.
