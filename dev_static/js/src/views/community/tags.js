/**
 * Created by dupeng on 15-6-4.
 */
define([
	'jquery',
	'backbone',
	'underscore',
	'text!src/tpl/community/tags.tpl',
	'text!src/tpl/community/edit-tags.tpl'
], function ($, Backbone, _, tpl, editTpl) {
	'use strict';

	var view = Backbone.View.extend({
		el: "#main",
		template: _.template(tpl),
		editTemplate: _.template(editTpl),
		events: {
			'click .edit-link': 'renderEdit',
			'click .save-btn': 'saveEdit',
			'click .cancel-btn': 'render'
		},
		tagList: [],
		saveEdit: function(){
            if(!this.validateTags()){
                $(".hint-block").text("标签不可重复，请重新编辑！");
                setTimeout(function(){
                    $(".hint-block").text("");
                }, 2000);
                return;
            }
			var view = this;
			var tagArr = [];
			$(".tags-view").find(".tag-input").each(function(idx){
				var tagNode = $(this);
				var tagId = tagNode.attr("data-tag-id");
				var label = tagNode.val();
				tagArr.push({
					tagId: tagId,
					label: label
				});
			});
			$.ajax({
				loader: true,
				type: "post",
                //url: '../static/js/src/data/posts-list.json',
                url: 'post/save_tags',
				data: {
					tags: JSON.stringify(tagArr)
				},
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						//view.tagList = tagArr;
                        //view.render();
                        view.initialize();
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
        validateTags: function() {
            var flag = true;
            var arr = $(".tags-view").find(".tag-input");
            arr.each(function(idx1){
                var label = $(this).val();
                if(label != ""){
                    arr.each(function(idx2){
                        if(idx1 != idx2){
                            var label2 = $(this).val();
                            if(label == label2){
                                flag = false;
                            }
                        }
                    });
                }
            });
            return flag;
        },
		initialize: function (opt) {
			var view = this;
			$.ajax({
				url: 'post/edit_tag',
				dataType: "json",
				success: function (data, status) {
					if (data.statusCode) {
						view.tagList = data.list;
						view.render();
					}
				},
				error: function (xhr, errorType, error) {
					console.log(error);
				}
			});
		},
		render: function() {
			var data = this.tagList;
			this.$el.html(this.template({list: data}));
		},
		renderEdit: function() {
			var data = this.tagList;
			this.$el.html(this.editTemplate({list: data}));
		}
	});
	return view;
});
