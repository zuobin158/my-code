/**
 * Created by dupeng on 15-5-25.
 */
var require = {
	baseUrl: 'static/js',
	paths: {
		//模块路径定义
		text: 'libs/text',
		css: 'libs/css',
		jquery: 'libs/jquery',
		backbone:"libs/backbone",
		underscore:"libs/underscore",
		bootstrap: 'plugins/bootstrap',
		cookie: 'plugins/jquery.cookie',
		datepicker: 'plugins/bootstrap-datepicker',
		datepicker_locale: 'plugins/bootstrap-datepicker.zh-CN',
		umeditor: 'plugins/umeditor/umeditor.min',
		umeditor_config: 'plugins/umeditor/umeditor.config',
		umeditor_locale: 'plugins/umeditor/umeditor.zh-cn',
		fileupload: 'plugins/jquery.fileupload',
		'jquery.ui.widget': 'plugins/jquery.ui.widget',
		iframe_transport: 'plugins/jquery.iframe-transport',
        'carousel': 'plugins/carousel'
	},
	shim: {
		backbone: {
			deps: ['jquery', 'underscore'],
			exports: 'Backbone'
		},
		bootstrap: {
			deps: ['jquery']
		},
		datepicker_locale: {
			deps: ['datepicker']
		},
		umeditor_locale: {
			deps: ['umeditor']
		},
		fileupload: {
			deps: ['iframe_transport']
		}
	}
};
