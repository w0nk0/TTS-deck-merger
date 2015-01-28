__author__ = 'nico'

default_style = """
/* DARK style*/

* { alternate-background-color: #222; background: #111; border-color: #630; border-width: 2px; color: #aaa}
QWidget { background: #222; }
QTextEdit,QStatusBar { background: #333; border-color: #630; border-style: inset; border-width: 1px; }
QPushButton { background: #666; color: #fa0; padding:  1px; height: 1.25em; }
QPushButton:disabled, QLineEdit:disabled { background: #444; color: #a60; padding:  1px; height: 1.25em; }
xQPushButton { background: #333; color: #fa0; padding:  1px; height: 1.25em; }
QLineEdit, QCheckBox, QComboBox, QComboBox QAbstractItemView { color: #fc8; background: #333; }
QLabel { color: #fa0; background: #222; }
QLabel#lbl_header { color: #fa0; background: #444; }
QLineEdit { background: #000; color: #f80; border-style:none; }
QPushButton, QLabel { border-width: 2px; border-radius: 2px; padding: 2px;  min-width: 3em;}
QComboBox { max-width: 9.5em; background-color: #333;  }
QAbstractItemView { background-color: #333; }
QCheckBox { alternate-background-color: #222; spacing: 5px;}
QTextEdit { color: #ffe; }

"""

dark_orange = """
QToolTip
{
     border: 1px solid black;
     background-color: #ffa02f;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

QWidget
{
    color: #f1c181;
    background-color: #323232;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);
    color: #000000;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #ffaa00;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434/*,
        stop:0.2 #343434,
        stop:0.1 #ffaa00*/
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #000000;
}

QWidget:disabled
{
    color: #404040;
    background-color: #323232;
}

QAbstractItemView
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);
}

QWidget:focus
{
    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/
}

QLineEdit
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
    padding: 1px;
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QPushButton
{
    color: #f1c181;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 12px;
    padding-left: 5px;
    padding-right: 5px;
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}

QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QComboBox:hover,QPushButton:hover
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}


QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
    selection-background-color: #ffaa00;
}

QComboBox QAbstractItemView
{
    border: 2px solid darkgray;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 0px;
     border-left-color: darkgray;
     border-left-style: solid; /* just a single line */
     border-top-right-radius: 3px; /* same radius as the QComboBox */
     border-bottom-right-radius: 3px;
 }

QComboBox::down-arrow
{
     image: url(:/down_arrow.png);
}

QGroupBox:focus
{
border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QTextEdit:focus
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
     height: 7px;
     margin: 0px 16px 0 16px;
}

QScrollBar::handle:horizontal
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
      subcontrol-position: right;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
      width: 7px;
      margin: 16px 0 16px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
      height: 14px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);
      height: 14px;
      subcontrol-position: top;
      subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}

QTextEdit
{
    background-color: #242424;
}

QPlainTextEdit
{
    background-color: #242424;
}

QHeaderView::section
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
color: #414141;
}

QDockWidget::title
{
    text-align: center;
    spacing: 3px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button, QDockWidget::float-button
{
    text-align: center;
    spacing: 1px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
{
    background: #242424;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
{
    padding: 1px -1px -1px 1px;
}

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QToolBar::handle
{
     spacing: 3px; /* spacing between items in the tool bar */
     background: url(:/images/handle.png);
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk
{
    background-color: #d7801a;
    width: 2.15px;
    margin: 0.5px;
}

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #444;
    border-bottom-style: none;
    background-color: #323232;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}

QTabWidget::pane {
    border: 1px solid #444;
    top: 1px;
}

QTabBar::tab:last
{
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
 margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */


    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;
}

QTabBar::tab:!selected:hover
{
    /*border-top: 2px solid #ffaa00;
    padding-bottom: 3px;*/
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);
}

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    border-radius: 6px;
}

QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #ffaa00,
        stop: 0.3 #323232
    );
}

QCheckBox::indicator{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 6px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #ffaa00;
}

QCheckBox::indicator:checked
{
    image:url(:/images/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}
"""

level4 = """
/* Basic Palette
border styles: dashed | dot-dash | dot-dot-dash | dotted | double | groove | inset | outset | ridge | solid | none
*/

/* Set the selection colors for all widgets. */
QWidget
{
	color: #111111;
	border: 0px solid #737373;
	background: #727272;
	selection-color: #cccccc;
	selection-background-color: #686868;
	padding: 0px;
	margin: 0px;
}

QMainWindow
{
	background: #727272;
	padding: 0px;
	margin: 0px;
	border: 0px solid #1a1a1a;
}

QMainWindow::separator:horizontal
{
    background: #ff0000;
    max-width: 2px;
	width: 2px;
	border-top: 1px solid #393939;
	border-bottom: 1px solid #959595;
}

QMainWindow::separator:vertical
{
    background: #ff0000;
    max-height: 2px;
	height: 2px;
	border-left: 1px solid #393939;
	border-right: 1px solid #959595;
}

QMainWindow::separator:hover
{
    background: #686868;
}

/* Customize check boxes. */
QCheckBox
{
    spacing: 5px;
   	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	max-width: 13px;
    max-height: 13px;
}

QCheckBox::indicator
{
    width: 13px;
    height: 13px;
}


QCheckBox::indicator:checked
{
    image: url(:/checkbox_checked);
}

QCheckBox::indicator:checked:hover
{
    image: url(:/checkbox_checked_hover);
}

QCheckBox::indicator:checked:pressed
{
    image: url(:/checkbox_checked_pressed);
}

/* Combobox */
QComboBox
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	color: #c8c8c8;
	border-top-left-radius: 4px; /* same radius as the QComboBox */
	border-bottom-left-radius: 4px;
	border-top-right-radius: 4px;
	border-bottom-right-radius: 4px;
	padding: 1px 18px 1px 13px;
	min-width: 6em;
	max-height: 15px;
}

/* The popup */
QComboBox QAbstractItemView {
	border: 1px solid #303030;
	background: #212121;
	selection-background-color: #484848;
	selection-color: #ffffff;
	color: #c8c8c8;
}

QComboBox:editable
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
}

QComboBox:!editable, QComboBox::drop-down:editable
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);

}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on
{
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);

}

QComboBox:on
{
	/* shift the text when the popup opens */
	padding-top: 3px;
	padding-left: 4px;
	border: 1px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
}

/* Drop down button */
QComboBox::drop-down
{
	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: 15px;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	border: 0px solid #818181;
	border-top-right-radius: 6px; /* same radius as the QComboBox */
	border-bottom-right-radius: 6px;
}

QComboBox::down-arrow
{
     image: url(:/arrow_down);
     width: 11px;
     height: 6px;
}

QComboBox::up-arrow
{
     image: url(:/arrow_up);
     width: 11px;
     height: 6px;
}

QDockWidget
{
    border-top: 1px solid #1a1a1a;
	border-bottom: 1px solid #1a1a1a;
	border-radius: 0px;
}

QDockWidget::title
{
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4c4c4c, stop:1 #434343);
}

QFrame
{
     border: 0px solid #737373;
     border-radius: 0px;
     padding: 0px;
     background-color: transparent;
}

QGroupBox
 {
     border: 1px solid #3a3a3a;
     background: #808080;
     border-radius: 5px;
     margin-top: 13px;
 }

QGroupBox::title
{
     subcontrol-origin: margin;
     subcontrol-position: top left;
     padding: 0px 10px;
     color: #0b0b0b;
}

/* Header for ... */
QHeaderView::section
{
	color: #cccccc;
	background: transparent;
	padding-left: 4px;
	border-top: 0px solid #393939;
	border-bottom: 0px solid #959595;
	min-height: 15px;
}

/* Text input box */
QLineEdit
{
	color: #c8c8c8;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #808080, stop:1 #8c8c8c);
    border: 1px solid #4d4d4d;
	padding: 0 8px;
	selection-background-color: #222222;
	selection-color: #f5f5f5;
	margin-left: 5px;
	margin-right: 5px;
	border-radius: 5px;
	max-height: 14px;
	height: 14px;
}

QLabel
{
	margin-left: 5px;
	margin-right: 5px;
	background: none;
	border: 0px;
}

/* Drop down style */
QMenu
{
	background: #212121;
	border: 1px solid #303030;
	color: #eaeaea;
}

QMenu::separator
{
     image: none;
     border-top: 1px solid #262626;
}

QMenu::item
{
	/* sets background of menu item. set this to something non-transparent
	if you want menu color and menu item color to be different */
	background-color: transparent;
}

QMenu::item:selected
{
	/* when user selects item using mouse or keyboard */
	background: #3e3e3e;
	color: #ffffff;
}

QMenuBar
{
    border-top: 1px solid #8b8b8b;
	border-left: 0px solid #606060;
	border-bottom: 1px solid #939393;
	border-right: 0px solid #303030;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #686868, stop:0.8 #686868, stop:0.9 #474747, stop:1 #000000);
	min-height: 20px;
}

QMenuBar::item
{
	spacing: 3px; /* spacing between menu bar items */
	padding: 1px 4px;
	background: transparent;
	color: #111111;
	max-height: 16px;
}

/* when selected using mouse or keyboard */

QMenuBar::item:selected
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #ffffff;
	border-radius: 5px;
	border:	1px solid #222222;
}

QMenuBar::item:pressed
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #ffffff;
	border-radius: 5px;
	border:	1px solid #222222;
}

QPushButton
{
    color: #0b0b0b;
    border: 1px solid #353535;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	border-radius: 3px;
	padding-left: 5px;
	padding-right: 5px;
}

/* all types of push button */
QPushButton:hover
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #ffffff;
}

QPushButton:pressed
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #565656, stop:1 #464646);
	color: #e5e5e5;
}

/* Customize radio buttons. */
QRadioButton
{
    spacing: 5px;
}

QRadioButton::indicator
{
    width: 13px;
    height: 13px;
}

QRadioButton::indicator::unchecked
{
    image: url(:/radiobutton_unchecked);
}

QRadioButton::indicator:unchecked:hover
{
    image: url(:/radiobutton_unchecked_hover);
}

QRadioButton::indicator:unchecked:pressed
{
    image: url(:/radiobutton_unchecked_pressed);
}

QRadioButton::indicator::checked
{
    image: url(:/radiobutton_checked);
}

QRadioButton::indicator:checked:hover
{
    image: url(:/radiobutton_checked_hover);
}

QRadioButton::indicator:checked:pressed
{
    image: url(:/radiobutton_checked_pressed);
}

/* Customize arrows.
*::down-arrow, *::menu-indicator {
    image: url(:/arrow_down);
    width: 9px;
    height: 9px;
}

*::down-arrow:disabled, *::down-arrow:off {
   image: url(:/down_arrow_disabled.png);
}

*::up-arrow {
    image: url(:/arrow_up);
    width: 9px;
    height: 9px;
}

*::up-arrow:disabled, *::up-arrow:off {
   image: url(:/up_arrow_disabled.png);
}

*/

QScrollBar QAbstractScrollArea
{
	background: transparent;
}

QScrollBar:horizontal
{
	max-height: 12px;
	min-height: 12px;
	margin: 0px 22px 0px 22px;
    border: 0px solid #474747;
    border-radius: 0px;
    background: transparent;
}

QScrollBar::handle:horizontal
{
	border: 1px solid #383838;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #969696, stop:1 #7b7b7b);
	border-radius: 3px;
	min-height: 8px;
	max-height: 8px;
	height: 8px;
}

QScrollBar::add-line:horizontal
{
	border: 0px solid #1e1e1e;
    background-color: transparent;
    width: 0px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
	border: 0px solid #1e1e1e;
    background-color: transparent;
    width: 0px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::left-arrow:horizontal
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::right-arrow:horizontal
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background-color: transparent;
}

QScrollBar:vertical
{
    border: 0px solid #1e1e1e;
    border-radius: 0px;
    background: transparent;
    max-width: 12px;
	min-width: 12px;
	margin: 22px 0px 22px 0px;
}

QScrollBar::handle:vertical
{
	border: 1px solid #383838;
	background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #969696, stop:1 #7b7b7b);
	border-radius: 3px;
	min-width: 8px;
	max-width: 8px;
	min-height: 20px;
	max-height: 20px;
	width: 8px;

}

QScrollBar::add-line:vertical
{
    subcontrol-position: top;
    subcontrol-origin: margin;
	border: 0px solid #1e1e1e;
	background-color: transparent;
	height: 0px;
}

QScrollBar::sub-line:vertical
{
    subcontrol-position: bottom;
    subcontrol-origin: margin;
	border: 0px solid #1e1e1e;
	background-color: transparent;
	height: 0px;
}

QScrollBar::up-arrow:vertical
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::down-arrow:vertical
{
	background-color: transparent;
    width: 0px;
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
	background-color: transparent;
}

QSlider
{
	background-color: #808080;
}

QSlider::groove:vertical
{
	background-color: transperant;
	position: absolute;
	left: 4px; right: 4px;
}

QSlider::handle:vertical
{
     height: 10px;
     background: #ff7603;
     border: 1px solid #62340e;
     margin: 0 -4px; /* expand outside the groove */
}

QSlider::add-page:vertical
{
     background: #222222;
}

QSlider::sub-page:vertical
{
     background: #222222;
}

QSpinBox
{
    padding-right: 15px; /* make room for the arrows */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #808080, stop:1 #8c8c8c);
    border: 1px solid #4d4d4d;
    color: #ffffff;
   	border-top-left-radius: 3px; /* same radius as the QComboBox */
	border-bottom-left-radius: 3px;
}

QSpinBox::up-button
{
    subcontrol-origin: border;
    subcontrol-position: top right; /* position at the top right corner */
    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #979797);
    border: 1px solid #323232;
	border-bottom-width: 0;
}

QSpinBox::up-button:hover
{
	background: #3e3e3e;
}

QSpinBox::up-button:pressed
{
	background: #3e3e3e;
}

QSpinBox::up-arrow
{
     image: url(:/arrow_up);
     width: 11px;
     height: 6px;
}

QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off
{ /* off state when value is max */
    image: url(:/arrow_up);
}

QSpinBox::down-button
{
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* position at bottom right corner */
    width: 16px;
	border-top: 0px solid #323232;
	border-left: 1px solid #323232;
	border-bottom: 1px solid #323232;
	border-right: 1px solid #323232;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #979797, stop:1 #8a8a8a);
    border-top-width: 0;
}

QSpinBox::down-button:hover
{
	background: #3e3e3e;
}

QSpinBox::down-button:pressed
{
	background: #3e3e3e;
}

QSpinBox::down-arrow
{
     image: url(:/arrow_down);
     width: 11px;
     height: 6px;
}

QSpinBox::down-arrow:disabled,
QSpinBox::down-arrow:off
{ /* off state when value in min */
    image: url(:/arrow_down);
}

QSplitter::handle
{
    background: transparent;
}

QSplitter::handle:horizontal
{
 	background: transparent;
 	min-width: 2px;
	max-width: 2px;
	width: 2px;
	border-left: 1px solid #393939;
	border-right: 1px solid #959595;
	padding: 0px;
	margin: 0px;
}

QSplitter::handle:vertical
{
   	background: transparent;
   	max-height: 2px;
	min-height: 2px;
	height: 2px;
	border-top: 1px solid #393939;
	border-bottom: 1px solid #959595;
	padding: 0px;
	margin: 0px;
}

QStatusBar
{
   	border: 0px solid #262626;
	background: #686868;
}

/* Table View */
QTableView
{
	background: #727272;
	selection-background-color: #787878;
	selection-color: #f5f5f5;
	padding-left: 5px;
	padding-right: 5px;
	color: #000000;
	margin: 5px;
}

QTreeView
{
	margin-top: 1px;
	border: 0px solid #434343;
	border-radius: 0px;
	padding: 0px;
	background: #727272;
	paint-alternating-row-colors-for-empty-area: 1;
	show-decoration-selected: 1;
	alternate-background-color: #727272;
}

QTreeView::item
{
	color: #cccccc;
	padding-left: 10px;
}

QTreeView::item:hover
{
	color: #e5e5e5;
}

QTreeView::item:selected
{
	color: #ffffff;
	background: #686868;
}

QTreeView::item:selected:active
{
	color: #f5f5f5;
	background: #686868;
}

QTreeView::item:selected:!active
{
	color: #f5f5f5;
	background: #686868;
}

QTreeView::branch:has-siblings:!adjoins-item
{
     border-image: url(:/vline) 0;
}

QTreeView::branch:has-siblings:adjoins-item
{
     border-image: url(:/branch-more) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
     border-image: url(:/branch-end) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings
{
         image: url(:/branch-closed);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings
{
         border-image: none;
         image: url(:/branch-open);
}

/* The tab widget frame */
QTabWidget::pane
{
    border: 1px solid #353535;
	margin: 0px;
	padding: 0px;

}

QTabWidget::tab-bar
{
	background: #323232;
	border: 1px solid #1e1e1e;
}

/* Style the tab using the tab sub-control. */
QTabBar::tab
{
	border: 1px solid #353535;
	border-bottom: 0px solid #242424;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #373737);
	color: #aaaaaa;
	padding: 3px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
	margin-top: 1px;
	margin-bottom: 0px;
	margin-left: 5px;
}

QTabBar::tab:hover
{
	color: #ffffff;
}

QTabBar::tab:selected
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	color: #010101
}

/* Style for main toolbar */
QToolBar
{
    border: 0px solid #8b8b8b;
	background-color: transparent;
	spacing: 2px; /* spacing between items in the tool bar */
	margin-left: 3px;
	color: #e5e5e5;
	max-height: 22px;
}

QToolBar::handle
{
     image: none;
     background-color: transparent;
}

QToolBar::separator
{
     width: 5px;
     border: 0px;
     background-color: transparent;
}

/* All types of tool button */
QToolButton
{
	border: 1px solid #353535;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	color: #e5e5e5;
	border-radius: 5px;
	max-height: 18px;
	min-width: 18px;
}

QToolButton[popupMode="1"]
{
	/* only for MenuButtonPopup */
	padding-right: 20px; /* make way for the popup button */
	/* max-width: 32px; */
}

QToolButton::menu-button
{
     /* 16px width + 4px for border = 20px allocated above */
	border-top: 1px solid #323232;
	border-left: 1px solid #222222;
	border-bottom: 1px solid #323232;
	border-right: 1px solid #323232;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #8a8a8a);
	color: #111111;
}

QToolButton:hover
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e5e5e5, stop:0.2 #a6a6a6, stop:0.8 #8a8a8a, stop:1 #4a4a4a);
	color: #c8c8c8;
}

QToolButton:pressed
{
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e5e5e5, stop:0.2 #a6a6a6, stop:0.8 #8a8a8a, stop:1 #4a4a4a);
	color: #c8c8c8;
}

QToolTip
{
	border: 1px solid #111111;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #363636, stop:0.2 #e5e5e5, stop:0.8 #ffffff, stop:1 #262626);
	padding: 3px;
	border-radius: 0px;
	opacity: 150;
	color: #000000;
}

QDoubleSpinBox
{
    padding-right: 15px; /* make room for the arrows */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #808080, stop:1 #8c8c8c);
    border: 1px solid #4d4d4d;
    color: #ffffff;
   	border-top-left-radius: 3px; /* same radius as the QComboBox */
	border-bottom-left-radius: 3px;
}

QDoubleSpinBox::up-button
{
    subcontrol-origin: border;
    subcontrol-position: top right; /* position at the top right corner */
    width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #a6a6a6, stop:1 #979797);
    border: 1px solid #323232;
	border-bottom-width: 0;
}

QDoubleSpinBox::up-button:hover
{
	background: #3e3e3e;
}

QDoubleSpinBox::up-button:pressed
{
	background: #3e3e3e;
}

QDoubleSpinBox::up-arrow
{
     image: url(:/arrow_up);
     width: 11px;
     height: 6px;
}

QDoubleSpinBox::up-arrow:disabled, QDoubleSpinBox::up-arrow:off
{ /* off state when value is max */
    image: url(:/arrow_up);
}

QDoubleSpinBox::down-button
{
    subcontrol-origin: border;
    subcontrol-position: bottom right; /* position at bottom right corner */
    width: 16px;
	border-top: 0px solid #323232;
	border-left: 1px solid #323232;
	border-bottom: 1px solid #323232;
	border-right: 1px solid #323232;
	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #979797, stop:1 #8a8a8a);
    border-top-width: 0;
}

QDoubleSpinBox::down-button:hover
{
	background: #3e3e3e;
}

QDoubleSpinBox::down-button:pressed
{
	background: #3e3e3e;
}

QDoubleSpinBox::down-arrow
{
     image: url(:/arrow_down);
     width: 11px;
     height: 6px;
}

QDoubleSpinBox::down-arrow:disabled,
QDoubleSpinBox::down-arrow:off
{ /* off state when value in min */
    image: url(:/arrow_down);
}
"""

# default_style = dark_orange
#default_style = level4
