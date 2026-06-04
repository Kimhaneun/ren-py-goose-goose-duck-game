# =========================
# 탐정 노트 / 사전 / 인물 파일 시스템
# systems/note_file_system.rpy
# =========================


# =========================
# UI 상태
# =========================

default detective_note_tab = "clue"

# 인물 파일은 처음에 아무 인물도 선택하지 않은 상태.
# 인물 정보가 해금되면 unlock_character()에서 자동으로 선택됨.
default character_file_selected = None


# =========================
# 단서 획득 상태
# =========================

default unlocked_clues = []
default clue_acquired_order = {}
default clue_acquired_counter = 0


# =========================
# 단서 데이터
# icon     = 단서 목록에서 보이는 이미지
# evidence = 단서 상세에서 크게 보이는 이미지
# =========================

define CLUE_DATABASE = {
    "igature": {
        "id": "igature",
        "title": "삭흔",
        "icon": "igature",
        "evidence": "ev_igature",
        "desc": "모로의 목 주변에서 발견된 둥근 압박 자국. \n단순한 화상 자국과는 형태가 다르다.",
        "order": 10,
    },

    "ashes": {
        "id": "ashes",
        "title": "불탄 천 조각",
        "icon": "ashes",
        "evidence": "ev_ashes",
        "desc": "서재 화로 안에서 발견된 불탄 천 조각. \n일부러 태우려 한 흔적이 있으며, 강하게 비틀리거나 당겨진 듯한 자국이 남아 있다.",
        "order": 20,
    },

    "stab": {
        "id": "stab",
        "title": "복부 자상",
        "icon": "stab",
        "evidence": "ev_stab",
        "desc": "피해자의 복부에서 발견된 날카로운 자상. \n그을음에 가려져 있었지만, 날카로운 날붙이로 생긴 듯 하다.",
        "order": 30,
    },

    "cctv": {
        "id": "cctv",
        "title": "고장난 CCTV",
        "icon": "cctv",
        "evidence": "ev_cctv",
        "desc": "서재 입구에 설치된 CCTV. \n화재로 인해 장치가 손상되었다.",
        "order": 40,
    },

    "footprint": {
        "id": "footprint",
        "title": "와인이 묻은 발자국",
        "icon": "footprint",
        "evidence": "ev_footprint",
        "desc": "복도에 쏟아진 와인 위를 누군가 밟고 지나간 흔적. \n주변에 와인이 묻은 발자국이 찍혀있다.",
        "order": 50,
    },
}


# =========================
# 사전 데이터
# 처음부터 표시되는 내용
# =========================

define DICTIONARY_DATABASE = [
    {
        "title": "초능력자",
        "desc": "원격으로 벽 넘어의 거위를 조종할 수 있다. 능력 중에는 서로 움직일 수 없다. 조종 당한 인물은 후유증이 남는 것으로 파악된다.",
        "order": 10,
    },
    {
        "title": "변장술사",
        "desc": "다른 인물로 외형을 완벽하게 변장할 수 있다. 최대 10분 정도 유지되는 것으로 파악된다.",
        "order": 20,
    },
    {
        "title": "투명오리",
        "desc": "일정 시간 동안 외부 시야에서 자신의 모습을 감출 수 있는 이능 보유자. 다만 물리적 흔적까지 사라지는 것은 아니다.",
        "order": 30,
    },
]


# =========================
# 인물 파일 데이터
#
# icon               = 인물 파일에 표시할 캐릭터 아이콘 이미지
# tab_color          = 해금된 탭 기본 색
# tab_selected_color = 선택된 탭 색
#
# 탭에는 텍스트를 표시하지 않고 색상으로만 구분함.
# =========================

define CHARACTER_DATABASE = {
    "mina": {
        "id": "mina",
        "name": "미나",
        "age": "28",
        "gender": "여성",
        "hand": "오른손",
        "desc": "\"굿덕터\"의 여주인공을 맡았던 배우. \n말이 많고 사람들과 대화하는 것을 좋아한다. \n민감한 모습도 간간히 보인다.",
        "icon": "ic_mina",
        "tab_color": "#ff00ee",
        "tab_selected_color": "#ffffff",
        "order": 10,
    },

    "nio": {
        "id": "nio",
        "name": "니오",
        "age": "22",
        "gender": "여성",
        "hand": "오른손",
        "desc": "호기심이 많고 주변을 잘 살피는 인물. \n처음 보는 장소와 사람에게 쉽게 관심을 보인다. \n가벼워 보이지만 관찰한 것을 잘 기억한다.",
        "icon": "ic_nio",
        "tab_color": "#ffd900",
        "tab_selected_color": "#ffffff",
        "order": 20,
    },

    "sein": {
        "id": "sein",
        "name": "세인",
        "age": "46",
        "gender": "남성",
        "hand": "오른손",
        "desc": "감정 표현이 적고 말수가 적은 인물. \n어떤 상황에서도 크게 동요하지 않아 속내를 읽기 어렵다.",
        "icon": "ic_sein",
        "tab_color": "#000000",
        "tab_selected_color": "#ffffff",
        "order": 30,
    },

    "kato": {
        "id": "kato",
        "name": "카토",
        "age": "30",
        "gender": "남성",
        "hand": "왼손",
        "desc": "차분하고 묘한 분위기를 풍긴다. \n허공을 자주 보거나 누군가를 노려본다. \n농담인지 진심인지 알 수 없는 말을 자주 한다.",
        "icon": "ic_kato",
        "tab_color": "#0077ff",
        "tab_selected_color": "#ffffff",
        "order": 40,
    },

    "rui": {
        "id": "rui",
        "name": "루이",
        "age": "49",
        "gender": "남성",
        "hand": "왼손",
        "desc": "서로 충동하는 상황을 피하는 성격처럼 보인다. \n계산적이고 논리적인 모습을 보인다.",
        "icon": "ic_rui",
        "tab_color": "#bf00ff",
        "tab_selected_color": "#ffffff",
        "order": 50,
    },

    "ian": {
        "id": "ian",
        "name": "이안",
        "age": "33",
        "gender": "여성",
        "hand": "오른손",
        "desc": "주변을 경계하는 듯한 태도의 인물. \n말수가 적고 자신의 행적을 쉽게 드러내지 않는 듯하다.",
        "icon": "ic_ian",
        "tab_color": "#ff0000d2",
        "tab_selected_color": "#ffffff",
        "order": 60,
    },

    "moro": {
        "id": "moro",
        "name": "모로",
        "age": "55",
        "gender": "남성",
        "hand": "오른손",
        "desc": "비밀을 숨기고 있는 듯한 나이든 남성. \n자꾸 혼자 중얼거리면서 무언가를 찾는 듯하다. \n의문의 쪽지를 건냈다.",
        "icon": "ic_moro",
        "tab_color": "#00ff00",
        "tab_selected_color": "#ffffff",
        "order": 70,
    },

    "jun": {
        "id": "jun",
        "name": "준",
        "age": "52",
        "gender": "남성",
        "hand": "오른손",
        "desc": "청둥오리 저택의 집사. \n정중하고 침착하지만, 저택의 사정과 청둥오리의 부재에 대해 어딘가 숨기는 듯한 태도를 보인다.",
        "icon": "ic_jun",
        "tab_color": "#2c1313",
        "tab_selected_color": "#ffffff",
        "order": 80,
    },

}


# 처음에는 아무 인물 정보도 없음.
# 그래서 인물 파일을 열어도 탭과 내용이 표시되지 않음.
default unlocked_characters = []


default character_alive = {
    "mina": True,
    "nio": True,
    "sein": True,
    "kato": True,
    "rui": True,
    "ian": True,
    "moro": True,
    "jun": True,
}


# 진행 중 인물 정보 갱신용
default character_file_override = {}


# =========================
# 배치 좌표
# =========================

define NOTE_CLUE_SLOTS = [
    # 왼쪽 페이지
    (175, 120),
    (490, 120),
    (175, 380),
    (490, 380),
    (175, 640),
    (490, 640),

    # 오른쪽 페이지
    (955, 120),
    (1270, 120),
    (955, 380),
    (1270, 380),
    (955, 640),
    (1270, 640),
]

define DICTIONARY_SLOTS = [
    (180, 125),
    (180, 490),
    (960, 125),
    (960, 490),
]


# =========================
# 함수
# =========================

init python:

    def add_clue(clue_id, notify=True):
        global clue_acquired_counter

        if clue_id not in CLUE_DATABASE:
            raise Exception("존재하지 않는 clue_id입니다: {}".format(clue_id))

        if clue_id not in unlocked_clues:
            unlocked_clues.append(clue_id)

            clue_acquired_counter += 1
            clue_acquired_order[clue_id] = clue_acquired_counter

            renpy.restart_interaction()


    def get_unlocked_clues_sorted():
        result = []

        for clue_id in unlocked_clues:
            if clue_id in CLUE_DATABASE:
                result.append(dict(CLUE_DATABASE[clue_id]))

        result.sort(
            key=lambda item: (
                item.get("order", 9999),
                clue_acquired_order.get(item["id"], 9999)
            )
        )

        return result


    def get_dictionary_entries():
        result = list(DICTIONARY_DATABASE)
        result.sort(key=lambda item: item.get("order", 9999))
        return result


    def unlock_character(character_id, notify=True):
        """
        인물 정보 해금.
        이 함수가 호출되어야 인물 파일에 탭 버튼이 생김.
        """

        global character_file_selected

        if character_id not in CHARACTER_DATABASE:
            raise Exception("존재하지 않는 character_id입니다: {}".format(character_id))

        if character_id not in unlocked_characters:
            unlocked_characters.append(character_id)

            if character_file_selected is None:
                character_file_selected = character_id

            renpy.restart_interaction()


    def get_character_info(character_id):
        if character_id not in CHARACTER_DATABASE:
            return {
                "id": character_id,
                "name": "???",
                "age": "??",
                "gender": "미상",
                "hand": "미상",
                "desc": "정보 없음",
                "icon": None,
                "tab_color": "#f8f3df",
                "tab_selected_color": "#8f8f8f",
                "order": 9999,
            }

        data = dict(CHARACTER_DATABASE[character_id])

        if character_id in character_file_override:
            data.update(character_file_override[character_id])

        return data


    def update_character_info(
        character_id,
        name=None,
        age=None,
        gender=None,
        hand=None,
        desc=None,
        icon=None,
        profile_image=None,
        notify=True
    ):
        """
        인물 정보 갱신.
        아직 해금되지 않은 인물이면 자동으로 해금함.

        icon 또는 profile_image 둘 다 사용 가능.
        새 구조에서는 icon 사용을 권장.
        """

        if character_id not in CHARACTER_DATABASE:
            raise Exception("존재하지 않는 character_id입니다: {}".format(character_id))

        if character_id not in unlocked_characters:
            unlock_character(character_id, notify=False)

        if character_id not in character_file_override:
            character_file_override[character_id] = {}

        if name is not None:
            character_file_override[character_id]["name"] = name

        if age is not None:
            character_file_override[character_id]["age"] = age

        if gender is not None:
            character_file_override[character_id]["gender"] = gender

        if hand is not None:
            character_file_override[character_id]["hand"] = hand

        if desc is not None:
            character_file_override[character_id]["desc"] = desc

        if icon is not None:
            character_file_override[character_id]["icon"] = icon

        if profile_image is not None:
            character_file_override[character_id]["icon"] = profile_image

        if notify:
            renpy.notify("인물 파일 갱신: {}".format(get_character_info(character_id)["name"]))

        renpy.restart_interaction()


    def set_character_dead(character_id, notify=True):
        character_alive[character_id] = False

        if notify:
            renpy.notify("{} 사망".format(get_character_info(character_id)["name"]))

        renpy.restart_interaction()


    def set_character_alive(character_id, notify=True):
        character_alive[character_id] = True

        if notify:
            renpy.notify("{} 생존".format(get_character_info(character_id)["name"]))

        renpy.restart_interaction()


    def get_unlocked_characters_sorted():
        result = []

        for character_id in unlocked_characters:
            if character_id in CHARACTER_DATABASE:
                result.append(character_id)

        result.sort(
            key=lambda character_id: get_character_info(character_id).get("order", 9999)
        )

        return result


    def get_selected_character_id():
        """
        현재 선택된 인물이 유효하면 반환.
        아니면 해금된 첫 번째 인물을 반환.
        해금된 인물이 없으면 None.
        """

        global character_file_selected

        ids = get_unlocked_characters_sorted()

        if character_file_selected in ids:
            return character_file_selected

        if ids:
            character_file_selected = ids[0]
            return ids[0]

        return None