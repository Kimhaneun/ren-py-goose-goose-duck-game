default active_characters = {}
default current_speaker_tag = None


transform char_flip(is_flip=False):
    xzoom (-1.0 if is_flip else 1.0)


init -9 python:

    def get_char_focus_transform(tag):
        """
        현재 화자 상태에 따라 적용할 transform 반환.
        아직 화자가 없으면 전부 밝게 표시.
        """

        if current_speaker_tag is None:
            return char_speaker

        if tag == current_speaker_tag:
            return char_speaker

        return char_nonspeaker


    def show_char(tag, pos="center", flip=False):
        """
        캐릭터 표시.
        expression 없이 tag만 사용한다.

        예:
            $ show_char("jin", "left")
            $ show_char("jin", "left", flip=True)
        """

        image_name = tag

        active_characters[tag] = {
            "image": image_name,
            "pos": pos,
            "flip": flip,
        }

        renpy.show(
            image_name,
            at_list=[
                char_pos(pos),
                char_flip(flip),
                get_char_focus_transform(tag)
            ]
        )


    def change_char(tag, pos=None, flip=None):
        """
        캐릭터 위치 / 좌우반전 변경.

        예:
            $ change_char("jin", pos="right")
            $ change_char("jin", flip=True)
            $ change_char("jin", pos="right", flip=True)
        """

        if tag not in active_characters:
            return

        old_data = active_characters[tag]

        image_name = old_data["image"]

        if pos is None:
            pos = old_data["pos"]

        if flip is None:
            flip = old_data.get("flip", False)

        active_characters[tag] = {
            "image": image_name,
            "pos": pos,
            "flip": flip,
        }

        renpy.show(
            image_name,
            at_list=[
                char_pos(pos),
                char_flip(flip),
                get_char_focus_transform(tag)
            ]
        )


    def flip_char(tag, flip=True):
        """
        캐릭터 좌우반전만 변경.

        예:
            $ flip_char("jin", True)
            $ flip_char("jin", False)
        """

        if tag not in active_characters:
            return

        change_char(tag, flip=flip)


    def hide_char(tag):
        """
        캐릭터 숨김.
        """

        if tag in active_characters:
            del active_characters[tag]

        renpy.hide(tag)


    def clear_chars():
        """
        장면 전환 후 캐릭터 상태 초기화.
        """

        global current_speaker_tag

        active_characters.clear()
        current_speaker_tag = None


    def focus_speaker(speaker_tag):
        """
        화자만 밝게, 나머지는 어둡게.
        """

        global current_speaker_tag

        # 현재 화면에 없는 캐릭터가 말하면 아무도 어둡게 하지 않음.
        if speaker_tag not in active_characters:
            current_speaker_tag = None
            return

        current_speaker_tag = speaker_tag

        for tag, data in active_characters.items():

            renpy.show(
                data["image"],
                at_list=[
                    char_pos(data["pos"]),
                    char_flip(data.get("flip", False)),
                    get_char_focus_transform(tag)
                ]
            )


    def stop_dialogue_sfx():
        renpy.music.stop(channel="dialogue_sfx")


    def dialogue_callback(event, interact=True, speaker_tag=None, sfx=None, **kwargs):
        """
        Character callback.

        1. 대사 시작 시 speaker_tag 캐릭터를 강조
        2. 글자 출력 중 TypeWriter SFX 반복 재생
        3. 글자 출력 종료/대사 종료 시 SFX 정지
        """

        if not interact:
            return

        # 대사 시작 시 화자 강조
        if event == "begin":

            if speaker_tag is not None:
                focus_speaker(speaker_tag)


        # 대사 타이핑 효과음
        if not dialogue_callback:
            return

        if sfx is None:
            return

        if event == "show_done":

            renpy.music.play(
                sfx,
                channel="dialogue_sfx",
                loop=True
            )

        elif event == "slow_done":

            stop_dialogue_sfx()

        elif event == "end":

            stop_dialogue_sfx()