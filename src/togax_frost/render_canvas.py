from __future__ import annotations
from functools import cached_property
from typing import TYPE_CHECKING
from toga import Canvas
from toga.platform import get_factory
from toga.types import Size
if TYPE_CHECKING:
    from toga.images import ImageT, SizeT
import toga


class RenderCanvas(Canvas):
    @cached_property
    def factory(self):
        return get_factory("togax_frost")

    def _create(self):
        return self.factory.RenderCanvas(interface=self)

    def as_image(self, format: type[ImageT] = toga.Image, size: SizeT | None = None) -> ImageT:
        """Render the canvas as an image.

        :param format: Format to provide. Defaults to [`Image`][toga.images.Image]; also
            supports [`PIL.Image.Image`][] if Pillow is installed, as well as any image
            types defined by installed [image format plugins][image-format-plugins].
        :param size: The size of the image to be rendered to.
            
            **Note**:  The size parameter may or may not internally resize the canvas;
            on_resize signals in this process are internally suppressed, so one must
            manually set up a resize for your Canvas content before the call with a non-normal
            size.
        :returns: The canvas as an image of the specified type.
        """
        return toga.Image(self._impl.get_image_data(Size(*size))).as_format(format)