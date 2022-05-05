from .carrito import Carrito

def valor_total_carrito(request):
    Carrito(request)  
    total=0
    if request.user.is_authenticated:
      for key,value in request.session["carrito"].items():
          total+=float(value["precio"])
    return {"valor_total_carrito":total}