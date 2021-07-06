#!/usr/bin/python3

import cgi
import subprocess
import json

print("context-type:text/html")
print()

print('''<style>
body{
       background-image: url('https://www.autoguide.com/blog/wp-content/uploads/                                                       2021/06/2022-Hyundai-Elantra-N-Teasers-02.jpg');
       background-repeat: no-repeat;
       background-attachment: fixed;
       background-size: cover;
}

#d1{
    height: 80%;
    width: 40%;
    font-size: 20px;
    font-weight: bold;
    background-color: #ffffff10;
    background-size: cover;
    border-radius: 10px;
    margin-top: 2%;
    margin-left: 10%;
    border-width: 2px;
    overflow : auto;
    overflow-y: auto;
    color:rgb(5, 5, 5);
}
#d{
        padding-top: 30px;
        padding-left: 150px;
}

input{
        width: 34.2%;
        height: 6%;
        border: 3px solid #4cddf7;
        border-radius: 15px;
        font-size: 16px;
        background-color: white;
        background-position: 10px 10px;
        background-repeat: no-repeat;
        padding: 12px 30px 12px 30px;
}


#btn1{
        width: 8.5%;
        height: 6%;
        margin-left: 1.1%;
        border-radius: 10px;
        background-color: white;
        color: black;
        font-weight: bold;
        border: 2px solid #4cddf7;
        transition-duration: 0.1s;
}

#btn1:hover{
        background-color: #0492c2;
    }

</style>''')
f = cgi.FieldStorage()
cmd = f.getvalue("x")
#out = subprocess.getoutput(cmd)
cm1 = json.dumps(cmd, indent = 1)
if cmd != '':
    print("<body>")
    print('''<div id='d'>
            <input id='inp1' placeholder="Enter Registration Number Here...">
            <button onclick="cmd()" id='btn1'>submit</button>
        </div>
     ''')
    print(f'''<div id='d1' align='center'>
            <h1  style="color: rgb(243, 23, 23);"><b>Details of car</b></h1>
           <p id='p1'>{cm1}</p>
`           </div>
    ''')
    print('''<script>
    function cmd(){
    i = document.getElementById('inp1').value;
    x = document.getElementById('p1');
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://192.168.99.102/cgi-bin/car1.py?x="+i,false);
    xhr.send();
    var output1 = xhr.responseText;
    x.innerHTML = output1;
}

   </script>''')
    print("</body>")
