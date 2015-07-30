<div class="letters-view">
	<form class="form-horizontal q-form">
		<div class="form-group">
			<div class="inline-desc">收信人ID：</div>
			<div class="col-xs-2">
				<input type="text" class="form-control input-sm" name="user_id" placeholder="例：123456">
			</div>
			<div class="inline-desc">发送时间：</div>
			<div class="col-xs-2">
				<input type="text" class="form-control input-sm start-date" name="create_time_start">
			</div>
			<div class="inline-desc fluid">至</div>
			<div class="col-xs-2">
				<input type="text" class="form-control input-sm end-date" name="create_time_end">
			</div>
		</div>
		<div class="form-group">
			<div class="inline-desc">发信人：</div>
			<div class="col-xs-2">
				<input type="text" class="form-control input-sm" name="update_user" placeholder="例：学堂在线">
			</div>
			<div class="inline-desc">关键字：</div>
			<div class="col-xs-4">
				<input type="text" class="form-control input-sm" name="keywords" placeholder="请输入 站内信标题 关键词...">
			</div>
		</div>
		<div class="form-group">
			<div class="col-xs-10 text-danger hint-block"></div>
			<div class="col-xs-2">
				<button type="button" class="btn btn-default q-btn">查询</button>
				<button type="button" class="btn btn-default c-btn">新建</button>
			</div>
		</div>
	</form>
	<table class="table table-bordered table-xt">
		<thead>
			<tr>
				<th style="width: 20%;">发送时间</th>
				<th style="width: 30%;">站内信标题</th>
				<th style="width: 30%;">收信人ID</th>
				<th style="width: 10%;">发信人</th>
				<th style="width: 10%;">操作</th>
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
	<div id="letter-detail" class="detail-layer"></div>
</div>
