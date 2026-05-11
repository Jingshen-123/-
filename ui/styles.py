def get_dark_theme_stylesheet() -> str:
    return """
    /* === 全局 === */
    QMainWindow, QDialog {
        background-color: #0d0d0d;
        font-family: "Microsoft YaHei";
    }

    QWidget {
        background-color: #0d0d0d;
        color: #e0e0e0;
        font-family: "Microsoft YaHei";
    }

    /* === 输入框 / 文本框 === */
    QTextEdit, QPlainTextEdit {
        background-color: #1e1e1e;
        color: #e0e0e0;
        border: 1px solid #2a2a2a;
        border-radius: 6px;
        padding: 12px;
        font-size: 14px;
        selection-background-color: rgba(0, 212, 255, 0.3);
        selection-color: #ffffff;
    }

    QTextEdit:focus, QPlainTextEdit:focus {
        border-color: #00d4ff;
    }

    QTextEdit[readOnly="true"] {
        background-color: #181818;
    }

    /* === 行编辑（设置弹窗用）=== */
    QLineEdit {
        background-color: #1e1e1e;
        color: #e0e0e0;
        border: 1px solid #2a2a2a;
        border-radius: 6px;
        padding: 8px 12px;
        font-size: 13px;
        selection-background-color: rgba(0, 212, 255, 0.3);
    }

    QLineEdit:focus {
        border-color: #00d4ff;
    }

    /* === 标签 === */
    QLabel {
        color: #e0e0e0;
        background-color: transparent;
        font-size: 13px;
    }

    /* === 主按钮（润色）=== */
    QPushButton#polishButton {
        background-color: #00d4ff;
        color: #000000;
        border: none;
        border-radius: 6px;
        padding: 10px 32px;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton#polishButton:hover {
        background-color: #00e5ff;
    }

    QPushButton#polishButton:pressed {
        background-color: #00b8e6;
    }

    QPushButton#polishButton:disabled {
        background-color: #333333;
        color: #666666;
    }

    /* === 次要按钮（清空、复制）=== */
    QPushButton#secondaryButton {
        background-color: transparent;
        color: #cccccc;
        border: 1px solid #444444;
        border-radius: 6px;
        padding: 10px 24px;
        font-size: 13px;
    }

    QPushButton#secondaryButton:hover {
        border-color: #00d4ff;
        color: #00d4ff;
    }

    QPushButton#secondaryButton:pressed {
        background-color: #1a1a1a;
    }

    /* === 设置按钮 === */
    QPushButton#settingsButton {
        background-color: transparent;
        color: #888888;
        border: 1px solid #333333;
        border-radius: 6px;
        padding: 6px 14px;
        font-size: 13px;
    }

    QPushButton#settingsButton:hover {
        color: #00d4ff;
        border-color: #00d4ff;
    }

    /* === 对话框按钮 === */
    QPushButton#dialogPrimary {
        background-color: #00d4ff;
        color: #000000;
        border: none;
        border-radius: 6px;
        padding: 8px 20px;
        font-size: 13px;
    }

    QPushButton#dialogPrimary:hover {
        background-color: #00e5ff;
    }

    QPushButton#dialogSecondary {
        background-color: transparent;
        color: #cccccc;
        border: 1px solid #444444;
        border-radius: 6px;
        padding: 8px 20px;
        font-size: 13px;
    }

    QPushButton#dialogSecondary:hover {
        border-color: #00d4ff;
        color: #00d4ff;
    }

    /* === 状态栏 === */
    QStatusBar {
        background-color: #111111;
        color: #888888;
        font-size: 12px;
        border-top: 1px solid #1a1a1a;
    }

    QStatusBar QLabel {
        color: #888888;
        font-size: 12px;
    }

    /* === 滚动条 === */
    QScrollBar:vertical {
        background-color: #1a1a1a;
        width: 8px;
        border: none;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical {
        background-color: #444444;
        min-height: 30px;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #555555;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background-color: transparent;
    }

    QScrollBar:horizontal {
        background-color: #1a1a1a;
        height: 8px;
        border: none;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal {
        background-color: #444444;
        min-width: 30px;
        border-radius: 4px;
    }

    QScrollBar::handle:horizontal:hover {
        background-color: #555555;
    }

    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0px;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background-color: transparent;
    }

    /* === 提示框 === */
    QToolTip {
        background-color: #1e1e1e;
        color: #e0e0e0;
        border: 1px solid #00d4ff;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 12px;
    }
    """
