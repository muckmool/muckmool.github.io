var express = require('express');
var app = express();
var db_config = require(__dirname + '/config/database.js');
var conn = db_config.init();
var bodyParser = require('body-parser');

db_config.connect(conn);

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : false}));

app.get('/', function (req, res) {
    res.send('ROOT');
});


// list

app.get('/list', function (req, res) {
    var sql = 'SELECT * FROM board order by SEQN';    
    conn.query(sql, function (err, rows, fields) {
        if(err) console.log('query is not excuted. select fail...\n' + err);
        else res.render('list2.ejs', {list : rows});
    });
});

app.get('/list-desc', function (req, res) {
    var sql = 'SELECT * FROM board order by SEQN DESC limit 50';    
    conn.query(sql, function (err, rows, fields) {
        if(err) console.log('query is not excuted. select fail...\n' + err);
        else res.render('list2.ejs', {list : rows});
    });
});


app.post('/listAf', function (req, res) {
    var body = req.body;
    console.log(body);

    var sql = 'SELECT * FROM board WHERE LINK = (?)';
    var params = [body.LINK];
    console.log(sql);
    conn.query(sql, params, function (err, rows, fields) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else res.render('list2.ejs', {list : rows});
    });
});



// publish

app.get('/publish', function (req, res) {
    var sql = 'SELECT MAX(SEQN) as SEQN FROM board';

    console.log(sql);
    conn.query(sql, function (err, rows, fields) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else res.render('publish.ejs', {list : rows});
    });

});




app.post('/publishAf', function (req, res) {
    var body = req.body;
    console.log(body);

    var sql = 'SELECT * FROM board WHERE SEQN = (?) OR HANJA = (?) OR HANGUL = (?)';
    var params = [body.HANGUL, body.HANGUL, body.HANGUL];
    console.log(sql);
    conn.query(sql, params, function (err, rows, fields) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else 
        
        
        sql = 'SELECT * FROM board WHERE HANGUL = (?) UNION ALL SELECT * FROM board WHERE HANGUL = (?) UNION ALL SELECT * FROM board WHERE HANGUL = (?) UNION ALL SELECT * FROM board WHERE HANGUL = (?) UNION ALL SELECT * FROM board WHERE HANGUL = (?) UNION ALL SELECT * FROM board WHERE HANGUL = (?)';
        params = [rows[0].HANGUL, rows[0].H1, rows[0].H2, rows[0].H3, rows[0].H4, rows[0].H5];
        console.log(sql);
        conn.query(sql, params, function (err, rows, fields) {
            if(err) console.log('query is not excuted. insert fail...\n' + err);
            else res.render('publish_result.ejs', {list : rows});
        });


    });
});


// search

app.get('/search', function (req, res) {
    var sql = 'SELECT MAX(SEQN) as SEQN FROM board';

    console.log(sql);
    conn.query(sql, function (err, rows, fields) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else res.render('search.ejs', {list : rows});
    });

});



app.post('/searchAf', function (req, res) {
    var body = req.body;
    console.log(body);

    var sql = 'SELECT * FROM board WHERE HANGUL = (?) OR SEQN = (?) OR HANJA = (?)';
    var params = [body.HANGUL, body.HANGUL, body.HANGUL];
    console.log(sql);
    conn.query(sql, params, function (err, rows, fields) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else res.render('search_list.ejs', {list : rows});
    });
});



app.post('/searchAf2', function (req, res) {
    var body = req.body;
    console.log(body);
   

    var sql = 'SELECT * FROM board WHERE HANGUL = ?';
    var params = [body.HANGUL];
    conn.query(sql, params, function (err, rows, fields) {
        if(err) console.log('query is not excuted. select fail...\n' + err);
        else console.log(rows[0].HANGUL, rows[0].H1, rows[0].H2, rows[0].H3, rows[0].H4, rows[0].H5, );

        var sql = 'SELECT * FROM board WHERE HANGUL = ? OR HANGUL = ? OR HANGUL = ? OR HANGUL = ? OR HANGUL = ? OR HANGUL = ?';                      
        var params = [body.HANGUL, rows[0].H1, rows[0].H2, rows[0].H3, rows[0].H4, rows[0].H5];
        console.log(sql);
        conn.query(sql, params, function (err, rows, fields) {
            if(err) console.log('query is not excuted. select fail...\n' + err);
            else res.render('list2.ejs', {list : rows});
        });


    });


});




app.post('/updateAf', function (req, res) {
    var body = req.body;
    console.log(body);

 
    var sql = 'UPDATE board SET SEQN=?, H1=?, C1=?, H2=?, C2=?, H3=?, C3=?, H4=?, C4=?, H5=?, C5=? ,EXPL=? ,LINK=? WHERE HANGUL = ?';
    var SEQN = body.SEQN;
    var H1 = body.H1;
    var H2 = body.H2; 
    var H3 = body.H3;   
    var H4 = body.H4;
    var H5 = body.H5;
    var EXPL = body.EXPL;
    var LINK = body.LINK;
    var HANGUL = body.HANGUL;
    console.log(sql);
    conn.query(sql, [SEQN, H1, H1, H2, H2, H3, H3, H4, H4, H5, H5, EXPL, '.', HANGUL], function (err) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else console.log('hangul update success'); // console.log(body);
    });

    
    var sql = 'SELECT * FROM board WHERE HANGUL = ?';
    var params = [body.HANGUL];
    console.log(sql);
    conn.query(sql, params, function (err, rows, fields) {
        if(err) console.log('query is not excuted. select fail...\n' + err);
        else res.render('update_list.ejs', {list : rows});
    });
   
    

});



app.post('/updateAf_3', function (req, res) {
    var body = req.body;
    console.log(body);

    // hangul update

    var sql = 'UPDATE board SET SEQN=?, HANJA=?, H1=?, C1=?, H2=?, C2=?, H3=?, C3=?, H4=?, C4=?, H5=?, C5=? ,EXPL=? ,LINK=? ,CHINESE=? ,JAPANESE=? WHERE HANGUL = ?';
    var SEQN = body.SEQN;
    var HANJA = body.HANJA;
    var H1 = body.H1;
    var H2 = body.H2; 
    var H3 = body.H3;   
    var H4 = body.H4;
    var H5 = body.H5;
    var EXPL = body.EXPL;
    var LINK = body.LINK;
    var CHINESE = body.CHINESE;
    var JAPANESE = body.JAPANESE;
    var HANGUL = body.HANGUL;
    console.log(sql);
    conn.query(sql, [SEQN, HANJA, H1, H1, H2, H2, H3, H3, H4, H4, H5, H5, EXPL, LINK, CHINESE, JAPANESE, HANGUL], function (err) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else console.log('hangul update success'); // console.log(body);
    });


        // change c1

            var sql = 'SELECT HANJA FROM board WHERE HANGUL = ?';
            var params = [body.H1];
            console.log(sql);
            conn.query(sql, params, function (err, rows, fields) {
                if(err) console.log('query is not excuted. select fail...\n' + err);
                else if(rows.length >0) 
                     var C1 = rows[0].HANJA; 
                     body.C1 = C1;
                     var HANGUL = body.HANGUL;
                     var sql = 'UPDATE board SET C1=? WHERE HANGUL = ?';
                     console.log(sql);
                     conn.query(sql, [C1, HANGUL], function (err) {
                         if(err) console.log('query is not excuted. insert fail...\n' + err);
                         else console.log(C1);
                     
                     }); 

            });

                    // change c2

                    var sql = 'SELECT HANJA FROM board WHERE HANGUL = ?';
                    var params = [body.H2];
                    console.log(sql);
                    conn.query(sql, params, function (err, rows, fields) {
                        if(err) console.log('query is not excuted. select fail...\n' + err);
                        else if(rows.length >0) 
                             var C2 = rows[0].HANJA; 
                             body.C2 = C2;
                             var HANGUL = body.HANGUL;
                             var sql = 'UPDATE board SET C2=? WHERE HANGUL = ?';
                             console.log(sql);
                             conn.query(sql, [C2, HANGUL], function (err) {
                                 if(err) console.log('query is not excuted. insert fail...\n' + err);
                                 else console.log(C2);
                             
                             }); 
        
                    });

                            // change c3

            var sql = 'SELECT HANJA FROM board WHERE HANGUL = ?';
            var params = [body.H3];
            console.log(sql);
            conn.query(sql, params, function (err, rows, fields) {
                if(err) console.log('query is not excuted. select fail...\n' + err);
                else if(rows.length >0) 
                     var C3 = rows[0].HANJA; 
                     body.C3 = C3;
                     var HANGUL = body.HANGUL;
                     var sql = 'UPDATE board SET C3=? WHERE HANGUL = ?';
                     console.log(sql);
                     conn.query(sql, [C3, HANGUL], function (err) {
                         if(err) console.log('query is not excuted. insert fail...\n' + err);
                         else console.log(C3);
                     
                     }); 

            });

                    // change c4

                    var sql = 'SELECT HANJA FROM board WHERE HANGUL = ?';
                    var params = [body.H4];
                    console.log(sql);
                    conn.query(sql, params, function (err, rows, fields) {
                        if(err) console.log('query is not excuted. select fail...\n' + err);
                        else if(rows.length >0) 
                             var C4 = rows[0].HANJA; 
                             body.C4 = C4;
                             var HANGUL = body.HANGUL;
                             var sql = 'UPDATE board SET C4=? WHERE HANGUL = ?';
                             console.log(sql);
                             conn.query(sql, [C4, HANGUL], function (err) {
                                 if(err) console.log('query is not excuted. insert fail...\n' + err);
                                 else console.log(C4);
                             
                             }); 
        
                    });


                            // change c5

            var sql = 'SELECT HANJA FROM board WHERE HANGUL = ?';
            var params = [body.H5];
            console.log(sql);
            conn.query(sql, params, function (err, rows, fields) {
                if(err) console.log('query is not excuted. select fail...\n' + err);
                else if(rows.length >0) 
                     var C5 = rows[0].HANJA; 
                     body.C5 = C5;
                     var HANGUL = body.HANGUL;
                     var sql = 'UPDATE board SET C5=? WHERE HANGUL = ?';
                     console.log(sql);
                     conn.query(sql, [C5, HANGUL], function (err) {
                         if(err) console.log('query is not excuted. insert fail...\n' + err);
                         else console.log(C5);
                     
                     }); 

            });
       
        


    
    var sql = 'SELECT * FROM board WHERE HANGUL = ?';
    var params = [body.HANGUL];
    console.log(sql);
    conn.query(sql, params, function (err, rows, fields) {
        if(err) console.log('query is not excuted. select fail...\n' + err);
        else res.render('search_list.ejs', {list : rows});
    });
    

});


app.get('/write', function (req, res) {
    var sql = 'SELECT MAX(SEQN)+1 as SEQN FROM board';
        
    console.log(sql);
    conn.query(sql, function (err, rows, fields) {
        if(err) console.log('query is not excuted. select fail...\n' + err);
        else res.render('write.ejs', {list : rows});
    });
});


app.post('/writeAf', function (req, res) {
    var body = req.body;
    console.log(body);


    var sql = 'INSERT INTO board (`SEQN`, `HANGUL`, `HANJA`, `H1`, `H2`, `H3`, `H4`, `H5`, `C1`, `C2`, `C3`, `C4`, `C5`, `EXPL`, `LINK`) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';
    var params = [body.SEQN, body.HANGUL, ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."];
    console.log(sql);
    conn.query(sql, params, function(err) {
        if(err) console.log('query is not excuted. insert fail...\n' + err);
        else res.redirect('/list-desc');
    });
});


app.listen(8080, () => console.log('Server is running on port 8080...'));
