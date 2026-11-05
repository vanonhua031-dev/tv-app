from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class MyTVApp(App):
    def build(self):
        # Tạo giao diện chính
        self.layout = GridLayout(cols=2, padding=20, spacing=20)
        
        # Nhãn hiển thị trạng thái
        self.status_label = Label(text="DUNG REMOTE DE DIEU KHIEN", font_size='22sp')
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(Label(text="Xin chao!", font_size='20sp'))
        
        # Danh sách các nút
        self.buttons = [
            Button(text="Xem Phim", font_size='20sp'),
            Button(text="Nghe Nhac", font_size='20sp'),
            Button(text="Choi Game", font_size='20sp'),
            Button(text="Cai Dat", font_size='20sp')
        ]
        
        # Thêm các nút vào layout và gán sự kiện khi bấm (click/OK)
        for btn in self.buttons:
            btn.bind(on_press=self.on_button_click)
            self.layout.add_widget(btn)

        # Quản lý vị trí đang chọn (focus) bằng Remote
        self.current_index = 0
        self.update_focus()

        # Lắng nghe phím bấm từ Remote TV
        Window.bind(on_key_down=self.on_key_down)

        return self.layout

    def update_focus(self):
        """Đổi màu nút đang được chọn để nhận biết trên màn hình TV"""
        for i, btn in enumerate(self.buttons):
            if i == self.current_index:
                btn.background_color = (0, 0.7, 1, 1)  # Đổi sang màu xanh khi Focus
            else:
                btn.background_color = (1, 1, 1, 1)    # Mặc định

    def on_button_click(self, instance):
        self.status_label.text = f"Ban da chon: {instance.text}"

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        """Xử lý nút bấm trên Remote (Mũi tên & OK)"""
        # Phím Mũi tên Phải
        if key in (275, 19) or scancode == 79:
            if self.current_index < len(self.buttons) - 1:
                self.current_index += 1
                self.update_focus()
            return True

        # Phím Mũi tên Trái
        elif key in (276, 21) or scancode == 80:
            if self.current_index > 0:
                self.current_index -= 1
                self.update_focus()
            return True

        # Phím Mũi tên Xuống
        elif key in (274, 20) or scancode == 81:
            if self.current_index + 2 < len(self.buttons):
                self.current_index += 2
                self.update_focus()
            return True

        # Phím Mũi tên Lên
        elif key in (273, 19) or scancode == 82:
            if self.current_index - 2 >= 0:
                self.current_index -= 2
                self.update_focus()
            return True

        # Phím Enter / OK trên Remote
        elif key in (13, 66) or scancode == 40:
            self.on_button_click(self.buttons[self.current_index])
            return True

        return False

if __name__ == '__main__':
    MyTVApp().run()
