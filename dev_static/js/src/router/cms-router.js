/**
 * Created by dupeng on 15-5-28.
 */
define([
	'jquery',
	'backbone'
], function ($, Backbone) {
	'use strict';

	var Workspace = Backbone.Router.extend({
		routes: {
			'': 'initPanel',
			'home': 'initPanel',
            'homepage/banner': 'homepageBanner',
			'community': 'communityPosts',
			'community/posts': 'communityPosts',
			'community/comments': 'communityComments',
			'community/user': 'communityUser',
			'community/reports': 'communityReport',
			'community/tags': 'communityTags',
			'letter/letters': 'letterQuery',
			'letter/create': 'letterCreate',
            'admin': 'adminPanel',
            'admin/newuser': 'newUser',
            'admin/edituser/:id': 'editUser'
		},
		initialize: function(opt){
			var router = this;
			require(['src/views/nav'],function(nav){
				new nav();
			});
		},
		execute: function(callback, args, name) {
			//unbind all events on main node for next view to be rendered
			$("#main").off();
            //destroy editor
            if(window.um && $("#"+window.um.id).length){window.um.destroy();}
			//apply original callback
			if (callback) callback.apply(this, args);
		},

		initPanel: function() {
			require(['src/views/system/home'], function(view){
				new view();
			});
		},
		communityPosts: function(){
			require(['src/views/community/posts'], function(view){
				new view();
			});
		},
		communityComments: function(){
			require(['src/views/community/comments'], function(view){
				new view();
			});
		},
		communityTags: function(){
			require(['src/views/community/tags'], function(view){
				new view();
			});
		},
		communityUser: function(){
			require(['src/views/community/user'], function(view){
				new view();
			});
		},
		communityReport: function(){
			require(['src/views/community/reports'], function(view){
				new view();
			});
		},
		letterQuery: function(){
			require(['src/views/letter/letters'], function(view){
				new view();
			});
		},
		letterCreate: function(){
			require(['src/views/letter/create'], function(view){
				new view();
			});
		},
        homepageBanner: function(){
            require(['src/views/homepage/banner'], function(view){
                new view();
            });
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
