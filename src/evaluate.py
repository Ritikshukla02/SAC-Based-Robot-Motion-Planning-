"""
Evaluate the trained SAC model and generate
the robot trajectory for visualization.
"""

from stable_baselines3 import SAC     # loading Model

model = SAC.load("../models/best_sac_model")

obs, _ = env.reset()                          # generating file tracjectroy

trajectory = []

for step in range(2000):

    action, _ = model.predict(
        obs,
        deterministic=True
    )

    obs, reward, done, truncated, _ = env.step(action)

    trajectory.append([
        step * env.dt,
        env.x,
        env.y,
        np.rad2deg(env.theta)
    ])

    if done or truncated:
        print("Episode Ended")
        print("Step:", step)
        print("Final X:", env.x)
        print("Final Y:", env.y)
        print("Final Theta:", np.rad2deg(env.theta))
        print("Reward:", reward)
        print(
        "Distance to Goal:",
        np.sqrt(
            (env.x - GOAL_X)**2 +
            (env.y - GOAL_Y)**2
        )
    )
        orientation_error = abs(
    np.arctan2(
        np.sin(env.theta - GOAL_THETA),
        np.cos(env.theta - GOAL_THETA)
    )
)

        print(
    "Orientation Error:",
        np.rad2deg(orientation_error)
)

        if reward == -1000.0:
          print("Result: COLLISION")
        elif done:
          print("Result: GOAL REACHED")
        elif truncated:
          print("Result: TIME LIMIT")

        break
#-----------------------------------
df = pd.DataFrame(
    trajectory,
    columns=[
        "time",
        "x",
        "y",
        "theta_deg"
    ]
)

df.to_csv(
    "../trajectories/trajectory_final.csv",
    index=False
)
#------------------------------------
