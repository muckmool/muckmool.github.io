
        let isAbleDraw = false;

        const options = {
            type: 'stroke',
            strokeStyle: 'black',
            lineWidth: 4,
        };

        const rects = [];
        let currentRect = null;



        document.getElementById('main').addEventListener('pointerdown', () => {
            isAbleDraw = true;
            currentRect = {
                type: options.type,
                strokeStyle: options.strokeStyle,
                lineWidth: options.lineWidth,
                coordinates: [],
            };
        });

        document.getElementById('main').addEventListener('pointermove', (e) => {
            if (isAbleDraw) {
                const ctx = e.target.getContext('2d');
                const [x, y] = [e.offsetX, e.offsetY];
                currentRect.coordinates.push([x, y]);

                if (currentRect.type === 'stroke') drawTools.stroke(currentRect.coordinates, 'rgba(0, 0, 0, 1)', currentRect.lineWidth);
            }
        });

        
        document.getElementById('main').addEventListener('pointerup', () => {
            
       
            
            isAbleDraw = false;
            
        });



        const drawTools = {

            stroke(coordinates, color, lineWidth) {
            	// 마우스가 이동한 경로를 따라 실선 그리기
                if (coordinates.length > 0) {
                    const ctx = document.getElementById('main').getContext('2d');
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



