from django.shortcuts import render,  get_object_or_404, redirect
from main.models import mortgage_list, calculation as calc_model, calculation_content
from django.contrib.auth.decorators import login_required
from django.db import models, connection
from django.http import Http404

# Create your views here.

# cards = [
#     {
#         "id": 1,
#         "title": "Аннуитетные платежи",
#         "description": "Узнайте, сколько нужно платить в месяц в рассчете на равные доли",
#         "desc_extended": "Аннуитетным называется тип расчёта по кредиту, при котором общая сумма  задолженности, включая тело долга и начисленные за расчётный период  пользования кредитом проценты, разделены на равные части. Заёмщик раз в  месяц вносит одну и ту же сумму до тех пор, пока полностью не  рассчитается с банком (последний платёж закрывает остаток задолженности, поэтому незначительно может отличаться от аннуитетного платежа).",
#         "image": "http://172.18.0.4:9000/images/аннуитетные_платежи.png",
#     },
#     {
#         "id": 2, 
#         "title": "Дифференцированные платежи",
#         "description": "Спланируйте оплату ипотеки уменьшающимися платежами",
#         "desc_extended": "",
#         "image": "http://172.18.0.4:9000/images/дифф_платежи.png",
#     },
#     {
#         "id": 3,
#         "title": "Страхование ипотеки",
#         "description": "Рассчитайте ежемесячные платежи за страховку ипотеки",
#         "desc_extended": "",
#         "image": "http://172.18.0.4:9000/images/страхование.jpg",
#     },
# ]

# calcs_list = [
#     {
#         'id':1,
#         'user': 'Александр',
#         'percentage': 20,
#         '': 300000,
#         'items':[1, 2],
#     },
#     {
#         'id':2,
#         'user': 'Александр',
#         'percentage': 15,
#         'cost': 4500000,
#         'items':[1, 2],
#     },
# ]

def mortgage_home(request):

    current_calculation = None

    search = request.GET.get('search_text', "")
    if search:
        cards_data = mortgage_list.objects.filter(title__icontains=search, status=True)
    else:
        cards_data = mortgage_list.objects.filter(status=True)

    if request.user.is_authenticated:
        current_calculation = calc_model.objects.filter(user=request.user, status=1).first()

    calcs_count = calculation_content.objects.filter(calculation=current_calculation).aggregate(quantity=models.Count('id'))['quantity'] if current_calculation else 0

    return render(request, 'main/mortgage_home.html', {
        "data": cards_data, 
        "calc_id": current_calculation.id if current_calculation else None,
        "calcs_count": calcs_count
        })

def mortgage_desc(request, id):

    data = get_object_or_404(mortgage_list, id=id)

    return render(request, 'main/mortgage_desc.html', {"data": data})

@login_required
def calculation(request, id):
    current_calculation = calc_model.objects.filter(id=id)

    if current_calculation.first().status == 0:
        raise Http404()

    current_contents = calculation_content.objects.filter(calculation__in=current_calculation)
    
    content_in_calc = [current_content.mortgage_type for current_content in current_contents]

    return render(request, 'main/calculation.html',{
        'calc_data': current_calculation.first(),
        'order_cards': content_in_calc,
        'calc_card_content': current_contents,
    })

@login_required
def add_calculation(request, id):
    
    mortgage = get_object_or_404(mortgage_list, id=id)

    current_calculation, created_calculation = calc_model.objects.get_or_create(
        user=request.user,
        status=1
    )

    current_calculation_content, created_calculation_content = calculation_content.objects.get_or_create(
        calculation=current_calculation,
        mortgage_type=mortgage,
    )

    return redirect('mortgage_home')

@login_required
def delete_calculation(request, id):
    cursor = connection.cursor()
    cursor.execute(f"""
        UPDATE calculation
        SET status = 0
        WHERE id = {id}
    """)
    return redirect('mortgage_home')