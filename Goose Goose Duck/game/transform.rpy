define CHAR_POSITIONS = {
    "left": 0.1,
    "center": 0.5,
    "right": 0.92,
}

transform char_pos(pos="center"):
    xalign CHAR_POSITIONS[pos]
    yalign 0.9
    xanchor 0.5
    yanchor 1.0

transform char_speaker:
    ease 0.15 matrixcolor BrightnessMatrix(0.0)

transform char_nonspeaker:
    ease 0.15 matrixcolor BrightnessMatrix(-0.35)

transform char_flip(is_flip=False):
    xzoom (-1.0 if is_flip else 1.0)

transform continue_bottom_right:
    xalign 0.92
    yalign 0.88
    xanchor 0.5
    yanchor 0.5

# =========================
# 화면 전환 / 흔들림 연출
# systems/transition_effects.rpy
# =========================


# =========================
# 기본 fade 계열
# =========================

# 일반 장소 이동용 암전
define fade_scene = Fade(0.35, 0.15, 0.35, color="#000000")

# 좀 더 느린 암전
define fade_slow = Fade(0.6, 0.25, 0.6, color="#000000")

# 빠른 장면 끊기용 암전
define fade_cut = Fade(0.12, 0.0, 0.12, color="#000000")

# 시간 경과용. 중간 암전 유지 시간이 조금 김.
define fade_time = Fade(0.45, 0.8, 0.45, color="#000000")

# 충격 / 단서 발견 / 반박용 흰색 플래시
define flash_white = Fade(0.06, 0.0, 0.28, color="#ffffff")

# 강한 흰색 플래시
define flash_strong = Fade(0.03, 0.04, 0.35, color="#ffffff")

# 부드러운 디졸브
define dissolve_fast = Dissolve(0.2)
define dissolve_normal = Dissolve(0.5)
define dissolve_slow = Dissolve(1.0)


# =========================
# 레이어 흔들림용 transform
# =========================

transform layer_reset:
    xoffset 0
    yoffset 0


# 약한 가로 흔들림
transform shake_small:
    xoffset 0
    yoffset 0

    linear 0.03 xoffset -8
    linear 0.03 xoffset 8
    linear 0.03 xoffset -6
    linear 0.03 xoffset 6
    linear 0.03 xoffset -3
    linear 0.03 xoffset 3
    linear 0.03 xoffset 0


# 강한 가로 흔들림
transform shake_hard:
    xoffset 0
    yoffset 0

    linear 0.025 xoffset -24
    linear 0.025 xoffset 24
    linear 0.025 xoffset -20
    linear 0.025 xoffset 20
    linear 0.025 xoffset -14
    linear 0.025 xoffset 14
    linear 0.025 xoffset -8
    linear 0.025 xoffset 8
    linear 0.025 xoffset 0


# 위아래 충격 흔들림
transform shake_vertical:
    xoffset 0
    yoffset 0

    linear 0.025 yoffset -18
    linear 0.025 yoffset 18
    linear 0.025 yoffset -14
    linear 0.025 yoffset 14
    linear 0.025 yoffset -8
    linear 0.025 yoffset 8
    linear 0.025 yoffset 0


# 좌우 + 상하 섞인 충격 흔들림
transform shake_impact:
    xoffset 0
    yoffset 0

    linear 0.025 xoffset -22 yoffset 8
    linear 0.025 xoffset 20 yoffset -8
    linear 0.025 xoffset -16 yoffset 6
    linear 0.025 xoffset 14 yoffset -6
    linear 0.025 xoffset -8 yoffset 3
    linear 0.025 xoffset 8 yoffset -3
    linear 0.025 xoffset 0 yoffset 0

label effect_shake_small:

    show layer master at shake_small
    pause 0.25
    show layer master at layer_reset

    return


label effect_shake_hard:

    show layer master at shake_hard
    pause 0.25
    show layer master at layer_reset

    return


label effect_shake_impact:

    show layer master at shake_impact
    pause 0.25
    show layer master at layer_reset

    return