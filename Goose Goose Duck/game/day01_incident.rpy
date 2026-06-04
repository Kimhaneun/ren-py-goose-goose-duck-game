# =========================
# 1일차 사건 / 수사 파트
# story/day01/day01_incident_investigation.rpy
# =========================


# =========================
# tg 이미지 연출
# 이미지를 보여주고, 입력이 들어오면 천천히 사라짐
# =========================

label day01_tg_igature:

    window hide dissolve_fast

    show igature at truecenter
    with dissolve_normal

    pause

    hide igature
    with dissolve_slow

    window show dissolve_fast

    return


label day01_tg_ashes:

    window hide dissolve_fast

    show ashes at truecenter
    with dissolve_normal

    pause

    hide ashes
    with dissolve_slow

    window show dissolve_fast

    return


label day01_tg_stab:

    window hide dissolve_fast

    show stab at truecenter
    with dissolve_normal

    pause

    hide stab
    with dissolve_slow

    window show dissolve_fast

    return


label day01_tg_cctv:

    window hide dissolve_fast

    show cctv at truecenter
    with dissolve_normal

    pause

    hide cctv
    with dissolve_slow

    window show dissolve_fast

    return


label day01_tg_footprint:

    window hide dissolve_fast

    show footprint at truecenter
    with dissolve_normal

    pause

    hide footprint
    with dissolve_slow

    window show dissolve_fast

    return


# =========================
# 화재경보 발생
# 장소: 독서실 + 검은 연기
# bg reading room
# BGM: 긴박한 상황
# =========================

label day01_incident_start:

    play music bgm_TensionBuild fadeout 0.5 fadein 0.5 if_changed loop

    window hide dissolve_normal

    scene bg reading room
    with fade_cut

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    jin "어디서 나는 거지?"

    "진은 경보음이 울리는 방향으로 달렸다."

    "통로 끝을 지나 독서실로 들어서자, 매캐한 연기가 코를 찔렀다."

    "독서실 너머."

    "서재로 이어지는 문틈에서 검은 연기가 새어 나오고 있었다."

    jin "서재 쪽이다!"

    "뒤에서 누군가의 발소리가 들렸다."

    $ show_char("nia", "right", flip=True)
    with dissolve_normal

    nia "진님! 무슨 일인가요?"

    jin "서재에서 불이 난 것 같습니다."

    $ hide_char("nia")
    $ show_char("kato", "right", flip=True)

    kato "이..이런!"

    jin "서재 문을 열겠습니다. 모두 뒤로 물러나세요."

    "손수건으로 입과 코를 막고 서재 문손잡이를 잡았다."

    "문 안쪽에서 뜨거운 열기가 느껴졌다."

    "서재 문을 밀어 열었다."

    window hide

    with flash_white
    call effect_shake_small from _call_effect_shake_small_2

    window show

    "검은 연기가 쏟아져 나왔다."

    $ hide_char("kato")
    $ show_char("nia", "right", flip=True)

    nia "여.. 여기 소화기를 찾았어요! 이걸 사용하세요!"

    jin "어서 저한테 주세요..!"

    jump day01_study_fire


# =========================
# 서재 화재
# 장소: 불타는 서재 / 소화 중 / 불 꺼진 서재
# bg study fire
# bg study extinguishing
# bg study burnt
# =========================

label day01_study_fire:

    play music bgm_TensionBuild fadeout 0.5 fadein 0.5 if_changed loop

    window hide dissolve_normal

    scene bg study fire
    with fade_cut

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("nia", "right", flip=True)

    window show dissolve_normal

    "서재는 연기로 자욱했다."

    nia "앞이 안 보여요!"

    $ hide_char("nia")
    $ show_char("kato", "right", flip=True)

    kato "안쪽에..."

    window hide dissolve_normal

    scene bg study extinguishing
    with flash_white

    call effect_shake_small from _call_effect_shake_small_3

    window show dissolve_normal

    "소화기를 들고 안전핀을 뽑았다."

    "불길을 향해 소화기를 분사했다."

    "흰 분말이 연기와 뒤섞이며 서재 안을 가득 채웠다."

    "불길은 쉽게 잡히지 않았지만, 조금씩 잦아들기 시작했다."

    $ hide_char("kato")
    $ show_char("nia", "right", flip=True)

    nia "부..불이 잦아들고 있어요!"

    "진은 책상 아래와 벽난로 근처를 향해 다시 소화기를 뿌렸다."

    window hide dissolve_normal

    scene bg study burnt
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    "마침내 불길이 거의 사라졌다."

    "연기만이 방 안에 무겁게 남았다."

    jin "하아... 다들 무사하시죠?"

    "연기 속에서 천천히 주변을 살폈다."

    "쓰러진 의자."

    "그을린 책."

    "바닥에 흩어진 종이 조각들."

    "그리고 책상 옆."

    "누군가 쓰러져 있었다."

    jin "......"

    $ show_char("nia", "right", flip=True)

    nia "꺄아아악!"

    window hide

    with flash_strong
    call effect_shake_impact from _call_effect_shake_impact_1

    window show

    "반대편 입구에는 미나, 루이, 세인, 준, 이안이 있었다."

    $ hide_char("nia")
    $ show_char("mina", "right", flip=True)

    mina "누.. 누구지?"

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "비켜주세요!"

    "루이가 서재 안으로 들어왔다."

    $ hide_char("rui")
    $ show_char("sein", "right", flip=True)

    sein "......"

    $ hide_char("sein")
    $ show_char("nia", "right", flip=True)

    nia "저 사람... 모로 씨 아닌가요?"

    "그렇다, 그는 모로였다."

    jin "모로 씨. 들리십니까?"

    "반응은 없었다."

    $ hide_char("nia")
    $ show_char("mina", "right", flip=True)

    mina "안 돼... 장난이죠? 그냥 기절한 거죠?"

    $ hide_char("mina")
    $ show_char("kato", "right", flip=True)

    kato "......"

    "모로의 목덜미 쪽에 손을 가져갔다."

    jin "돌아가셨습니다."

    $ set_character_dead("moro")

    $ hide_char("kato")
    $ show_char("jun", "right", flip=True)

    jun "주인님의 저택에서 이런 일이 벌어지다니.."

    jump day01_panic


# =========================
# 패닉
# =========================

label day01_panic:

    play music bgm_TensionBuild fadeout 0.5 fadein 0.5 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    $ show_char("mina", "right", flip=True)
    with dissolve_normal

    mina "말도 안 돼요. 방금 전까지 같이 있었잖아요!"

    $ hide_char("mina")
    $ show_char("sein", "right", flip=True)

    sein "이게 무슨 일이야.."

    $ hide_char("sein")
    $ show_char("jun", "right", flip=True)

    jun "진정해 주십시오. 모두 진정해 주십시오."

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "진정하게 생겼어요?! 사람이 죽었는데!"

    $ hide_char("mina")
    $ show_char("jun", "right", flip=True)

    jun "우선 모두 서재 밖으로 나가주십시오."

    jin "아니요."

    jun "진 씨?"

    jin "아무도 멀리 가지 마십시오."

    jun "그건 무슨 뜻입니까?"

    jin "이건 단순한 화재가 아닐 가능성이 있습니다."

    $ hide_char("jun")
    $ show_char("mina", "right", flip=True)

    mina "그게 무슨 말이에요?"

    jin "확인해야 할 게 있습니다."

    $ hide_char("mina")
    $ show_char("jun", "right", flip=True)

    jun "하지만 현장은 위험합니다. 제가 먼저 정리하겠습니다."

    jin "정리하면 안 됩니다. 잠시 수사할 시간을 주십쇼."

    jump day01_investigation_start


# =========================
# 서재 수사 시작
# BGM: 미스터리
# =========================

label day01_investigation_start:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg study burnt
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    "서재 안에는 아직 연기가 남아 있었다."

    "불은 꺼졌지만, 그을음 냄새가 진하게 퍼져 있었다."

    "모로는 책상 옆에 쓰러져 있었다."

    "진은 천천히 주변을 둘러보았다."

    jin "모두 문 밖에서 기다려주십시오."

    $ show_char("mina", "right", flip=True)

    mina "저... 정말 살인일 수도 있다는 거예요?"

    jin "아직 단정하지 않겠습니다."

    $ hide_char("mina")
    $ show_char("rui", "right", flip=True)

    rui "필요한 게 있으면 말해주십시오."

    $ hide_char("rui")
    $ show_char("nia", "right", flip=True)

    nia "저는... 밖에 있어도 되죠?"

    jin "네. 하지만 저택 밖으로는 나가지 마십시오."

    $ hide_char("nia")
    $ show_char("jun", "right", flip=True)

    jun "제가 손님들을 식당으로 모시겠습니다."

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "다시 모로의 시신 쪽으로 시선을 돌렸다."

    "화재. 시신. 그리고 이 방에 남은 흔적들."

    "모로 씨가 죽은 이유는, 아직 이 안에 있다."

    jump day01_investigation_body_burn


# =========================
# 장의사의 화상 확인
# =========================

label day01_investigation_body_burn:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "모로의 몸을 조심스럽게 살폈다."

    "겉옷은 불에 그을려 있었다."

    "손등과 소매 끝도 검게 타 있었다."

    jin "불에 휩쓸린 것처럼 보이긴 한다."

    jin "하지만... 뭔가 이질감이 느껴져."

    jump day01_investigation_igature


# =========================
# 목의 압박 흔적
# 단서: igature
# 표시 이미지: igature
# =========================

label day01_investigation_igature:

    "모로의 목 주변 그을음을 조심스럽게 털어냈다."

    call day01_tg_igature from _call_day01_tg_igature

    "피부 위로 선명한 자국이 드러났다."

    "불에 탄 자국과는 달랐다."

    "목을 둥글게 감싸는 듯한 압박 흔적."

    jin "이건.. 화상 자국이 아니야."

    jin "목이 졸린 흔적인가?"

    jin "그렇다면 대체 누가... 그리고 뭐로?"

    "시신 주변을 다시 둘러보았다."

    "책상 옆."

    "바닥."

    "그리고 화로."

    "불길이 가장 강했던 곳 근처에 검게 탄 무언가가 남아 있었다."

    $ add_clue("igature")

    jump day01_investigation_ashes


# =========================
# 불탄 천 조각
# 단서: ashes
# 표시 이미지: ashes
# =========================

label day01_investigation_ashes:

    "화로 안쪽에는 재와 그을음이 쌓여 있었다."

    call day01_tg_ashes from _call_day01_tg_ashes

    "그 사이에 완전히 타지 않은 천 조각이 걸려 있었다."

    "진은 집게로 그것을 조심스럽게 집어 올렸다."

    jin "이건.. 천 조각인데?"

    jin "일부러 화로 안쪽에 밀어 넣은 것처럼 보이기도 해."

    $ show_char("sein", "right", flip=True)
    with dissolve_normal

    sein "누군가 태우려 했군."

    $ hide_char("sein")

    "진은 천 조각을 살폈다."

    "끝부분은 검게 탔지만,"

    "중간에는 비틀린 자국이 남아 있었다."

    $ add_clue("ashes")

    jump day01_investigation_stab


# =========================
# 복부 확인
# 단서: stab
# 표시 이미지: stab
# =========================

label day01_investigation_stab:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "진은 조심스럽게 모로의 겉옷을 살폈다."

    call day01_tg_stab from _call_day01_tg_stab

    "불에 그을린 천 사이로 검게 눌어붙은 자국이 보였다."

    jin "......"

    jin "이건 화상 자국이 아니야."

    "진은 옷자락을 조금 걷어 올렸다."

    "복부 쪽에 날카로운 것에 찔린 듯한 상처가 남아 있었다."

    "불길에 일부 가려졌지만,"

    "상처의 형태는 분명했다."

    "칼에 찔린 자상."

    jin "누군가 모로 씨를 찔렀고..."

    "진은 다시 상처 주변을 살폈다."

    jin "출혈 흔적은 옷 안쪽에 남아 있다."

    jin "하지만 바닥에는 생각보다 피가 적어."

    jin "먼저 움직이지 못하게 만든 뒤 찔렀겠군."

    $ add_clue("stab")

    jump day01_investigation_cctv


# =========================
# CCTV 제안
# 단서: cctv
# 표시 이미지: cctv
# =========================

label day01_investigation_cctv:

    $ clear_chars()
    $ show_char("jin", "left")
    with dissolve_normal

    "서재 천장 구석을 살펴봤다."

    call day01_tg_cctv from _call_day01_tg_cctv

    "그곳에는 검은 렌즈가 달린 작은 CCTV가 있었다."

    jin "CCTV가 있었군!"

    "하지만, 자세히 살펴보니 렌즈 쪽이 그을렸고, 표시등도 꺼져있다."

    jin "화재 때문에 고장났나.."

    jin "나중에 집사에게 물어봐야겠군."

    $ add_clue("cctv")

    jin "일단 단서는 얼추 모았어. 식당으로 이동해보자."

    jump day01_move_to_dining_room


# =========================
# 식당으로 이동
# 복도에서 와인이 묻은 발자국 발견
# 단서: footprint
# 표시 이미지: footprint
# =========================

label day01_move_to_dining_room:

    play music bgm_MysteryClue fadeout 1.0 fadein 1.0 if_changed loop

    window hide dissolve_normal

    scene bg corridor footprint
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    "서재에서 식당으로 가려면 부엌 앞 복도를 지나야 했다."

    call day01_tg_footprint from _call_day01_tg_footprint

    "복도에는 아직 와인이 말라붙지 않은 채 번져 있었다."

    "아까 미나와 세인이 부딪혀 쏟은 와인 자국이었다."

    jin "......저게 뭐지?"

    "와인 자국 위로 누군가 지나간 듯한 발자국이 남아 있었다."

    "진한 붉은 와인이 신발 밑창에 묻어,"

    "복도 바닥에 희미한 자국을 찍어놓고 있었다."

    jin "발자국이 있군."

    "발자국을 조심스럽게 살폈다."

    "발자국은 서재 방향에서 나와, 복도 안쪽으로 이어져 있었다."

    jin "일단 기억해두자."

    $ add_clue("footprint")

    jump day01_to_deduction_part


# =========================
# 사건/수사 파트 종료
# 다음 파일: 추리 파트로 연결
# =========================

label day01_to_deduction_part:

    window hide dissolve_normal

    scene bg dining room
    with fade_scene

    $ clear_chars()
    $ show_char("jin", "left")

    window show dissolve_normal

    # 다음 파일에서 구현할 추리 파트 시작 라벨.
    # 추리 파트 파일을 만들면 이 주석을 해제.
    jump day01_deduction_start

    return