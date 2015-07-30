/**
 * Created by dupeng on 15-5-25.
 */
require([
	'jquery',
	'backbone',
	'src/router/cms-router'
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
        if(xhr.responseText == "logout" || xhr.responseText.indexOf('<meta name="ajax_to_login" />')>0){
            location.href = "/logout";
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
