def setup():
    size(100, 100)
    noStroke()
    
def eye(x, y):
    fill(255)
    ellipse(x, y, 60, 60)
    fill(0)
    ellipse(x+10, y, 30, 30)
    fill(255)
    ellipse(x+16, y-5, 6, 6)
    
def draw():
    background(204)
    eye(65, 44)
    eye(20, 50)
    eye(65, 74)
    eye(20, 80)
    eye(65, 104)
    eye(20, 110)
