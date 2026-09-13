import qrcode

url = "https://primaveraeventsgroup.com"

# Level M
qr_m = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, border=2)
qr_m.add_data(url)
qr_m.make(fit=True)
matrix_m = qr_m.modules
print(f"Level M matrix size: {len(matrix_m)}x{len(matrix_m[0])}")

# Level L
qr_l = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, border=2)
qr_l.add_data(url)
qr_l.make(fit=True)
matrix_l = qr_l.modules
print(f"Level L matrix size: {len(matrix_l)}x{len(matrix_l[0])}")
