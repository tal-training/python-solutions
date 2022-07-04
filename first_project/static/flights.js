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

function refresh(interval=10000){
    setInterval('on_refresh()', interval); 
}


refresh();

function filter_table(field){
    for (let r of table.rows) {
        console.log(r.cells.namedItem("city"));
    }
}

