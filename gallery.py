from pyscript import document

photos = [
    {"name": "Class Fun", "desc": "Will miss!", "img": "classfun.jpg"}, 
    {"name": "Intramurals", "desc": "Green Hornets!", "img": "intrams.jpg"}, 
    {"name": "Food Fair", "desc": "Basketball and prices!", "img": "foodfair.jpg"}, 
    {"name": "CAT Graduation", "desc": "Finally graduated!", "img": "CAT Graduation.jpeg"}, 
]

gallery = document.getElementById("gallery")

html = ""

for p in photos:
    html += f"""
    <div class="card">
        <img src="{p['img']}" alt="{p['name']}">
        <h3>{p['name']}</h3>
        <p>{p['desc']}</p>
    </div>
    """

gallery.innerHTML = html