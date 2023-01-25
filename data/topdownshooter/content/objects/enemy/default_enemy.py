from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.ai.ai_component import AIComponent
from data.topdownshooter.content.ai.ai_wander import WanderAI
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy


class DefaultEnemy(ShooterEnemy):
    def __init__(self, man, pde, position=None, velocity=4, weapon=None):
        super().__init__(man, pde, position, velocity, weapon)

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        self.components["AI"] = AIComponent(owner=self)
        self.components["AI"].addstate(name="wander", state=WanderAI)
        self.components["AI"].state = "wander"

    def update(self):
        super().update()