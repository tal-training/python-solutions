table=document.getElementById('flights');

document.onload=check_status()

function check_status() {
    for (let r of table.rows) {
        if (r.rowIndex==0){
            continue;
        }
        if (r.cells.namedItem("status").innerText=="מבוטלת"){
            r.bgColor="pink"
        }
    }
}

function on_refresh() {
    
    location.reload();
}

function refresh(interval=60*5*1000){
    setInterval('on_refresh()', interval); 
}

let q="";
let rowstack=[]
function search_flights(e){
    if (document.getElementById("searchbox").value.length==0){
        q="";    
        while (rowstack!=[]){
            table.appendChild(rowstack.pop())
        }
        rowstack=[]
        return 
    }
    if (e.key=="Backspace"){
        q=q.slice(0,q.length-1);
        table.appendChild(rowstack.pop())
        return 
    }
    q=q+e.key
    for (let r of table.rows) {
        if (r.rowIndex==0){
            continue
        }
        for (let c of r.cells){
            if (c.innerText.toLowerCase().search(q)>-1){
                c.bgColor="yellow"
                break
            }
            else {
                c.bgColor="white"
                rowstack.push(r)
                r.remove()
                // FILTER REMOVE r.remove()
            }
        }
    }
}

refresh();

let tag=document.createElement("h3");
let date=document.createTextNode("Refreshed on: "+Date());
tag.appendChild(date);
document.getElementsByTagName("body")[0].appendChild(tag);

let search=document.createElement("div");
search.setAttribute("id", "search")
let searchbox=document.createElement("input")
searchbox.addEventListener('keydown', search_flights)
searchbox.setAttribute("id", "searchbox")
let searchlabel=document.createTextNode("Search Flights:")
search.appendChild(searchbox)
document.getElementsByTagName("body")[0].appendChild(searchlabel);
document.getElementsByTagName("body")[0].appendChild(search);
searchbox.focus()


