function enterSearch() {
    if(event.keyCode == 13){
        
        popup();
        
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
 
    document.write('<p><p>한글 <span class="green_window"> <input id=hangul type="text" class="input_text" name="hangul"   style="width:300px" onkeydown="enterSearch()"  value = ', f_hangul , ' ></span>');
    document.write('<p><p>한자 <span class="green_window"> <input id=hanja type="text" class="input_text" name="hanja"     style="width:300px" onkeydown="enterSearch()"  value = ', f_hanja , ' ></span>');
    document.write('<p><p>스펠 <span class="green_window"> <input id=spell type="text" class="input_text" name="spell"     style="width:600px" onkeydown="enterSearch()"  value = ', f_spell , ' ></span>');
    document.write('<p><p>풀이 <span class="green_window"> <input id=story type="text" class="input_text" name="story"     style="width:600px" onkeydown="enterSearch()"  value = ', f_story , ' ></span>'); 
    document.write('<p><p>영어 <span class="green_window"> <input id=english type="text" class="input_text" name="english" style="width:300px" onkeydown="enterSearch()"  value = ', f_english , ' ></span>');
    document.write('<p><p>중국 <span class="green_window"> <input id=china type="text" class="input_text" name="china"     style="width:300px" onkeydown="enterSearch()"  value = ', f_china , ' ></span>');
    document.write('<p><p>일뜻 <span class="green_window"> <input id=meaning type="text" class="input_text" name="meaning" style="width:300px" onkeydown="enterSearch()"  value = ', f_meaning , ' ></span>');
    document.write('<p><p>일음 <span class="green_window"> <input id=sound type="text" class="input_text" name="sound"     style="width:300px" onkeydown="enterSearch()"  value = ', f_sound , ' ></span>');
  
    document.write('<input type="button" class="sch_smit" value="발행" onclick="myFunction()"/>');
    
    document.write('<script type="text/javascript" src="write2.js"></script>');
    
    
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
