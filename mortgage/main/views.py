from django.shortcuts import render

# Create your views here.

cards = [
    {
        "id": "annuity_payments",
        "title": "Аннуитетные платежи",
        "description": "Узнайте, сколько нужно платить в месяц в рассчете на равные доли",
        "desc_extended": "Аннуитетным называется тип расчёта по кредиту, при котором общая сумма  задолженности, включая тело долга и начисленные за расчётный период  пользования кредитом проценты, разделены на равные части. Заёмщик раз в  месяц вносит одну и ту же сумму до тех пор, пока полностью не  рассчитается с банком (последний платёж закрывает остаток задолженности, поэтому незначительно может отличаться от аннуитетного платежа)."
        "image": "http://172.18.0.3:9000/images/аннуитетные_платежи.png",
    },
    {
        "id": "differentiated_payments", 
        "title": "Дифференцированные платежи",
        "description": "Спланируйте оплату ипотеки уменьшающимися платежами",
        "desc_extended": ""
        "image": "http://172.18.0.3:9000/images/дифф_платежи.png",
    },
    {
        "id": "insurance",
        "title": "Страхование ипотеки",
        "description": "Рассчитайте ежемесячные платежи за страховку ипотеки",
        "desc_extended": ""
        "image": "http://172.18.0.3:9000/images/страхование.jpg",
    },
]

def services(request):
    data = cards    
    
    search = request.GET.get('text', "")
    if search:
        data = [card for card in cards if search.lower() in card['title'].lower()]
    
    return render(request, 'main/services.html', {"data": data})

def service_description(request):
    return render(request, 'main/service_description.html')

def calculations(request):
    return render(request, 'main/calculations.html')