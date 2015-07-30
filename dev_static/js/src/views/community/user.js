/**
 * Created by dupeng on 15-6-9.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'bootstrap',
	'text!src/tpl/community/user.tpl',
	'text!src/tpl/community/user-list.tpl',
	'text!src/tpl/community/pagination.tpl',
	'src/util'
], function ($, Backbone, _, bootstrap, tpl, listTpl, pageTpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: "#main",
		template: _.template(tpl),
		listTemplate: _.template(listTpl),
		pageTemplate: _.template(pageTpl),
		events: {
			'click .q-btn': 'startQuery',
			'click .prohib-link': 'prohibitUser',
			'click .delete-avatar-link': 'deleteAvatar',
			//pagination events
			'change .records-select': 'changePage',
			'click .pagination .first-page': 'firstPage',
			'click .pagination .prev-page': 'prevPage',
			'click .pagination .next-page': 'nextPage',
			'click .pagination .last-page': 'lastPage'
		},
		pageInfo: {
			page: 1,
			totalPage: 0,
			recordsPerPage: 10,
			totalRecord: 0
		},
		refreshList: function() {
			var view = this;
			var formValues = $(".user-view .q-form").serialize() + "&psize=" + view.pageInfo.recordsPerPage + "&page=" + view.pageInfo.page;
            formValues = decodeURIComponent(formValues);
			var param = qStrToJson(formValues);
			$.ajax({
				loader: true,
                //url: '../static/js/src/data/user-list.json',
                url: 'userprofile/list',
				data: param,
				dataType: "json",
				success: function (data, status) {
					if (!data.statusCode) {
						view.pageInfo.totalPage = data.pages.totalPage;
						view.pageInfo.totalRecord = data.pages.totalRecord;
						view.renderResults(data);
					}
				},
				error: function (xhr, errorType, error) {
					console.log(error);
				}
			});
		},
		startQuery: function(){
            /**
			var nickname = this.$el.find("input[name='nickname']").val();
			if(nickname == ""){
				$(".hint-block").text("用户昵称不能为空！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}**/
			var view = this;
			view.pageInfo.page = 1,
			this.refreshList();
		},
		prohibitUser: function(e){
			var target = $(e.currentTarget);
			var prohibitStatus = (target.text() == "取消禁言");
			var userId = target.attr("data-user-id");
			var statusNode = $("tr[data-user-id="+ userId +"] .prohib-status");
			$.ajax({
                type: "post",
				loader: true,
				url: 'userprofile/forbid_user',
				data: {
					user_id: userId,
					user_status: prohibitStatus == true? "N" : "Y"
				},
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						target.text(prohibitStatus == true ? "禁言" : "取消禁言");
						statusNode.text(prohibitStatus == true ? "否" : "是");
					}else{
						$(".hint-block").text("操作失败，请稍后重试！");
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
		deleteAvatar: function(e){
			var target = $(e.currentTarget);
			var userId = target.attr("data-user-id");
			$.ajax({
				loader: true,
				url: '../static/js/src/data/user-list.json',
				data: {
					userId: userId
				},
				dataType: "json",
				success: function (data, status) {
					if (!data.statusCode) {
						target.text("");
					}else{
						$(".hint-block").text("操作失败，请稍后重试！");
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
		changePage: function(e){
			this.pageInfo.recordsPerPage = e.currentTarget.value;
            this.startQuery();
		},
		firstPage: function(){
			var view = this;
			view.pageInfo.page = 1;
			view.refreshList();
		},
		prevPage: function(){
			var view = this;
			if(view.pageInfo.page != 1){
				view.pageInfo.page --;
				view.refreshList();
			}
		},
		nextPage: function(){
			var view = this;
			if(view.pageInfo.page < view.pageInfo.totalPage){
				view.pageInfo.page ++;
				view.refreshList();
			}
		},
		lastPage: function(){
			var view = this;
			view.pageInfo.page = view.pageInfo.totalPage;
			view.refreshList();
		},
		initialize: function (opt) {
			this.render();
            this.startQuery();
		},
		render: function() {
			this.$el.html(this.template);
		},
		renderResults: function(data) {
			this.$el.find(".user-view .list-content").html(this.listTemplate(data));
			this.$el.find(".user-view .page-content").html(this.pageTemplate(data));
		}
	});
	return view;
});
