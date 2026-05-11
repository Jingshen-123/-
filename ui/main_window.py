from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QStatusBar,
    QApplication,
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal

from config.settings import get_api_key
from services.text_processor import polish_text, PolishError
from ui.settings_dialog import SettingsDialog


class _PolishWorker(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, text: str, api_key: str):
        super().__init__()
        self._text = text
        self._api_key = api_key

    def run(self):
        try:
            result = polish_text(self._text, self._api_key)
            self.finished.emit(result)
        except PolishError as e:
            self.error.emit(str(e))
        except Exception as e:
            self.error.emit(f"未知错误：{e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("中文语序调整器")
        self.resize(900, 700)
        self.setMinimumSize(600, 450)

        central = QWidget()
        self.setCentralWidget(central)

        root = QVBoxLayout(central)
        root.setContentsMargins(20, 16, 20, 0)
        root.setSpacing(12)

        # --- Top bar: title + settings ---
        top_bar = QHBoxLayout()

        title = QLabel("中文语序调整器")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #e0e0e0;")
        top_bar.addWidget(title)

        top_bar.addStretch()

        settings_btn = QPushButton(" 设置")
        settings_btn.setObjectName("settingsButton")
        settings_btn.setFixedWidth(70)
        settings_btn.clicked.connect(self._open_settings)
        top_bar.addWidget(settings_btn)

        root.addLayout(top_bar)

        # --- Input area ---
        input_label = QLabel("输入文本")
        input_label.setStyleSheet("font-size: 13px; color: #888888;")
        root.addWidget(input_label)

        self.input_edit = QTextEdit()
        self.input_edit.setPlaceholderText("请输入需要润色的中文文本...")
        self.input_edit.setMinimumHeight(180)
        root.addWidget(self.input_edit)

        # --- Buttons ---
        btn_row = QHBoxLayout()

        self.polish_btn = QPushButton("润色")
        self.polish_btn.setObjectName("polishButton")
        self.polish_btn.clicked.connect(self._on_polish)
        btn_row.addWidget(self.polish_btn)

        clear_btn = QPushButton("清空")
        clear_btn.setObjectName("secondaryButton")
        clear_btn.clicked.connect(self._on_clear)
        btn_row.addWidget(clear_btn)

        btn_row.addStretch()
        root.addLayout(btn_row)

        # --- Output area ---
        output_label = QLabel("润色结果")
        output_label.setStyleSheet("font-size: 13px; color: #888888;")
        root.addWidget(output_label)

        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)
        self.output_edit.setPlaceholderText("润色结果将显示在这里...")
        self.output_edit.setMinimumHeight(180)
        root.addWidget(self.output_edit)

        # --- Status bar ---
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.status_label = QLabel("就绪")
        self.status_bar.addWidget(self.status_label)

        self.status_bar.addPermanentWidget(QLabel(""))

        copy_btn = QPushButton("复制结果")
        copy_btn.setObjectName("secondaryButton")
        copy_btn.clicked.connect(self._on_copy)
        self.status_bar.addPermanentWidget(copy_btn)

        # --- Worker ref ---
        self._worker = None

    # --- Slots ---

    def _open_settings(self):
        dlg = SettingsDialog(self)
        dlg.exec()

    def _on_polish(self):
        api_key = get_api_key()
        if not api_key:
            self._set_status("请先设置 API Key", "warn")
            self._open_settings()
            return

        text = self.input_edit.toPlainText().strip()
        if not text:
            self._set_status("请输入需要润色的文本", "warn")
            return

        self._set_loading(True)

        self._worker = _PolishWorker(text, api_key)
        self._worker.finished.connect(self._on_result)
        self._worker.error.connect(self._on_error)
        self._worker.start()

    def _on_result(self, text: str):
        self.output_edit.setPlainText(text)
        self._set_loading(False)
        self._set_status("润色完成", "ok")

    def _on_error(self, msg: str):
        self._set_loading(False)
        self._set_status(msg, "error")

    def _on_clear(self):
        self.input_edit.clear()
        self.output_edit.clear()

    def _on_copy(self):
        text = self.output_edit.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self._set_status("已复制到剪贴板", "ok")

    def _set_loading(self, loading: bool):
        self.polish_btn.setEnabled(not loading)
        if loading:
            self.polish_btn.setText("处理中...")
            self._set_status("正在润色...", "")
        else:
            self.polish_btn.setText("润色")

    def _set_status(self, msg: str, kind: str):
        color_map = {
            "ok": "#00c853",
            "error": "#ff5252",
            "warn": "#ffab00",
        }
        color = color_map.get(kind, "#888888")
        self.status_label.setStyleSheet(f"color: {color}; font-size: 12px;")
        self.status_label.setText(msg)
