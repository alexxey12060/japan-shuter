class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_scale_x, player_scale_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_scale_x, player_scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


