"""
Defines the robot geometry, collision detection,
visualization utilities, and Gymnasium environment
used for SAC training.
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon, Rectangle
from shapely.geometry import Polygon as ShapelyPolygon

import gymnasium as gym
from gymnasium import spaces

# Geometry Parameters

BASE = 50      # mm
HEIGHT = 150   # mm

# Rectangle obstacle
RECT_X = -280
RECT_Y = -250
RECT_W = 280
RECT_H = 250
GOAL_X = 50
GOAL_Y = -200
GOAL_THETA = np.deg2rad(90)

# Triangle Model

class Triangle:

    def __init__(self, x, y, theta_deg):
        """
        x,y = centroid
        theta_deg = orientation
        """

        self.x = x
        self.y = y
        self.theta = np.deg2rad(theta_deg)

    def vertices(self):

        # Local coordinates
        A = np.array([-50, 25])
        B = np.array([-50,-25])
        TIP = np.array([100,0])

        pts = np.array([A,B,TIP])

        # Rotation matrix
        c = np.cos(self.theta)
        s = np.sin(self.theta)

        R = np.array([
            [c,-s],
            [s,c]
        ])

        pts = pts @ R.T

        pts[:,0] += self.x
        pts[:,1] += self.y

        return pts
#-------------------------
start_triangle = Triangle(
    x=-150,
    y=50,
    theta_deg=0
)

goal_triangle = Triangle(
    x=50,
    y=-200,
    theta_deg=90
)
#-------------------------
def draw_scene(triangle1, triangle2=None):

    fig, ax = plt.subplots(figsize=(8,8))

    # obstacle
    rect = Rectangle(
        (RECT_X,RECT_Y),
        RECT_W,
        RECT_H,
        fill=False,
        linewidth=2
    )

    ax.add_patch(rect)

    # start
    verts = triangle1.vertices()

    ax.add_patch(
        Polygon(
            verts,
            closed=True,
            fill=False,
            linewidth=2,
            label="Triangle"
        )
    )

    if triangle2 is not None:

        verts2 = triangle2.vertices()

        ax.add_patch(
            Polygon(
                verts2,
                closed=True,
                fill=False,
                linestyle="--",
                linewidth=2,
                label="Goal"
            )
        )

    ax.plot(0,0,'o')
    ax.text(5,5,"Corner")

    ax.set_aspect('equal')
    ax.grid(True)

    ax.set_xlim(-300,150)
    ax.set_ylim(-450,150)

    plt.legend()
    plt.show()
#------------------------
if __name__ == "__main__":

    draw_scene(
        start_triangle,
        goal_triangle
    )

#define Rectangle ----------------------------------------------- main start from here
rectangle_poly = ShapelyPolygon([
    (RECT_X, RECT_Y),
    (RECT_X + RECT_W, RECT_Y),
    (RECT_X + RECT_W, RECT_Y + RECT_H),
    (RECT_X, RECT_Y + RECT_H)
])
#------------------------Collision Detection Function
def check_collision(triangle):

    verts = triangle.vertices()

    triangle_poly = ShapelyPolygon(verts)

    return triangle_poly.intersects(rectangle_poly)

#------------------------- Triangle Environment
class TriangleEnv(gym.Env):

    def __init__(self):

        super().__init__()

        self.dt = 0.05

        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(9,),
            dtype=np.float32
        )

        self.action_space = spaces.Box(
            low=np.array([-11,-11,-5]),
            high=np.array([11,11,5]),
            dtype=np.float32
        )

        self.reset()

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.x = -150.0
        self.y = 50.0

        self.theta = 0.0

        self.vx = 0.0
        self.vy = 0.0

        self.omega = 0.0
        self.step_count = 0
        self.previous_distance = np.sqrt(
            (self.x - GOAL_X)**2 +
            (self.y - GOAL_Y)**2
)

        self.triangle = Triangle(
        self.x,
        self.y,

        np.rad2deg(self.theta)
    )

        state = np.array([
            self.x,
            self.y,
            self.theta,
            self.vx,
            self.vy,
            self.omega,


            GOAL_X - self.x,

            GOAL_Y - self.y,
            GOAL_THETA - self.theta
        ], dtype=np.float32)

        return state, {}

    def step(self, action):

        ax, ay, alpha = action
        self.step_count += 1

        self.vx += ax * self.dt
        self.vy += ay * self.dt

        self.omega += alpha * self.dt

        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

        self.theta += self.omega * self.dt
        self.theta = np.arctan2(
          np.sin(self.theta),
          np.cos(self.theta))


        self.triangle.x = self.x
        self.triangle.y = self.y
        self.triangle.theta = self.theta
        speed = np.sqrt(
    self.vx**2 +
    self.vy**2
)

        collision = check_collision(self.triangle)
        distance_error = np.sqrt(
            (self.x - GOAL_X)**2 +
            (self.y - GOAL_Y)**2
           )
        progress = self.previous_distance - distance_error

        orientation_error = np.arctan2(
            np.sin(self.theta - GOAL_THETA),
            np.cos(self.theta - GOAL_THETA)

           )
        orientation_error = abs(orientation_error)

        state = np.array([
            self.x,
            self.y,
            self.theta,
            self.vx,
            self.vy,
            self.omega,

            GOAL_X - self.x,

            GOAL_Y - self.y,
            GOAL_THETA - self.theta
        ], dtype=np.float32)


        reward = -0.1
        reward += 30.0 * progress
        reward += -0.01 * distance_error                                         # Giving rewards.

        if distance_error < 100:
           reward += -30.0 * (
        orientation_error / np.pi
)


        if speed < 0.5:
           reward -= 1.0

        if distance_error < 100:
           reward += 10

        if distance_error < 50:
          reward += 25

        if distance_error < 20:
          reward += 100

        terminated = False
        truncated = False

        if collision:
          reward = -1000.0
          terminated = True


        elif (
          distance_error < 20
    and
          orientation_error < np.deg2rad(10)):

          reward = 5000.0

          terminated = True



        elif self.step_count >= 2000:

          truncated = True



        self.previous_distance = distance_error
        return (
            state,
            reward,
            terminated,
            truncated,
            {}
        )
