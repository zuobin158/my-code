/**
 * Created by dupeng on 15-6-17.
 */
define({
	"roleMap": [
		{"id":"1", "role":"首页管理员", "usergroup":"CMS", "authorities":"CMS-首页管理-Banner；CMS-首页管理-系列课程组；CMS-首页管理-系列课程；CMS-首页管理-帖子管理；"},
		{"id":"2", "role":"社区管理员", "usergroup":"CMS", "authorities":"CMS-社区管理-学堂公告；CMS-社区管理-Banner；CMS-社区管理-推荐活动；CMS-社区管理-标签；CMS-社区管理-帖子；CMS-社区管理-评论；CMS-社区管理-用户；CMS-社区管理-举报；"},
		{"id":"3", "role":"站内信管理员", "usergroup":"CMS", "authorities":"CMS-站内信；"},
		{"id":"4", "role":"系统用户管理员", "usergroup":"SSO", "authorities":"SSO；"},
		{"id":"5", "role":"Admin", "usergroup":"CMS,SSO", "authorities":"CMS-首页管理-Banner；CMS-首页管理-系列课程组；CMS-首页管理-系列课程；CMS-首页管理-帖子管理；CMS-社区管理-学堂公告；CMS-社区管理-Banner；CMS-社区管理-推荐活动；CMS-社区管理-标签；CMS-社区管理-帖子；CMS-社区管理-评论；CMS-社区管理-用户；CMS-社区管理-举报；CMS-站内信；SSO；"}
	]
});