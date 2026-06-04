define audio.bgm_DailyVibe = "audio/bgm/DailyVibe.ogg"
define audio.bgm_MysteryClue = "audio/bgm/MysteryClue.ogg"
define audio.bgm_TensionBuild = "audio/bgm/TensionBuild.ogg"

define audio.sfx_ButtonClick = "audio/sfx/ButtonClick.ogg"
define audio.sfx_ChandelierDrop = "audio/sfx/ChandelierDrop.ogg"
define audio.sfx_DoorCreak = "audio/sfx/DoorCreak.ogg"
define audio.sfx_FireExtinguishing = "audio/sfx/FireExtinguishing.ogg"
define audio.sfx_TypeWriter = "audio/sfx/TypeWriter.ogg"

# default dialogue_sfx_enabled = True

# init -10 python:

#     renpy.music.register_channel("dialogue_sfx", mixer="sfx", loop=False)

#     def typing_sfx_callback(event, interact=True, sfx=None, **kwargs):

#         if not interact:
#             return

#         if not dialogue_sfx_enabled:
#             return

#         if sfx is None:
#             return

#         # 글자가 화면에 출력되기 시작했을 때
#         if event == "show_done":
#             renpy.music.play(
#                 sfx,
#                 channel="dialogue_sfx",
#                 loop=True
#             )

#         # 글자 출력이 끝났을 때
#         elif event == "slow_done":
#             renpy.music.stop(
#                 channel="dialogue_sfx"
#             )

#         # 대사 종료 시 안전하게 종료
#         elif event == "end":
#             renpy.music.stop(
#                 channel="dialogue_sfx"
#             )

init -10 python:

    renpy.music.register_channel(
        "dialogue_sfx",
        mixer="sfx",
        loop=False
    )

    renpy.music.register_channel(
        "ui_sfx",
        mixer="sfx",
        loop=False
    )

    def typing_sfx_callback(event, interact=True, sfx=None, **kwargs):

        if not interact:
            return

        if not dialogue_sfx_enabled:
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
            renpy.music.stop(
                channel="dialogue_sfx"
            )

        elif event == "end":
            renpy.music.stop(
                channel="dialogue_sfx"
            )


    def stop_dialogue_sfx():

        renpy.music.stop(
            channel="dialogue_sfx"
        )


    def play_button_click_sfx():

        renpy.music.play(
            audio.sfx_ButtonClick,
            channel="ui_sfx",
            loop=False
        )


    def open_ui_sfx():

        renpy.music.stop(
            channel="dialogue_sfx"
        )

        renpy.music.play(
            audio.sfx_ButtonClick,
            channel="ui_sfx",
            loop=False
        )