const form=document.getElementById('riskForm');
const $=id=>document.getElementById(id);
function setExample(values){
  for(const [k,v] of Object.entries(values)){
    const el=form.elements[k]; if(!el)continue;
    if(el.type==='checkbox')el.checked=!!v;else el.value=v;
  }
}
$('safeExample').addEventListener('click',()=>setExample({amount:850,new_payee:false,urgent_request:false,collect_request:false,unknown_qr:false,unusual_time:false,message:'Payment for a known local shop'}));
$('scamExample').addEventListener('click',()=>setExample({amount:32000,new_payee:true,urgent_request:true,collect_request:true,unknown_qr:true,unusual_time:true,message:'URGENT: account blocked. Verify now, share OTP for refund'}));
form.addEventListener('submit',async e=>{
 e.preventDefault();$('error').textContent='';
 const data={};new FormData(form).forEach((v,k)=>data[k]=v);
 ['new_payee','urgent_request','collect_request','unknown_qr','unusual_time'].forEach(k=>data[k]=form.elements[k].checked);
 try{
  const r=await fetch('/assess',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
  const d=await r.json();if(!r.ok)throw new Error(d.error||'Assessment failed');
  $('empty').hidden=true;$('result').hidden=false;
  $('score').textContent=d.score;$('level').textContent=d.level;$('level').className='level '+d.color;
  $('meterFill').style.width=d.score+'%';$('meterFill').className=d.color;
  $('reasons').innerHTML='';d.reasons.forEach(reason=>{const li=document.createElement('li');li.textContent=reason;$('reasons').appendChild(li)});
  $('advice').textContent=d.advice;$('disclaimer').textContent=d.disclaimer;
 }catch(err){$('error').textContent=err.message}
});
