import pgzrun
import random


WIDTH = 800
HEIGHT = 600
TITLE = "Pygame Zero Pong"

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5


BALL_RADIUS = 10
BALL_SPEED = 5


player1_score = 0
player2_score = 0
game_over = False


player1_paddle = Rect((50, HEIGHT / 2 - PADDLE_HEIGHT / 2), (PADDLE_WIDTH, PADDLE_HEIGHT))
player2_paddle = Rect((WIDTH - 50 - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2), (PADDLE_WIDTH, PADDLE_HEIGHT))


ball = Rect((WIDTH / 2 - BALL_RADIUS, HEIGHT / 2 - BALL_RADIUS), (BALL_RADIUS * 2, BALL_RADIUS * 2))
ball_dx = BALL_SPEED * random.choice([-1, 1])  # Initial horizontal direction
ball_dy = BALL_SPEED * random.choice([-1, 1])  # Initial vertical direction

# Function to initialize or reset the ball's position and direction
def init_ball():
    global ball_dx, ball_dy
    ball.center = (WIDTH / 2, HEIGHT / 2)
    ball_dx = BALL_SPEED * random.choice([-1, 1])
    ball_dy = BALL_SPEED * random.choice([-1, 1])


def draw():
    screen.fill((0, 0, 0))  # Black background
    screen.draw.filled_rect(player1_paddle, BLUE)  # Draw player 1's paddle
    screen.draw.filled_rect(player2_paddle, RED)  # Draw player 2's paddle
    screen.draw.filled_circle(ball.center, BALL_RADIUS, WHITE)  # Draw the ball


    screen.draw.text(str(player1_score), center=(WIDTH / 4, 50), color=WHITE, fontsize=60)
    screen.draw.text(str(player2_score), center=(WIDTH * 3 / 4, 50), color=WHITE, fontsize=60)


    if game_over:
        screen.draw.text("Game Over!", center=(WIDTH / 2, HEIGHT / 2), color=WHITE, fontsize=80)


def update():
    global ball_dx, ball_dy, player1_score, player2_score, game_over

    if game_over:
        return


    if keyboard.w and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keyboard.s and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += PADDLE_SPEED


    if keyboard.up and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keyboard.down and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += PADDLE_SPEED


    ball.x += ball_dx
    ball.y += ball_dy


    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_dy *= -1


    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_dx *= -1


    if ball.left < 0:
        player2_score += 1
        init_ball()
        if player2_score >= 3:
            game_over = True
    elif ball.right > WIDTH:
        player1_score += 1
        init_ball()
        if player1_score >= 3:
            game_over = True


init_ball()
pgzrun.go()
