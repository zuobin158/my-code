/**
 * Created by dupeng on 15-6-3.
 */
//transform query string to json object
function qStrToJson(queryStr){
	if(typeof(queryStr) == "string"){
		u = queryStr.split("&");
		var get = {};
		for(var i in u){
			var j = u[i].split("=");
			if(j[0] in get){
				get[j[0]] = [].concat(get[j[0]], [j[1]]);
			}else{
				get[j[0]] = j[1];
			}
		}
		return get;
	} else {
		return {};
	}
}
//integer validation
function isInteger(num){
	var reg =/^\+?[1-9][0-9]*$/;
	return reg.test(num);
}
//id validation
function isValidId(num){
	var reg =/^\+?[1-9][0-9;]*$/;
	return reg.test(num);
}
//mobile validation
function isMobile(num){
	var reg =/^1[3|4|5|8][0-9]\d{8}$/;
	return reg.test(num);
}
//email validation
function isEmail(str){
	var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
	return reg.test(str);
}
//string validation
function checkStr(str){
	var reg = /^[^@\/\'\\\"#$%&\^\*]+$/;
	return reg.test(str);
}
//alert modal function
function alertModal(msg){
    var modal = $(".alert-modal");
    modal.find(".modal-body").text(msg);
    modal.modal();
}
