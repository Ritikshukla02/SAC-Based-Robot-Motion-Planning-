# Reward Function

The reward function is designed to encourage safe and efficient navigation while guiding the robot towards the target position with the desired final orientation.

Rather than relying on a single reward, multiple reward components work together to balance navigation, obstacle avoidance, and orientation control.

---

## Reward Components

### Progress Reward

The agent receives a positive reward when it moves closer to the target.

This encourages continuous progress and prevents unnecessary movements.

---

### Distance Reward

As the robot approaches the goal, additional rewards are provided at different distance thresholds.

This helps the agent learn to reach the target more accurately.

---

### Orientation Reward

Orientation becomes increasingly important near the target position.

The reward encourages the robot to gradually align with the desired final orientation while approaching the goal.

---

### Collision Penalty

A large negative reward is assigned whenever the robot collides with an obstacle.

This teaches the agent to avoid unsafe trajectories.

---

### Goal Reward

A high positive reward is provided when both conditions are satisfied:

- The robot reaches the target position.
- The robot achieves the required final orientation.

This represents successful completion of the task.

---

## Episode Termination

An episode ends when one of the following conditions is met:

- The robot reaches the goal successfully.
- The robot collides with an obstacle.
- The maximum number of simulation steps is reached.

---

## Reward Design Strategy

The reward function was refined through multiple experiments.

Initially, the agent learned to reach the target position but struggled to achieve the desired orientation.

Several reward adjustments were evaluated to balance navigation and orientation without degrading obstacle avoidance performance.

The final reward design successfully enabled the agent to reach the target while maintaining the required final orientation.
