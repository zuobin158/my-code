/**
 * Created by dupeng on 15-5-25.
 */
require(['jquery', 'cookie'], function($){
	$(function(){
		//reset form validation
		$("#reset-form").on("submit", function(e){
			var str_pwd1 = $("#pwd1").val();
			var str_pwd2 = $("#pwd2").val();
			if(str_pwd1 == ""){
				$(".hint-block").text("请输入密码！");
				return false;
			}else if(str_pwd1 != str_pwd2){
				$(".hint-block").text("两次密码输入不一致，请重新输入！");
				return false;
			}
			$.ajax({
				type: 'post',
				url: '/reset_pwd',
				data: {reset_pwd: str_pwd2},
				dataType: "json",
				success: function(data, status){
					if(data.statusCode){
						location.href = "/logout";
					}else{
                        $(".hint-block").text("密码修改失败，内部异常，请稍后重试");
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
