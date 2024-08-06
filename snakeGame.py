import tkinter as tk
import random

# Global variables
WIDTH = 400
HEIGHT = 400
DELAY = 100
DOT_SIZE = 10
SCORE_INCREMENT = 10

# Initialize the game
def start_game():
    global snake_direction, score, game_over

    snake_direction = "Right"
    score = 0
    game_over = False

    # Starting position for the snake
    x = WIDTH / 2
    y = HEIGHT / 2

    # Create the snake
    global snake
    snake = [(x, y), (x - DOT_SIZE, y), (x - (2 * DOT_SIZE), y)]

    # Create the food
    global food
    create_food()

    # Start the game loop
    game_loop()


# Update the game state
def game_loop():
    global game_over

    if not game_over:
        move_snake()
        check_collision()
        update_score()
        game_canvas.after(DELAY, game_loop)
    else:
        game_canvas.create_text(WIDTH/2, HEIGHT/2, text="Game Over", font=("Helvetica", 24), fill="red")


# Handle keyboard input
def change_direction(event):
    global snake_direction

    if event.keysym == "Up" and snake_direction != "Down":
        snake_direction = "Up"
    elif event.keysym == "Down" and snake_direction != "Up":
        snake_direction = "Down"
    elif event.keysym == "Left" and snake_direction != "Right":
        snake_direction = "Left"
    elif event.keysym == "Right" and snake_direction != "Left":
        snake_direction = "Right"


# Move the snake
def move_snake():
    head_x, head_y = snake[0]
    if snake_direction == "Up":
        new_head = (head_x, head_y - DOT_SIZE)
    elif snake_direction == "Down":
        new_head = (head_x, head_y + DOT_SIZE)
    elif snake_direction == "Left":
        new_head = (head_x - DOT_SIZE, head_y)
    elif snake_direction == "Right":
        new_head = (head_x + DOT_SIZE, head_y)

    snake.insert(0, new_head)
    snake.pop()


# Check for collisions
def check_collision():
    global game_over

    head = snake[0]

    # Check for collision with the boundaries
    if (
        head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
    ):
        game_over = True

    # Check for collision with itself
    if head in snake[1:]:
        game_over = True

    # Check for collision with the food
    if head == food:
        snake.append(food)
        create_food()


# Create the food
def create_food():
    global food

    # Generate random coordinates for the food
    x = random.randint(0, (WIDTH - DOT_SIZE) / DOT_SIZE) * DOT_SIZE
    y = random.randint(0, (HEIGHT - DOT_SIZE) / DOT_SIZE) * DOT_SIZE

    food = (x, y)


# Update the score display
def update_score():
    global score
    score += SCORE_INCREMENT
    # score_label.config(text="Score: {}".format(score))


# Create the main window
window = tk.Tk()
window.title("Snake Game")

# Create the canvas
game_canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
game_canvas.pack
window.mainloop()