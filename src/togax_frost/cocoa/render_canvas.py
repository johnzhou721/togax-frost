from travertino.size import at_least

from ctypes import cdll, util
from toga_cocoa.colors import native_color
from toga_cocoa.libs import NSTextAlignment, NSTextField, NSBitmapImageRep, core_graphics, NSImage
from toga_cocoa.widgets.canvas import Canvas

from rubicon.objc import ObjCClass, objc_const, CGSize

AppKit = cdll.LoadLibrary(util.find_library("AppKit"))
NSCalibratedRGBColorSpace = objc_const(AppKit, "NSCalibratedRGBColorSpace")


class RenderCanvas(Canvas):
    def get_image_data(self, size):
        bitmap = NSBitmapImageRep.alloc().initWithBitmapDataPlanes(
            None,
            pixelsWide=int(size.width),
            pixelsHigh=int(size.height),
            bitsPerSample=8,
            samplesPerPixel=4,
            hasAlpha=True,
            isPlanar=False,
            colorSpaceName=NSCalibratedRGBColorSpace,
            bitmapFormat=0,
            bytesPerRow=0,
            bitsPerPixel=0,
        )
        bitmap.setSize(self.native.bounds.size)
        self.native.cacheDisplayInRect(self.native.bounds, toBitmapImageRep=bitmap)

        # Get a reference to the CGImage from the bitmap
        cg_image = bitmap.CGImage

        target_size = CGSize(
            core_graphics.CGImageGetWidth(cg_image),
            core_graphics.CGImageGetHeight(cg_image),
        )
        ns_image = NSImage.alloc().initWithCGImage(cg_image, size=target_size)
        return ns_image
