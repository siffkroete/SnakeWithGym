import gym
import gym_snake

# Construct Environment
env = gym.make('snake-v0')
env.n_foods = 1
observation = env.reset() # Constructs an instance of the game

# Controller
game_controller = env.controller

# Grid
grid_object = game_controller.grid
grid_pixels = grid_object.grid

# Snake(s)
snakes_array = game_controller.snakes
snake_object1 = snakes_array[0]

done = False

while not done:
    action = 0
    env.step(action)
    env.render()

env.close()
