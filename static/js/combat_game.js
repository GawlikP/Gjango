

console.log('starting battle');
// document.getElementById('myTextarea').value = '';
var startGame = function() {
var text_area = document.getElementById('game_textarea');
text_area.value += player.name + "\n";
text_area.value += player.clss + "\n";
text_area.value += enemy.name + "\n"
text_area.value += enemy.clss + "\n"
while(player.hp > 0 && enemy.hp > 0){
  start_tour(player,text_area);
  attack(player,enemy,text_area);
  if(enemy.hp < 0) break;
  start_tour(enemy,text_area);
  attack(enemy,player,text_area);
}
if(player.hp < 0) text_area.value += " Enemy win !";
else text_area.value += "Player win !";

}

var start_tour = function(character,text_area){
    text_area.value += character.name + " is starting tour \n";
    text_area.value += character.name + " HP :"+ character.hp + " regenerated hp " + character.regeneration + " hp.  \n";
    character.hp += character.regeneration;
    if (character.hp > character.max_hp) character.hp = character.max_hp;
}

var attack = function(attacking,defending,text_area){
    if(getRandomInt(1,100000) <= defending.dodge){
      text_area.value += defending.name + " is dodged ! \n"
      return;
    }
    dmg = attacking.dmg;
    if(getRandomInt(1,10000) <= attacking.crit_chance*1000) {
      text_area.value += attacking.name + " critical damage !\n"
      dmg += dmg + attacking.crit_chance;
    }
    armor = defending.armor;
    armor -= attacking.armmor_pen;
    dmg = dmg * (1 - armor/100);
    defending.hp -= dmg
    text_area.value += attacking.name +" is dealing " + dmg + " dmg ! \n";
}

function getRandomInt(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}
