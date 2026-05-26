from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Healthy Bites - სნექების სრული მონაცემთა ბაზა კალორიებითა და ფუნქციური დანიშნულებით
PRODUCTS = {
    'energy': {
        'name': 'ENERGY RUSH',
        'ingredients': 'ბანანის ჩირი, თაფლი, ნუში, შავი შოკოლადი, შვრია',
        'vitamins': 'B6, ვიტამინ E, მაგნიუმი, კალიუმი',
        'benefit': 'ბუნებრივი ენერგია',
        'purpose': 'სწრაფი ენერგიის მუხტი და ფიზიკური გამძლეობა',
        'calories': '185 კკალ'
    },
    'focus': {
        'name': 'BRAIN FUEL',
        'ingredients': 'ნიგოზი, ქიშმიში, გოგრის თესლი, კაკაო, შავი შოკოლადი',
        'vitamins': 'ომეგა-3, B1, მაგნიუმი, რკინა',
        'benefit': 'ფოკუსი და მეხსიერება',
        'purpose': 'გონებრივი აქტივობა, კონცენტრაცია და მეხსიერების გაუმჯობესება',
        'calories': '195 კკალ'
    },
    'recovery': {
        'name': 'RECOVERY BITE',
        'ingredients': 'კაკალი, შვრია, თაფლი, ქოქოსი, გოგრის თესლი',
        'vitamins': 'ცილა, თუთია, ვიტამინი E, მაგნიუმი',
        'benefit': 'კუნთების აღდგენა',
        'purpose': 'ვარჯიშის შემდგომი აღდგენა და ძალების სწრაფი აღდგენა',
        'calories': '210 კკალ'
    },
    'skin': {
        'name': 'GLOW MIX',
        'ingredients': 'მარწყვი, ქოქოსი, ნუში, იოგურტის მოსასხამი',
        'vitamins': 'ვიტამინი C, ვიტამინი E, კალციუმი',
        'benefit': 'კანის ბზინვარება',
        'purpose': 'ბუნებრივი კოლაგენი, ანტიოქსიდანტები და უჯრედების კვება',
        'calories': '170 კკალ'
    },
    'calm': {
        'name': 'CALM BITE',
        'ingredients': 'ნუში, თაფლი, ქოქოსი, შვრია, ვანილი',
        'vitamins': 'მაგნიუმი, B ჯგუფის ვიტამინები, ვიტამინი E',
        'benefit': 'დამშვიდება და უკეთესი ძილი',
        'purpose': 'სტრესის შემცირება, რელაქსაცია და მშვიდი ძილი',
        'calories': '160 კკალ'
    },
    'sweet': {
        'name': 'SWEET WITHOUT GUILT',
        'ingredients': 'ფინიკი, არაქისის კარაქი, შავი შოკოლადი, თხილი',
        'vitamins': 'B ჯგუფის ვიტამინები, ბოჭკო, მაგნიუმი',
        'benefit': 'ჯანსაღი ტკბილი',
        'purpose': 'ჯანსაღი ალტერნატივა ტკბილეულის მოყვარულთათვის',
        'calories': '180 კკალ'
    }
}


# მთავარი გვერდის როუტი
@app.route('/')
def index():
    return render_template('index.html')


# "ჩვენს შესახებ" გვერდის როუტი
@app.route('/about')
def about():
    return render_template('about.html')


# პროდუქტების კატალოგის როუტი
@app.route('/products')
def products():
    # პროდუქტების სიის გადაცემა შაბლონში დინამიური გენერაციისთვის
    return render_template('products.html', products=PRODUCTS)


# სმარტ ქვიზის დამუშავების ლოგიკა
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # მონაცემების წამოღება ფორმიდან
        gender = request.form.get('gender')
        age = request.form.get('age')
        weight = request.form.get('weight')
        activity = request.form.get('activity')
        need = request.form.get('need')
        vitamin = request.form.get('vitamin')

        # შესაბამისი სნექის შერჩევა მომხმარებლის მთავარი საჭიროების (need) მიხედვით
        selected_snack = PRODUCTS.get(need, PRODUCTS['energy'])

        # შედეგის გვერდზე გადაგზავნა შერჩეული პროდუქტით და არჩეული ვიტამინით
        return render_template('result.html', snack=selected_snack, user_vitamin=vitamin)

    # GET მოთხოვნის შემთხვევაში ქვიზის გვერდის ჩვენება
    return render_template('quiz.html')
#########################################################################
from flask import Flask, render_template, abort


# სნექების ერთიანი მონაცემთა ბაზა (ID-ები, სერთიფიკატები და დეტალები)
SNACKS_DATABASE = {
    "energy-rush": {
        "name": "ENERGY RUSH",
        "ingredients": "ფინიკი, ნუშის კარაქი, ჩია, კაკაოს მარცვლები",
        "vitamins": "რკინა, მაგნიუმი, ვიტამინი B6",
        "benefit": "სწრაფი და ბუნებრივი მუხტი",
        "batch": "#HB-2026-ENE",
        "honey_origin": "რაჭა, შოვი",
        "nuts_origin": "კახეთი, Premium A",
        "lab_status": "გავლილია ✓",
        "description": "ეს ციფრული პასპორტი ადასტურებს, რომ ENERGY RUSH დამზადებულია მაღალი თერმული დამუშავების გარეშე, რაც ინარჩუნებს ფინიკისა და ნედლი ნუშის სასარგებლო თვისებებს 100%-ით."
    },
    "brain-fuel": {
        "name": "BRAIN FUEL",
        "ingredients": "ნიგოზი, გოგრის თესლი, შავი ქლიავი, როზმარინი",
        "vitamins": "ომეგა-3, თუთია, ვიტამინი E",
        "benefit": "გონებრივი მუშაობა და ფოკუსი",
        "batch": "#HB-2026-BRA",
        "honey_origin": "იმერეთი, ტყიბული",
        "nuts_origin": "მარტვილი, Premium A",
        "lab_status": "გავლილია ✓",
        "description": "ციფრული სერთიფიკატი ანიჭებს ბრენდს გარანტიას, რომ გამოყენებული ნიგოზი არის ალფა-ლინოლენური მჟავის (Omega-3) უმდიდრესი წყარო ტვინის უჯრედებისთვის."
    },
    "recovery-bite": {
        "name": "RECOVERY BITE",
        "ingredients": "არაქისის პროტეინი, ბანანი, შვრია, კანაფის თესლი",
        "vitamins": "მაგნიუმი, კალიუმი, მცენარეული ცილა",
        "benefit": "კუნთების სწრაფი რეკოვერი ვარჯიშის შემდეგ",
        "batch": "#HB-2026-REC",
        "honey_origin": "ყვარელი, კახეთი",
        "nuts_origin": "გურია, Premium A",
        "lab_status": "გავლილია ✓",
        "description": "ვარჯიშის შემდგომი აღდგენის ფორმულა. ლაბორატორიულად შემოწმებული ელექტროლიტების ბალანსი კუნთების სპაზმების პრევენციისთვის."
    },
    "glow-mix": {
        "name": "GLOW MIX",
        "ingredients": "გოჯი კენკრა, ნუში, სელის თესლი, ქოქოსის ფანტელი",
        "vitamins": "ვიტამინი C, ანტიოქსიდანტები, კოლაგენის ბუსტერი",
        "benefit": "ბზინვარება და უჯრედოვანი კვება",
        "batch": "#HB-2026-GLO",
        "honey_origin": "მესტია, სვანეთი",
        "nuts_origin": "კახეთი, Premium A",
        "lab_status": "გავლილია ✓",
        "description": "ანტიოქსიდანტების უმაღლესი კონცენტრაცია. ხელს უწყობს კანის ელასტიურობას და იცავს უჯრედებს ოქსიდაციური სტრესისგან."
    },
    "calm-bite": {
        "name": "CALM BITE",
        "ingredients": "სეზამი, ყავისფერი ბრინჯის სიროფი, გვირილის ექსტრაქტი",
        "vitamins": "მაგნიუმი, ვიტამინი D, B12",
        "benefit": "რელაქსაცია და სტრესის მოხსნა",
        "batch": "#HB-2026-CAL",
        "honey_origin": "ასპინძა, მესხეთი",
        "nuts_origin": "ქართლი, Premium A",
        "lab_status": "გავლილია ✓",
        "description": "საღამოს სნექი ნერვული სისტემის დასამშვიდებლად. ბუნებრივი ადაპტოგენები ეხმარება სხეულს კორტიზოლის (სტრესის ჰორმონის) დარეგულირებაში."
    },
    "sweet-without-guilt": {
        "name": "SWEET WITHOUT GUILT",
        "ingredients": "სუფთა კაკაო 85%, სტივია, თხილი, ვანილი",
        "vitamins": "ვიტამინი C, ფლავონოიდები",
        "benefit": "სინდისის ქენჯნის გარეშე სიტკბო",
        "batch": "#HB-2026-SWE",
        "honey_origin": "ნატურალური სტივია (უშაქრო)",
        "nuts_origin": "გურია, საუცხოო ხარისხი",
        "lab_status": "გავლილია ✓",
        "description": "დაბალკალორიული, გლიკემიური ინდექსის მქონე ნამდვილი შოკოლადის ალტერნატივა კეტო და ჯანსაღი დიეტისთვის."
    }
}

# 1. ყველა სნექის ციფრული პასპორტების ჩამონათვალი
@app.route('/passports')
def list_passports():
    return render_template('passports.html', snacks=SNACKS_DATABASE)

# 2. კონკრეტული სნექის ციფრული პასპორტი (გაიხსნება QR კოდის სკანირებისას)
@app.route('/passport/<snack_id>')
def passport_detail(snack_id):
    snack_data = SNACKS_DATABASE.get(snack_id)
    if not snack_data:
        abort(404) # თუ არასწორი ID-ია, გამოაგდებს 404-ს
    return render_template('passport_detail.html', snack=snack_data)


if __name__ == '__main__':
    app.run(debug=True)
