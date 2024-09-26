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

calcs_list = [
    {
        'id':1,
        'items':[1, 2, 3],
    },
    {
        'id':2,
        'items':[1, 2],
    },
]

def services(request):
    calcs_list_id = 1
    calcs_count = 0
    cards_data = cards  

    search = request.GET.get('text', "")
    if search:
        cards_data = [card for card in cards if search.lower() in card['title'].lower()]

    calcs_count = len(next((calc for calc in calcs_list if calcs_list_id == calc['id']), {'items' : []})['items'])

    return render(request, 'main/services.html', {"data": cards_data, "calcs_list_id": calcs_list_id,"calcs_count": calcs_count})

def service_description(request, id):
    data = next((card for card in cards if id == card['id']), None)
    if not data:
        return get_object_or_404(data)
    return render(request, 'main/service_description.html', {"data": data})

def calculations(request, id):
    calcs = next((calc for calc in calcs_list if calc['id'] == id), None)
    order_cards = []
    if calcs:
        order_cards = [card for card in cards if card['id'] in calcs['items']]
    return render(request, 'main/calculations.html',{
        'calcs':calcs_list,
        'order_cards':order_cards,
    })