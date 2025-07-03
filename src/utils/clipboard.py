from PySide6.QtCore import QObject, Signal
import clipboard
from pynput import keyboard
from pynput.keyboard import Listener


class ClipboardMonitor(QObject):
    text_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._previous_text = ""
        self._current_keys = set()

    def start_listening(self):
        def on_key_press(key):
            self._current_keys.add(key)
            coped_text = clipboard.paste()

            if (
                keyboard.Key.ctrl_l in self._current_keys
                or keyboard.Key.ctrl_r in self._current_keys
                and self._previous_text != coped_text
            ):
                if (
                    keyboard.KeyCode.from_char("c") in self._current_keys
                    and keyboard.KeyCode.from_char("z") in self._current_keys
                ):
                    self.text_changed.emit(coped_text)
                    self._previous_text = coped_text
                    self._current_keys.clear()

        def on_key_release(key):
            if key in self._current_keys:
                self._current_keys.remove(key)

        self.listener = Listener(on_press=on_key_press, on_release=on_key_release)
        self.listener.start()

    def stop(self):
        self._timer.stop()
