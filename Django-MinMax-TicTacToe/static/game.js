var room_code = '{{ room_code }}'
console.log(room_code )

var username = '{{ username }}'
var player = '{{ player }}'

let socket = new WebSocket('ws://localhost:8000/ws/game/' + room_code)

let gameState = ['' ,'','','','','', '','', '']

socket.onopen = function(e){
    console.log('connected')
}
