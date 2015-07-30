/**
 * Created by dupeng on 15-5-28.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'bootstrap',
	'text!src/tpl/community/posts.tpl',
	'text!src/tpl/community/posts-list.tpl',
	'text!src/tpl/community/pagination.tpl',
	'src/util',
	'datepicker_locale'
], function ($, Backbone, _, bootstrap, tpl, listTpl, pageTpl, datepicker) {
	'use strict';

	var view = Backbone.View.extend({
		el: "#main",
		template: _.template(tpl),
		listTemplate: _.template(listTpl),
		pageTemplate: _.template(pageTpl),
		events: {
			'click .q-btn': 'startQuery',
			'click .popup-link': 'popupPost',
			'click .hide-link': 'toggleHide',
			'click .tag-submit': 'saveTags',
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
			var formValues = $(".posts-view .q-form").serialize() + "&psize=" + view.pageInfo.recordsPerPage + "&page=" + view.pageInfo.page;
            formValues = decodeURIComponent(formValues);
			var param = qStrToJson(formValues);
			$.ajax({
				loader: true,
				//url: '../static/js/src/data/posts-list.json',
				url: 'post/list',
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
			var keyWords = this.$el.find("input[name='keywords']").val();
			if(postId != "" && !isInteger(postId)){
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
		toggleHide: function(e){
			var target = $(e.currentTarget);
			var postId = target.attr("data-post-id");
			var hideStatus = target.attr("data-hide-status");
			var statusNode = $("tr[data-post-id="+ postId +"] .hide-status");
			$.ajax({
				loader: true,
				url: 'post/update_status',
				data: {
					post_id: postId,
					hideAction: hideStatus=="true" ? "false" : "true"
				},
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						target.attr("data-hide-status", hideStatus=="true" ? "false" : "true");
						target.text(hideStatus=="true" ? "隐藏" : "取消隐藏");
						statusNode.text(hideStatus=="true" ? "否" : "是");
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
		saveTags: function(e){
			var target = $(e.currentTarget);
			var postId = target.attr("data-post-id");
			var tagArr = "";
			$("tr[data-post-id="+ postId +"]>.tags .tag-checkbox").each(function(idx){
				var tagNode = $(this);
				var tagId = tagNode.attr("data-tag-id");
				var isChecked = tagNode.prop("checked");
                if (isChecked){
                    tagArr = tagArr + tagId + ","
                }
			});
			$.ajax({
				loader: true,
				url: 'post/update_tag',
				data: {
					post_id: postId,
					tags: tagArr
				},
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						//save tag successfully
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
			this.$el.find(".posts-view .list-content").html(this.listTemplate(data));
			this.$el.find(".posts-view .page-content").html(this.pageTemplate(data));
		}
	});
	return view;
});
