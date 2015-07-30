/**
 * Created by dupeng on 15-6-15.
 */
define([
	'jquery',
	'backbone'
], function ($, Backbone) {
	'use strict';

	var Workspace = Backbone.Router.extend({
		routes: {
			'': 'adminPanel',
			'admin': 'adminPanel',
			'admin/newuser': 'newUser',
			'admin/edituser/:id': 'editUser'
		},
		initialize: function(opt){
			var router = this;
			require(['src/views/system/nav'],function(nav){
				new nav();
			});
		},
		execute: function(callback, args, name) {
			//unbind all events on main node for next view to be rendered
			$("#main").off();
			//apply original callback
			if (callback) callback.apply(this, args);
		},

		adminPanel: function() {
			require(['src/views/system/admin'], function(view){
				new view();
			});
		},
		newUser: function(){
			require(['src/views/system/newuser'], function(view){
				new view();
			});
		},
		editUser: function(userId){
			require(['src/views/system/edituser'], function(view){
				new view({userId: userId});
			});
		}
	});
	return Workspace;
});