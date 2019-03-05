
var Vit_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_vit');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Vit_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_vit');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};

var Str_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_str');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Str_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_str');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};
var Agi_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_agi');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Agi_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_agi');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};
var Dex_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_dex');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Dex_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_dex');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};
var Inte_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_inte');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Inte_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_inte');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};
var Wis_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_wis');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Wis_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_wis');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};
var Pow_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_pow');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Pow_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_pow');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};
var Def_plus = function(button) {

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_def');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value >= 0.5){
  value += 0.5;
  label.innerHTML = value;
  ap_value -= 0.5;
  act_points.innerHTML = ap_value;
}

};

var Def_minus = function(button) {

  s_points = document.getElementById('source_points');
  var sp_value = parseFloat(s_points.textContent)
  if(isNaN(sp_value)){
    sp_value = 0.0
  }

  act_points = document.getElementById('act_points');
  var ap_value = parseFloat(act_points.textContent)
  if(isNaN(ap_value)){
    ap_value = 0.0
  }
  label = document.getElementById('add_def');
  var value = parseFloat(label.textContent);
  if(isNaN(value)){
    value = 0.0
  }
  if(ap_value < sp_value && value > 0){
  value -= 0.5;
  label.innerHTML = value;
  ap_value += 0.5;
  act_points.innerHTML = ap_value;
}

};

var set_post = function(button){

    var str_points = document.getElementById('add_str').textContent;
    var vit_points = document.getElementById('add_vit').textContent;
    var agi_points = document.getElementById('add_agi').textContent;
    var dex_points = document.getElementById('add_dex').textContent;
    var inte_points = document.getElementById('add_inte').textContent;
    var wis_points = document.getElementById('add_wis').textContent;
    var pow_points = document.getElementById('add_pow').textContent;
    var def_points = document.getElementById('add_def').textContent;

    var hid = document.getElementById('Points_data');
    hid.value = "Str:"+str_points + " " + "Vit:" + vit_points + " " + "Agi:" + agi_points + " "+
                 "Dex:" + dex_points + " " + "Int:" + inte_points + " "+ "Wis:" + wis_points + " "+
                 "Pow:" + pow_points + " " + "Def:" + def_points + " ";
}
