import ee

def init_gee():
    """Khởi tạo Earth Engine"""
    ee.Initialize()

def get_region(lat, lon, buffer=10000):
    """Trả về geometry buffer quanh point"""
    point = ee.Geometry.Point([lon, lat])
    return point.buffer(buffer).bounds()

def make_preview(img):
    """Scale ảnh 0-10000 → 0-255 để xem nhanh"""
    return img.select(["B4","B3","B2"]).divide(10000).multiply(255).uint8()

def split_region(region, n_tiles=2):
    """Chia geometry thành grid n_tiles x n_tiles"""
    bounds = region.bounds().getInfo()['coordinates'][0]
    minx = min([c[0] for c in bounds])
    maxx = max([c[0] for c in bounds])
    miny = min([c[1] for c in bounds])
    maxy = max([c[1] for c in bounds])
    
    tiles = []
    dx = (maxx - minx)/n_tiles
    dy = (maxy - miny)/n_tiles
    for i in range(n_tiles):
        for j in range(n_tiles):
            tile = ee.Geometry.Rectangle([
                minx + i*dx, miny + j*dy,
                minx + (i+1)*dx, miny + (j+1)*dy
            ])
            tiles.append(tile)
    return tiles
