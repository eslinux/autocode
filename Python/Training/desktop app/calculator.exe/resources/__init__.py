# resource package: expose icon_png as base64 string
import icon_png_data

try:
    icon_png = icon_png_data
except Exception:
    icon_png = None
