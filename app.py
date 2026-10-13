
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EduGenie - AI Study Assistant</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;background:#f2f5ff;color:#20264b}
header{background:#514fe5;color:white;padding:20px;text-align:center}
header h1{margin:0;font-size:28px}
header p{margin:7px 0 0}
.container{max-width:800px;margin:25px auto;padding:20px}
.card{background:white;padding:22px;border-radius:18px;box-shadow:0 5px 20px #0001}
h2{color:#514fe5}
label{display:block;font-weight:bold;margin:14px 0 7px}
select,textarea,input{width:100%;padding:12px;border:1px solid #d5d9ef;border-radius:10px;font-size:16px}
textarea{resize:vertical}
button{background:#514fe5;color:white;border:0;padding:13px 18px;border-radius:10px;font-size:16px;cursor:pointer}
button:hover{background:#3937bd}
#askBtn{width:100%;margin-top:15px}
#answer{white-space:pre-wrap;line-height:1.7;margin-top:20px}
.examples{display:flex;gap:8px;flex-wrap:wrap;margin-top:15px}
.examples button{font-size:13px;padding:9px}
footer{text-align:center;padding:20px;color:#777}
</style>
</head>
<body>
<header>
<h1>✦ EduGenie</h1>
<p>Your AI Study Assistant</p>
</header>

<div class="container">
<div class="card">
<h2>What do you want to learn today?</h2>
<p>Ask questions about any subject and learn step by step.</p>

<label for="subject">Choose Subject</label>
<select id="subject">
<option>General</option>
<option>Mathematics</option>
<option>Computer Science</option>
<option>Python</option>
<option>Java</option>
<option>Science</option>
<option>English</option>
<option>Tamil</option>
<option>History</option>
</select>

<label for="language">Choose Language</label>
<select id="language">
<option>Simple English</option>
<option>Tamil</option>
<option>Tanglish</option>
</select>

<label for="style">Answer Type</label>
<select id="style">
<option>Explain simply</option>
<option>Step-by-step explanation</option>
<option>2-mark answer</option>
<option>5-mark answer</option>
<option>10-mark answer</option>
<option>Give examples</option>
<option>Quiz questions</option>
</select>

<label for="question">Ask Your Question</label>
<textarea id="question" rows="4" placeholder="Type any study question here..."></textarea>

<button id="askBtn" onclick="askQuestion()">Ask EduGenie ✨</button>

<div class="examples">
<button onclick="fillQuestion('Explain Python in simple words')">Python</button>
<button onclick="fillQuestion('Explain algebra step by step')">Maths</button>
<button onclick="fillQuestion('Explain photosynthesis')">Science</button>
<button onclick="fillQuestion('Explain object oriented programming')">Computer Science</button>
</div>

<div id="answer"></div>
</div>
</div>

<footer>EduGenie © 2026 | Learn Something New Every Day</footer>

<script>
function fillQuestion(text){
 document.getElementById("question").value=text;
}

async function askQuestion(){
 const question=document.getElementById("question").value.trim();
 const subject=document.getElementById("subject").value;
 const language=document.getElementById("language").value;
 const style=document.getElementById("style").value;
 const answer=document.getElementById("answer");

 if(!question){
  answer.textContent="Please enter your question.";
  return;
 }

 answer.textContent="EduGenie is preparing your answer...";

 try{
  const response=await fetch("/api/ask",{
   method:"POST",
   headers:{"Content-Type":"application/json"},
   body:JSON.stringify({question,subject,language,style})
  });

  const data=await response.json();

  if(!response.ok){
   throw new Error(data.error||"Unable to answer right now.");
  }

  answer.textContent=data.answer;
 }catch(error){
  answer.textContent="Could not connect to the AI assistant. Please run the EduGenie backend and configure your private AI API key.\n\nDetails: "+error.message;
 }
}
</script>
</body>
</html>
