default reasoning_max = 5
default reasoning_hp = 5


init python:

    def reset_reasoning(value=None):
        global reasoning_max
        global reasoning_hp

        if value is not None:
            reasoning_max = value

        reasoning_hp = reasoning_max
        renpy.restart_interaction()


    def damage_reasoning(amount=1, notify=True):
        global reasoning_hp

        reasoning_hp -= amount

        if reasoning_hp < 0:
            reasoning_hp = 0

        if notify:
            renpy.notify("추리력 감소")

        renpy.restart_interaction()

        return reasoning_hp


    def heal_reasoning(amount=1, notify=True):
        global reasoning_hp

        reasoning_hp += amount

        if reasoning_hp > reasoning_max:
            reasoning_hp = reasoning_max

        if notify:
            renpy.notify("추리력 회복")

        renpy.restart_interaction()

        return reasoning_hp