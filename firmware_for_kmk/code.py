import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap



keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP6,board.GP7,board.GP8,)
keyboard.col_pins = (board.GP9,board.GP10,board.GP12, board.GP13, board.GP14, board.GP15, board.GP27, board.GP26, board.GP22, board.GP21, board.GP20, board.GP19,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())

keyboard.keymap = [
    [#0
        KC.ESC,     KC.MT(KC.Q, KC.LALT),   KC.W,  KC.E,  KC.R, KC.T, KC.Y,     KC.U, KC.I, KC.O,    KC.P,     KC.BSPC,
        KC.LCTRL,   KC.A,   KC.S,  KC.D,  KC.F, KC.G, KC.H,     KC.J, KC.K, KC.L,    KC.MINS,  KC.ENT,
        KC.LSFT,    KC.MT(KC.Z,KC.LGUI),   KC.MT(KC.X, KC.LGUI),  KC.C,  KC.V, KC.LT(2,KC.B), KC.SPACE, KC.LT(1,KC.N), KC.M, KC.COMM, KC.DOT,   KC.SPACE,
    ],
    [#1
        KC.TAB,     KC.N1,     KC.N2,   KC.N3,    KC.N4,     KC.N5,      KC.N6,         KC.N7,        KC.N8,    KC.N9,         KC.N0,          KC.BSPC,
        KC.LCTRL,   KC.EXLM,   KC.AT,   KC.HASH,  KC.DOLLAR, KC.PERCENT, KC.CIRCUMFLEX, KC.AMPERSAND, KC.ASTERISK, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.ENT,
        KC.LSFT,    KC.PLUS,   KC.MINS, KC.PAST,  KC.SLASH,  KC.EQUAL,   KC.NO,      KC.N,         KC.M,       KC.LSFT(KC.LBRC),       KC.LSFT(KC.RBRC),         KC.SPACE,
    ],
    [#2
        KC.TAB,     KC.F1,     KC.F2,   KC.F3,    KC.F4,     KC.F5,      KC.F6,         KC.F7,        KC.F8,    KC.F9,         KC.F10,          KC.BSPC,
        KC.LCTRL,   KC.AT,   KC.BSLASH,   KC.SCOLON,  KC.LSFT(KC.SCOLON), KC.QUOTE, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.LSFT(KC.SLASH), KC.ENT,
        KC.LSFT,    KC.PLUS,   KC.MINS, KC.PAST,  KC.SLASH,  KC.EQUAL,   KC.NO,      KC.GRAVE,         KC.M,       KC.LBRC,       KC.RBRC,         KC.SPACE,
    ],
]

if __name__ == '__main__':
    keyboard.go()
