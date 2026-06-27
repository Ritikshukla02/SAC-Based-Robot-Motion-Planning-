# Limitations and Future Work

## Current Limitations

The current implementation was developed and evaluated in a simulated environment with a single static obstacle.

Although the trained policy successfully reaches the target while avoiding collisions, the following limitations remain:

- The policy has been evaluated on a single environment configuration.
- Dynamic or moving obstacles are not considered.
- The model has not been deployed on a physical robot.
- Performance has not been compared with other reinforcement learning algorithms.

---

## Future Work

The following improvements can further extend this project:

- Evaluate the policy under different obstacle configurations.
- Introduce dynamic obstacle avoidance.
- Compare SAC with other reinforcement learning algorithms such as PPO and TD3.
- Deploy the trained policy on a real robotic platform.
- Investigate sim-to-real transfer for practical applications.

---

## Conclusion

This project demonstrates that Soft Actor-Critic (SAC) can successfully learn collision-free motion planning for a triangular mobile robot while satisfying both position and orientation objectives.

The proposed framework provides a solid foundation for future research on autonomous robot navigation in more complex environments.
