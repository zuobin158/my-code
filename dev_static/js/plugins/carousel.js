define(function(require, exports, module) {
	var $ = require('jquery');
	require('css!../css/carousel');

	(function($) {
		$.fn.carousel = function(option) {
			// 父级加 display: none;
			// ul 加class carousel_wrap
			// li 加 carousel_item

			var opt = $.extend({
				'animate': 'fade', // move，fade
				'nav': true, // true => 如果有data-img为小图，否则圆点。  jq对象为自指定
				'directionBtn': 'responsive', // false=>没有按钮 true=>自动生成按钮 responsive=>自动生成的响应式按钮  []=>自己指定 [$left, $right]
				'event': 'mouseover',
				'speed': 500,
				'autoPlay': true,
				'touch': true, // 暂未支持
				'time': 5000,
				'navAlign': 'center'  // right 有bug
			}, option || {});

			// 回调事件
			// carousel.start 每次动画开始前
			// carousel.end 每次动画结束后
			// 参数 $('#carousel')[0].cParam.$li 当前的运动li
			// 参数 $('#carousel')[0].cParam.$nav 当前的运动navli
			// 参数 $('#carousel')[0].cParam.index 当前运动元素的键值

			return this.each(function() {
				var $container = $(this);
				var $wrap = $container.find('.carousel_wrap');
				var $li = $wrap.find('.carousel_item');
				var $len = $li.length;
				var nowActive = 0;

				// trigger 的参数
				$container[0].cParam = {}

				// 设置背景
				$li.each(function() {
					var $t = $(this);
					var bg = $t.data('bg');
					var bgWidth = $t.data('bgWidth');
					var bgColor = $t.data('bgColor');
					if (bg) {
						if (bg.charAt(0) == '#') {
							// 颜色
							$t.css({
								background: bg
							});
						} else {
							// 图片
							//图片宽度1920 需要居中显示
							if(bgWidth > 1900){
								$t.css({
									background: 'url(' + bg + ') center top no-repeat',
									backgroundColor: bgColor
								});
							}else{//小图片 需要平铺显示
								$t.css({
									background: 'url(' + bg + ')'
								});
							}

						}
					}
				});

				// 页面布局
				if (opt.animate == 'move') {
					$wrap.width($len * 100 + '%').addClass('carousel_move').css({
						'transition-duration': opt.speed + 'ms'
					});
					$li.width(100 / $len + '%');
				} else if (opt.animate == 'fade') {
					$wrap.addClass('carousel_fade');
					$li.css({
						// 'transition-duration': opt.speed + 'ms'
						'transition-duration': '0'
					}).eq(0).css({
						'z-index': 3
					});
					$container.show();
					$wrap.height($li.height());
					$(window).on('resize', function() {
						$wrap.height($li.height());
					});
				}
				$container.show();

				// 生成导航
				var $nav = null;
				if (opt.nav instanceof jQuery) {
					$nav = opt.nav;
				} else if (opt.nav) {
					var navHTML = '';
					var navAlign = '';
					if (opt.navAlign == 'left') {
						navAlign = 'carousel_nav_left';
					} else if (opt.navAlign == 'right') {
						navAlign = 'carousel_nav_right';
					} else if (opt.navAlign == 'center'){
						navAlign = 'carousel_nav_center';
					}
					if ($li.data('img')) {
						navHTML = '<ol class="' + navAlign + ' carousel_nav_img carousel_nav">';
						$li.each(function() {
							navHTML += '<li><img src="' + $(this).data('img') + '"></li>';
						});
					} else {
						navHTML = '<ol class="' + navAlign + ' carousel_nav_circle carousel_nav" id="carousel_nav">';
						$li.each(function() {
							navHTML += '<li></li>';
						});
					}
					navHTML += '</ol>';
					$nav = $(navHTML).appendTo($container);
				}

				// 导航事件
				var $navLi = $nav.find('li');
				// move事件函数
				var activeMove = function(index) {
					/*if ($.support.transition) {
						$wrap.on('bsTransitionEnd', function() {
							$container.trigger('carousel.end');
							$wrap.off('bsTransitionEnd');
						});
						$container.trigger('carousel.start');
						$wrap.css({
							transform: 'translate3d(' + (-index * (100 / $len)) + '%,0,0)'
						});
					} else {*/
						$container.trigger('carousel.start');
						$wrap.css({
							transform: 'translate(' + (-index * (100 / $len)) + '%,0)'
						});
						$container.trigger('carousel.end');
					/*}*/
					$navLi.eq(index).addClass('active').siblings().removeClass('active');
				};
				// fade 事件函数
				var activeFade = function(index) {

					$container[0].cParam.$li.css({
						'z-index': 2
					}).stop().animate({
						opacity: 1
					}, opt.speed).siblings().css({
						'z-index': 1
					}).stop().animate({
						opacity: 0
					}, opt.speed);

					$navLi.eq(index).addClass('active').siblings().removeClass('active');

					// $container.on('carousel.start', function() {
					// 	$container[0].cParam.$li.css({
					// 		'display': 'block'
					// 	});
					// 	setInterval(function() {
					// 		$container[0].cParam.$li.css({
					// 			opacity: 1
					// 		}).siblings().css({
					// 			opacity: 0
					// 		});
					// 	}, 50);
					// });
					// $container.on('carousel.end', function() {
					// 	$container[0].cParam.$li.siblings().css({
					// 		'display': 'none'
					// 	});
					// });
					// var $thisLi = $li.eq(index);
					// if ($.support.transition) {
					// 	$thisLi.on('bsTransitionEnd', function() {
					// 		$container.trigger('carousel.end');
					// 		$(this).off('bsTransitionEnd');
					// 	});
					// 	$container.trigger('carousel.start');
					// } else {
					// 	$container.trigger('carousel.start');
					// 	$container.trigger('carousel.end');
					// }
					// $navLi.eq(index).addClass('active').siblings().removeClass('active');
				};
				// 总事件函数
				var activeFn = function(nowActive) {
					$container[0].cParam.$li = $li.eq(nowActive);
					$container[0].cParam.$nav = $navLi.eq(nowActive);
					$container[0].cParam.index = nowActive;
					if (opt.animate == 'move') {
						activeMove(nowActive);
					} else if (opt.animate == 'fade') {
						activeFade(nowActive);
					}
				};

				$navLi.on(opt.event, function() {
					var $t = $(this);
					nowActive = $t.index();
					activeFn(nowActive);
				}).eq(0).addClass('active');

				// 自动播放
				var autoPlay = function() {
					nowActive = (nowActive + 1) % $len;
					activeFn(nowActive);
				};
				var timer = null;
				if (opt.autoPlay) {
					timer = setInterval(autoPlay, opt.time);
					$container.on({
						'mouseover': function() {
							clearInterval(timer);
						},
						'mouseout': function() {
							clearInterval(timer);
							timer = setInterval(autoPlay, opt.time);
						}
					});
				}

				// 左右按钮
				var directionBtns = [];
				if (opt.directionBtn === true || opt.directionBtn === 'responsive') {
					var responsive = opt.directionBtn === 'responsive' ? 'carousel_responsive_direction_btn' : 'carousel_direction_btn';
					var $dirLeft = $('<span class="' + responsive + ' carousel_left_btn"></span>');
					var $dirRight = $('<span class="' + responsive + ' carousel_right_btn"></span>');
					$container.append($dirLeft.add($dirRight));
					directionBtns.push($dirLeft);
					directionBtns.push($dirRight);
				} else if (opt.directionBtn instanceof Array) {
					directionBtns = opt.directionBtn;
				}

				if (opt.directionBtn) {
					directionBtns[0].on("click", function() {
						nowActive = (nowActive + $len - 1) % $len;
						activeFn(nowActive);
					});
					directionBtns[1].on("click", function() {
						autoPlay();
					});
				}
			});
		};
	})(jQuery);
});
