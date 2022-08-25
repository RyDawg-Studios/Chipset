from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity


class Dummy(ShooterEntity):
    def __init__(self, man, pde, position=..., maxhp=100):
        scale = [32, 48]
        super().__init__(man, pde, position, scale, maxhp)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\objects\dummy\dummy.png',layer=2)

    def die(self, killer):
        self.hp = 100

    def takedamage(self, obj, dmg):
        print(f"Object {str(self.__class__.__name__)} Took {dmg} From {obj.__class__.__name__} By {obj.owner.owner.__class__.__name__}")
        return super().takedamage(obj, dmg)

    def update(self):
        return super().update()
