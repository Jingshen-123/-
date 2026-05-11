from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox,
)
from PyQt6.QtCore import Qt

from config.settings import get_api_key, save_api_key


def _mask_key(key: str) -> str:
    if len(key) <= 8:
        return key[:4] + "****"
    return key[:7] + "****" + key[-4:]


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("API Key 设置")
        self.setFixedSize(460, 250)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(14)

        # Title
        title = QLabel("DeepSeek API Key")
        title.setStyleSheet("font-size: 15px; font-weight: bold; color: #e0e0e0;")
        layout.addWidget(title)

        # Hint
        hint = QLabel("请输入你的 DeepSeek API Key，将安全保存在本地。")
        hint.setStyleSheet("font-size: 12px; color: #888888; margin-bottom: 4px;")
        hint.setWordWrap(True)
        layout.addWidget(hint)

        # Input
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("sk-...")
        self.key_input.setEchoMode(QLineEdit.EchoMode.Password)
        existing_key = get_api_key()
        if existing_key:
            self.key_input.setPlaceholderText(_mask_key(existing_key))
        layout.addWidget(self.key_input)

        layout.addStretch()

        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        cancel_btn = QPushButton("取消")
        cancel_btn.setObjectName("dialogSecondary")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(cancel_btn)

        save_btn = QPushButton("保存")
        save_btn.setObjectName("dialogPrimary")
        save_btn.clicked.connect(self._on_save)
        btn_layout.addWidget(save_btn)

        layout.addLayout(btn_layout)

    def _on_save(self):
        key = self.key_input.text().strip()
        if not key:
            QMessageBox.warning(self, "提示", "API Key 不能为空。")
            return
        if not key.startswith("sk-"):
            QMessageBox.warning(self, "提示", "API Key 格式不正确，应以 'sk-' 开头。")
            return
        save_api_key(key)
        self.accept()
