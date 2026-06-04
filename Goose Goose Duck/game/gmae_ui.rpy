# =========================
# 탐정 노트 / 사전 / 단서 상세 / 인물 파일 UI
# screens_custom/note_file_screens.rpy
# =========================


# =========================
# 노트 배경
# book은 반쪽 이미지라서
# 왼쪽 원본 + 오른쪽 플립으로 구성
# =========================

screen note_book_background():

    add "book":
        xpos 45
        ypos 35
        xysize (820, 895)
        fit "fill"

    add "book":
        xpos 865
        ypos 35
        xysize (820, 895)
        fit "fill"
        xzoom -1.0


# =========================
# 오른쪽 아래 기본 UI
# =========================

screen bottom_right_ui():

    zorder 10

    hbox:
        align (0.97, 0.95)
        spacing 45

        textbutton "{b}Z{/b} 탐정 노트":
            background None
            hover_background None
            text_size 28
            text_color "#ffffff"
            text_hover_color "#333333"
            action [
                Function(open_ui_sfx),
                SetVariable("detective_note_tab", "clue"),
                Show("detective_note_screen")
            ]

        textbutton "{b}X{/b} 인물 파일":
            background None
            hover_background None
            text_size 28
            text_color "#ffffff"
            text_hover_color "#333333"
            action [
                Function(open_ui_sfx),
                Show("character_file_screen")
            ]

        textbutton "{b}M{/b} 지도":
            background None
            hover_background None
            text_size 28
            text_color "#ffffff"
            text_hover_color "#333333"
            action [
                Function(open_ui_sfx),
                Show("map_screen")
            ]

    key "K_z" action [
        Function(open_ui_sfx),
        SetVariable("detective_note_tab", "clue"),
        Show("detective_note_screen")
    ]

    key "K_x" action [
        Function(open_ui_sfx),
        Show("character_file_screen")
    ]

    key "K_m" action [
        Function(open_ui_sfx),
        Show("map_screen")
    ]


# =========================
# 탐정 노트
# clue = 단서 목록
# dictionary = 사전
# =========================

screen detective_note_screen():

    zorder 30
    modal True

    key "K_ESCAPE" action Hide("detective_note_screen")

    add Solid("#00000077")

    if detective_note_tab == "clue":

        key "K_z" action [
            Function(play_button_click_sfx),
            SetVariable("detective_note_tab", "dictionary")
        ]

    else:

        key "K_z" action [
            Function(play_button_click_sfx),
            SetVariable("detective_note_tab", "clue")
        ]

    use note_book_background

    if detective_note_tab == "clue":

        $ clue_items = get_unlocked_clues_sorted()

        # 단서가 없으면 아무것도 표시하지 않음.
        # 빈 노트만 보임.
        for i, clue in enumerate(clue_items):

            if i < len(NOTE_CLUE_SLOTS):

                $ slot_x, slot_y = NOTE_CLUE_SLOTS[i]

                button:
                    xpos slot_x
                    ypos slot_y
                    xysize (296, 222)
                    background Solid("#ffffff")
                    hover_background Solid("#eeeeee")
                    padding (4, 4)
                    action Show("clue_detail_screen", clue_id=clue["id"])

                    add clue["icon"]:
                        xysize (288, 214)
                        fit "cover"


        textbutton "사전 Z":
            xpos 1450
            ypos 985
            background None
            hover_background None
            text_size 38
            text_color "#ffffff"
            text_hover_color "#333333"
            action SetVariable("detective_note_tab", "dictionary")


    elif detective_note_tab == "dictionary":

        $ dictionary_items = get_dictionary_entries()

        for i, item in enumerate(dictionary_items):

            if i < len(DICTIONARY_SLOTS):

                $ slot_x, slot_y = DICTIONARY_SLOTS[i]

                vbox:
                    xpos slot_x
                    ypos slot_y
                    spacing 12

                    text item["title"]:
                        size 38
                        color "#000000"
                        bold True

                    text item["desc"]:
                        xsize 560
                        size 34
                        color "#000000"
                        line_spacing 8


        textbutton "단서 X":
            xpos 1450
            ypos 985
            background None
            hover_background None
            text_size 38
            text_color "#ffffff"
            text_hover_color "#333333"
            action SetVariable("detective_note_tab", "clue")


    textbutton "닫기 ESC":
        xpos 1620
        ypos 985
        background None
        hover_background None
        text_size 38
        text_color "#ffffff"
        text_hover_color "#333333"
        action Hide("detective_note_screen")


# =========================
# 단서 상세 화면
# ESC로만 닫힘
# =========================

screen clue_detail_screen(clue_id):

    zorder 40
    modal True

    key "K_ESCAPE" action Hide("clue_detail_screen")

    $ clue = CLUE_DATABASE[clue_id]

    # 뒤 배경 어둡게 처리
    add Solid("#00000077")

    # 상세 이미지
    add clue["evidence"]:
        align (0.5, 0.35)

    # 상세 설명
    text clue["desc"]:
        xpos 600
        ypos 815
        xsize 820
        size 38
        color "#000000"
        line_spacing 30


# =========================
# 인물 파일 UI
#
# 정보가 없으면 탭과 내용이 표시되지 않음.
# 인물 정보가 해금되면 색상 탭 버튼이 생김.
# 탭 버튼에는 텍스트를 표시하지 않음.
# =========================

screen character_file_screen():

    zorder 250
    modal True

    key "K_ESCAPE" action Hide("character_file_screen")

    add Solid("#00000099")

    $ character_tabs = get_unlocked_characters_sorted()
    $ selected_id = get_selected_character_id()


    # =========================
    # 상단 탭
    # 해금된 인물만 표시
    # 텍스트 없음
    # =========================

    hbox:
        xpos 500
        ypos 70
        spacing 18

        for character_id in character_tabs:

            $ info = get_character_info(character_id)
            $ is_dead = not character_alive.get(character_id, True)
            $ is_selected = selected_id == character_id

            $ normal_color = info.get("tab_color", "#f8f3df")
            $ selected_color = info.get("tab_selected_color", "#8f8f8f")

            $ tab_bg = "#000000" if is_dead else (selected_color if is_selected else normal_color)
            $ tab_hover_bg = "#222222" if is_dead else selected_color

            button:
                xysize (100, 90)
                background Solid(tab_bg)
                hover_background Solid(tab_hover_bg)
                action SetVariable("character_file_selected", character_id)

                # 보이는 텍스트 없음.
                text ""


    # =========================
    # 본문 패널
    # 인물 정보가 없으면 빈 패널만 표시
    # =========================

    frame:
        align (0.5, 0.55)
        xysize (1100, 800)
        background Solid("#dddddd")
        padding (0, 0)

        fixed:

            if selected_id is not None:

                $ selected = get_character_info(selected_id)
                $ selected_dead = not character_alive.get(selected_id, True)

                # 캐릭터 아이콘 이미지
                if selected.get("icon", None):

                    add selected["icon"]:
                        xpos 140
                        ypos 120
                        xysize (360, 260)
                        fit "contain"

                else:

                    add Solid("#5a5a5a" if selected_dead else "#ffe47e"):
                        xpos 140
                        ypos 120
                        xysize (360, 260)


                vbox:
                    xpos 560
                    ypos 125
                    spacing 35

                    text "[selected['name']]([selected['age']])":
                        size 30
                        color "#000000"

                    text "성별 : [selected['gender']]":
                        size 30
                        color "#000000"

                    text "주 사용 손 : [selected['hand']]":
                        size 30
                        color "#000000"


                text selected["desc"]:
                    xpos 180
                    ypos 470
                    xsize 720
                    size 27
                    color "#000000"
                    line_spacing 4


            textbutton "닫기":
                xpos 950
                ypos 715
                background None
                hover_background None
                text_size 28
                text_color "#000000"
                text_hover_color "#555555"
                action Hide("character_file_screen")

screen map_screen():

    zorder 30
    modal True

    key "K_ESCAPE" action Hide("map_screen")

    add Solid("#00000077")

    textbutton "닫기 ESC":
        xpos 1620
        ypos 985
        background None
        hover_background None
        text_size 38
        text_color "#ffffff"
        text_hover_color "#333333"
        action Hide("map_screen")

    add "map":
        xysize (1100, 800)
        align (0.5, 0.35)

# =========================
# 추리력 UI
# screens_custom/reasoning_screens.rpy
# =========================

screen reasoning_gauge():

    zorder 120

    frame:
        xpos 1500
        ypos 60
        background Solid("#00000099")
        padding (20, 14)

        hbox:
            spacing 12

            text "추리력":
                size 28
                color "#ffffff"

            for i in range(reasoning_max):

                if i < reasoning_hp:
                    add Solid("#ffcc33"):
                        xysize (34, 34)
                else:
                    add Solid("#555555"):
                        xysize (34, 34)