from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import random

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Cathon - Python Board Game")
window.setWindowIcon(QIcon("textures/city_red.png"))
window.setGeometry(0, 0, 1920, 1000)
win_palette = QPalette()
win_palette.setColor(QPalette.ColorRole.Window, QColor("#3a6ad1"))
window.setPalette(win_palette)

widget = QWidget()
main_layout = QHBoxLayout(widget)

# GLOBALS
global balance_brick1
balance_brick1 = 2
global balance_fabric1
balance_fabric1 = 2
global balance_ore1
balance_ore1 = 2
global balance_wheat1
balance_wheat1 = 2
global balance_wood1
balance_wood1 = 2

global balance_brick2
balance_brick2 = 2
global balance_fabric2
balance_fabric2 = 2
global balance_ore2
balance_ore2 = 2
global balance_wheat2
balance_wheat2 = 2
global balance_wood2
balance_wood2 = 2

global balance_brick3
balance_brick3 = 0
global balance_fabric3
balance_fabric3 = 0
global balance_ore3
balance_ore3 = 0
global balance_wheat3
balance_wheat3 = 0
global balance_wood3
balance_wood3 = 0

global balance_brick4
balance_brick4 = 0
global balance_fabric4
balance_fabric4 = 0
global balance_ore4
balance_ore4 = 0
global balance_wheat4
balance_wheat4 = 0
global balance_wood4
balance_wood4 = 0

global vp1
vp1 = 0
global vp2
vp2 = 0
global vp3
vp3 = 0
global vp4
vp4 = 0


slotlist=[]

global selected_slot
selected_slot = 0
global selected_street
selected_street = 0
global street_rotation
street_rotation = 0

global current_player
current_player = 1

def set_current_player(player):
    global current_player
    current_player = player

    if current_player == 1:
        splay1.setChecked(True)
        splay2.setChecked(False)
        splay3.setChecked(False)
        splay4.setChecked(False)
    elif current_player == 2:
        splay1.setChecked(False)
        splay2.setChecked(True)
        splay3.setChecked(False)
        splay4.setChecked(False)
    elif current_player == 3:
        splay1.setChecked(False)
        splay2.setChecked(False)
        splay3.setChecked(True)
        splay4.setChecked(False)
    elif current_player == 4:
        splay1.setChecked(False)
        splay2.setChecked(False)
        splay3.setChecked(False)
        splay4.setChecked(True)

    update_balance()
    update_buylay()
    update_vp_bar()
    update_card_list()

# BOARD
b = QWidget()
b.setFixedSize(1080, 1000)

def _create_hexagon(material, x, y):
    hex = QPushButton(b)
    hex.setFixedSize(200,200)
    hex.setIcon(QIcon(f"textures/{material}_back.png"))
    hex.setIconSize(QSize(200, 200))
    hex.setGeometry(x, y, 10, 10)
    hex.setStyleSheet("border: none; background: transparent")
    return hex

h1 = _create_hexagon("wood", 288, 165)
h2 = _create_hexagon("brick", 463, 165)
h3 = _create_hexagon("fabric", 637, 165)

h4 = _create_hexagon("brick", 202, 315)
h5 = _create_hexagon("wheat", 376, 315)
h6 = _create_hexagon("ore", 550, 315)
h7 = _create_hexagon("wheat", 724, 315)

h8 = _create_hexagon("wood", 116, 465)
h9 = _create_hexagon("ore", 290, 465)
h10 = _create_hexagon("void", 464, 465)
h11 = _create_hexagon("brick", 638, 465)
h12 = _create_hexagon("wood", 812, 465)

h13 = _create_hexagon("fabric", 203, 615)
h14 = _create_hexagon("wheat", 377, 615)
h15 = _create_hexagon("ore", 551, 615)
h16 = _create_hexagon("fabric", 725, 615)

h17 = _create_hexagon("brick", 291, 765)
h18 = _create_hexagon("wheat", 639, 765)
h19 = _create_hexagon("wood", 464, 765)

def _create_material(material, x, y):
    mat = QPushButton(b)
    mat.setFixedSize(200,200)
    mat.setIcon(QIcon(f"textures/{material}.png"))
    mat.setIconSize(QSize(100, 100))
    mat.setGeometry(x, y, 10, 10)
    mat.setStyleSheet("border: none; background: transparent")
    return mat

m1 = _create_material("wood", 288, 145)
m2 = _create_material("brick", 463, 145)
m3 = _create_material("fabric", 637, 145)

m4 = _create_material("brick", 202, 295)
m5 = _create_material("wheat", 376, 295)
m6 = _create_material("ore", 550, 295)
m7 = _create_material("wheat", 724, 295)

m8 = _create_material("wood", 116, 445)
m9 = _create_material("ore", 290, 445)
m10 = _create_material("void", 464, 445)
m11 = _create_material("brick", 638, 445)
m12 = _create_material("wood", 812, 445)

m13 = _create_material("fabric", 203, 595)
m14 = _create_material("wheat", 377, 595)
m15 = _create_material("ore", 551, 595)
m16 = _create_material("fabric", 725, 595)

m17 = _create_material("brick", 291, 745)
m18 = _create_material("wheat", 639, 745)
m19 = _create_material("wood", 464, 745)

def _create_label(num, x, y):
    lab = QLabel(b)
    lab.setText(num)
    lab.setFixedSize(200,200)
    lab.setGeometry(x, y, 10, 10)
    lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
    lab.setStyleSheet("font-weight: bold; font-size: 40px; color: white; font-family: 'Inter'; border: none; background: transparent")
    return lab

l1 = _create_label("2", 288, 215)
l2 = _create_label("3", 463, 215)
l3 = _create_label("4", 637, 215)

l4 = _create_label("5", 202, 365)
l5 = _create_label("6", 376, 365)
l6 = _create_label("8", 550, 365)
l7 = _create_label("9", 724, 365)

l8 = _create_label("10", 116, 515)
l9 = _create_label("11", 290, 515)
l10 = _create_label("2", 464, 515)
l11 = _create_label("3", 638, 515)
l12 = _create_label("4", 812, 515)

l13 = _create_label("5", 203, 665)
l14 = _create_label("6", 377, 665)
l15 = _create_label("8", 551, 665)
l16 = _create_label("9", 725, 665)

l17 = _create_label("10", 291, 815)
l18 = _create_label("11", 639, 815)
l19 = _create_label("2", 464, 815)

# Streets
def on_street_selection(street, rotation):
    global selected_street
    selected_street = street
    global street_rotation
    street_rotation = rotation
    sselbuyv.hide()
    sselbuyc.hide()
    sselbuys.show()
    update_slot_type(street)
def on_street_deselection():
    sselbuyv.hide()
    sselbuyc.hide()
    sselbuys.hide()
    global street_rotation
    street_rotation = 0
    #update_slot_type(0)

def update_slot_type(slot: QPushButton):
    i = slot.property("type")
    if i == "slot_empty":
        ssellab.setText("Empty Slot")
        ssellab.setIcon(QIcon("textures/slot_empty.png"))

    elif i in ["street_empty", "street_empty_60", "street_empty_120"]:
        ssellab.setText("Empty Street")
        ssellab.setIcon(QIcon("textures/street_empty.png"))

    elif i in ["street_red", "street_red_60", "street_red_120"]:
        ssellab.setText("Red Street")
        ssellab.setIcon(QIcon("textures/street_red.png"))

    elif i in ["street_blue", "street_blue_60", "street_blue_120"]:
        ssellab.setText("Blue Street")
        ssellab.setIcon(QIcon("textures/street_blue.png"))

    elif i in ["street_green", "street_green_60", "street_green_120"]:
        ssellab.setText("Green Street")
        ssellab.setIcon(QIcon("textures/street_green.png"))

    elif i in ["street_yellow", "street_yellow_60", "street_yellow_120"]:
        ssellab.setText("Yellow Street")
        ssellab.setIcon(QIcon("textures/street_yellow.png"))


    elif i == "village_red":
        ssellab.setText("Red Village")
        ssellab.setIcon(QIcon("textures/village_red.png"))

    elif i == "village_blue":
        ssellab.setText("Blue Village")
        ssellab.setIcon(QIcon("textures/village_blue.png"))

    elif i == "village_green":
        ssellab.setText("Green Village")
        ssellab.setIcon(QIcon("textures/village_green.png"))

    elif i == "village_yellow":
        ssellab.setText("Yellow Village")
        ssellab.setIcon(QIcon("textures/village_yellow.png"))


    elif i == "city_red":
        ssellab.setText("Red City")
        ssellab.setIcon(QIcon("textures/city_red.png"))

    elif i == "city_blue":
        ssellab.setText("Blue City")
        ssellab.setIcon(QIcon("textures/city_blue.png"))

    elif i == "city_green":
        ssellab.setText("Green City")
        ssellab.setIcon(QIcon("textures/city_green.png"))

    elif i == "city_yellow":
        ssellab.setText("Yellow City")
        ssellab.setIcon(QIcon("textures/city_yellow.png"))

    else:
        ssellab.setText("No Selection")
        ssellab.setIcon(QIcon("textures/slot_empty.png"))


def _create_vert_street(x, y):
    street = QPushButton(b)
    street.setFixedSize(60, 60)
    street.setIcon(QIcon("textures/street_empty.png"))
    street.setProperty("type", "street_empty")
    street.setIconSize(QSize(60, 60))
    street.setCheckable(True)
    street.setGeometry(x, y, 60, 60)
    street.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(street)
    street.toggled.connect(lambda checked: on_street_selection(street, "vert") if checked else on_street_deselection())
    return street

v1 = _create_vert_street(270, 235)
v2 = _create_vert_street(445, 235)
v3 = _create_vert_street(620, 235)
v4 = _create_vert_street(795, 235)

v5 = _create_vert_street(185, 385)
v6 = _create_vert_street(360, 385)
v7 = _create_vert_street(533, 385)
v8 = _create_vert_street(707, 385)
v9 = _create_vert_street(882, 385)

v10 = _create_vert_street(100, 535)
v11 = _create_vert_street(272, 535)
v12 = _create_vert_street(447, 535)
v13 = _create_vert_street(622, 535)
v14 = _create_vert_street(795, 535)
v15 = _create_vert_street(968, 535)

v16 = _create_vert_street(186, 685)
v17 = _create_vert_street(360, 685)
v18 = _create_vert_street(535, 685)
v19 = _create_vert_street(709, 685)
v20 = _create_vert_street(883, 685)

v21 = _create_vert_street(272, 835)
v22 = _create_vert_street(447, 835)
v23 = _create_vert_street(622, 835)
v24 = _create_vert_street(797, 835)

def _create_60_street(x, y):
    street = QPushButton(b)
    street.setFixedSize(60, 60)
    street.setIcon(QIcon("textures/street_empty_60.png"))
    street.setProperty("type", "street_empty_60") 
    street.setIconSize(QSize(60, 60))
    street.setCheckable(True)
    street.setGeometry(x, y, 60, 60)
    street.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(street)
    street.toggled.connect(lambda checked: on_street_selection(street, "60") if checked else on_street_deselection())
    return street

d1 = _create_60_street(314, 161)
d2 = _create_60_street(489, 161)
d3 = _create_60_street(663, 161)

d4 = _create_60_street(228, 311)
d5 = _create_60_street(401, 311)
d6 = _create_60_street(576, 311)
d7 = _create_60_street(753, 311)

d8 = _create_60_street(140, 461)
d9 = _create_60_street(315, 461)
d10 = _create_60_street(490, 461)
d11 = _create_60_street(664, 461)
d12 = _create_60_street(839, 461)

d13 = _create_60_street(229, 611)
d14 = _create_60_street(402, 611)
d15 = _create_60_street(577, 611)
d16 = _create_60_street(754, 611)
d17 = _create_60_street(925, 611)

d18 = _create_60_street(316, 761)
d19 = _create_60_street(491, 761)
d20 = _create_60_street(665, 761)
d21 = _create_60_street(840, 761)

d22 = _create_60_street(403, 911)
d23 = _create_60_street(578, 911)
d24 = _create_60_street(755, 911)

def _create_120_street(x, y):
    street = QPushButton(b)
    street.setFixedSize(60, 60)
    street.setIcon(QIcon("textures/street_empty_120.png"))
    street.setProperty("type", "street_empty_120")
    street.setIconSize(QSize(60, 60))
    street.setCheckable(True)
    street.setGeometry(x, y, 60, 60)
    street.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(street)
    street.toggled.connect(lambda checked: on_street_selection(street, "120") if checked else on_street_deselection())
    return street

r1 = _create_120_street(402, 161)
r2 = _create_120_street(577, 161)
r3 = _create_120_street(753, 161)

r4 = _create_120_street(315, 311)
r5 = _create_120_street(490, 311)
r6 = _create_120_street(665, 311)
r7 = _create_120_street(840, 311)

r8 = _create_120_street(227, 461)
r9 = _create_120_street(402, 461)
r10 = _create_120_street(577, 461)
r11 = _create_120_street(751, 461)
r12 = _create_120_street(924, 461)

r13 = _create_120_street(142, 611)
r14 = _create_120_street(315, 611)
r15 = _create_120_street(490, 611)
r16 = _create_120_street(665, 611)
r17 = _create_120_street(840, 611)

r18 = _create_120_street(228, 761)
r19 = _create_120_street(403, 761)
r20 = _create_120_street(578, 761)
r21 = _create_120_street(752, 761)

r22 = _create_120_street(315, 911)
r23 = _create_120_street(490, 911)
r24 = _create_120_street(665, 911)


# Slots
def on_slot_selection(slot):
    global selected_slot
    selected_slot = slot
    sselbuyv.show()
    sselbuyc.show()
    sselbuys.hide()
    update_slot_type(slot)
def on_slot_deselection():
    sselbuyv.hide()
    sselbuyc.hide()
    sselbuys.hide()
    #update_slot_type(0)

def _create_slot(x, y):
    slot = QPushButton(b)
    slot.setFixedSize(60, 60)
    slot.setIcon(QIcon("textures/slot_empty.png"))
    slot.setProperty("type", "slot_empty")
    slot.setProperty("adjacent", ())
    slot.setIconSize(QSize(60, 60))
    slot.setGeometry(x, y, 60, 60)
    slot.setCheckable(True)
    slot.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(slot)
    slot.toggled.connect(lambda checked: on_slot_selection(slot) if checked else on_slot_deselection())
    return slot

s1 = _create_slot(358, 136)
s2 = _create_slot(533, 136)
s3 = _create_slot(708, 136)

s4 = _create_slot(271, 185)
s5 = _create_slot(446, 185)
s6 = _create_slot(621, 185)
s7 = _create_slot(795, 185)

s8 = _create_slot(271, 285)
s9 = _create_slot(446, 285)
s10 = _create_slot(621, 285)
s11 = _create_slot(795, 285)

s12 = _create_slot(185, 334)
s13 = _create_slot(359, 334)
s14 = _create_slot(533, 334)
s15 = _create_slot(707, 334)
s16 = _create_slot(881, 334)

s17 = _create_slot(185, 435)
s18 = _create_slot(359, 435)
s19 = _create_slot(533, 435)
s20 = _create_slot(707, 435)
s21 = _create_slot(881, 435)

s22 = _create_slot(100, 485)
s23 = _create_slot(273, 485)
s24 = _create_slot(447, 485)
s25 = _create_slot(622, 485)
s26 = _create_slot(795, 485)
s27 = _create_slot(969, 485)

s28 = _create_slot(100, 585)
s29 = _create_slot(273, 585)
s30 = _create_slot(447, 585)
s31 = _create_slot(622, 585)
s32 = _create_slot(795, 585)
s33 = _create_slot(969, 585)

s34 = _create_slot(185, 635)
s35 = _create_slot(360, 635)
s36 = _create_slot(534, 635)
s37 = _create_slot(709, 635)
s38 = _create_slot(882, 635)

s39 = _create_slot(185, 735)
s40 = _create_slot(360, 735)
s41 = _create_slot(534, 735)
s42 = _create_slot(709, 735)
s43 = _create_slot(882, 735)

s44 = _create_slot(273, 785)
s45 = _create_slot(447, 785)
s46 = _create_slot(621, 785)
s47 = _create_slot(796, 785)

s48 = _create_slot(273, 885)
s49 = _create_slot(447, 885)
s50 = _create_slot(621, 885)
s51 = _create_slot(796, 885)

s52 = _create_slot(360, 935)
s53 = _create_slot(535, 935)
s54 = _create_slot(710, 935)

slotbtngroup = QButtonGroup()
for e in slotlist:
    slotbtngroup.addButton(e)

s1.setProperty("adjacent", (s4, s5))
s2.setProperty("adjacent", (s5, s6))
s3.setProperty("adjacent", (s6, s7))

s4.setProperty("adjacent", (s1, s8))
s5.setProperty("adjacent", (s1, s2, s9))
s6.setProperty("adjacent", (s2, s3, s10))
s7.setProperty("adjacent", (s3, s11))

s8.setProperty("adjacent", (s4, s12, s13))
s9.setProperty("adjacent", (s5, s13, s14))
s10.setProperty("adjacent", (s6, s14, s15))
s11.setProperty("adjacent", (s7, s15, s16))

s12.setProperty("adjacent", (s8, s17))
s13.setProperty("adjacent", (s8, s9, s18))
s14.setProperty("adjacent", (s9, s10, s19))
s15.setProperty("adjacent", (s10, s11, s20))
s16.setProperty("adjacent", (s11, s21))

s17.setProperty("adjacent", (s12, s22, s23))
s18.setProperty("adjacent", (s13, s23, s24))
s19.setProperty("adjacent", (s14, s24, s25))
s20.setProperty("adjacent", (s15, s25, s26))
s21.setProperty("adjacent", (s16, s26, s27))

s22.setProperty("adjacent", (s17, s28))
s23.setProperty("adjacent", (s17, s18, s29))
s24.setProperty("adjacent", (s18, s19, s30))
s25.setProperty("adjacent", (s19, s20, s31))
s26.setProperty("adjacent", (s20, s21, s32))
s27.setProperty("adjacent", (s21, s33))

s28.setProperty("adjacent", (s22, s34))
s29.setProperty("adjacent", (s23, s34, s35))
s30.setProperty("adjacent", (s24, s35, s36))
s31.setProperty("adjacent", (s25, s36, s37))
s32.setProperty("adjacent", (s26, s37, s38))
s33.setProperty("adjacent", (s27, s38))

s34.setProperty("adjacent", (s28, s29, s39))
s35.setProperty("adjacent", (s29, s30, s40))
s36.setProperty("adjacent", (s30, s31, s41))
s37.setProperty("adjacent", (s31, s32, s42))
s38.setProperty("adjacent", (s32, s33, s43))

s39.setProperty("adjacent", (s34, s44))
s40.setProperty("adjacent", (s35, s44, s45))
s41.setProperty("adjacent", (s36, s45, s46))
s42.setProperty("adjacent", (s37, s46, s47))
s43.setProperty("adjacent", (s38, s47))

s44.setProperty("adjacent", (s39, s40, s48))
s45.setProperty("adjacent", (s40, s41, s49))
s46.setProperty("adjacent", (s41, s42, s50))
s47.setProperty("adjacent", (s42, s43, s51))

s48.setProperty("adjacent", (s44, s52))
s49.setProperty("adjacent", (s45, s52, s53))
s50.setProperty("adjacent", (s46, s53, s54))
s51.setProperty("adjacent", (s47, s54))

def _create_vert_street(x, y):
    street = QPushButton(b)
    street.setFixedSize(60, 60)
    street.setIcon(QIcon("textures/street_empty.png"))
    street.setProperty("type", "street_empty")
    street.setIconSize(QSize(60, 60))
    street.setCheckable(True)
    street.setGeometry(x, y, 60, 60)
    street.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(street)
    street.toggled.connect(lambda checked: on_street_selection(street, "vert") if checked else on_street_deselection())
    return street

v1 = _create_vert_street(270, 235)
v2 = _create_vert_street(445, 235)
v3 = _create_vert_street(620, 235)
v4 = _create_vert_street(795, 235)

v5 = _create_vert_street(185, 385)
v6 = _create_vert_street(360, 385)
v7 = _create_vert_street(533, 385)
v8 = _create_vert_street(707, 385)
v9 = _create_vert_street(882, 385)

v10 = _create_vert_street(100, 535)
v11 = _create_vert_street(272, 535)
v12 = _create_vert_street(447, 535)
v13 = _create_vert_street(622, 535)
v14 = _create_vert_street(795, 535)
v15 = _create_vert_street(968, 535)

v16 = _create_vert_street(186, 685)
v17 = _create_vert_street(360, 685)
v18 = _create_vert_street(535, 685)
v19 = _create_vert_street(709, 685)
v20 = _create_vert_street(883, 685)

v21 = _create_vert_street(272, 835)
v22 = _create_vert_street(447, 835)
v23 = _create_vert_street(622, 835)
v24 = _create_vert_street(797, 835)

def _create_60_street(x, y):
    street = QPushButton(b)
    street.setFixedSize(60, 60)
    street.setIcon(QIcon("textures/street_empty_60.png"))
    street.setProperty("type", "street_empty_60") 
    street.setIconSize(QSize(60, 60))
    street.setCheckable(True)
    street.setGeometry(x, y, 60, 60)
    street.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(street)
    street.toggled.connect(lambda checked: on_street_selection(street, "60") if checked else on_street_deselection())
    return street

d1 = _create_60_street(314, 161)
d2 = _create_60_street(489, 161)
d3 = _create_60_street(663, 161)

d4 = _create_60_street(228, 311)
d5 = _create_60_street(401, 311)
d6 = _create_60_street(576, 311)
d7 = _create_60_street(753, 311)

d8 = _create_60_street(140, 461)
d9 = _create_60_street(315, 461)
d10 = _create_60_street(490, 461)
d11 = _create_60_street(664, 461)
d12 = _create_60_street(839, 461)

d13 = _create_60_street(229, 611)
d14 = _create_60_street(402, 611)
d15 = _create_60_street(577, 611)
d16 = _create_60_street(754, 611)
d17 = _create_60_street(925, 611)

d18 = _create_60_street(316, 761)
d19 = _create_60_street(491, 761)
d20 = _create_60_street(665, 761)
d21 = _create_60_street(840, 761)

d22 = _create_60_street(403, 911)
d23 = _create_60_street(578, 911)
d24 = _create_60_street(755, 911)

def _create_120_street(x, y):
    street = QPushButton(b)
    street.setFixedSize(60, 60)
    street.setIcon(QIcon("textures/street_empty_120.png"))
    street.setProperty("type", "street_empty_120")
    street.setIconSize(QSize(60, 60))
    street.setCheckable(True)
    street.setGeometry(x, y, 60, 60)
    street.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(street)
    street.toggled.connect(lambda checked: on_street_selection(street, "120") if checked else on_street_deselection())
    return street

r1 = _create_120_street(402, 161)
r2 = _create_120_street(577, 161)
r3 = _create_120_street(753, 161)

r4 = _create_120_street(315, 311)
r5 = _create_120_street(490, 311)
r6 = _create_120_street(665, 311)
r7 = _create_120_street(840, 311)

r8 = _create_120_street(227, 461)
r9 = _create_120_street(402, 461)
r10 = _create_120_street(577, 461)
r11 = _create_120_street(751, 461)
r12 = _create_120_street(924, 461)

r13 = _create_120_street(142, 611)
r14 = _create_120_street(315, 611)
r15 = _create_120_street(490, 611)
r16 = _create_120_street(665, 611)
r17 = _create_120_street(840, 611)

r18 = _create_120_street(228, 761)
r19 = _create_120_street(403, 761)
r20 = _create_120_street(578, 761)
r21 = _create_120_street(752, 761)

r22 = _create_120_street(315, 911)
r23 = _create_120_street(490, 911)
r24 = _create_120_street(665, 911)


# Slots
def on_slot_selection(slot):
    global selected_slot
    selected_slot = slot
    sselbuyv.show()
    sselbuyc.show()
    sselbuys.hide()
    update_slot_type(slot)
def on_slot_deselection():
    sselbuyv.hide()
    sselbuyc.hide()
    sselbuys.hide()
    #update_slot_type(0)

def _create_slot(x, y):
    slot = QPushButton(b)
    slot.setFixedSize(60, 60)
    slot.setIcon(QIcon("textures/slot_empty.png"))
    slot.setProperty("type", "slot_empty")
    slot.setProperty("adjacent", ())
    slot.setProperty("blocked", False)
    slot.setIconSize(QSize(60, 60))
    slot.setGeometry(x, y, 60, 60)
    slot.setCheckable(True)
    slot.setStyleSheet("""
        QPushButton {
            background: transparent;
            border: none;
        }
        QPushButton:checked {
            background: transparent;
            border: 5px solid white;
            border-radius: 30px;
        }
    """)
    slotlist.append(slot)
    slot.toggled.connect(lambda checked: on_slot_selection(slot) if checked else on_slot_deselection())
    return slot

s1 = _create_slot(358, 136)
s2 = _create_slot(533, 136)
s3 = _create_slot(708, 136)

s4 = _create_slot(271, 185)
s5 = _create_slot(446, 185)
s6 = _create_slot(621, 185)
s7 = _create_slot(795, 185)

s8 = _create_slot(271, 285)
s9 = _create_slot(446, 285)
s10 = _create_slot(621, 285)
s11 = _create_slot(795, 285)

s12 = _create_slot(185, 334)
s13 = _create_slot(359, 334)
s14 = _create_slot(533, 334)
s15 = _create_slot(707, 334)
s16 = _create_slot(881, 334)

s17 = _create_slot(185, 435)
s18 = _create_slot(359, 435)
s19 = _create_slot(533, 435)
s20 = _create_slot(707, 435)
s21 = _create_slot(881, 435)

s22 = _create_slot(100, 485)
s23 = _create_slot(273, 485)
s24 = _create_slot(447, 485)
s25 = _create_slot(622, 485)
s26 = _create_slot(795, 485)
s27 = _create_slot(969, 485)

s28 = _create_slot(100, 585)
s29 = _create_slot(273, 585)
s30 = _create_slot(447, 585)
s31 = _create_slot(622, 585)
s32 = _create_slot(795, 585)
s33 = _create_slot(969, 585)

s34 = _create_slot(185, 635)
s35 = _create_slot(360, 635)
s36 = _create_slot(534, 635)
s37 = _create_slot(709, 635)
s38 = _create_slot(882, 635)

s39 = _create_slot(185, 735)
s40 = _create_slot(360, 735)
s41 = _create_slot(534, 735)
s42 = _create_slot(709, 735)
s43 = _create_slot(882, 735)

s44 = _create_slot(273, 785)
s45 = _create_slot(447, 785)
s46 = _create_slot(621, 785)
s47 = _create_slot(796, 785)

s48 = _create_slot(273, 885)
s49 = _create_slot(447, 885)
s50 = _create_slot(621, 885)
s51 = _create_slot(796, 885)

s52 = _create_slot(360, 935)
s53 = _create_slot(535, 935)
s54 = _create_slot(710, 935)

slotbtngroup = QButtonGroup()
for e in slotlist:
    slotbtngroup.addButton(e)

s1.setProperty("adjacent", (s4, s5))
s2.setProperty("adjacent", (s5, s6))
s3.setProperty("adjacent", (s6, s7))

s4.setProperty("adjacent", (s1, s8))
s5.setProperty("adjacent", (s1, s2, s9))
s6.setProperty("adjacent", (s2, s3, s10))
s7.setProperty("adjacent", (s3, s11))

s8.setProperty("adjacent", (s4, s12, s13))
s9.setProperty("adjacent", (s5, s13, s14))
s10.setProperty("adjacent", (s6, s14, s15))
s11.setProperty("adjacent", (s7, s15, s16))

s12.setProperty("adjacent", (s8, s17))
s13.setProperty("adjacent", (s8, s9, s18))
s14.setProperty("adjacent", (s9, s10, s19))
s15.setProperty("adjacent", (s10, s11, s20))
s16.setProperty("adjacent", (s11, s21))

s17.setProperty("adjacent", (s12, s22, s23))
s18.setProperty("adjacent", (s13, s23, s24))
s19.setProperty("adjacent", (s14, s24, s25))
s20.setProperty("adjacent", (s15, s25, s26))
s21.setProperty("adjacent", (s16, s26, s27))

s22.setProperty("adjacent", (s17, s28))
s23.setProperty("adjacent", (s17, s18, s29))
s24.setProperty("adjacent", (s18, s19, s30))
s25.setProperty("adjacent", (s19, s20, s31))
s26.setProperty("adjacent", (s20, s21, s32))
s27.setProperty("adjacent", (s21, s33))

s28.setProperty("adjacent", (s22, s34))
s29.setProperty("adjacent", (s23, s34, s35))
s30.setProperty("adjacent", (s24, s35, s36))
s31.setProperty("adjacent", (s25, s36, s37))
s32.setProperty("adjacent", (s26, s37, s38))
s33.setProperty("adjacent", (s27, s38))

s34.setProperty("adjacent", (s28, s29, s39))
s35.setProperty("adjacent", (s29, s30, s40))
s36.setProperty("adjacent", (s30, s31, s41))
s37.setProperty("adjacent", (s31, s32, s42))
s38.setProperty("adjacent", (s32, s33, s43))

s39.setProperty("adjacent", (s34, s44))
s40.setProperty("adjacent", (s35, s44, s45))
s41.setProperty("adjacent", (s36, s45, s46))
s42.setProperty("adjacent", (s37, s46, s47))
s43.setProperty("adjacent", (s38, s47))

s44.setProperty("adjacent", (s39, s40, s48))
s45.setProperty("adjacent", (s40, s41, s49))
s46.setProperty("adjacent", (s41, s42, s50))
s47.setProperty("adjacent", (s42, s43, s51))

s48.setProperty("adjacent", (s44, s52))
s49.setProperty("adjacent", (s45, s52, s53))
s50.setProperty("adjacent", (s46, s53, s54))
s51.setProperty("adjacent", (s47, s54))


# SIDE BAR
s = QWidget()
s.setFixedSize(700, 1000)
s.setStyleSheet("""
    QWidget {
        border: none;
        border-radius: 25px;
        background-color: #1f1f1f;
    }
""")
slay = QVBoxLayout(s)

ssel = QWidget(s)
ssellay = QVBoxLayout()

ssellablay = QHBoxLayout()
ssellab  = QPushButton("No Selection")
ssellab.setIcon(QIcon("textures/slot_empty.png"))
ssellab.setIconSize(QSize(50,50))
ssellab.setStyleSheet("""
    QPushButton {
        font-size: 40px;
        color: white;
        font-family: 'Inter';
        font-weight: bold;
        text-align: left;
        padding-left: 10px;        
        border: none;
        background-color: #808080;
        border-radius: 15px;
    }
""")
ssellablay.addWidget(ssellab)

def update_balance():
    
    global current_player
    if current_player == 1:
        sbalmat1.setText(str(balance_brick1))
        sbalmat2.setText(str(balance_fabric1))
        sbalmat3.setText(str(balance_ore1))
        sbalmat4.setText(str(balance_wheat1))
        sbalmat5.setText(str(balance_wood1))
    elif current_player == 2:
        sbalmat1.setText(str(balance_brick2))
        sbalmat2.setText(str(balance_fabric2))
        sbalmat3.setText(str(balance_ore2))
        sbalmat4.setText(str(balance_wheat2))
        sbalmat5.setText(str(balance_wood2))
    elif current_player == 3:
        sbalmat1.setText(str(balance_brick3))
        sbalmat2.setText(str(balance_fabric3))
        sbalmat3.setText(str(balance_ore3))
        sbalmat4.setText(str(balance_wheat3))
        sbalmat5.setText(str(balance_wood3))
    elif current_player == 4:
        sbalmat1.setText(str(balance_brick4))
        sbalmat2.setText(str(balance_fabric4))
        sbalmat3.setText(str(balance_ore4))
        sbalmat4.setText(str(balance_wheat4))
        sbalmat5.setText(str(balance_wood4))

def block_adj_slots(slot: QPushButton):
    adj = slot.property("adjacent")
    for a in adj:
        a.setProperty("blocked", True)
def on_buy(slot: QPushButton, type):
    global street_rotation, current_player
    global balance_brick1, balance_fabric1, balance_ore1, balance_wheat1, balance_wood1
    global balance_brick2, balance_fabric2, balance_ore2, balance_wheat2, balance_wood2
    global balance_brick3, balance_fabric3, balance_ore3, balance_wheat3, balance_wood3
    global balance_brick4, balance_fabric4, balance_ore4, balance_wheat4, balance_wood4

    blocked = slot.property("blocked")
    if current_player == 1:
        if balance_brick1 >= 1 and balance_wood1 >= 1:
            if type  == "s":
                if street_rotation == "vert":
                    slot.setIcon(QIcon("textures/street_red.png"))
                    slot.setProperty("type", "street_red")
                    balance_brick1 = balance_brick1 - 1
                    balance_wood1 = balance_wood1 - 1
                    update_balance()
                elif street_rotation == "60":
                    slot.setIcon(QIcon("textures/street_red_60.png"))
                    slot.setProperty("type", "street_red_60")
                    balance_brick1 = balance_brick1 - 1
                    balance_wood1 = balance_wood1 - 1
                    update_balance()
                elif street_rotation == "120":
                    slot.setIcon(QIcon("textures/street_red_120.png"))
                    slot.setProperty("type", "street_red_120")
                    balance_brick1 = balance_brick1 - 1
                    balance_wood1 = balance_wood1 - 1
                    update_balance()
            if balance_brick1 >= 1 and balance_fabric1 >= 1 and balance_wheat1 >= 1 and balance_wood1 >= 1:
                if blocked == False:
                    if type  == "v":
                        slot.setIcon(QIcon("textures/village_red.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "village_red")
                        balance_brick1 = balance_brick1 - 1
                        balance_fabric1 = balance_fabric1 - 1
                        balance_wheat1 = balance_wheat1 - 1
                        balance_wood1 = balance_wood1 - 1
                        update_balance()
                        block_adj_slots(slot)
                        vp1 = vp1 + 1
                        update_vp_bar()
            if balance_ore1 >= 3 and balance_wheat1 >= 2:
                if blocked == False:
                    if type  == "c":
                        slot.setIcon(QIcon("textures/city_red.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "city_red")
                        balance_ore1 = balance_ore1 - 3
                        balance_wheat1 = balance_wheat1 - 2
                        update_balance()
                        block_adj_slots(slot)
                        vp1 = vp1 + 2
                        update_vp_bar()
            update_slot_type(slot)

    elif current_player == 2:
        if balance_brick2 >= 1 and balance_wood2 >= 1:
            if type  == "s":
                if street_rotation == "vert":
                    slot.setIcon(QIcon("textures/street_blue.png"))
                    slot.setProperty("type", "street_blue")
                    balance_brick2 = balance_brick2 - 1
                    balance_wood2 = balance_wood2 - 1
                    update_balance()
                elif street_rotation == "60":
                    slot.setIcon(QIcon("textures/street_blue_60.png"))
                    slot.setProperty("type", "street_blue_60")
                    balance_brick2 = balance_brick2 - 1
                    balance_wood2 = balance_wood2 - 1
                    update_balance()
                elif street_rotation == "120":
                    slot.setIcon(QIcon("textures/street_blue_120.png"))
                    slot.setProperty("type", "street_blue_120")
                    balance_brick2 = balance_brick2 - 1
                    balance_wood2 = balance_wood2 - 1
                    update_balance()
            if balance_brick2 >= 1 and balance_fabric2 >= 1 and balance_wheat2 >= 1 and balance_wood2 >= 1:
                if blocked == False:
                    if type  == "v":
                        slot.setIcon(QIcon("textures/village_blue.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "village_blue")
                        balance_brick2 = balance_brick2 - 1
                        balance_fabric2 = balance_fabric2 - 1
                        balance_wheat2 = balance_wheat2 - 1
                        balance_wood2 = balance_wood2 - 1
                        update_balance()
                        block_adj_slots(slot)
                        vp2 = vp2 + 1
                        update_vp_bar()
            if balance_ore2 >= 3 and balance_wheat2 >= 2:
                if blocked == False:
                    if type  == "c":
                        slot.setIcon(QIcon("textures/city_blue.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "city_blue")
                        balance_ore2 = balance_ore2 - 3
                        balance_wheat2 = balance_wheat2 - 2
                        update_balance()
                        block_adj_slots(slot)
                        vp2 = vp2 + 2
                        update_vp_bar()
            update_slot_type(slot)

    elif current_player == 3:
        if balance_brick3 >= 1 and balance_wood3 >= 1:
            if type  == "s":
                if street_rotation == "vert":
                    slot.setIcon(QIcon("textures/street_green.png"))
                    slot.setProperty("type", "street_green")
                    balance_brick3 = balance_brick3 - 1
                    balance_wood3 = balance_wood3 - 1
                    update_balance()
                elif street_rotation == "60":
                    slot.setIcon(QIcon("textures/street_green_60.png"))
                    slot.setProperty("type", "street_green_60")
                    balance_brick3 = balance_brick3 - 1
                    balance_wood3 = balance_wood3 - 1
                    update_balance()
                elif street_rotation == "120":
                    slot.setIcon(QIcon("textures/street_green_120.png"))
                    slot.setProperty("type", "street_green_120")
                    balance_brick3 = balance_brick3 - 1
                    balance_wood3 = balance_wood3 - 1
                    update_balance()
            if balance_brick3 >= 1 and balance_fabric3 >= 1 and balance_wheat3 >= 1 and balance_wood3 >= 1:
                if blocked == False:
                    if type  == "v":
                        slot.setIcon(QIcon("textures/village_green.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "village_green")
                        balance_brick3 = balance_brick3 - 1
                        balance_fabric3 = balance_fabric3 - 1
                        balance_wheat3 = balance_wheat3 - 1
                        balance_wood3 = balance_wood3 - 1
                        update_balance()
                        block_adj_slots(slot)
                        vp3 = vp3 + 1
                        update_vp_bar()
            if balance_ore3 >= 3 and balance_wheat3 >= 2:
                if blocked == False:
                    if type  == "c":
                        slot.setIcon(QIcon("textures/city_green.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "city_green")
                        balance_ore3 = balance_ore3 - 3
                        balance_wheat3 = balance_wheat3 - 2
                        update_balance()
                        block_adj_slots(slot)
                        vp3 = vp3 + 2
                        update_vp_bar()
            update_slot_type(slot)

    elif current_player == 4:
        if balance_brick4 >= 1 and balance_wood4 >= 1:
            if type  == "s":
                if street_rotation == "vert":
                    slot.setIcon(QIcon("textures/street_yellow.png"))
                    slot.setProperty("type", "street_yellow")
                    balance_brick4 = balance_brick4 - 1
                    balance_wood4 = balance_wood4 - 1
                    update_balance()
                elif street_rotation == "60":
                    slot.setIcon(QIcon("textures/street_yellow_60.png"))
                    slot.setProperty("type", "street_yellow_60")
                    balance_brick4 = balance_brick4 - 1
                    balance_wood4 = balance_wood4 - 1
                    update_balance()
                elif street_rotation == "120":
                    slot.setIcon(QIcon("textures/street_yellow_120.png"))
                    slot.setProperty("type", "street_yellow_120")
                    balance_brick4 = balance_brick4 - 1
                    balance_wood4 = balance_wood4 - 1
                    update_balance()
            if balance_brick4 >= 1 and balance_fabric4 >= 1 and balance_wheat4 >= 1 and balance_wood4 >= 1:
                if blocked == False:
                    if type  == "v":
                        slot.setIcon(QIcon("textures/village_yellow.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "village_yellow")
                        balance_brick4 = balance_brick4 - 1
                        balance_fabric4 = balance_fabric4 - 1
                        balance_wheat4 = balance_wheat4 - 1
                        balance_wood4 = balance_wood4 - 1
                        update_balance()
                        block_adj_slots(slot)
                        vp4 = vp4 + 1
                        update_vp_bar()
            if balance_ore4 >= 3 and balance_wheat4 >= 2:
                if blocked == False:
                    if type  == "c":
                        slot.setIcon(QIcon("textures/city_yellow.png"))
                        slot.setIconSize(QSize(60, 60))
                        slot.setProperty("type", "city_yellow")
                        balance_ore4 = balance_ore4 - 3
                        balance_wheat4 = balance_wheat4 - 2
                        update_balance()
                        block_adj_slots(slot)
                        vp4 = vp4 + 2
                        update_vp_bar()
            update_slot_type(slot)

def update_buylay():
    global current_player
    player = current_player
    if player == 1:
        sselbuyvbtn.setIcon(QIcon("textures/village_red.png"))
        sselbuycbtn.setIcon(QIcon("textures/city_red.png"))
        sselbuysbtn.setIcon(QIcon("textures/street_red.png"))
        sbalscp.setIcon(QIcon("textures/card_red.png"))
    if player == 2:
        sselbuyvbtn.setIcon(QIcon("textures/village_blue.png"))
        sselbuycbtn.setIcon(QIcon("textures/city_blue.png"))
        sselbuysbtn.setIcon(QIcon("textures/street_blue.png"))
        sbalscp.setIcon(QIcon("textures/card_blue.png"))
    if player == 3:
        sselbuyvbtn.setIcon(QIcon("textures/village_green.png"))
        sselbuycbtn.setIcon(QIcon("textures/city_green.png"))
        sselbuysbtn.setIcon(QIcon("textures/street_green.png"))
        sbalscp.setIcon(QIcon("textures/card_green.png"))
    if player == 4:
        sselbuyvbtn.setIcon(QIcon("textures/village_yellow.png"))
        sselbuycbtn.setIcon(QIcon("textures/city_yellow.png"))
        sselbuysbtn.setIcon(QIcon("textures/street_yellow.png"))
        sbalscp.setIcon(QIcon("textures/card_yellow.png"))




sselbuylayslot = QHBoxLayout()

sselbuyv = QWidget()
sselbuyv.hide()
sselbuyv.setFixedHeight(120)
sselbuyv.setStyleSheet("""
        QWidget {       
            border: none;
            background-color: #808080;
            border-radius: 15px;
        }
        QPushButton {
            font-size: 30px;
            color: white;
            font-family: 'Inter';
            font-weight: bold;
            text-align: left;     
            border: none;
            background-color: transparent;
            border-radius: 15px;
            icon-size: 30px;
        }
    """)
sselbuyvlay = QHBoxLayout()
sselbuyvbtn = QPushButton(sselbuyv)
sselbuyvbtn.setIcon(QIcon("textures/village_red.png"))
sselbuyvbtn.setIconSize(QSize(75,75))
sselbuyvbtn.clicked.connect(lambda: on_buy(selected_slot, "v"))
sselbuyvlay.addWidget(sselbuyvbtn)
sselbuyvcostlay = QHBoxLayout()
sselbuyvcostlay1 = QVBoxLayout()
sselbuyvcostlay2 = QVBoxLayout()
sselbuyvcost1  = QPushButton("1")
sselbuyvcost1.setIcon(QIcon("textures/brick.png"))
sselbuyvcostlay1.addWidget(sselbuyvcost1)
sselbuyvcost2  = QPushButton("1")
sselbuyvcost2.setIcon(QIcon("textures/fabric.png"))
sselbuyvcostlay1.addWidget(sselbuyvcost2)
sselbuyvcost3  = QPushButton("1")
sselbuyvcost3.setIcon(QIcon("textures/wheat.png"))
sselbuyvcostlay2.addWidget(sselbuyvcost3)
sselbuyvcost4  = QPushButton("1")
sselbuyvcost4.setIcon(QIcon("textures/wood.png"))
sselbuyvcostlay2.addWidget(sselbuyvcost4)
sselbuyvcostlay.addLayout(sselbuyvcostlay1)
sselbuyvcostlay.addLayout(sselbuyvcostlay2)
sselbuyvlay.addLayout(sselbuyvcostlay)
sselbuyv.setLayout(sselbuyvlay)


sselbuyc = QWidget()
sselbuyc.hide()
sselbuyc.setFixedHeight(120)
sselbuyc.setStyleSheet(sselbuyv.styleSheet())
sselbuyclay = QHBoxLayout()
sselbuycbtn = QPushButton(sselbuyc)
sselbuycbtn.setIcon(QIcon("textures/city_red.png"))
sselbuycbtn.setIconSize(QSize(75,75))
sselbuycbtn.clicked.connect(lambda: on_buy(selected_slot, "c"))
sselbuyclay.addWidget(sselbuycbtn)
sselbuyccostlay = QVBoxLayout()
sselbuyccost1  = QPushButton("3")
sselbuyccost1.setIcon(QIcon("textures/ore.png"))
sselbuyccostlay.addWidget(sselbuyccost1)
sselbuyccost2  = QPushButton("2")
sselbuyccost2.setIcon(QIcon("textures/wheat.png"))
sselbuyccostlay.addWidget(sselbuyccost2)
sselbuyclay.addLayout(sselbuyccostlay)
sselbuyc.setLayout(sselbuyclay)

sselbuys = QWidget()
sselbuys.hide()
sselbuys.setFixedHeight(120)
sselbuys.setStyleSheet(sselbuyv.styleSheet())
sselbuyslay = QHBoxLayout()
sselbuysbtn = QPushButton(sselbuys)
sselbuysbtn.setIcon(QIcon("textures/street_red.png"))
sselbuysbtn.setIconSize(QSize(75,75))
sselbuysbtn.clicked.connect(lambda: on_buy(selected_street, "s"))
sselbuyslay.addWidget(sselbuysbtn)
sselbuyscostlay = QVBoxLayout()
sselbuyscost1  = QPushButton("1")
sselbuyscost1.setIcon(QIcon("textures/brick.png"))
sselbuyscostlay.addWidget(sselbuyscost1)
sselbuyscost2  = QPushButton("1")
sselbuyscost2.setIcon(QIcon("textures/wood.png"))
sselbuyscostlay.addWidget(sselbuyscost2)
sselbuyslay.addLayout(sselbuyscostlay)
sselbuys.setLayout(sselbuyslay)

sselbuylayslot.addWidget(sselbuyv)
sselbuylayslot.addWidget(sselbuyc)
sselbuylayslot.addWidget(sselbuys)

ssellay.addLayout(ssellablay)
ssellay.addLayout(sselbuylayslot)
ssel.setLayout(ssellay)

sbal = QWidget(s)
sbal.setMaximumHeight(350)
sballay = QVBoxLayout()
sbal.setLayout(sballay)

sbalhlay = QHBoxLayout()
sbalh = QPushButton("Balance")
sbalh.setIcon(QIcon("textures/star.png"))
sbalh.setIconSize(QSize(50,50))
sbalh.setStyleSheet(ssellab.styleSheet())
sbalhlay.addWidget(sbalh)

sbalt = QHBoxLayout()

sbalmat = QWidget()
sbalmat.setStyleSheet(sselbuyv.styleSheet())
sbalmatlay = QHBoxLayout()
sbalmatlay1 = QVBoxLayout()
sbalmatlay2 = QVBoxLayout()
sbalmat1  = QPushButton(str(balance_brick1))
sbalmat1.setIcon(QIcon("textures/brick.png"))
sbalmatlay1.addWidget(sbalmat1)
sbalmat2  = QPushButton(str(balance_fabric1))
sbalmat2.setIcon(QIcon("textures/fabric.png"))
sbalmatlay1.addWidget(sbalmat2)
sbalmat3  = QPushButton(str(balance_ore1))
sbalmat3.setIcon(QIcon("textures/ore.png"))
sbalmatlay1.addWidget(sbalmat3)
sbalmat4  = QPushButton(str(balance_wheat1))
sbalmat4.setIcon(QIcon("textures/wheat.png"))
sbalmatlay2.addWidget(sbalmat4)
sbalmat5  = QPushButton(str(balance_wood1))
sbalmat5.setIcon(QIcon("textures/wood.png"))
sbalmatlay2.addWidget(sbalmat5)
sbalmatlay.addLayout(sbalmatlay1)
sbalmatlay.addLayout(sbalmatlay2)
sbalmat.setLayout(sbalmatlay)

sbalsc = QWidget()
sbalsc.setStyleSheet(sselbuyv.styleSheet())
sbalsclay = QHBoxLayout()
sbalscp = QPushButton()
sbalscp.setIcon(QIcon("textures/card_red.png"))
sbalscp.setIconSize(QSize(75,75))
sbalsclay.addWidget(sbalscp)
sbalsclay2 = QVBoxLayout()
sbalsc1  = QPushButton("1")
sbalsc1.setIcon(QIcon("textures/fabric.png"))
sbalsclay2.addWidget(sbalsc1)
sbalsc2  = QPushButton("1")
sbalsc2.setIcon(QIcon("textures/ore.png"))
sbalsclay2.addWidget(sbalsc2)
sbalsc3  = QPushButton("1")
sbalsc3.setIcon(QIcon("textures/wheat.png"))
sbalsclay2.addWidget(sbalsc3)
sbalsclay.addLayout(sbalsclay2)
sbalsc.setLayout(sbalsclay)

def on_card_click(item: QListWidgetItem):
    global current_player, vp1, vp2, vp3, vp4

    if current_player == 1:
        lw = sbalscl1
    elif current_player == 2:
        lw = sbalscl2
    elif current_player == 3:
        lw = sbalscl3
    elif current_player == 4:
        lw = sbalscl4

    name = item.text()
    if name == "+1 Victory Point":
        if current_player == 1:
            vp1 += 1
        elif current_player == 2:
            vp2 += 1
        elif current_player == 3:
            vp3 += 1
        elif current_player == 4:
            vp4 += 1
        update_vp_bar()

        row = lw.row(item)
        lw.takeItem(row)

sbalscl = QWidget()
sbalscl.setStyleSheet(sselbuyv.styleSheet())
sbalscllay = QHBoxLayout()

def _create_card_list():
    lw = QListWidget()
    lw.setStyleSheet("""
    QListWidget {
        background-color: #808080;
        color: white;
        border-radius: 15px;
        font-family: 'Inter';
        font-weight: bold;
        font-size: 30px;
        padding: 2px;
    }
    QListWidget::item {
        background-color: #1f1f1f;
        border-radius: 15px;
        color: white;
        border: 5px solid transparent; 
        border-radius: 15px;
        height: 35px; 
        width: 35px;
        padding: 10px;
    }
    """)
    lw.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
    lw.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    lw.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    lw.setDragEnabled(False)
    lw.setAcceptDrops(False)
    lw.setDropIndicatorShown(False)
    lw.itemClicked.connect(on_card_click)
    sbalscllay.addWidget(lw)
    return lw

def update_card_list():
    if current_player == 1:
        sbalscl1.show()
        sbalscl2.hide()
        sbalscl3.hide()
        sbalscl4.hide()
    elif current_player == 2:
        sbalscl1.hide()
        sbalscl2.show()
        sbalscl3.hide()
        sbalscl4.hide()
    elif current_player == 3:
        sbalscl1.hide()
        sbalscl2.hide()
        sbalscl3.show()
        sbalscl4.hide()
    elif current_player == 4:
        sbalscl1.hide()
        sbalscl2.hide()
        sbalscl3.hide()
        sbalscl4.show()

sbalscl1 = _create_card_list()
sbalscl1.addItem("+1 Victory Point")
sbalscl1.addItem("Knight")

sbalscl2 = _create_card_list()
sbalscl2.addItem("Knight")
sbalscl2.hide()

sbalscl3 = _create_card_list()
sbalscl3.addItem("+1 Victory Point")
sbalscl3.addItem("+1 Victory Point")
sbalscl3.hide()

sbalscl4 = _create_card_list()
sbalscl4.addItem("+1 Victory Point")
sbalscl4.hide()

sbalscl.setLayout(sbalscllay)

def update_vp_bar():
    global current_player
    if current_player == 1:
        sbalvcbar.setValue(vp1)
        sbalvcbar.setFormat(f"{vp1} / {sbalvcbar_total}")
    if current_player == 2:
        sbalvcbar.setValue(vp2)
        sbalvcbar.setFormat(f"{vp2} / {sbalvcbar_total}")
    if current_player == 3:
        sbalvcbar.setValue(vp3)
        sbalvcbar.setFormat(f"{vp3} / {sbalvcbar_total}")
    if current_player == 4:
        sbalvcbar.setValue(vp4)
        sbalvcbar.setFormat(f"{vp4} / {sbalvcbar_total}")


sbalvc = QWidget()
sbalvc.setStyleSheet("""
        QWidget {       
            border: none;
            background-color: #808080;
            border-radius: 15px;
        }
        QPushButton {
            font-size: 30px;
            color: white;
            font-family: 'Inter';
            font-weight: bold;
            text-align: left;     
            border: none;
            background-color: transparent;
            border-radius: 15px;
            icon-size: 30px;
        }
        QProgressBar {
            border: none;
            border-radius: 20px;
            background-color: #1f1f1f;
            font-size: 30px;
            color: white;
            font-weight: bold;
            text-align: center;
            font-family: 'Inter';
        }
        QProgressBar::chunk {
            background-color: #FFDE68;
            margin: 0px;
            border-radius: 20px;
        }
    """)
sbalvclay = QHBoxLayout()
sbalvcbar = QProgressBar()
sbalvcbar.setTextVisible(True)
sbalvcbar_total = 12
sbalvcbar.setFormat(f"{vp1} / {sbalvcbar_total}")
sbalvcbar.setMinimum(0)
sbalvcbar.setMaximum(sbalvcbar_total)
sbalvcbar.setValue(vp1)
sbalvclay.addWidget(sbalvcbar)
sbalvc.setLayout(sbalvclay)

sbalt.addWidget(sbalmat)
sbalt.addWidget(sbalsc)
sbalt.addWidget(sbalscl)

sballay.addLayout(sbalhlay)
sballay.addLayout(sbalt)
sballay.addWidget(sbalvc)


def translate_n2dice(n):
    if n == 1:
        return "⚀"
    elif n == 2:
        return "⚁"
    elif n == 3:
        return "⚂"
    elif n == 4:
        return "⚃"
    elif n == 5:
        return "⚄"
    elif n == 6:
        return "⚅"
    
def use_dice():
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    r = n1 + n2
    sdice1.setText(translate_n2dice(n1))
    sdice2.setText(translate_n2dice(n2))
    sdicer.setText(str(r))

sdice = QWidget(s)
sdicelay = QHBoxLayout()
sdice.setLayout(sdicelay)

sdiced = QWidget()
sdiced.setStyleSheet("background-color: #808080; border-radius: 15px;")
sdicedlay = QHBoxLayout()
sdiced.setLayout(sdicedlay)

sdices = QPushButton("🎲")
sdices.setFixedSize(100,100)
sdices.setStyleSheet("font-size: 60px; color: white; font-family: 'Inter'; background-color: #5DB55A; border-radius: 15px;")
sdices.clicked.connect(use_dice)

sdice1 = QPushButton()
sdice1.setFixedSize(100,100)
sdice1.setStyleSheet("font-size: 70px; color: white; font-family: 'Inter'; background-color: #1f1f1f; border-radius: 15px;")

sdicep = QPushButton("+")
sdicep.setFixedSize(50,100)
sdicep.setStyleSheet("font-size: 50px; color: white; font-family: 'Inter'; background-color: #1f1f1f; border-radius: 15px;")

sdice2 = QPushButton()
sdice2.setFixedSize(100,100)
sdice2.setStyleSheet("font-size: 70px; color: white; font-family: 'Inter'; background-color: #1f1f1f; border-radius: 15px;")

sdicee = QPushButton("=")
sdicee.setFixedSize(50,100)
sdicee.setStyleSheet("font-size: 50px; color: white; font-family: 'Inter'; background-color: #1f1f1f; border-radius: 15px;")

sdicer = QPushButton()
sdicer.setFixedSize(100,100)
sdicer.setStyleSheet("font-size: 50px; color: white; font-family: 'Inter'; background-color: #5DB2FF; border-radius: 15px; font-weight: bold;")

sdicedlay.addWidget(sdices)
sdicedlay.addWidget(sdice1)
sdicedlay.addWidget(sdicep)
sdicedlay.addWidget(sdice2)
sdicedlay.addWidget(sdicee)
sdicedlay.addWidget(sdicer)

sdicelay.addWidget(sdiced)

def pass_on_turn():
    global current_player
    if current_player <= 3:
        set_current_player(current_player + 1)
    elif current_player == 4:
        set_current_player(1)


splay = QWidget(s)
splaylay = QVBoxLayout()
splay.setLayout(splaylay)

spassb = QWidget()
spassb.setStyleSheet("background-color: #808080; border-radius: 15px;")
spassblay = QHBoxLayout()
spassb.setLayout(spassblay)

spassbtn = QPushButton("Pass on turn")
spassbtn.setStyleSheet("font-size: 50px; color: white; font-family: 'Inter'; background-color: #5DB55A; border-radius: 15px; font-weight: bold;")
spassbtn.clicked.connect(pass_on_turn)
spassblay.addWidget(spassbtn)

splaym = QWidget()
splaym.setStyleSheet("""
    QWidget {
        background-color: #808080;
        border-radius: 15px;
    }
    QPushButton {
        font-size: 30px;
        color: white;
        font-family: 'Inter';
        font-weight: bold;
        text-align: left;     
        border: none;
        background-color: transparent;
        border-radius: 15px;
        icon-size: 50px;
    }
    QPushButton:checked {
        font-size: 30px;
        color: white;
        font-family: 'Inter';
        font-weight: bold;
        text-align: left;     
        border: none;
        background-color: #1f1f1f;
        border-radius: 15px;
        icon-size: 50px;
    }
""")
splaymlay = QHBoxLayout()
splaym.setLayout(splaymlay)

splay1 = QPushButton("Red")
splay1.setCheckable(True)
splay1.setChecked(True)
#splay1.setDisabled(True)
splay1.setIcon(QIcon("textures/player_red.png"))


splay2 = QPushButton("Blue")
splay2.setCheckable(True)
#splay2.setDisabled(True)
splay2.setIcon(QIcon("textures/player_blue.png"))

splay3 = QPushButton("Green")
splay3.setCheckable(True)
#splay3.setDisabled(True)
splay3.setIcon(QIcon("textures/player_green.png"))

splay4 = QPushButton("Yellow")
splay4.setCheckable(True)
#splay4.setDisabled(True)
splay4.setIcon(QIcon("textures/player_yellow.png"))




splayers = QButtonGroup()
splayers.addButton(splay1)
splayers.addButton(splay2)
splayers.addButton(splay3)
splayers.addButton(splay4)

splaymlay.addWidget(splay1)
splaymlay.addWidget(splay2)
splaymlay.addWidget(splay3)
splaymlay.addWidget(splay4)

splaylay.addWidget(spassb)
splaylay.addWidget(splaym)

slay.addWidget(ssel,  alignment=Qt.AlignmentFlag.AlignTop)
slay.addWidget(sbal)
slay.addWidget(sdice)
slay.addWidget(splay, alignment=Qt.AlignmentFlag.AlignBottom)


main_layout.addWidget(b)
main_layout.addWidget(s, alignment=Qt.AlignmentFlag.AlignRight)


window.setCentralWidget(widget)
window.show()
sys.exit(app.exec())