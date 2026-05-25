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


if __name__ == '__main__':
    app.run(debug=True)