function search_hangul(x) {

//document.write("시작");

   const request = new XMLHttpRequest();
   const url = 'https://muckmool.github.io/hangul_alphabet/' + x + '.html';

   request.open('GET', url, true);
   request.onload = function () {
      if( request.status == 200) {
         const str = request.responseText ;
         const strArray = str.split(" "); 
         
         //document.write(strArray[0].slice(3, 15));
         //document.write(strArray[1]); 

         document.write('<p><a href="https://muckmool.github.io/hangul_alphabet/'+ strArray[0].slice(3, 15) + '.html" target="main">' + x + '</a>');
         
      } else {
                console.log( request.status );
               document.write("문서없음");
             }   
    };
    request.send();

            
}