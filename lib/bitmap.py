import displayio

class Bitmap:
    def create_bitmap_tile(self,xSize,ySize,x,y,palette):
        bitmap = displayio.Bitmap(xSize, ySize, len(palette))
        tile = displayio.TileGrid(bitmap, pixel_shader=palette, x=x, y=y,tile_width=xSize,tile_height=ySize)
        return tile,bitmap

    def get_bitmap(self,name):
        image = displayio.OnDiskBitmap(name)
        tile_grid = displayio.TileGrid(image, pixel_shader=image.pixel_shader,tile_width=128,tile_height=160)
        return tile_grid

