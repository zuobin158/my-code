/**
 * Created by dupeng on 15-5-28.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'text!src/tpl/leftnav.tpl',
	'text!src/tpl/topnav.tpl'
], function ($, Backbone, _, navTpl, topnavTpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: '#leftnav',
		template: _.template(navTpl),
		topNavTemplate: _.template(topnavTpl),
        events: {
            'click .cms-nav .toggle-nav': 'toggleNav',
            'click .cms-nav a': 'activeLink'
        },
        toggleNav: function(e) {
            var target = $(e.currentTarget);
            var icon = target.find(".toggle-icon");
            var collapse = target.siblings(".secondmenu");
            icon.toggleClass("glyphicon-triangle-right glyphicon-triangle-bottom");
            collapse.toggleClass("in");
            return false;
        },
		activeLink: function(e){
			var target = $(e.currentTarget);
			$(".cms-nav li>a").removeClass("active");
			target.addClass("active");
		},
		initialize: function (opt) {
			var view = this;
			$.ajax({
				type: 'post',
				url: '/api/get_system_menu',
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
		render: function(data) {
			this.$el.html(this.template(data));
			$('header .container').append(this.topNavTemplate(data));
		}
	});
	return view;
});
