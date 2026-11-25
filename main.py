from pyscript import document, when,window
from PIL import Image
import io
from js import document, Blob, URL
from js import Blob, URL, Uint8Array
@when('click','#b')
async def on_click(event):
    file=document.querySelector('#input')
    if file.files.length==0:
        print('no file selected')
        return
    file = file.files.item(0)
    buffer = await file.arrayBuffer()
    data = buffer.to_bytes()
    img = Image.open(io.BytesIO(data))
    quality = int(document.querySelector("#q").value)
    out = io.BytesIO()
    img.convert("RGB").save(out, format="JPEG", quality=quality, optimize=True)
    new_size = len(out.getvalue())   
    data = out.getvalue()
    js_data = Uint8Array.new(len(data))
    js_data.assign(data)

    blob = Blob.new([js_data], {"type": "image/jpeg"})
    url = URL.createObjectURL(blob)

    link = document.createElement("a")
    link.href = url
    link.download = "compressed.jpg"
    link.click()
    document.querySelector("#original-size").innerText = f"{file.size / 1024:.1f} KB"
    document.querySelector("#compressed-size").innerText = f"{new_size / 1024:.1f} KB" 
