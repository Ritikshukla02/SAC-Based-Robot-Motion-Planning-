"""
Train a Soft Actor-Critic (SAC) agent for
collision-free robot motion planning.
"""
from stable_baselines3 import SAC

from environment import TriangleEnv


def main():

    env = TriangleEnv()

    model = SAC(

        "MlpPolicy",

        env,

        verbose=1,

        learning_rate=3e-4,

        buffer_size=300000,

        batch_size=256,

        gamma=0.99,

        learning_starts=5000

    )

    model.learn(

        total_timesteps=300000,

        reset_num_timesteps=False

    )

    model.save("../models/best_sac_model")


if __name__ == "__main__":

    main()

