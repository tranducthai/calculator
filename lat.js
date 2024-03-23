let va=document.getElementById("a");
let vb=document.getElementById("b");
let re=document.getElementById("resu");
function cong()
{

    let numA = parseFloat(va.value) || 0;
    let numB = parseFloat(vb.value) || 0;
    let c=numA+numB;

re.innerText="Result = "+c;
}
function tru()
{

    let numA = parseFloat(va.value) || 0;
    let numB = parseFloat(vb.value) || 0;
    let c=numA-numB;

re.innerText="Result = "+c;
}
function nhan()
{

    let numA = parseFloat(va.value) || 0;
    let numB = parseFloat(vb.value) || 0;
    let c=numA*numB;

re.innerText="Result = "+c;
}
function chia()
{

    let numA = parseFloat(va.value) || 0;
    let numB = parseFloat(vb.value) || 0;
    let c=numA/numB;

re.innerText="Result = "+c;
}



