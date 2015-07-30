/**
 * Created by dupeng on 15-6-17.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'text!src/tpl/system/edit-user.tpl',
	'src/util'
], function ($, Backbone, _, tpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: "#main",
		template: _.template(tpl),
		events: {
			'click .next-btn': 'validateUser',
			'click .previous-btn': 'firstStep',
			'click .cancel-btn': 'cancelEdit',
			'click .confirm-btn': 'saveUser'
		},
		validateUser: function(){
			var username = this.$el.find("input[name='name']").val();
			var name = this.$el.find("input[name='real_name']").val();
			var email = this.$el.find("input[name='email']").val();
			var mobile = this.$el.find("input[name='phone']").val();
			var status = this.$el.find("input[name='is_active']:checked").val();
			if(username == ""){
				$(".hint-block").text("请输入用户名！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(name == ""){
				$(".hint-block").text("请输入姓名！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(email == ""){
				$(".hint-block").text("请输入邮箱地址！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(email == "" || !isEmail(email)){
				$(".hint-block").text("请输入正确的邮箱格式！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(mobile != "" && !isMobile(mobile)){
				$(".hint-block").text("请输入正确的手机号码！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(status == undefined){
				$(".hint-block").text("用户状态不能为空！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			this.secondStep();
            /**
			var view = this;
			$.ajax({
				loader: true,
				type: "post",
				url: '../static/js/src/data/edit-user.json',
				data: {
					email: email
				},
				dataType: "json",
				success: function (data, status) {
					if (!data.statusCode) {
						view.secondStep();
					}else{
						$(".hint-block").text("您输入的邮箱不存在，请输入正确的邮箱。");
						setTimeout(function(){
							$(".hint-block").text("");
						}, 2000);
					}
				},
				error: function (xhr, errorType, error) {
					console.log(error);
				}
			});
            **/
		},
		secondStep: function(){
			this.$el.find(".step-1").hide();
			this.$el.find(".step-2").show();
		},
		firstStep: function(){
			this.$el.find(".step-2").hide();
			this.$el.find(".step-1").show();
		},
		cancelEdit: function(){
			location.href = "#admin";
		},
		saveUser: function(){
			var view = this;
			var formValues = $(".edit-user .edit-form").serialize();
            formValues = decodeURIComponent(formValues);
			var param = qStrToJson(formValues);
            param.groups_ids = [].concat([], param.groups_ids);
			$.ajax({
				loader: true,
				type: "post",
				//url: '../static/js/src/data/edit-user.json',
				url: 'per_user/save',
				data: param,
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						location.href = "#admin";
					}else{
						$(".hint-block").text("保存失败，请稍后重试！");
						setTimeout(function(){
							$(".hint-block").text("");
						}, 2000);
					}
				},
				error: function (xhr, errorType, error) {
					console.log(error);
				}
			});
		},
		initialize: function (opt) {
			var view = this;
			$.ajax({
				//url: '../static/js/src/data/edit-user.json',
				url: 'per_user/edit',
				dataType: "json",
                data: {
                    'userId': opt.userId
                },
				success: function (data, status) {
					if (data.statusCode) {
						var obj = {
							editFlag: true,
							user: data.user
						};
						view.render(obj);
					}
				},
				error: function (xhr, errorType, error) {
					console.log(error);
				}
			});
		},
		render: function(data) {
			this.$el.html(this.template(data));
		}
	});
	return view;
});
