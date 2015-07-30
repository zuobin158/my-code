/**
 * Created by dupeng on 15-6-12.
 */
define([
	'jquery',
	'underscore',
	'backbone',
	'text!src/tpl/letter/create.tpl',
	'src/util',
	'umeditor',
	'umeditor_locale',
	'fileupload'
], function ($, _, Backbone, tpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: '#main',
		template: _.template(tpl),
		events: {
			'input .need-count': 'countChars',
			'click .send-btn': 'validateLetter',
			'click .cancel-btn': 'cancelSend'
		},
		countChars: function(e){
			var view = this;
			var target = $(e.currentTarget);
			if(maxLen && maxLen > 0){
				var maxLen = $(target).attr("maxlength");
				var curLen = $(target).val().length;
				var remainLen = maxLen - curLen;
				var curNode = target.parent().parent().find(".current-chars");
				var remainNode = target.parent().parent().find(".remain-chars");
				curNode.text(curLen);
				remainNode.text(remainLen);
			}else if(target.hasClass("edui-body-container")){
				var maxLen = view.um.options.maximumWords;
				var curLen = view.um.getContentLength(true);
				var remainLen = maxLen - curLen;
				var curNode = $(".editor-desc").find(".current-chars");
				var remainNode = $(".editor-desc").find(".remain-chars");
				curNode.text(curLen);
				remainNode.text(remainLen);
				/*if(remainLen <= 0){
					var content = view.getContentTxt();
					content = content.substring(0, maxLen);
					return false;
				}else{
					var curNode = $(".editor-desc").find(".current-chars");
					var remainNode = $(".editor-desc").find(".remain-chars");
					curNode.text(curLen);
					remainNode.text(remainLen);
				}*/
			}
		},
		initEditor: function(){
			window.um = this.um = UM.getEditor("letterEditor", {
				UMEDITOR_HOME_URL: "/static/js/plugins/umeditor/",
				toolbar: ['forecolor | bold italic underline | justifyleft justifycenter justifyright |'],
				maximumWords: 1000,
				wordCount:true
			});
		},
		initUpload: function(){
			var view = this;
			$('#fileupload').fileupload({
				//url: "../static/js/src/data/letter-detail.json",
				url: "notification/load_send_users",
				dataType: 'json',
				add: function(e, data){
					var goUpload = true;
					var uploadFile = data.files[0];
					//file type validation
					if (!(/(\.|\/)(xlsx?)$/i).test(uploadFile.name)) {
						$(".hint-block").text("仅支持excel格式文件，请重新选择");
						setTimeout(function(){
							$(".hint-block").text("");
						}, 2000);
						goUpload = false;
					}
					if(goUpload == true){
						data.submit();
					}
				},
				done: function (e, data) {
					var list = data.result.user_ids;
					view.$el.find("input[name='user_ids']").val(list.join(";"));
					/*$.each(data.result.files, function (index, file) {
						$('<p/>').text(file.name).appendTo('#files');
					});*/
				}
			}).prop('disabled', !$.support.fileInput);
		},
		validateLetter: function(){
			var recipient = this.$el.find("input[name='user_ids']").val();
			var title = this.$el.find("input[name='title']").val();
			var content = this.$el.find("textarea[name='content']").val();
			if(recipient == ""){
				$(".hint-block").text("收信人ID不能为空，请输入收信人ID。");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
            /**else if(!isValidId(recipient)){
				$(".hint-block").text("收信人ID格式不正确，请输入正确的收信人ID。");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}**/
			if(title.trim() == ""){
				$(".hint-block").text("标题不能为空，请输入标题。");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(content.trim() == ""){
				$(".hint-block").text("正文不能为空，请输入正文。");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			this.sendLetter();
		},
		sendLetter: function(){
            var outlink = this.$el.find(".q-form [name='outlink']").val().trim();
            var flag = outlink.substring(0, 4) == "http";
            var param = {
                user_ids: this.$el.find(".q-form [name='user_ids']").val(),
                title: this.$el.find(".q-form [name='title']").val(),
                content: this.$el.find(".q-form [name='content']").val(),
                link_remark: this.$el.find(".q-form [name='link_remark']").val(),
                outlink: flag ? outlink : "http://" + outlink
            };
			$.ajax({
				loader: true,
				type: "post",
				url: 'notification/save_notify',
				data: param,
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						location.href = "#letter/letters";
					}else{
                        $(".hint-block").text(data.msg);
                        setTimeout(function(){
                            $(".hint-block").text("");
                        }, 5000);
                    }
				},
				error: function (xhr, errorType, error) {
					console.log(error);
				}
			});
		},
		cancelSend: function(){
			location.href = "#letter/letters";
		},
		initialize: function (opt) {
			this.render();
			var view = this;
			setTimeout(function(){
				view.initEditor();
				view.initUpload();
			}, 100);
		},
		render: function(data) {
			this.$el.html(this.template);
		}
	});
	return view;
});
