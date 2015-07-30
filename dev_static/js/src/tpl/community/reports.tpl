<div class="reports-view">
	<form class="form-horizontal q-form">
		<div class="form-group">
			<div class="inline-desc">帖子ID：</div>
			<div class="inline-input">
				<input type="text" class="form-control input-sm" name="post_id" placeholder="例：123456">
			</div>
			<div class="inline-desc fluid">评论ID：</div>
			<div class="inline-input">
				<input type="text" class="form-control input-sm" name="comment_id" placeholder="例：123456">
			</div>
			<div class="inline-desc fluid">举报人昵称：</div>
			<div class="inline-input">
				<input type="text" class="form-control input-sm" name="reporter_nickname" placeholder="例：学堂在线">
			</div>
			<div class="inline-desc fluid">被举报人昵称：</div>
			<div class="inline-input">
				<input type="text" class="form-control input-sm" name="reportered_nickname" placeholder="例：学堂在线">
			</div>
		</div>
		<div class="form-group">
			<div class="inline-desc">举报类型：</div>
			<div class="inline-input">
				<select class="form-control input-sm" name="object_type">
					<option value="">全部</option>
					<option value="post">帖子</option>
					<option value="comment">评论</option>
				</select>
			</div>
			<div class="inline-desc">举报原因：</div>
			<div class="inline-input">
				<select class="form-control input-sm" name="reason">
					<option value="">全部</option>
					<option value="1001">广告或垃圾信息</option>
					<option value="1002">内容含违规信息</option>
					<option value="1003">不宜公开讨论</option>
					<option value="0">其他</option>
				</select>
			</div>
			<div class="inline-desc">举报时间：</div>
			<div class="inline-input">
				<input type="text" class="form-control input-sm start-date" name="create_time_start">
			</div>
			<div class="inline-desc fluid">至</div>
			<div class="inline-input">
				<input type="text" class="form-control input-sm end-date" name="create_time_end">
			</div>
		</div>
		<div class="form-group">
			<div class="inline-desc">状态：</div>
			<div class="inline-input">
				<select class="form-control input-sm" name="status">
					<option value="">全部</option>
					<option value="1">隐藏</option>
					<option value="2">忽略</option>
					<option value="0">未处理</option>
				</select>
			</div>
			<div class="inline-desc">关键字：</div>
			<div class="col-xs-4">
				<input type="text" class="form-control input-sm" name="keywords" placeholder="请输入 帖子标题/评论 关键词...">
			</div>
		</div>
		<div class="form-group">
			<div class="col-xs-10 text-danger hint-block"></div>
			<div class="col-xs-2">
				<button type="button" class="btn btn-default q-btn">查询</button>
			</div>
		</div>
	</form>
	<table class="table table-bordered table-xt">
		<thead>
			<tr>
				<th style="width: 9%;">举报时间</th>
				<th style="width: 9%;">举报类型</th>
				<th style="width: 10%;">举报原因</th>
				<th style="width: 9%;">举报人昵称</th>
				<th style="width: 9%;">被举报人昵称</th>
				<th style="width: 7%;">帖子ID</th>
				<th style="width: 12%;">帖子标题</th>
				<th style="width: 7%;">评论ID</th>
				<th style="width: 10%;">评论内容</th>
				<th style="width: 7%;">状态</th>
				<th style="width: 11%;">操作</th>
			</tr>
		</thead>
		<tbody class="list-content"></tbody>
	</table>
	<nav class="page-content">
		<ul class="pagination">
			<li class="disabled"><a href="javascript:;"><span>&laquo;第1页</span></a></li>
			<li class="disabled"><a href="javascript:;"><span>&lt;上一页</span></a></li>
			<li><span class="page-desc">第0页，共0页</span></li>
			<li class="disabled"><a href="javascript:;"><span>下一页&gt;</span></a></li>
			<li class="disabled"><a href="javascript:;"><span>最后1页&raquo;</span></a></li>
		</ul>
		<div class="records-control">
			共0条数据，每页显示
			<select class="records-select">
				<option value="10">10条</option>
				<option value="20">20条</option>
				<option value="50">50条</option>
				<option value="100">100条</option>
			</select>
		</div>
	</nav>
	<div class="modal fade" id="post-modal" tabindex="-1" role="dialog">
		<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal"><span>&times;</span></button>
					<h4 class="modal-title"></h4>
				</div>
				<div class="modal-body"></div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">返回</button>
				</div>
			</div>
		</div>
	</div>
</div>
