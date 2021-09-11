import GlobalVariables


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = GlobalVariables.PG_LIB.mask.from_surface(self.img)

    def draw(self, window):  # створення лазеру
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):   # рух лазеру
        self.y += vel

    def off_screen(self, height):   # вихід лазеру за рамки
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):       # дотикання до лазеру
        return collide(self, obj)


def collide(obj1, obj2):        # чи дотикнулись об'єкти
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, int(offset_y))) is not None



