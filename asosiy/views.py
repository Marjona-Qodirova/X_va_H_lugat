from django.shortcuts import render

from .models import *


def home(request):
    qidiruv_sozi=request.GET.get("qidirish")
    if qidiruv_sozi is None:
        n=""
        s=""


    else:
        togri=Togri.objects.filter(soz=qidiruv_sozi)
        if len(togri)>0:
            s=togri[0]
            n=Notogri.objects.filter(togri=s)
        elif len(togri)==0:
            n=Notogri.objects.filter(n_soz=qidiruv_sozi)
            if len(n)>0:
                s = n[0].togri
                n=Notogri.objects.filter(togri=s)
            elif len(togri) == 0:
                s = ["Bunday soz yoq"]

    data={"notogrisi": n, "togrisi": s,}


    return render(request, "result.html", data)

