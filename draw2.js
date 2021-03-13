window.onload = function() {

var filter = "win16|win32|win64|mac|macintel"; 

if ( navigator.platform ) { 

      if ( filter.indexOf( navigator.platform.toLowerCase() ) < 0 ) { 
            document.write("터치");
            document.write('<script src ="https://muckmool.github.io/draw_touch.js"><', '/script>');
            
      } 
      else { 
               document.write("마우스");
               document.write('<script src ="https://muckmool.github.io/draw_mouse.js"><', '/script>');
               
            } 
}

}


