from toga_gtk.widgets.canvas import Canvas
from toga_gtk.libs import cairo
from io import BytesIO


class RenderCanvas(Canvas):
    def reset_transform(self, *args, **kwargs):
        raise NotImplementedError("Not impl'd for GTK using togax-frost")
    def get_image_data(self, size):
        width, height = self._size()

        surface = cairo.ImageSurface(
            cairo.FORMAT_ARGB32,
            int(size.width),
            int(size.height),
        )

        context = cairo.Context(surface)
        context.scale(size.width / width, size.height / height)

        self.gtk_draw_callback(self.native, context, width, height)

        data = BytesIO()
        surface.write_to_png(data)
        return data.getbuffer()
