from toga_winforms.widgets.canvas import Canvas, Context
import System.Windows.Forms as WinForms
from System.Drawing import Bitmap, Graphics, Rectangle
from System.Drawing.Imaging import ImageFormat
from System.IO import MemoryStream
from toga_winforms.colors import native_color

class RenderCanvas(Canvas):
    def reset_transform(self, *args, **kwargs):
        raise NotImplementedError("Not impl'd for WinForms using togax-frost")
    def winforms_paint(self, panel, event, *args):
        context = Context(self, event.Graphics)
        # Bug in core toga.
        context.scale(self.dpi_scale, self.dpi_scale)
        self.interface.root_state._draw(context)
    def get_image_data(self, size):
        self.native.SuspendLayout()
        # Presumably the "or transparent" part is yet another Toga bug
        # but i gotta get this app out soon so I can get funding
        current_background_color = self.interface.style.background_color or "transparent"
        self.native.BackColor = native_color(current_background_color)

        width = int(size.width)
        height = int(size.height)

        bitmap = Bitmap(width, height)
        rect = Rectangle(0, 0, width, height)

        graphics = Graphics.FromImage(bitmap)
        graphics.Clear(self.native.BackColor)

        scale_width = size.width / self.native.Width
        scale_height = size.height / self.native.Height

        # Scale all drawing operations
        graphics.ScaleTransform(scale_width, scale_height)

        self.native.OnPaint(WinForms.PaintEventArgs(graphics, rect))

        stream = MemoryStream()
        bitmap.Save(stream, ImageFormat.Png)

        self.set_background_color(current_background_color)
        self.native.ResumeLayout()

        return bytes(stream.ToArray())
