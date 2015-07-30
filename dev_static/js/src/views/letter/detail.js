/**
 * Created by dupeng on 15-6-11.
 */
define([
	'jquery',
	'underscore',
	'backbone',
	'text!src/tpl/letter/detail.tpl'
], function ($, _, Backbone, tpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: '#letter-detail',
		template: _.template(tpl),
		events: {
			'click .expand-icon': 'expandRecipient',
			'click .back-btn': 'closeDetail'
		},
		initialize: function (opt) {
			var view = this;
			$.ajax({
				//url: '../static/js/src/data/letter-detail.json',
				url: 'notification/show_detail',
				data: {nid: opt.letterId},
				dataType: "json",
				success: function(data, status){
					if(data.statusCode){
						view.render(data);
					}
				},
				error: function(xhr, errorType, error){
					console.log(error);
				}
			});
		},
		expandRecipient: function(e){
			$(e.currentTarget).toggleClass("glyphicon-triangle-top glyphicon-triangle-bottom");
			this.$el.find(".recipient-list").toggleClass("expanded");
		},
		closeDetail: function(){
			this.$el.off().hide().html("");
		},
		render: function(data) {
			this.$el.html(this.template(data));
		}
	});
	return view;
});
