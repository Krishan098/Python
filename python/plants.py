import pygame
import math
# Plan to add more planets later onwards

pygame.init()

WIDTH, HEIGHT = 1350, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 237)
RED = (190, 0, 0)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("bradley hand itc", 18)

class Planet:
    AU = 149.6e6 * 1000 # AU is one Astronomical Unit, aka, the distance between earth and sun
    G = 6.67428e-11 # Gravitational constant
    SCALE = 200 / AU    # 1 AU = 100 pixels
    TIMESTEP = (60*60) * 24 # 1 day in seconds

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False
        self.distancetosun = 0
        # This list stores all the points your planet has passed through so that we can create an orbit

        self.x_velocity = 0
        self.y_velocity = 0
        # Add this with planets instead
        # self.total_velocity = math.sqrt(self.x_velocity ** 2 + self.y_velocity ** 2)


    def draw(self, win):
        # The last expression in the given formulas makes it so that the planets are drawn in the middle of window
        # This is done by dividing the width and height of the window by 2
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        if len(self.orbit) >= 3:
            updated_points = []
            # Adds points which are properly scaled down to the screen size
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
        
            pygame.draw.lines(win, self.color, False, updated_points, 2)
            # The False argument above makes it so that the line drawn between any two points is not enclosed.
            # 2 is the thickness of line
        
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if self.sun:
            text = FONT.render(f"Sun", 2, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2 ))

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distancetosun / 1000, 1)} km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2 ))
    

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distancetosun = distance
        
        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y


    def update_position(self, planets):
        total_forcex = total_forcey = 0
        for planet in planets:
            if self == planet:
                continue
            
            forcex, forcey = self.attraction(planet)
            total_forcex += forcex
            total_forcey += forcey
        
        self.x_velocity += total_forcex / self.mass * self.TIMESTEP
        self.y_velocity += total_forcey / self.mass * self.TIMESTEP

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        self.orbit.append((self.x, self.y))



def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.9882 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    earth.y_velocity = 29.783 * 1000 # in kilometres

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
    mars.y_velocity = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10 ** 23)
    mercury.y_velocity = -47.4 * 1000     # Negative velocity here indicates the opposite direction

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)
    venus.y_velocity = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WINDOW.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WINDOW)
        
        pygame.display.update()

    pygame.quit()
print("print("")")

main()