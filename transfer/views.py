from django.shortcuts import render
from django.http import HttpResponse
from customers.models import Customers

def loadTransferPage(request):
    customers = Customers.objects.all()
    
    context = {
        'customers': customers,
    }

    amt = Customers.objects.get(current_balance='1000000')
    print(str(amt))
    amt = str(amt)
    
    ju = float(amt)
    main_amt = int(ju)
    

    if request.method == 'POST':
        amount = request.POST['amount']
        num = main_amt - int(amount)
        print(amount)
        print(num)

        transferees = request.POST.getlist('select')
        print(list(transferees))
        for i in range(len(transferees)):
            pk = transferees[i]
            print(pk)
            
            if Customers.objects.filter(id=pk).exists():
                print('exists')
                user_amt = Customers.objects.get(id=pk)
                print(user_amt)
                user_amt = str(user_amt)
                user_amt = float(user_amt)
                useri_amt = int(user_amt)
                print(useri_amt)

                new_amt = main_amt - int(amount)
                print(new_amt)

                amt_to = useri_amt + int(amount)
               
                print(amt_to)
                 

    return render(request, 'pages/transfer.html', context)


