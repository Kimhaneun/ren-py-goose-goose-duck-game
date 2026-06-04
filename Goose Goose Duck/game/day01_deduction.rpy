# =========================
# 1일차 추리 파트
# story/day01/day01_deduction.rpy
# =========================


# =========================
# 추리 파트용 증거 이미지 연출
# 이미지를 보여주고, 입력이 들어오면 천천히 사라짐
# =========================

label day01_deduction_tg_igature:

    window hide dissolve_fast

    show igature at truecenter
    with dissolve_normal

    pause

    hide igature
    with dissolve_slow

    window show dissolve_fast

    return


label day01_deduction_tg_ashes:

    window hide dissolve_fast

    show ashes at truecenter
    with dissolve_normal

    pause

    hide ashes
    with dissolve_slow

    window show dissolve_fast

    return


label day01_deduction_tg_stab:

    window hide dissolve_fast

    show stab at truecenter
    with dissolve_normal

    pause

    hide stab
    with dissolve_slow

    window show dissolve_fast

    return


label day01_deduction_tg_cctv:

    window hide dissolve_fast

    show cctv at truecenter
    with dissolve_normal

    pause

    hide cctv
    with dissolve_slow

    window show dissolve_fast

    return

label day01_deduction_tg_cctv_screen:

    window hide dissolve_fast

    show cctv_screen at truecenter
    with dissolve_normal

    pause

    hide cctv_screen
    with dissolve_slow

    window show dissolve_fast

    return


label day01_deduction_tg_footprint:

    window hide dissolve_fast

    show footprint at truecenter
    with dissolve_normal

    pause

    hide footprint
    with dissolve_slow

    window show dissolve_fast

    return


# =========================
# 오답 공통 처리
# =========================

label day01_deduction_wrong(amount=1):

    $ damage_reasoning(amount)

    with hpunch

    if reasoning_hp <= 0:
        jump day01_deduction_failed

    return


label day01_deduction_failed:

    hide screen reasoning_gauge

    stop music fadeout 1.0

    $ clear_chars()

    window hide dissolve_normal

    # 게임오버 화면으로 페이드 인
    scene bg over
    with fade_scene

    # 몇 초간 게임오버 화면 유지
    pause 2.0

    # 다시 검은 화면으로 페이드
    scene black
    with fade_scene

    # 검은 화면 위에 선택지 표시
    menu:
        "추리 파트를 다시 시작한다.":
            jump day01_deduction_start

        "사건 수사로 돌아간다.":
            jump day01_tg_igature


# =========================
# 추리 파트 시작
# 식당 재집합
# =========================

label day01_deduction_start:

    $ reset_reasoning(5)
    show screen reasoning_gauge

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg dining room
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)

    window show dissolve_normal

    "모두가 다시 식당에 모였다."

    "방금 전까지 만찬이 준비되어 있던 식탁은,"

    "이제 전혀 다른 의미의 장소가 되어 있었다."

    mina "대체 이게 무슨 일이에요..."

    $ hide_char("mina")
    $ show_char("nia", "right", flip=True)

    nia "모로 씨가 정말 죽은 거예요?"

    jin "네."

    $ hide_char("nia")
    $ show_char("jun", "right", flip=True)

    jun "모로 님의 죽음이 정말 사고가 아니라는 겁니까?"

    jin "모로 씨는 화재 때문에 죽은 것이 아닙니다."

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "그럼... 누가 죽였다는 거예요?"

    jin "그걸 지금부터 확인하겠습니다."

    jin "그 전에, 준 씨."

    $ hide_char("mina")
    $ show_char("jun", "right", flip=True)

    jun "예."

    jin "서재 입구의 CCTV 기록을 확인해야 합니다."

    jin "화재 때문에 카메라가 고장난 것처럼 보였지만, 기록 장치에 일부 영상이 남아 있을 수도 있습니다."

    jun "관리실에 기록 장치가 있습니다."

    jun "다만, 화재로 회선이 손상됐다면 영상이 온전하지 않을 가능성이 큽니다."

    jin "일부라도 괜찮습니다."

    jin "그 안에 누가 서재에 드나들었는지 찍혀 있을지도 모릅니다."

    jun "알겠습니다. 바로 확인해 보겠습니다."

    "준은 짧게 고개를 숙인 뒤 식당을 나섰다."

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "식당 문이 닫히자, 남은 사람들 사이에 무거운 침묵이 내려앉았다."

    jin "준 씨가 기록을 확인하는 동안, 우리는 우리가 아는 사실부터 정리하겠습니다."

    jin "모로 씨가 어떻게 죽었는지부터요."

    jump day01_deduction_cause_question


# =========================
# 첫 번째 논점: 사인
# =========================

label day01_deduction_cause_question:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("rui", "right", flip=True)
    with dissolve_normal

    rui "먼저 분명히 해야 할 게 있습니다."

    rui "모로 씨의 사인은 무엇입니까?"

    menu:
        "흉기에 찔린 자상이다.":
            jump day01_deduction_cause_right

        "화재로 인한 질식사다.":
            jump day01_deduction_cause_wrong


label day01_deduction_cause_wrong:

    call day01_deduction_wrong(1) from _call_day01_deduction_wrong

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("sein", "right", flip=True)

    sein "흠... 아닌 것 같습니다."

    sein "그렇다기엔 탐정님이 가지고 있는 단서들을 설명할 수 없는 걸요."

    jump day01_deduction_cause_question


label day01_deduction_cause_right:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "모로 씨의 직접적인 사인은 흉기에 찔린 자상입니다."

    call day01_deduction_tg_stab from _call_day01_deduction_tg_stab

    $ show_char("mina", "right", flip=True)

    mina "찔렸다고요?"

    jin "네."

    jin "그을음 때문에 처음엔 잘 보이지 않았지만, 옷 안쪽에 자상이 있었습니다."

    $ hide_char("mina")
    $ show_char("nia", "right", flip=True)

    nia "그럼 불에 타 죽은 게 아니라..."

    jin "누군가 먼저 그를 공격했고, 이후 불을 낸 겁니다."

    call day01_deduction_tg_igature from _call_day01_deduction_tg_igature

    $ hide_char("nia")
    $ show_char("sein", "right", flip=True)

    sein "다른 흔적도 있었나요?"

    jin "목에 졸린 듯한 흔적이 있었습니다. 그건 사망 전 모로 씨를 제압하기 위한 흔적입니다."

    $ hide_char("sein")
    $ show_char("kato", "right", flip=True)

    kato "먼저 숨을 막고, 그 다음 찔렀군요."

    jin "그렇게 보는 게 자연스럽습니다."

    jump day01_deduction_weapon_question


# =========================
# 두 번째 논점: 흉기 / 제압 방식
# =========================

label day01_deduction_weapon_question:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("nia", "right", flip=True)
    with dissolve_normal

    nia "잠깐만요."

    nia "그럼 범인은 뭘로 모로 씨를 죽인 거예요?"

    menu:
        "화로의 불길로 죽였다.":
            jump day01_deduction_weapon_wrong

        "천으로 제압한 뒤, 서재의 날붙이로 찔렀다.":
            jump day01_deduction_weapon_right


label day01_deduction_weapon_wrong:

    call day01_deduction_wrong(1) from _call_day01_deduction_wrong_1

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)

    mina "흠... 아닌 거 같은데요?"

    mina "진 씨가 아까 불에 타 죽은 건 아니라고 했잖아요."

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "화재는 사망 이후에 일어난 일로 보는 게 맞습니다."

    jump day01_deduction_weapon_question


label day01_deduction_weapon_right:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "범인은 먼저 천으로 모로 씨의 목을 졸라 제압했습니다."

    jin "화로에서 발견된 불탄 천 조각입니다."

    call day01_deduction_tg_ashes from _call_day01_deduction_tg_ashes

    jin "천 조각에는 강하게 비틀리고 당겨진 흔적이 남아 있었습니다."

    jin "목의 압박 흔적과도 맞습니다."

    $ show_char("sein", "right", flip=True)

    sein "그럼 찌른 흉기는요?"

    jin "부엌에 있던 날붙이일 가능성이 큽니다."

    $ hide_char("sein")
    $ show_char("rui", "right", flip=True)

    rui "그렇다면 요리용 칼이겠군요."

    jin "네. 범인은 모로 씨를 기절시키거나 움직이지 못하게 한 뒤, 찔러 죽였습니다."

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "그럼 대체 누가 그런 짓을..."

    jin "그걸 밝히기 위해 필요한 게 하나 있습니다."

    "그 순간 집사가 사진을 들고 식당으로 들어왔다."

    jump day01_deduction_cctv_recovery


# =========================
# CCTV 복구
# =========================

label day01_deduction_cctv_recovery:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("jun", "right", flip=True)
    with dissolve_normal

    jin "준 씨, CCTV는 어떻게 됐습니까?"

    jun "기록 장치에 일부 사진이 남아 있었습니다."

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "정말요?"

    $ hide_char("mina")
    $ show_char("jun", "right", flip=True)

    jun "다만 화재 영향으로 아주 찰나의 순간만 포착되었습니다."

    "준은 식탁 위에 복구한 사진을 내려놓았다."

    call day01_deduction_tg_cctv_screen from _call_day01_deduction_tg_cctv_screen

    "사진에는 서재 안쪽이 흐릿하게 찍혀 있었다."

    "쓰러진 모로."

    "그리고 그 앞에 선 인물."

    "그 인물은 오른손에 날붙이를 들고 있었다."

    "그 얼굴은—"

    "루이였다."

    $ add_clue("cctv_screen")

    ##

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "루이 씨...?"

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "아니요. 제가 아닙니다."

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "하지만 사진에는 루이 씨가..."

    $ hide_char("nia")
    $ show_char("sein", "right", flip=True)

    sein "사진만 보면 그렇게 보입니다."

    $ hide_char("sein")
    $ show_char("rui", "right", flip=True)

    rui "전 모로 씨를 찌른 적 없습니다."

    $ hide_char("rui")
    $ show_char("kato", "right", flip=True)

    kato "카메라는 거짓말을 하지 않는다고들 하죠."

    jin "하지만 카메라가 본 것이 언제나 진실이라는 뜻은 아닙니다."

    $ hide_char("kato")
    $ show_char("mina", "right", flip=True)

    mina "그게 무슨 말이에요?"

    jin "아직 단정하지 말자는 뜻입니다."

    $ hide_char("mina")
    $ show_char("jun", "right", flip=True)

    jun "사진 속 인물이 루이 님처럼 보이는 건 사실입니다."

    $ hide_char("jun")
    $ show_char("rui", "right", flip=True)

    rui "저는 억울합니다!!!"

    jin "루이 씨."

    rui "네?"

    jin "그 시간에 어디 있었습니까?"

    rui "그 시간이라면, 화재난 순간인가요? 전 그때 화장실에.."

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "알리바이를 증명해 줄 사람은 없다는 거군요."

    $ hide_char("mina")
    $ show_char("nia", "right", flip=True)

    nia "뭐야.. 진짜 루이씨가 범인?"

    jin "그걸 지금부터 확인해야 합니다."

    jump day01_deduction_disguise_question


# =========================
# 세 번째 논점: 사진을 설명할 변수
# =========================

label day01_deduction_disguise_question:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("jun", "right", flip=True)
    with dissolve_normal

    jun "그렇다면 이 사진을 설명할 다른 변수는 무엇입니까?"

    menu:
        "누군가 루이의 모습으로 변장했다.":
            jump day01_deduction_disguise_right

        "카메라가 완전히 잘못된 장면을 찍었다.":
            jump day01_deduction_disguise_wrong


label day01_deduction_disguise_wrong:

    call day01_deduction_wrong(1) from _call_day01_deduction_wrong_2

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("jun", "right", flip=True)

    jun "흠... 아닌 것 같습니다."

    jun "영상이 손상되긴 했지만, 존재하지 않는 사람을 만들어낼 정도는 아닙니다."

    $ hide_char("jun")
    $ show_char("sein", "right", flip=True)

    sein "사진 속 인물이 있었다는 사실 자체는 받아들여야 합니다."

    jump day01_deduction_disguise_question


label day01_deduction_disguise_right:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "누군가 루이 씨의 모습으로 변장한 겁니다."

    $ show_char("mina", "right", flip=True)

    mina "변장이라니..."

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "이 마을에선 불가능한 이야기가 아니죠."

    $ hide_char("sein")
    $ show_char("kato", "right", flip=True)

    kato "오리가 있다는 말씀이군요."

    $ hide_char("kato")
    $ show_char("rui", "right", flip=True)

    rui "그럼 저 사진 속 인물은 제가 아니라..."

    jin "루이 씨의 모습을 한 누군가입니다."

    $ hide_char("rui")
    $ show_char("jun", "right", flip=True)

    jun "변장술사."

    "식당 안이 술렁였다."

    $ hide_char("jun")
    $ show_char("nia", "right", flip=True)

    nia "잠깐만요. 그럼 우리 중에 변장술사가 있다는 거예요?"

    $ hide_char("nia")
    $ show_char("sein", "right", flip=True)

    sein "가능성은 생겼습니다."

    $ hide_char("sein")
    $ show_char("rui", "right", flip=True)

    rui "하지만 가능성만으로는 부족합니다."

    jin "맞습니다."

    jin "사진 속 인물이 루이 씨처럼 보인다는 것만으로는 부족하고,"

    jin "그게 진짜 루이 씨가 아니라는 근거도 필요합니다."

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "그걸 어떻게 밝혀요?"

    jin "그래서 다음 질문으로 가야 합니다."

    jump day01_deduction_fire_purpose_intro


# =========================
# 네 번째 논점: 화재의 목적
# =========================

label day01_deduction_fire_purpose_intro:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "변장술사가 루이 씨의 모습으로 CCTV에 찍혔다고 가정합시다."

    $ show_char("mina", "right", flip=True)

    mina "그럼 루이 씨한테 누명을 씌우려고 한 거겠죠."

    jin "그렇다면 이상한 점이 있습니다."

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "불을 낸 이유군요."

    jin "네."

    jin "범인의 목적이 루이 씨에게 누명을 씌우는 것이라면, CCTV에 찍힌 것만으로 충분했습니다."

    jin "그런데 범인은 굳이 서재에 불을 냈습니다."

    $ hide_char("rui")
    $ show_char("sein", "right", flip=True)

    sein "왜 그랬을까요."

    jump day01_deduction_fire_reason_question


label day01_deduction_fire_reason_question:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("sein", "right", flip=True)
    with dissolve_normal

    sein "변장술사 입장에서, 굳이 화재를 낸 이유는 무엇입니까?"

    menu:
        "CCTV에 찍힌 장면의 문제점을 숨기기 위해서다.":
            jump day01_deduction_fire_reason_right

        "시신을 완전히 없애기 위해서다.":
            jump day01_deduction_fire_reason_wrong


label day01_deduction_fire_reason_wrong:

    call day01_deduction_wrong(1) from _call_day01_deduction_wrong_3

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("kato", "right", flip=True)

    kato "흠... 아닌 것 같습니다."

    kato "불길은 시신을 없애기엔 부족했습니다."

    $ hide_char("kato")
    $ show_char("sein", "right", flip=True)

    sein "실제로 시신도 대부분 남아 있었습니다. 완전 소각이 목적이었다고 보긴 어렵습니다."

    jump day01_deduction_fire_reason_question


label day01_deduction_fire_reason_right:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "범인은 CCTV 장면을 남기고 싶었습니다."

    jin "하지만 동시에 그 장면 속 문제점은 숨기고 싶었습니다."

    $ show_char("mina", "right", flip=True)

    mina "문제점이요?"

    jin "네."

    jin "사진 속 인물은 겉보기엔 루이 씨입니다."

    jin "하지만 결정적인 부분에서 진짜 루이 씨와 다릅니다."

    $ hide_char("mina")
    $ show_char("nia", "right", flip=True)

    nia "뭐가요?"

    jin "범인은 그 차이를 감추기 위해 화재를 일으켰습니다."

    jin "카메라를 손상시키고, 영상의 선명도를 떨어뜨리기 위해서요."

    $ hide_char("nia")
    $ show_char("jun", "right", flip=True)

    jun "그 차이가 무엇입니까?"

    jump day01_deduction_hidden_detail_question


# =========================
# 다섯 번째 논점: 숨기고 싶었던 것
# =========================

label day01_deduction_hidden_detail_question:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("jun", "right", flip=True)
    with dissolve_normal

    jun "범인이 CCTV 장면에서 숨기고 싶었던 것은 무엇입니까?"

    menu:
        "사진 속 인물의 얼굴이다.":
            jump day01_deduction_hidden_detail_wrong

        "사진 속 인물이 오른손을 쓰고 있다는 점이다.":
            jump day01_deduction_hidden_detail_right


label day01_deduction_hidden_detail_wrong:

    call day01_deduction_wrong(1) from _call_day01_deduction_wrong_4

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)

    mina "흠... 아닌 거 같은데요?"

    mina "얼굴은 오히려 루이 씨처럼 보였잖아요."

    jump day01_deduction_hidden_detail_question


label day01_deduction_hidden_detail_right:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "사진 속 인물은 오른손으로 칼을 들고 서재를 빠져나가고 있습니다."

    $ show_char("rui", "right", flip=True)

    rui "......"

    jin "하지만 루이 씨는 왼손잡이입니다."

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "왼손잡이요?"

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "맞습니다. 저는 왼손을 씁니다."

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "그러고 보니 아까도 메모할 때 왼손으로 쓰셨던 것 같은데요."

    $ hide_char("nia")
    $ show_char("sein", "right", flip=True)

    sein "사진 속 인물은 오른손을 쓰고 있었습니다."

    $ hide_char("sein")
    $ show_char("rui", "right", flip=True)

    rui "그 정도는 일부러 오른손을 쓸 수도 있지 않습니까?"

    jin "평소라면 가능하겠죠."

    jin "하지만 이 사진 속 인물은 모로 씨를 쓰러뜨린 직후입니다."

    jin "급박한 상황에서 결정적인 행동을 할 때, 사람은 가장 익숙한 손을 씁니다."

    $ hide_char("rui")
    $ show_char("kato", "right", flip=True)

    kato "가짜는 얼굴을 빌렸지만, 습관까지 빌리지는 못했군요."

    jin "그렇습니다."

    $ hide_char("kato")
    $ show_char("mina", "right", flip=True)

    mina "그럼 사진 속 인물은 루이 씨가 아니라..."

    jin "루이 씨로 변장한 범인입니다."

    "식당 안이 다시 술렁였다."

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "그렇다면 범인은 자신의 실수를 깨달았겠군요."

    jin "네."

    jin "그래서 다시 움직였습니다."

    jump day01_deduction_mistake_and_fire


# =========================
# 실수와 화재
# =========================

label day01_deduction_mistake_and_fire:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "범인은 CCTV에 루이 씨의 모습으로 찍혔습니다."

    jin "하지만 곧 자신이 오른손을 썼다는 실수를 깨달았을 겁니다."

    $ show_char("rui", "right", flip=True)

    rui "그래서 영상을 못 쓰게 만들기 위해 화재를 냈다?"

    jin "맞습니다."

    jin "서재에 불을 내서 카메라가 망가지길 바란거죠."

    jin "실수를 숨기기 위해, 다시 현장으로 돌아간 겁니다."

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "그럼 그때 뭔가 남겼겠네요?"

    jin "남겼습니다."

    $ hide_char("nia")
    $ show_char("sein", "right", flip=True)

    sein "무엇을 말입니까?"

    jin "범인이 다시 서재로 향했다면, 반드시 지나쳐야 했던 곳이 있습니다."

    jin "그리고 그곳에는 이미 다른 흔적이 남아 있었죠."

    jump day01_deduction_footprint_question


# =========================
# 여섯 번째 논점: 와인 발자국
# =========================

label day01_deduction_footprint_question:

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("sein", "right", flip=True)
    with dissolve_normal

    sein "범인이 다시 서재로 향했다면, 무엇을 밟았을 가능성이 있습니까?"

    menu:
        "복도에 쏟아진 와인이다.":
            jump day01_deduction_footprint_right

        "서재의 소화기 분말이다.":
            jump day01_deduction_footprint_wrong


label day01_deduction_footprint_wrong:

    call day01_deduction_wrong(1) from _call_day01_deduction_wrong_5

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("nia", "right", flip=True)

    nia "흠... 아닌 것 같은데요?"

    nia "소화기는 진 씨가 불을 끌 때 쓴 거잖아요. 범인이 다시 갔던 건 그 전일 수도 있잖아요?"

    $ hide_char("nia")
    $ show_char("rui", "right", flip=True)

    rui "시간 순서상 와인 자국이 더 먼저 생겼습니다."

    jump day01_deduction_footprint_question


label day01_deduction_footprint_right:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    jin "복도에 쏟아진 와인입니다."

    call day01_deduction_tg_footprint from _call_day01_deduction_tg_footprint

    jin "미나 씨와 세인 씨가 부딪히면서, 복도에 와인이 쏟아졌습니다."

    $ show_char("mina", "right", flip=True)

    mina "맞아요. 그건 제가 봤어요."

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "저도 기억합니다."

    jin "그리고 범인은 CCTV에 찍힌 뒤, 자신의 실수를 숨기기 위해 다시 서재 쪽으로 향했습니다."

    jin "그 과정에서 와인 자국을 밟았습니다."

    $ hide_char("sein")
    $ show_char("rui", "right", flip=True)

    rui "하지만 저는 그 와인을 밟지 않았습니다."

    jin "맞습니다."

    jin "루이 씨는 그 뒤 안뜰에서 저와 만나 제가 복도를 조심하라고 직접 당부드렸습니다."

    jin "그리고 애초에 루이 씨의 신발에는 와인 자국이 없었습니다."

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "그럼 사진 속 루이 씨는..."

    jin "진짜 루이 씨가 아닙니다."

    jin "루이 씨로 변장한 범인이죠."

    $ hide_char("nia")
    $ show_char("rui", "right", flip=True)

    rui "그렇다면 발자국을 비교하면 되겠군요!"

    jin "네."

    jin "와인 위에 남은 발자국은 범인이 다시 서재로 향하며 남긴 흔적입니다."

    jin "그리고 그 발자국은,"

    jin "사진 속 인물이 진짜 루이 씨가 아니었다는 마지막 증거가 됩니다."

    $ hide_char("rui")
    $ show_char("ian", "right", flip=True)

    ian "......"

    jin "모두 신발을 확인하겠습니다."

    jin "특히, 서재 방향으로 이어진 와인 발자국과 같은 밑창을 가진 사람을요."

    jin "그 사람이 루이 씨로 변장해 CCTV에 찍히고,"

    jin "자신의 실수를 숨기기 위해 다시 불을 지른 범인입니다."

    jin "비교해보면 바로 알 수 있습니다."

    jump day01_confession


# =========================
# 범인 자백
# =========================

label day01_confession:

    play music bgm_TensionBuild fadeout 0.8 fadein 0.8 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("ian", "right", flip=True)
    with dissolve_normal

    ian "그만."

    window hide

    with flash_white
    call effect_shake_small from _call_effect_shake_small_1

    window show

    "모두의 시선이 이안에게 향했다."

    $ hide_char("ian")
    $ show_char("rui", "right", flip=True)

    rui "이안 씨...?"

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "잠깐. 설마..."

    $ hide_char("nia")
    $ show_char("ian", "right", flip=True)

    ian "맞습니다."

    ian "제가 했습니다."

    "식당 안이 얼어붙었다."

    $ hide_char("ian")
    $ show_char("jun", "right", flip=True)

    jun "이안 님..."

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "그럼 CCTV에 찍힌 루이 씨는..."

    jin "이안 씨가 변장한 모습이었습니다."

    "식당 안이 다시 술렁였다."

    $ hide_char("mina")
    $ show_char("ian", "right", flip=True)

    jin "이안 씨."

    jin "당신은 루이 씨로 변장해 모로 씨를 공격했습니다."

    jin "그 뒤 CCTV에 일부러 찍혔고,"

    jin "루이 씨에게 죄를 뒤집어씌우려 했습니다."

    jin "하지만 오른손을 쓴 실수를 감추기 위해 다시 서재로 향했고,"

    jin "그 과정에서 와인 위의 발자국을 남겼습니다."

    ian "......"

    ian "네."

    ian "제가 죽였습니다."

    jin "모로 씨를 죽인 범인은 당신입니다."

    jump day01_case_end


# =========================
# 첫 번째 사건 종료
# =========================

label day01_case_end:

    hide screen reasoning_gauge

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "식당에는 아무 말도 없었다."

    "만찬은 시작되지 않았다."

    "하지만 첫 번째 진실은 드러났다."

    "모로는 사고로 죽은 것이 아니었다."

    "루이도 범인이 아니었다."

    "진짜 범인은,"

    "루이의 얼굴을 빌린 변장술사 이안이었다."

    jin "......"

    "하지만 아직 끝난 게 아니다."

    "이안이 모로를 죽인 이유."

    "모로가 알고 있던 것."

    "그리고 청둥오리의 죽음."

    "이 저택에는 아직 더 깊은 비밀이 남아 있다."

    window hide dissolve_normal

    stop music fadeout 2.0

    $ clear_chars()

    scene black
    hide screen bottom_right_ui
    with fade_slow

    show text "{color=#ffffff}{size=32}계속{/size}{/color}" at continue_bottom_right
    with dissolve_slow

    pause 2.0

    hide text
    with dissolve_slow

    return