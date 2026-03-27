import struct

def get_png_info(file_path):
    with open(file_path, 'rb') as f:
        data = f.read(24)
        if data[:8] == b'\x89PNG\r\n\x1a\n' and data[12:16] == b'IHDR':
            w, h = struct.unpack('>LL', data[16:24])
            return w, h
    return None

path = r"d:\Projects\티즈틴(TIZ-TINE)\assets\images\branding\tiztine_banner.png"
res = get_png_info(path)
if res:
    print(f"Resolution of {path}: {res[0]}x{res[1]}")
else:
    print(f"Failed to read PNG header for {path}")
