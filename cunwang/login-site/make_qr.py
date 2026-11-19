import qrcode
from qrcode.constants import ERROR_CORRECT_M

url = "https://4mhmmw24kgkzw.doubao.link/app/app_17j9d213w7t"
out = r"C:\Users\li\Doubao\chats\2026-11-18\new-chat\cunwang\login-site\登录入口二维码.png"

qr = qrcode.QRCode(
    error_correction=ERROR_CORRECT_M,
    box_size=12,
    border=3,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="#3a2f22", back_color="#f1e9d6")
img.save(out)
print("saved:", out)
