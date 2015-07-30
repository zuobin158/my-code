/**
 * Created by dupeng on 15-6-9.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'bootstrap',
	'text!src/tpl/community/reports.tpl',
	'text!src/tpl/community/reports-list.tpl',
	'text!src/tpl/community/pagination.tpl',
	'src/util',
	'datepicker_locale'
], function ($, Backbone, _, bootstrap, tpl, listTpl, pageTpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: "#main",
		template: _.template(tpl),
		listTemplate: _.template(listTpl),
		pageTemplate: _.template(pageTpl),
		events: {
			'click .q-btn': 'startQuery',
			'click .popup-link': 'popupPost',
			'click .action-link': 'handleReport',
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
			var formValues = $(".reports-view .q-form").serialize() + "&psize=" + view.pageInfo.recordsPerPage + "&page=" + view.pageInfo.page;
            formValues = decodeURIComponent(formValues);
			var param = qStrToJson(formValues);
			$.ajax({
				loader: true,
				url: 'report/list',
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
			var postId = this.$el.find("input[name='post_id']").val();
			var commentId = this.$el.find("input[name='comment_id']").val();
			var keyWords = this.$el.find("input[name='keywords']").val();
			if(postId != "" && !isInteger(postId)){
				$(".hint-block").text("请输入正确的帖子ID！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(commentId != "" && !isInteger(commentId)){
				$(".hint-block").text("请输入正确的帖子ID！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			if(keyWords != "" && !checkStr(keyWords)){
				$(".hint-block").text("关键字只能输入空格或字符！");
				setTimeout(function(){
					$(".hint-block").text("");
				}, 2000);
				return false;
			}
			this.refreshList();
		},
		popupPost: function(e){
			var view = this;
			var target = $(e.currentTarget);
			var postId = target.attr("data-post-id");
			$.ajax({
				loader: true,
				//url: '../static/js/src/data/post-detail.json',
				url: 'report/post_detail',
				data: {
					post_id: postId
				},
				dataType: "json",
				success: function (data, status) {
					if (!data.statusCode) {
						$("#post-modal .modal-title").html(data.postTitle);
						$("#post-modal .modal-body").html(data.postBody);
						$("#post-modal").modal("show");
					}else{
						$(".hint-block").text("获取数据失败，请稍后重试！");
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
		handleReport: function(e){
			var target = $(e.currentTarget);
			var reportId = target.attr("data-report-id");
			var actionType = target.attr("data-action-type");
			var statusNode = $("tr[data-report-id="+ reportId +"] .action-status");
			var actionNode = $("tr[data-report-id="+ reportId +"] .action-node");
			$.ajax({
				loader: true,
                //url: '../static/js/src/data/reports-list.json',
				url: 'report/update_status',
				data: {
					reportId: reportId,
					action: actionType
				},
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						var afterStatus = (actionType == "hide") ? "已隐藏" : "已忽略";
						statusNode.text(afterStatus);
						actionNode.html("");
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
			var view = this;
			setTimeout(function(){
				//initiate date picker and make date constrain
				var startPicker = view.$el.find('.start-date').datepicker({
					language:  'zh-CN',
					format: 'yyyy-mm-dd',
					autoclose: 1,
					todayHighlight: 1
				}).on('changeDate',function(e){
						endPicker.datepicker('setStartDate', e.date);
					});
				var endPicker = view.$el.find('.end-date').datepicker({
					language:  'zh-CN',
					format: 'yyyy-mm-dd',
					autoclose: 1,
					todayHighlight: 1
				}).on('changeDate',function(e){
						startPicker.datepicker('setEndDate', e.date);
					});
				//startPicker.datepicker("setDate", new Date());
				//endPicker.datepicker("setDate", new Date());
			}, 500);
            this.startQuery();
		},
		render: function() {
			this.$el.html(this.template);
		},
		renderResults: function(data) {
			this.$el.find(".reports-view .list-content").html(this.listTemplate(data));
			this.$el.find(".reports-view .page-content").html(this.pageTemplate(data));
		}
	});
	return view;
});
