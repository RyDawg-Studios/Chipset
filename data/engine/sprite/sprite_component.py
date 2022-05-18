import pygame
from pygame.sprite import AbstractGroup
from data.engine.component.component import Component


class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, sprite, rotation, scale, layer: AbstractGroup) -> None:
        super().__init__()
        self.parent = parent
        self.layer = layer
        self.sprite = sprite
        self.scale = scale
        self.rotation = rotation

        #Use sprite from cache if already loaded, otherwise load it and add it to cache
        if self.sprite in self.parent.pde.sprite_manager.sprites:
            self.image = self.parent.pde.sprite_manager.sprites[self.sprite]
        else:
            try: 
                self.image = pygame.image.load(self.sprite).convert_alpha()
            except FileNotFoundError:
                self.image = pygame.image.load(r'data\assets\sprites\undef.png').convert_alpha()
            self.parent.pde.sprite_manager.sprites[self.sprite] = self.image


        self.ogimage = self.image

        self.rect = self.ogimage.get_rect()
 
        #add sprite to sprite layer
        parent.pde.display_manager.group.add(self)


    def updatetransform(self):
        img = pygame.transform.scale(self.ogimage, self.scale)
        img = pygame.transform.rotate(img, self.rotation)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = self.parent.rect.center

    def update(self):
        self.updatetransform()
        super().update()

    
    def deconstruct(self):
        self.kill()
        del self




class SpriteComponent(Component):
    def __init__(self, owner, sprite, layer=0, **kwargs) -> None:
        super().__init__(owner, **kwargs)

        self.path = sprite

        if self.owner.useSpriteRectForCollision:
            self.owner.rect = self.sprite.image.get_rect()

        self.sprite = Sprite(parent=owner, sprite=sprite, layer=layer, rotation=self.owner.rotation, scale=self.owner.scale)

    def update(self):
        self.sprite.update()

    def deconstruct(self):
        print(f'Sprite {self} - Owner {self.owner}')
        self.sprite.deconstruct()
        super().deconstruct()
