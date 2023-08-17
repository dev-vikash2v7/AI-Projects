from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Game

# Create your views here.
def home(request):
    if request.method == 'POST':

        user_name = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room-code')

        print(option)


        if option == '1':
            
            game = Game.objects.filter(room_code=room_code).first()
            # game = Game object (6)


            if game is None:
                message.success(request , 'room code not found')
                return redirect('/')

            elif game.is_over:
                message.success(request , 'game is over now !!')
                return redirect('/')
            
            game.game_oppenent = user_name
            game.save()
            return redirect('/play/' + room_code + '?username=' + 'O'+user_name)


        elif option == '2':
            game = Game(game_creator = user_name , room_code = room_code) 
            game.save()

            return redirect('/play/' + room_code + '?username=' + 'X'+user_name)

    return render(request , 'index.html')



def play(request , room_code):
    username = request.GET.get('username')

    context = { 'room_code' : room_code , 'username': username}

    return render(request , 'play.html',context)                