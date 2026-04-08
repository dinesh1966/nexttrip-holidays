import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

bg_images = {
    'mountains': 'images/kashmir_tour_1775545905366.png',
    'backwaters': 'images/kerala_tour_1775545920618.png',
    'hills': 'images/munnar_tour_1775546087248.png',
    'beaches': 'images/goa_tour_1775545953325.png',
    'desert': 'images/rajasthan_tour_1775545936775.png',
    'wildlife': 'images/wildlife_safari_1775546695667.png',
    'temple': 'images/indian_temple_1775546710882.png',
    'heritage': 'images/indian_heritage_1775546727559.png',
    'city': 'images/mumbai_city_1775546762516.png',
    'agra': 'images/agra_taj_1775546746151.png'
}

mapping = {
    'Kashmir': bg_images['mountains'],
    'Ladakh': bg_images['mountains'],
    'Shimla': bg_images['mountains'],
    'Manali': bg_images['mountains'],
    'Gangtok': bg_images['mountains'],
    'Spiti Valley': bg_images['mountains'],
    
    'Kerala': bg_images['backwaters'],
    
    'Mussoorie': bg_images['hills'],
    'Ooty': bg_images['hills'],
    'Kodaikanal': bg_images['hills'],
    'Munnar': bg_images['hills'],
    'Darjeeling': bg_images['hills'],
    'Coorg': bg_images['hills'],
    
    'Goa': bg_images['beaches'],
    'Andaman': bg_images['beaches'],
    'Lakshadweep': bg_images['beaches'],
    
    'Jaipur': bg_images['desert'],
    'Jodhpur': bg_images['desert'],
    'Udaipur': bg_images['desert'],
    'Jaisalmer': bg_images['desert'],
    
    'Jim Corbett': bg_images['wildlife'],
    'Ranthambore': bg_images['wildlife'],
    
    'Rishikesh': bg_images['temple'],
    'Varanasi': bg_images['temple'],
    'Rameswaram': bg_images['temple'],
    'Kanyakumari': bg_images['temple'],
    'Madurai': bg_images['temple'],
    'Tirupati': bg_images['temple'],
    'Shirdi': bg_images['temple'],
    'Amritsar': bg_images['temple'],
    
    'Agra': bg_images['agra'],
    'Mysore': bg_images['heritage'],
    'Hampi': bg_images['heritage'],
    'Mahabalipuram': bg_images['heritage'],
    
    'Mumbai': bg_images['city'],
    'Pondicherry': bg_images['city'],
}

def replacer(match):
    full_pill = match.group(0)
    onclick = match.group(1)
    name = match.group(2)
    
    bg = mapping.get(name, bg_images['mountains']) # default to mountains if not found
    
    new_pill = f"""<div class="place-pill" onclick="{onclick}" style="background: url('{bg}') center/cover no-repeat;">
                <div class="pill-name">{name}</div>
            </div>"""
    return new_pill

# The pills look like: 
# <div class="place-pill" onclick="openBooking('Kashmir Tour')">
#     <div class="pill-icon">🏔️</div>
#     <div class="pill-name">Kashmir</div>
# </div>

pattern = re.compile(r'<div class="place-pill" onclick="([^"]+)">\s*<div class="pill-icon">.*?</div>\s*<div class="pill-name">(.*?)</div>\s*</div>', re.DOTALL)

new_content = pattern.sub(replacer, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done replacing pills")
