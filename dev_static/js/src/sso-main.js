/**
 * Created by dupeng on 15-6-15.
 */
require([
	'jquery',
	'backbone',
	'src/router/sso-router'
], function($, Backbone, router){
	//register global ajax events handler
	$(document).ajaxSend(function(event, xhr, settings){
		if (settings.loader){
			$(".loading").show();
		}
	});
	$(document).ajaxComplete(function(event, xhr, settings){
		if (settings.loader){
			$(".loading").fadeOut("fast");
		}
	});
	$(document).ajaxError(function(event, xhr, settings){
		if (settings.loader){
			$(".loading").fadeOut("fast");
		}
	});
	//initiate router
	new router();
	Backbone.history.start();
});