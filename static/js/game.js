
var gamequad;

function startGame() {
  myGameArea.start();
  gamequad = new component(30,30,100,100,"red");
}

var myGameArea = {
  canvas : document.getElementById('gameCanvas'),
  start : function() {
    this.canvas.width = 480;
    this.canvas.height = 270;
    this.context = this.canvas.getContext("2d");
    document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    this.interval = setInterval(updateGameArea, 30);
    widnow.addEventListener('keydown', function(e){
      myGameArea.key = e.keyCode;
    })
    window.addEventListener('keyup', function(e){
      myGameArea.key = false;
    })
  },
  clear : function(){
    this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
  }

}

var component = function(x,y,width,height,color){
  this.width = width;
  this.height = height;
  this.x = x;
  this.y = y;
  this.update = function(){
  ctx = myGameArea.context;
  ctx.fillStyle = color;
  ctx.fillRect(this.x, this.y, this.width , this.height);
  }
  this.move_down = function(){
    this.y += 1;
  }
  this.move_up = function(){
    this.y -= 1;
  }
  this.move_left = function(){
    this.x -= 1;
  }
  this.move_right = function(){
    this.x += 1;
  }
}

var updateGameArea = function(){
  myGameArea.clear();
  if (myGameArea.key && myGameArea.key == 37) {gamequad.move_left(); }
  if (myGameArea.key && myGameArea.key == 39) {gamequad.move_right(); }
  if (myGameArea.key && myGameArea.key == 38) {gamequad.move_up(); }
  if (myGameArea.key && myGameArea.key == 40) {gamequad.move_down(); }
  gamequad.update();
}
