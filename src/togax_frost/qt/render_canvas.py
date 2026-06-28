from PySide6.QtCore import QBuffer, QIODevice, QPoint
from PySide6.QtGui import QImage, QPainter, QTransform
from toga_qt.widgets.canvas import Canvas


class RenderCanvas(Canvas):
    def reset_transform(self, *args, **kwargs):
        raise NotImplementedError("Not impl'd for Qt using togax-frost")
    def get_image_data(self, size):
        target_width, target_height = size.width, size.height
        image = QImage(
            target_width,
            target_height,
            QImage.Format.Format_ARGB32_Premultiplied
        )
        painter = QPainter(image)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        current_size = self.native.size()
        painter.setWindow(0, 0, current_size.width(), current_size.height())
        self.native.render(painter, QPoint(0, 0))
        painter.end()
        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        image.save(buffer, "PNG")
        img_bytes = bytes(buffer.data())
        buffer.close()
        return img_bytes
