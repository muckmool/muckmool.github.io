//모바일용


  document.ontouchmove = function(e){ e.preventDefault(); }

  var canvas  = document.getElementById('main');
  var canvastop = canvas.offsetTop

  var context = canvas.getContext("2d");

  var lastx;
  var lasty;

  context.strokeStyle = "#000000";
  context.lineCap = 'round';
  context.lineJoin = 'round';
  context.lineWidth = 5;

  function clear() {
    context.fillStyle = "#ffffff";
    context.rect(0, 0, 300, 300);
    context.fill();
  }

  function dot(x,y) {
    context.beginPath();
    context.fillStyle = "#000000";
    context.arc(x,y,1,0,Math.PI*2,true);
    context.fill();
    context.stroke();
    context.closePath();
  }

  function line(fromx,fromy, tox,toy) {
    context.beginPath();
    context.moveTo(fromx, fromy);
    context.lineTo(tox, toy);
    context.stroke();
    context.closePath();
  }

  canvas.ontouchstart = function(event){                   
    event.preventDefault();                 
    
    lastx = event.touches[0].clientX;
    lasty = event.touches[0].clientY - canvastop;

    dot(lastx,lasty);
  }

  canvas.ontouchmove = function(event){                   
    event.preventDefault();                 

    var newx = event.touches[0].clientX;
    var newy = event.touches[0].clientY - canvastop;

    line(lastx,lasty, newx,newy);
    
    lastx = newx;
    lasty = newy;
  }

/*
  var clearButton = document.getElementById('clear')
  clearButton.onclick = clear

  clear()
*/

// PC용

let isAbleDraw = false;

        const options = {
            type: 'stroke',
            strokeStyle: 'black',
            lineWidth: 7,
        };

        const rects = [];
        let currentRect = null;

        document.getElementById('main2').addEventListener('mousedown', () => {
            isAbleDraw = true;
            currentRect = {
                type: options.type,
                strokeStyle: options.strokeStyle,
                lineWidth: options.lineWidth,
                coordinates: [],
            };
        });

        document.getElementById('main2').addEventListener('mousemove', (e) => {
            if (isAbleDraw) {
                const ctx = e.target.getContext('2d');
                const [x, y] = [e.offsetX, e.offsetY];
                currentRect.coordinates.push([x, y]);

                if (currentRect.type === 'stroke') drawTools.stroke(currentRect.coordinates, 'rgba(0, 0, 0, 1)', currentRect.lineWidth);
            }
        });

        
        document.getElementById('main2').addEventListener('mouseup', () => {
            isAbleDraw = false;
        });
       

        const drawTools = {

            stroke(coordinates, color, lineWidth) {
            	// 마우스가 이동한 경로를 따라 실선 그리기
                if (coordinates.length > 0) {
                    const ctx = document.getElementById('canvas').getContext('2d');
                    const firstCoordinate = coordinates[0];
                    ctx.beginPath();
                    ctx.moveTo(firstCoordinate[0], firstCoordinate[1]);
                    for (let i = 1; i < coordinates.length; i += 1) {
                        ctx.lineTo(coordinates[i][0], coordinates[i][1]);
                    }
                    ctx.strokeStyle = color;
                    ctx.lineWidth = lineWidth;
                    ctx.stroke();
                    ctx.closePath();
                }
            },

        };


