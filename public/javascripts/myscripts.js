//code for the car
function forward(){
  console.log("hello");
  //socket= new WebSocket('ws://95.44.225.20:2000');
  //socket.send('forward');
}
function moveleft(){
  socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send('moveleft');
}
function moveright(){
  socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send('moveright');
}
function backward(){
  socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send(' backward');
}
// code for the camera axis
function up(){
	socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send('up');

}
function left(){
	socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send('left');
}
function right(){
	socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send('right');
}
function down(){
	socket= new WebSocket('ws://95.44.225.20:2000');
  socket.send('down');
}
