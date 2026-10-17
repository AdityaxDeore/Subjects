from PIL import Image

im = Image.open('full_doc.png')
w, h = im.size

col = [im.getpixel((200, y)) for y in range(h)]

pages = []
in_page = False
start_y = 0
for y, pixel in enumerate(col):
    is_white = (pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255)
    if is_white and not in_page:
        in_page = True
        start_y = y
    elif not is_white and in_page:
        in_page = False
        pages.append((start_y, y))

if in_page:
    pages.append((start_y, h))

print(f"Detected {len(pages)} actual pages:")
for i, (p_start, p_end) in enumerate(pages, 1):
    page_h = p_end - p_start
    # Find last content row in this page (x between 280 and 920)
    last_content_y = p_start
    for y in range(p_end - 1, p_start, -1):
        has_content = False
        for x in range(280, 920, 5):
            p = im.getpixel((x, y))
            if p != (255, 255, 255):
                has_content = True
                break
        if has_content:
            last_content_y = y
            break
    free_bottom = p_end - last_content_y
    print(f"Page {i}: top={p_start}, bottom={p_end}, height={page_h}px | Content ends at {last_content_y} | Bottom free space = {free_bottom}px")
