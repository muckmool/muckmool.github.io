function enterSearch() {
    if(event.keyCode == 13){
        myFunction();  // 실행할 이벤트
    }
}
  
function myFunction() {
  
    var f_hangul = document.getElementById("hangul").value;
    var f_hanja = document.getElementById("hanja").value;
    var f_spell = document.getElementById("spell").value;
    var f_story = document.getElementById("story").value;
    var f_english = document.getElementById("english").value;
    var f_china = document.getElementById("china").value;
    var f_meaning = document.getElementById("meaning").value;
    var f_sound = document.getElementById("sound").value;
    
    window.open(popup.html);
    
    document.write('<p>----------------------------------------------------------------');
    document.write('<p>', f_hangul ,' ', f_hanja, ' [', f_english , ' ' , f_china , ']' );
    document.write('<p>스펠: ', f_spell);
    document.write('<p>풀이: ', f_story);
    document.write('<p>영어: ', f_english);
    document.write('<p>중국: ', f_china);    
    document.write('<p>일뜻: ', f_meaning);
    document.write('<p>일음: ', f_sound);
    document.write('<p>');
  
}
