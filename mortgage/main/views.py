from django.shortcuts import render,  get_object_or_404

# Create your views here.

cards = [
    {
        "id": 1,
        "title": "Аннуитетные платежи",
        "description": "Узнайте, сколько нужно платить в месяц в рассчете на равные доли",
        "desc_extended": "Аннуитетным называется тип расчёта по кредиту, при котором общая сумма  задолженности, включая тело долга и начисленные за расчётный период  пользования кредитом проценты, разделены на равные части. Заёмщик раз в  месяц вносит одну и ту же сумму до тех пор, пока полностью не  рассчитается с банком (последний платёж закрывает остаток задолженности, поэтому незначительно может отличаться от аннуитетного платежа).",
        "image": "http://172.18.0.3:9000/images/аннуитетные_платежи.png",
    },
    {
        "id": 2, 
        "title": "Дифференцированные платежи",
        "description": "Спланируйте оплату ипотеки уменьшающимися платежами",
        "desc_extended": "",
        "image": "http://172.18.0.3:9000/images/дифф_платежи.png",
    },
    {
        "id": 3,
        "title": "Страхование ипотеки",
        "description": "Рассчитайте ежемесячные платежи за страховку ипотеки",
        "desc_extended": "",
        "image": "http://172.18.0.3:9000/images/страхование.jpg",
    },
]

calculations = [
    {
        'id':1,
        'items':[1, 2]
    },
]

def services(request):
    data = cards    
    
    search = request.GET.get('text', "")
    if search:
        data = [card for card in cards if search.lower() in card['title'].lower()]
    
    return render(request, 'main/services.html', {"data": data})

def service_description(request, id):
    data = next((card for card in cards if int(id) == int(card['id'])), None)
    if not data:
        return get_object_or_404(data)
    return render(request, 'main/service_description.html', {"data": data})

def calculations(request):
    calculation = next((calculation for calculation in calculations if int(calculation['id']) == int(1)), None)
    card_ids = calculation.get('items', [])
    order_cards = [card for card in cards if card['id'] in card_ids]
    return render(request, 'main/calculations.html',{
        'calculations':calculation,
        'cards':order_cards,
    })