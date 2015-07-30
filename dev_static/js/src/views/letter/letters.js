/**
 * Created by dupeng on 15-6-10.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'text!src/tpl/letter/letters.tpl',
	'text!src/tpl/letter/letters-list.tpl',
	'text!src/tpl/letter/pagination.tpl',
	'src/util',
	'datepicker_locale'
], function ($, Backbone, _, tpl, listTpl, pageTpl, datepicker) {
	'use strict';

	var view = Backbone.View.extend({
		el: "#main",
		template: _.template(tpl),
		listTemplate: _.template(listTpl),
		pageTemplate: _.template(pageTpl),
		events: {
			'click .q-btn': 'startQuery',
			'click .c-btn': 'createLetter',
			'click .detail-link': 'checkDetail',
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
			var formValues = $(".letters-view .q-form").serialize() + "&psize=" + view.pageInfo.recordsPerPage + "&page=" + view.pageInfo.page;
            formValues = decodeURIComponent(formValues);
			var param = qStrToJson(formValues);
			$.ajax({
				loader: true,
				//url: '../static/js/src/data/letters-list.json',
				url: 'notification/list',
				data: param,
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
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
			var recipient = this.$el.find("input[name='user_id']").val();
			var keyWords = this.$el.find("input[name='keywords']").val();
			if(recipient != "" && !isInteger(recipient)){
				$(".hint-block").text("请输入正确的收信人ID！");
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
		createLetter: function(){
			location.href = "#letter/create";
		},
		checkDetail: function(e){
			$("#letter-detail").show();
			var view = this;
			var target = $(e.currentTarget);
			var letterId = target.attr("data-letter-id");
			require(['src/views/letter/detail'], function(view){
				new view({letterId:letterId});
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
			this.$el.find(".letters-view .list-content").html(this.listTemplate(data));
			this.$el.find(".letters-view .page-content").html(this.pageTemplate(data));
		}
	});
	return view;
});
