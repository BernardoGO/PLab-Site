function point_it(event){
	alert(event);
	var milliseconds = (new Date).getTime();
	//window.location.href = "http://[IP]:[PORT]/index.html?mouse_x="+pos_x+"&mouse_y="+pos_y+ "&epoch="+milliseconds;
    window.location.href = "commd.py?cmd=" + event;
}

