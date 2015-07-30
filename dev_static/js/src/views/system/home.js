/**
 * Created by dupeng on 15-5-28.
 */
define([
	'jquery',
	'underscore',
	'backbone',
	'text!src/tpl/system/home.tpl'
], function ($, _, Backbone, tpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: '#main',
		template: _.template(tpl),
		initialize: function (opt) {
			var view = this;
			$.ajax({
				//url: '../static/js/src/data/home.json',
				url: 'permissions/get_user_info',
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
			//reset navbar status
			$(".cms-nav li>a").removeClass("active");
			this.$el.html(this.template(data));
		}
	});
	return view;
});
