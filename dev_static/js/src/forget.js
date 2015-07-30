/**
 * Created by dupeng on 15-5-25.
 */
require(['jquery', 'cookie'], function($){
	$(function(){
		//email check
		function isEmail(str){
			var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
			return reg.test(str);
		}
		//verify email address
		$("#send-verify").on("click", function(){
			var str_email = $("#email").val();
			if(str_email == ""){
				$(".hint-block").text("请输入邮箱地址！");
			}else if(!isEmail(str_email)){
				$(".hint-block").text("请输入正确的邮箱地址！");
			}else{
				$.ajax({
					type: 'post',
					url: '',
					data: {user_email: str_email},
					dataType: "json",
					success: function(data, status){
						if(data.statusCode){
							$(".hint-block").text("已发送验证邮件至邮箱，请查收");
						}
						var sendInterval = 30;
						$("#send-verify").text(sendInterval + "秒后再次发送").prop("disabled", true);
						var i = 0;
						var sendTimer = setInterval(function(){
							if(i == sendInterval){
								clearInterval(sendTimer);
								$("#send-verify").text("发送验证码").prop("disabled", false);
							}else{
								i++;
								$("#send-verify").text(sendInterval-i + "秒后可再次发送")
							}
						}, 1000);
					},
					error: function(xhr, errorType, error){
						console.log(error);
					}
				});
			}
		});
		//verify form validation
		$("#verify-form").on("submit", function(e){
			var str_email = $("#email").val();
			var str_verification = $("#verification").val();
			if(str_email == ""){
				$(".hint-block").text("请输入邮箱地址！");
				return false;
			}else if(!isEmail(str_email)){
				$(".hint-block").text("请输入正确的邮箱地址！");
				return false;
			}
			if(str_verification == ""){
				$(".hint-block").text("请输入验证码！");
				return false;
			}
			$.ajax({
				type: 'post',
				url: '',
				data: {reset_email: str_email, reset_verification: str_verification},
				dataType: "json",
				success: function(data, status){
					if(data.statusCode){
						$.cookie("reset_email", str_email);
						location.href = "reset.html";
					}else{
						$(".hint-block").text("验证码错误！！");
					}
				},
				error: function(xhr, errorType, error){
					console.log(error);
				}
			});
			return false;
		});
	});
});