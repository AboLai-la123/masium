function rettext(value) {
	if (value) {
		return $('<div/>').text(value).html();
	} else {
		return '';
	}
}


snack_wit = false;
added_snack = [];
snacks = 0;
function snackBar(title , tp="0"){
	if(tp == "1"){
		if(snack_wit == false){
			snack_wit = true;
			document.getElementById("snackbar").removeAttribute("style");
			setTimeout(function(){
				document.getElementById("snackbar").style.bottom="20px";
				document.getElementById("snackbarText").innerHTML = String(rettext(title));
				setTimeout(function(){
					document.getElementById("snackbar").removeAttribute("style");
					snack_wit = false;
					snacks -= 1;
					if(snacks == 0){}
					else{
						otherSnackbar(added_snack[snacks]);
					}
				} , 5000);
			},250);
		}
	}else{
		added_snack.push(String(rettext(title)));
		snacks += 1;
		if(snack_wit == false){
			snack_wit = true;
			document.getElementById("snackbar").removeAttribute("style");
			setTimeout(function(){
				document.getElementById("snackbar").style.bottom="20px";
				document.getElementById("snackbarText").innerHTML = String(rettext(title));
				setTimeout(function(){
					document.getElementById("snackbar").removeAttribute("style");
					snack_wit = false;
					snacks -= 1;
					if(snacks == 0){}
					else{
						otherSnackbar(added_snack[snacks]);
					}
				} , 5000);
			},250);
		}
	}
}
function otherSnackbar(title){
	if(snack_wit == false){
		snack_wit = true;
		document.getElementById("snackbar").removeAttribute("style");
		setTimeout(function(){
			document.getElementById("snackbar").style.bottom="20px";
			document.getElementById("snackbarText").innerHTML = String(title);
			setTimeout(function(){
				document.getElementById("snackbar").removeAttribute("style");
				snack_wit = false;
				snacks -= 1;
				if(snacks <= 0){}
				else{
					snackBar(added_snack[snacks],"1");
				}
			} , 5000);
		},250);
	}
}

$(document).on("submit", "form",function(e){
	e.preventDefault();
	this_el = this;
	this_el.style.opacity = ".8";
	var formData = new FormData(this);
	$.ajax({
		url: location.href,
		data: formData,
		type: 'POST',
		dataType: 'json',
		mimeType: 'multipart/form-data',
		contentType: false,
		cache: false,
		processData: false,
		success: function(res) {
			if(this_el.id == "chatForm"){
				if(document.getElementById("messageInput").value.trim() != ""){
					$(".chat-container").append(`<div class="width-100"><p class="text-user-1">${document.getElementById("messageInput").value}</p></div>`);
			
					document.getElementById("messageInput").value = "";
				}
				$('.chat-container').scrollTop(60000000600000006000000060000000);
			}
			this_el.removeAttribute("style");
			if(res.errtitle != ""){
				snackBar(res.errtitle);
			}else{
				if(this_el.dataset.function != undefined){
					window[this_el.dataset.function]();
				}
			}
		},
		error: function(res){
			console.log(res);
		}
	});
});



function homeRedirect(){
	location.href = '/';
}
function profileRedirect(){
	location.href = '/profile';
}

function profileRedirect(){
	location.href = '/profile';
}

$(document).on("change", "#brand", function(){
	if(this.value != "----------"){
		document.getElementById("carDetails").style.display = "block";
		if(this.value == "تويوتا"){
			types = [
				"----------",
				"كامري",
				"كورولا",
				"أفالون",
				"يارس",
				"هايلاندر",
				"فورتشنر",
				"لاندكروزر",
				"برادو"
			]
		}else if(this.value == "هونداي"){
			types = [
				"----------",
				"إكسنت",
				"إلنترا",
				"سوناتا",
				"أزيرا",
				"كريتا",
				"سنتافي"
			]
		}else if(this.value == "جمس"){
			types = [
				"----------",
				"سييرا",
				"يوكن",
				"يوكن XL",
				"أكاديا"
			]
		}else if(this.value == "فورد"){
			types = [
				"----------",
				"F150",
				"إكسبلورر",
				"إكسبديشن",
				"إيدج",
				"توروس",
				"فليكس",
				"كراون فكتوريا"
			]
		}
		$("#vehicleType").empty();
		document.getElementById("carDetails2").style.display = "none";
		types.forEach(type => {
			const newOption = document.createElement('option');
			const optionText = document.createTextNode(type);
			newOption.appendChild(optionText);
			newOption.setAttribute('value',type);
			const select = document.getElementById('vehicleType');
			select.appendChild(newOption);
		});
	}
	else{
		document.getElementById("carDetails").style.display = "none";
		document.getElementById("carDetails2").style.display = "none";
	}
});



$(document).on("change", "#vehicleType", function(){
	if(this.value != "----------"){
		document.getElementById("carDetails2").style.display = "block";
		if(this.value == "كامري"){
			types = [
				"----------",
				"GL",
				"GL Limited",
				"GL Standarnd",
				"GLX",
				"GLX Premium",
				"GLX Sport Z",
				"ستاندرد",
				"جراندي",
			]
		}else if(this.value == "كورولا"){
			types = [
				"----------",
				"XLI",
				"GLI",
				"Sport 1.6",
				"Limited 1.6",
				"كروس هايبرد ستاندرد",
				"كروس هايبرد نص فل",
				"كروس هايبرد فل كامل",
			]
		}
		else if(this.value == "أفالون"){
			types = [
				"----------",
				"ليميتد",
				"بريميوم",
				"ستاندرد",
				"XL",
				"SE",
			]
		}
		else if(this.value == "يارس"){
			types = [
				"----------",
				"S",
				"STD",
				"Y",
				"E",
				"SE",
			]
		}
		else if(this.value == "هايلاندر"){
			types = [
				"----------",
				"هايبرد",
				"ليميتد",
				"VXR",
				"GXR",
			]
		}
		else if(this.value == "فورتشنر"){
			types = [
				"----------",
				"GX",
				"VX",
				"TRD",
			]
		}
		else if(this.value == "لاندكروزر"){
			types = [
				"----------",
				"GXR",
				"VXR",
				"VXS",
				"GR",
				"VX",
			]
		}
		else if(this.value == "برادو"){
			types = [
				"----------",
				"TX",
				"TXL",
				"VX",
				"VXR",
			]
		}
		else if(this.value == "إكسنت"){
			types = [
				"----------",
				"GL",
				"GLS",
				"ستاندرد",
				"فل كامل",
				"نص فل",
			]
		}else if(this.value == "إلنترا"){
			types = [
				"----------",
				"فل كامل",
				"ستاندرد",
				"نص فل",
				"بريميوم",
				"ليميتد",
				"ميد",
			]
		}

		else if(this.value == "سوناتا"){
			types = [
				"----------",
				"GDI",
				"GL",
				"GLS",
				"ستاندرد",
				"فل كامل",
				"نص فل",
			]
		}
		else if(this.value == "أزيرا"){
			types = [
				"----------",
				"فل كامل",
				"ستاندرد",
				"نص فل",
				"بريميوم",
				"كلاسيك",
			]
		}
		else if(this.value == "كريتا"){
			types = [
				"----------",
				"GL",
				"GLS",
				"فل كامل",
				"نص فل",
				"ستاندرد",
			]
		}
		else if(this.value == "سنتافي"){
			types = [
				"----------",
				"GL",
				"GLS",
				"نص فل",
				"ستاندرد",
				"فل كامل",
			]
		}


		else if(this.value == "سييرا"){
			types = [
				"----------",
				"SLE",
				"ستاندرد",
				"دينالي",
				"SLT",
				"AT4",
			]
		}
		else if(this.value == "يوكن"){
			types = [
				"----------",
				"SLE",
				"SLT",
				"دينالي",
				"AT4",]
		}
		else if(this.value == "يوكن XL"){
			types = [
				"----------",
				"SLE",
				"SLT",
				"دينالي",]
		}
		else if(this.value == "أكاديا"){
			types = [
				"----------",
				"SLE",
				"SLT",
				"دينالي",
				"AT4",]
		}



		else if(this.value == "F150"){
			types = [
				"----------",
				"Lariat",
				"Raptor",
				"XLT",
				"بلاتينوم",
				"سبيشال اديشن",]
		}
		else if(this.value == "إكسبلورر"){
			types = [
				"----------",
				"XLT",
				"سبورت",
				"ستاندرد",
				"ليميتد",
				"نص فل",
				"بلاتينوم",]
		}
		else if(this.value == "إكسبديشن"){
			types = [
				"----------",
				"XL",
				"XLT",
				"ستاندرد",
				"ليميتد دبل",
				"بلاتينيوم",]
		}
		else if(this.value == "إيدج"){
			types = [
				"----------",
				"SEL",
				"SE",
				"تيتانيوم",
				"ليميتد",
				"ستاندرد",]
		}
		else if(this.value == "توروس"){
			types = [
				"----------",
				"SE",
				"SEL",
				"ليميتد",
				"ستاندرد",
				"فل كامل",
				"ايكوبوست",]
		}
		else if(this.value == "فليكس"){
			types = [
				"----------",
				"SEL",
				"ستاندرد",
				"ليميتد",]
		}
		else if(this.value == "كراون فكتوريا"){
			types = [
				"----------",
				"فل كامل",
				"نص فل",
				"بوليسي",]
		}

		$("#model").empty();
		types.forEach(type => {
			const newOption = document.createElement('option');
			const optionText = document.createTextNode(type);
			newOption.appendChild(optionText);
			newOption.setAttribute('value',type);
			const select = document.getElementById('model');
			select.appendChild(newOption);
		});
	}
	else{
		document.getElementById("carDetails2").style.display = "none";
	}
});


$(document).on("change", "#model,#modelYear,#maintenance,#status,#walkway,#interior", function(){
	if(this.value != "----------"){
		brands={
			"تويوتا":{
				"كامري":{
					"GL":90000,
					"GL Limited":112000,
					"GL Standarnd":99820,
					"GLX":102000,
					"GLX Premium":107000,
					"GLX Sport Z":120000,
					"ستاندرد":95000,
					"جراندي":150000,
				},
				"كورولا":{
					"XLI":68400,
					"GLI":109940,
					"Sport 1.6":68400,
					"Limited 1.6":109940,
					"كروس هايبرد ستاندرد":109940,
					"كروس هايبرد نص فل":109940,
					"كروس هايبرد فل كامل":109940,
				},

				"أفالون":{
					"ليميتد":163000,
					"بريميوم":180000,
					"ستاندرد":150000,
					"XL":114000,
					"SE":143000,
				},
				"يارس":{
					"S":53000,
					"STD":60000,
					"Y":60000,
					"E":53300,
					"SE":46000,
				},
				"هايلاندر":{
					"هايبرد":160000,
					"ليميتد":193000,
					"VXR":200000,
					"GXR":172000,
				},
				"فورتشنر":{
					"GX":135000,
					"VX":151000,
					"TRD":113000,
				},
				"لاندكروزر":{
					"GXR":286000,
					"VXR":304000,
					"VXS":330000,
					"GR":400000,
					"VX":350000,
				},
				"برادو":{
					"TX":145000,
					"TXL":176000,
					"VX":200000,
					"VXR":202000,
				},
			},
			"هونداي":{
				"إكسنت":{
					"GL":40000,
					"GLS":43000,
					"ستاندرد":67000,
					"فل كامل":76000,
					"نص فل":65000,
				},
				"إلنترا":{
					"فل كامل":90000,
					"ستاندرد":70000,
					"نص فل":80000,
					"بريميوم":105000,
					"ليميتد":78000,
					"ميد":90000,
				},
				"سوناتا":{
					"GDI":106000,
					"GL":75000,
					"GLS":90000,
					"ستاندرد":97000,
					"فل كامل":112000,
					"نص فل":100000,
				},
				"أزيرا":{
					"فل كامل":115000,
					"ستاندرد":85000,
					"نص فل":100000,
					"بريميوم":170000,
					"كلاسيك":150000,
				},
				"كريتا":{
					"GL":60000,
					"GLS":65000,
					"فل كامل":76000,
					"نص فل":89000,
					"ستاندرد":65000,
				},
				"سنتافي":{
					"GL":77000,
					"GLS":90000,
					"نص فل":100000,
					"ستاندرد":100000,
					"فل كامل":112000,
				},
			},
			"جمس":{
				"سييرا":{
					"SLE":184000,
					"ستاندرد":133000,
					"دينالي":290000,
					"SLT":250000,
					"AT4":225000,
				},
				"يوكن":{
					"SLE":240000,
					"SLT":280000,
					"دينالي":335000,
					"AT4":300000,
				},
				"يوكن XL":{
					"SLE":240000,
					"SLT":300000,
					"دينالي":290000,
				},
				"أكاديا":{
					"SLE":133000,
					"SLT":180000,
					"دينالي":200000,
					"AT4":165000,
				}
			},
			"فورد":{
				"F150":{
					"Lariat":193000,
					"Raptor":300000,
					"XLT":260000,
					"بلاتينوم":280000,
					"سبيشال اديشن":193000,
				},
				"إكسبلورر":{
					"XLT":135000,
					"سبورت":200000,
					"ستاندرد":150000,
					"ليميتد":200000,
					"نص فل":175000,
					"بلاتينوم":241000,
				},
				"إكسبديشن":{
					"XL":150000,
					"XLT":240000,
					"ستاندرد":158000,
					"ليميتد دبل":294000,
					"بلاتينيوم":293000,
				},
				"إيدج":{
					"SEL":166000,
					"SE":120000,
					"تيتانيوم":180000,
					"ليميتد":120000,
					"ستاندرد":133000,
				},
				"توروس":{
					"SE":112000,
					"SEL":130000,
					"ليميتد":158000,
					"ستاندرد":125000,
					"فل كامل":150000,
					"ايكوبوست":100000,
				},
				"فليكس":{
					"SEL":120000,
					"ستاندرد":144000,
					"ليميتد":111000,
				},
				"كراون فكتوريا":{
					"فل كامل":77000,
					"نص فل":70000,
					"بوليسي":92000,
				}
			},
		}

		car = brands[document.getElementById("brand").value][document.getElementById("vehicleType").value][document.getElementById("model").value]

		model_year={
			2024:1,
			2023:.95,
			2022:.9,
			2021:.85,
			2020:.8,
			2019:.75,
			2018:.7,
			2017:.65,
			2016:.6,
			2015:.55,
			2014:.5,
			2013:.45,
			2012:.4,
			2011:.35,
			2010:.3,
			2009:.25,
			2008:.2,
			2007:.15,
			2006:.14,
			2005:.13,
			2004:.12,
			2003:.11,
			2002:.1,
			2001:.09,
			2000:.08,
		}

		car = car*model_year[Number(document.getElementById("modelYear").value)]

		maintenance = {
			"داخل الوكالة":1,
			"خارج الوكالة":.95
		}
		car = car*maintenance[document.getElementById("maintenance").value]

		carStatus = {
			"جديدة":1,
			"صدمات خفيفة":.95,
			"صدمات قوية":.5,
		}
		car = car*carStatus[document.getElementById("status").value]

		walkway = {
			10000:.95,
			50000:.9,
			100000:.85,
			150000:.7,
			200000:.5,
			300000:.4,
			400000:.3,
		}
		car = car*walkway[Number(document.getElementById("walkway").value)]

		vehicle_interior = {
			"جديدة":1,
			"شبه جديدة":.95,
			"متوسطة":.9,
			"قديمة":.7,
		}
		car = car*vehicle_interior[document.getElementById("interior").value]
	}else{
		car = 0.00;
	}
	document.getElementById("price").innerHTML = car.toFixed(2);
});


$(document).on("click","[data-for]", function(){
	document.getElementById(this.dataset.for).click();
});

c = 0;
$(document).on("change", "#pickImage", function(evt){
	c+=1;
	this.id = `imagePicker${c}`;
	this.name = `imagePicker${c}`;


	imageBox = document.createElement("div");
	imageBox.className = "image-box";
	imageBox.id = `imageBox${c}`;
	img = document.createElement("img");
	var tgt = evt.target || window.event.srcElement,
		files = tgt.files;
	
	// FileReader support 
	if (FileReader && files && files.length) {
		var fr = new FileReader();
		fr.onload = function () {
			img.src = fr.result;
		}
		fr.readAsDataURL(files[0]);
	}
	else {
	}
	closeButton = document.createElement("button");
	closeButton.type = "button";
	closeButton.dataset.close = `imageBox${c}`;
	closeButton.style.marginTop = "-145px";
	closeButton.className = "ibtn";
	closeButton.style.marginLeft = "-115px";
	closeButton.style.position = "absolute";
	icon = document.createElement("span");
	icon.className = "material-icons";
	icon.innerHTML = "close";
	$(closeButton).append(icon);
	$(imageBox).append(img);
	$(imageBox).append(closeButton);

	imagePicker = document.createElement("input");
	imagePicker.type = "file";
	imagePicker.accept = "image/*";
	imagePicker.setAttribute("hidden","");
	imagePicker.id = "pickImage";
	$(`form`).append(imagePicker);

	$(`#images`).append(imageBox);
	document.getElementById(`imageBox${c}`).appendChild(this);
});


$(document).on("click", "[data-close]", function(){
	$(`#${this.dataset.close}`).remove();
});
$(document).on("click", "[data-dclose]", function(){
	$(`#imageBoxO${this.dataset.dclose}`).remove();
	$('#deletedImages').val(`${$('#deletedImages').val()} ${this.dataset.dclose}`);
});

if(document.querySelector("[data-default]") != null){
	document.querySelectorAll(".abtn").forEach(btn => {
		btn.style.display = "none";
	});
}

x = 0;
$(document).on("click",".lb",function(){
	a = document.querySelectorAll("[data-sub]").length*100;
	if(x <= a-(a*1.5)){
	}else{
		x -= 100;
		document.getElementById("defaultImage").style.marginLeft = `${x}%`;
	}
});

$(document).on("click",".rb",function(){
	if(x != 0){
		x += 100;
		document.getElementById("defaultImage").style.marginLeft = `${x}%`;
	}
});

$(document).on("click","[data-favorite]",function(){
	if(this.style.color == "" || this.style.color == "black"){
		this.style.color="red";
	}else{
		this.style.color="black";
	}
	$.ajax({
        type:"GET",
        data:{favorite:this.dataset.favorite},
        url:location.href,
    });
});


function createRate(){
	text = $("#content").val();
	$("#content").val("");
	sender = $("#sender").val();
	senderName = $("#senderName").val();
	$("#ratings").prepend(`
	<a href="/profile?user_id=${sender}">
		<div class="list-item-header">${senderName}</div>
		<div class="list-item-sub-header">${text}</div>
	</a>
	<br>
	`);
}

$(document).on("click",".search-btn",function(){
	nav = document.querySelector("nav");
	if(nav.style.height == "" || nav.style.height == "200px"){
		document.querySelector("nav").style.height = "260px";
	}else{
		document.querySelector("nav").style.height = "200px";
	}
});

$(document).on("change",".search-input",function(){
	location.href = `/search/${this.value}`;
});
