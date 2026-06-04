# =========================
# 1일차 일상 파트
# story/day01/day01_daily.rpy
# =========================


# =========================
# toggle 이미지 연출
# tg on 이미지가 보이고,
# 입력이 들어오면 천천히 사라짐
# =========================

label day01_tg_note:

    window hide dissolve_fast

    show note at truecenter
    with dissolve_normal

    pause

    hide note
    with dissolve_slow

    window show dissolve_fast

    return


label day01_tg_spill:

    window hide dissolve_fast

    show spill at truecenter
    with dissolve_normal

    pause

    hide spill
    with dissolve_slow

    window show dissolve_fast

    return


# =========================
# 1일차 일상 파트 시작
# Opening
# =========================

label day01_daily_start:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()

    window hide

    scene black
    with fade_scene

    window show dissolve_normal

    "구스구스덕 마을에는 두 종류의 새가 산다."

    "스스로 힘을 갈고닦는 새, 거위."

    "그리고 힘을 품은 채 태어나는 새, 오리."

    "서로 다른 힘을 가진 새들은,"

    "같은 마을에서,"

    "같은 하늘 아래 살아간다."

    "그리고 어느 날 밤,"

    "그들 중 몇몇이 청둥오리 저택의 만찬에 초대되었다."

    jump day01_invitation


# =========================
# 초대장
# bg01
# BGM: 일상
# =========================

label day01_invitation:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg letter
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    "나는 주머니에서 초대장을 꺼냈다."

    "청둥오리의 만찬에 초대합니다."

    "장소는 청둥오리 저택."

    "시간은 오늘 저녁 6시."

    "보낸 이는 청둥오리."

    jin "그 유명한 청둥오리가 왜 나를 부른 거지?"

    "청둥오리는 천재적인 감각을 가진 추리 소설 작가로 유명하다."

    "그러나 그보다 더 유명한 것은, 그는 사람을 거의 만나지 않는 은둔자라는 사실이었다."

    jin "... 평범한 식사 약속은 아니겠군."

    jump day01_mansion_entrance


# =========================
# 저택 입구
# bg02
# BGM: 일상 유지
# =========================

label day01_mansion_entrance:

    show screen bottom_right_ui

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg mansion entrance
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    "청둥오리 저택은 숲 안쪽에 있었다."

    "낡았지만 관리가 잘 된 저택."

    "나는 문 앞에서 잠시 멈춰 섰다."

    jin "기분 나쁜 집이네."

    "나는 현관문을 열었다."

    "안쪽에서 사람들의 목소리가 들렸다."

    jump day01_dining_first


# =========================
# 식당
# bg03
# BGM: 일상 유지
# =========================

label day01_dining_first:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg dining room
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)

    window show dissolve_normal

    "식당에는 이미 손님들이 모여 있었다."

    "긴 식탁."

    "준비된 음식."

    "하지만 주인석은 비어 있었다."

    mina "아, 또 한 명 오셨네. 혹시 당신도 초대받았어요?"

    jin "그렇습니다. 구스타프에서 온 진입니다."

    mina "구스타프요? 꽤 먼 곳에서 오셨네요."

    jin "미나 씨... 맞습니까?"

    mina "어머, 절 아세요?"

    jin "이름 정도는 압니다. 워낙 유명하시니까요."

    mina "후후, 이런 저택에서 알아봐 주시니 좀 안심되네요. 미나예요."

    $ unlock_character("mina")

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "루이입니다. 처음 뵙겠습니다."

    jin "반갑습니다."

    rui "저도 방금 도착했습니다. 아직 분위기를 파악하는 중입니다."

    jin "그렇군요."

    $ unlock_character("rui")

    jump day01_dining_guests_left


# =========================
# 손님들
# 카토 / 모로
# 중간에 모로의 쪽지에서 BGM을 미스터리로 전환
# =========================

label day01_dining_guests_left:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("kato", "right", flip=True)
    with dissolve_normal

    "이번에는 고개를 돌려 반대편을 둘러보았다."

    "그곳에도 여러 사람들이 모여 있었다."

    kato "카토라고 합니다."

    jin "반갑습니다. 진입니다."

    kato "진님도 청둥오리님과 친분이 있으신가요?"

    jin "아뇨 저는 잘... 처음 이곳에 왔습니다."

    kato "처음 온다라... 그것 참 희한하네요."

    "카토는 아리송하다는 듯이 쳐다보며 생각에 잠긴다."

    $ unlock_character("kato")

    $ hide_char("kato")
    $ show_char("moro", "right", flip=True)

    moro "......"

    jin "그쪽은?"

    moro "모로입니다."

    jin "만나서 반갑습니다."

    moro "저도... 기다리고 있었습니다."

    jin "저를요?"

    moro "아니요. 이 만찬을요."

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    $ unlock_character("moro")

    call day01_tg_note from _call_day01_tg_note

    "모로에게 의문의 쪽지를 건네받았다."

    "쪽지에는 작은 글씨로 8시에 서재에서 보자고 적혀 있었다."

    jump day01_dining_guests_right


# =========================
# 나머지와 이야기
# 니오 / 세인 / 이안
# BGM: 일상으로 복귀
# =========================

label day01_dining_guests_right:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("nia", "right", flip=True)
    with dissolve_normal

    nia "저기, 혹시 구스타프에서 오셨다고 했죠?"

    jin "그렇습니다."

    nia "역시. 말투가 좀 다르다 했어요."

    jin "관찰력이 좋으시군요."

    nia "그냥... 이런 곳에 오면 볼 게 많잖아요."

    nia "저 촛대도 그렇고, 벽에 걸린 그림도 그렇고."

    $ hide_char("nia")
    $ show_char("rui", "right", flip=True)

    rui "처음 온 저택에서 너무 돌아다니는 건 좋지 않을 겁니다."

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "하하, 그럼요. 제가 워낙 그냥 궁금한 게 많아서요."

    jin "성함은요?"

    nia "음~ 그냥 니오라고 불러주세요."

    $ unlock_character("nia")

    jin "옆에 계신 분은 혹시?"

    $ hide_char("nia")
    $ show_char("sein", "right", flip=True)

    sein "세인입니다."

    jin "그렇군요 반갑습니다. 진입니다."

    sein "......"

    jin "청둥오리 님과는 아는 사이입니까?"

    sein "한 번 만났습니다."

    jin "그뿐입니까?"

    sein "네."

    jin "그런데도 초대에 응하셨군요."

    sein "초대장이 왔으니까요."

    jin "이유는 궁금하지 않으셨습니까?"

    sein "궁금하다고 달라지는 건 없으니까요."

    $ unlock_character("sein")

    "그 옆에는 다른 손님들을 유심히 관찰하고 있는 남성이 보였다."

    $ hide_char("sein")
    $ show_char("ian", "right", flip=True)

    ian "흠... 어디 보자..."

    jin "반가워요. 혼자 무엇을 하고 계신지요."

    ian "아! 전 이안입니다. 그냥 관찰 중이었습니다."

    jin "흠 그렇군요. 전 진입니다."

    ian "혹시 뭐하시는 분인지 알 수 있을까요?"

    $ unlock_character("ian")

    menu:
        "탐정입니다.":
            jump day01_ian_talk_detective

        "알아서 좋을 거 없을 겁니다.":
            jump day01_ian_talk_secretive


# =========================
# 이안 선택지 1
# =========================

label day01_ian_talk_detective:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("ian", "right", flip=True)
    with dissolve_normal

    jin "탐정입니다."

    ian "탐정이요?"

    jin "네. 구스타프에서 사무소를 하고 있습니다."

    ian "오호. 그렇군요. 의뢰라도 받은 건가요?"

    jin "아니요. 저도 초대받은 이유는 아직 모릅니다."

    ian "그렇군요."

    ian "그럼 여기 있는 사람들을 조사하러 온 건 아닙니까?"

    jin "아직은 아닙니다."

    ian "아직은, 이라."

    jin "필요하면 그렇게 되겠죠."

    ian "......"

    ian "그런 일이 생기지 않았으면 좋겠습니다."

    jin "저도 같은 생각입니다."

    jump day01_butler_appears


# =========================
# 이안 선택지 2
# =========================

label day01_ian_talk_secretive:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("ian", "right", flip=True)
    with dissolve_normal

    jin "알아서 좋을 거 없을 겁니다."

    ian "......"

    ian "그런 식으로 대답하는 사람은 둘 중 하나죠."

    jin "뭡니까?"

    ian "숨기는 게 있거나,"

    ian "남이 숨기는 걸 캐러 왔거나."

    jin "꽤 예민하시군요."

    ian "낯선 저택에서 낯선 사람을 믿는 쪽이 더 이상한 겁니다."

    jin "그건 맞는 말이네요."

    ian "당신이 뭘 하는 사람이든 상관없습니다."

    ian "다만, 제 주변을 캐묻지는 말아주십시오."

    jin "그건 상황에 따라 다릅니다."

    ian "역시 마음에 안 드는 분이군요."

    jump day01_butler_appears


# =========================
# 집사 등장
# BGM: 일상으로 복귀
# =========================

label day01_butler_appears:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "그 순간 문쪽에서 구두 소리가 점점 크게 들려온다."

    # play sound sfx_door_open

    "식당 문이 열리고 한 나이든 사내가 들어온다."

    $ show_char("jun", "right", flip=True)
    with dissolve_normal

    jun "기다리게 해드려 죄송합니다."

    jun "저는 이 저택의 집사, 준이라고 합니다."

    $ unlock_character("jun")

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "집사님?"

    mina "그럼 청둥오리 님은요?"

    $ hide_char("mina")
    $ show_char("jun", "right", flip=True)

    jun "주인님께서는 잠시 자리를 비우셨습니다."

    $ hide_char("jun")
    $ show_char("rui", "right", flip=True)

    rui "자리를 비우셨다고요?"

    $ hide_char("rui")
    $ show_char("jun", "right", flip=True)

    jun "예. 급히 처리하셔야 할 일이 생겼다고만 들었습니다."

    $ hide_char("jun")
    $ show_char("kato", "right", flip=True)

    kato "이 만찬을 직접 열어놓고요?"

    $ hide_char("kato")
    $ show_char("jun", "right", flip=True)

    jun "주인님께서는 원래 예측하기 어려운 분입니다."

    $ hide_char("jun")
    $ show_char("nia", "right", flip=True)

    nia "그럼 저희는 여기서 계속 기다리면 되는 건가요?"

    $ hide_char("nia")
    $ show_char("jun", "right", flip=True)

    jun "오래 걸리지는 않을 겁니다."

    $ hide_char("jun")
    $ show_char("moro", "right", flip=True)

    moro "......"

    $ hide_char("moro")
    $ show_char("jin", "left")
    $ show_char("jun", "right", flip=True)

    jin "청둥오리 님께서 직접 그렇게 말씀하셨습니까?"

    jun "그렇습니다."

    jin "언제 말씀하셨죠?"

    jun "오늘 오후입니다."

    jin "......"

    jun "불편을 드려 죄송합니다."

    jun "주인님께서는 손님들께서 지루하지 않도록 저택을 자유롭게 둘러보셔도 좋다고 하셨습니다."

    $ hide_char("jun")
    $ show_char("rui", "right", flip=True)

    rui "저택을요?"

    $ hide_char("rui")
    $ show_char("jun", "right", flip=True)

    jun "예. 단, 지하와 주인님의 개인 침실은 출입을 삼가 주십시오."

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "음... 기다리는 것보단 낫겠네요."

    $ hide_char("mina")
    $ show_char("nia", "right", flip=True)

    nia "둘러봐도 된다고요?"

    $ hide_char("nia")
    $ show_char("jun", "right", flip=True)

    jun "물론입니다. 다만 위험한 물건이 많은 곳도 있으니 혼자 너무 멀리 가시지는 않는 편이 좋겠습니다."

    $ hide_char("jun")
    $ show_char("nia", "right", flip=True)

    nia "알겠습니다."

    $ hide_char("nia")
    $ show_char("jun", "right", flip=True)

    jun "만찬은 주인님께서 돌아오시는 대로 시작하겠습니다."

    jun "그전까지는 각자 편히 계셔도 좋습니다."

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "사람들은 하나둘 식당을 나섰다."

    jin "나도 움직여 보자."

    jin "청둥오리가 없는 만찬이라..."

    jump day01_kitchen


# =========================
# 부엌
# bg04
# BGM: 일상 유지
# =========================

label day01_kitchen:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg kitchen
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)

    window show dissolve_normal

    "부엌에는 미나가 먼저 와 있었다."

    "그녀는 냉장고 문을 열어둔 채 안쪽을 들여다보고 있었다."

    jin "미나 씨?"

    mina "아, 진 씨. 들켰네요."

    jin "뭘 찾고 계십니까?"

    mina "와인이요. 이 분위기엔 맨정신으로 못 있겠어서요."

    jin "마음대로 꺼내도 되는 겁니까?"

    mina "만찬에 초대했으면 이 정도는 괜찮지 않을까요?"

    "미나는 냉장고 안쪽에서 와인 한 병을 꺼냈다."

    mina "찾았다. 꽤 비싼 거 같은데요?"

    jin "조심하십시오."

    mina "괜찮아요. 이런 건 익숙하죠~"

    "미나는 와인병을 들고 복도 쪽으로 나갔다."

    jump day01_wine_hallway


# =========================
# 복도 와인
# bg05 / bg06
# BGM: 일상 유지
# =========================

label day01_wine_hallway:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg corridor
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)

    window show dissolve_normal

    "복도에 들어선 순간, 미나가 누군가와 부딪혔다."

    mina "꺄악!"

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "아! 뭐야?"

    window hide

    scene bg corridor wine
    with flash_white

    call effect_shake_small from _call_effect_shake_small

    window show

    "와인병이 기울어지고, 붉은 와인이 복도 바닥에 쏟아졌다."

    "짙은 와인 자국이 카펫 위로 번졌다."

    $ hide_char("sein")
    $ show_char("mina", "right", flip=True)

    mina "아, 진짜! 앞 좀 보고 다니세요!"

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "뭐? 앞 안 보고 다닌 게 누군데?"

    jin "다치신 곳은 없습니까?"

    $ hide_char("sein")
    $ show_char("mina", "right", flip=True)

    mina "전 괜찮아요. 근데 카펫은 안 괜찮겠네요."

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "치... 집사를 부를게요."

    jin "준 씨가 어디 있는지 아십니까?"

    sein "아니요."

    $ hide_char("sein")
    $ show_char("mina", "right", flip=True)

    "미나는 주변을 둘러봤지만, 준의 모습은 보이지 않았다."

    mina "이럴 땐 꼭 안 보인다니까."

    jin "일단 밟지 않게 조심하는 게 좋겠습니다."

    mina "저는 안뜰 쪽으로 갈래요. 여기 있으면 냄새만 맡겠어요."

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "참... 재수없게 진짜."

    "세인은 와인 자국을 잠시 내려다보다가 말없이 복도 반대편으로 걸어갔다."

    $ clear_chars()
    $ show_char("jin", "left")

    "얼룩진 복도를 내려다보았다."

    call day01_tg_spill from _call_day01_tg_spill

    jin "복도가 아주 난리가 났구만. 집사를 빨리 찾아야겠어."

    # 현재 CLUE_DATABASE에 spill 항목이 없다면 이 줄은 주석 유지.
    # $ add_clue("spill")

    jump day01_courtyard


# =========================
# 안뜰
# bg07
# BGM: 일상 유지
# =========================

label day01_courtyard:

    play music bgm_DailyVibe fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg courtyard
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("rui", "right", flip=True)

    window show dissolve_normal

    "안뜰에는 차가운 밤공기가 내려앉아 있었다."

    "루이가 난간 근처에 서 있었다."

    rui "진 씨."

    jin "루이 씨. 여기 계셨군요."

    rui "저택 안보다 이쪽이 조금 낫더군요."

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "두 분 다 여기 있었네요."

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "미나 씨. 기분이 별로 안 좋아 보이네요."

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "묻지 마세요. 와인을 쏟아 버려서 복도가 다 마시게 됐으니까."

    jin "정확히는 카펫이 마셨죠."

    mina "농담할 상황 아니거든요?"

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "복도에 쏟으셨다는 말입니까?"

    $ hide_char("rui")
    $ show_char("mina", "right", flip=True)

    mina "네. 세인 씨랑 부딪혀서요."

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "나중에 누가 미끄러질 수도 있겠군요."

    jin "준 씨에게 알려야겠습니다."

    rui "집사님은 로비로 이동하신 걸로 압니다."

    jin "감사합니다. 당분간 이쪽 복도는 피해주세요."

    rui "명심하겠습니다."

    "준을 찾기 위해 로비로 이동할 준비를 한다."

    jump day01_lobby_jun


# =========================
# 로비 준
# bg08
# BGM: 미스터리
# =========================

label day01_lobby_jun:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg lobby
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("jun", "right", flip=True)

    window show dissolve_normal

    "로비에는 준이 서 있었다."

    "그는 손님들을 찾는 듯 주변을 살피고 있었다."

    jun "진 씨."

    jin "준 씨. 찾고 있었습니다."

    jun "무슨 일이십니까?"

    jin "복도에 와인이 쏟아졌습니다. 미나 씨와 세인 씨가 부딪힌 것 같습니다."

    jun "와인이요?"

    jin "카펫에 많이 흘렀습니다. 확인하시는 편이 좋겠습니다."

    jun "알겠습니다. 곧 처리하겠습니다."

    jin "그런데 준 씨."

    jun "예."

    jin "무언가 찾고 계신 것처럼 보였습니다."

    jun "눈치가 빠르시군요."

    jin "직업병입니다."

    jun "이상한 점이 하나 있습니다."

    jin "무엇입니까?"

    jun "제가 준비한 초대장은 일곱 장입니다."

    jin "일곱 장."

    jun "예. 그런데 지금 저택에 들어온 손님은 여덟 분입니다."

    jin "초대받지 않은 사람이 있다는 뜻입니까?"

    jun "그렇다고 볼 수 있겠죠."

    jin "참 기묘한 일이군요. 알려주셔서 감사합니다."

    jun "네. 그럼 이만 저는 복도의 와인 자국을 확인하겠습니다."

    "준은 복도 쪽으로 걸어갔다."

    $ clear_chars()
    $ show_char("jin", "left")

    "일곱 장의 초대장. 여덟 명의 손님."

    "고민에 잠기며 서쪽 거실로 이동한다."

    jump day01_west_livingroom_kato


# =========================
# 서쪽 거실 카토
# bg09
# BGM: 미스터리 유지
# =========================

label day01_west_livingroom_kato:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg west living room
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("kato", "right", flip=True)

    window show dissolve_normal

    "서쪽 거실은 어둡고 조용했다."

    "벽난로에는 불이 꺼져 있었고, 창밖에는 안뜰의 그림자가 흔들리고 있었다."

    "카토가 방 한가운데 서 있었다."

    jin "카토 씨?"

    kato "......"

    jin "괜찮으십니까?"

    "카토는 대답하지 않았다."

    "그의 시선은 허공 어딘가에 고정되어 있었다."

    jin "카토 씨."

    kato "...문이 열립니다."

    jin "무슨 문 말입니까?"

    kato "닫혀 있어야 할 문."

    jin "......"

    jin "괜찮은 거 맞죠?"

    "카토는 천천히 고개를 돌려 진을 바라보았다."

    kato "......"

    "상태가 이상한 카토 씨로부터 도망치듯 통로로 이동한다."

    jump day01_corridor_power_device


# =========================
# 통로 전원장치
# bg10
# BGM: 미스터리 유지 → 화재 경보 때 긴박 BGM
# =========================

label day01_corridor_power_device:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg power
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    "서쪽 거실을 나와 통로로 들어서자, 공기가 차갑게 바뀌었다."

    "통로 벽에는 오래된 전등이 일정한 간격으로 달려 있었다."

    jin "이쪽은 손님들이 잘 다니는 길은 아닌 것 같은데."

    "벽 한쪽에 철제 함이 있었다."

    "덮개에는 낡은 글씨가 적혀 있었다."

    "전원 제어 장치."

    "덮개를 열자 안쪽에는 커다란 스위치와 작은 안내문이 붙어 있었다."

    "“로비 및 서쪽 구역 조명 제어”"

    jin "전등을 끄고 켜는 장치인가."

    "스위치에는 오래된 손때가 묻어 있었다."

    jin "혹시 모르니 기억해 둘 필요가 있겠어."

    "시계를 보니 곧 8시였다."

    "장의사가 준 쪽지를 다시 한 번 본다."

    jin "이제 슬슬 서재로 이동해야겠어."

    "그때 멀리서 희미한 냄새가 흘러왔다."

    "탄 냄새였다."

    jin "이게 무슨 냄새지?"

    "곧이어 날카로운 경보음이 저택 안에 울려 퍼졌다."

    "화재 경보였다."

    play music bgm_TensionBuild fadeout 0.5 fadein 0.5 if_changed loop

    window hide

    with flash_strong
    call effect_shake_impact from _call_effect_shake_impact

    window show

    jin "서재 쪽이다!"

    jump day01_incident_start

    return