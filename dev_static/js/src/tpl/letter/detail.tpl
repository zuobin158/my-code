<div class="letter-detail">
	<div class="detail-row">
		<div class="col-xs-2">收信人ID：</div>
		<div class="col-xs-10 recipient-col">
			<span class="recipient-list">
			<% _.each(user_ids, function(r, idx) { %>
			<%= r + ";" %>
			<% }); %>
			</span>
			<span class="glyphicon glyphicon-triangle-bottom expand-icon"></span>
		</div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2">发信人：</div>
		<div class="col-xs-10"><%= update_user %></div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2">发送时间：</div>
		<div class="col-xs-10"><%= create_time %></div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2">标题：</div>
		<div class="col-xs-10"><%= title %></div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2">正文：</div>
		<div class="col-xs-10"><%= content %></div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2">超链提示：</div>
		<div class="col-xs-10"><%= link_remark %></div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2">超链地址：</div>
		<div class="col-xs-10"><%= outlink %></div>
	</div>
	<div class="detail-row">
		<div class="col-xs-2"><button type="button" class="btn btn-default back-btn">返回</button></div>
	</div>
</div>
