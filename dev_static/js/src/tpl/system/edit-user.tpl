<div class="edit-user">
	<form class="form-horizontal edit-form">
		<div class="step-1">
			<h3><%= editFlag ? "编辑" : "新增" %>用户 - 第一步</h3>
			<div class="form-group">
				<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>用户名：</div>
				<div class="col-xs-3">
					<input type="hidden" name="userId" value="<%= user.id %>">
					<input type="text" class="form-control input-sm" name="name" value="<%= user.name %>" <%= editFlag ? "readonly" : "" %>>
				</div>
			</div>
			<div class="form-group">
				<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>姓名：</div>
				<div class="col-xs-3">
					<input type="text" class="form-control input-sm" name="real_name" value="<%= user.real_name %>">
				</div>
			</div>
			<div class="form-group">
				<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>邮箱：</div>
				<div class="col-xs-3">
					<input type="text" class="form-control input-sm" name="email" value="<%= user.email %>">
				</div>
			</div>
			<div class="form-group">
				<div class="col-xs-2 inline-desc">手机号：</div>
				<div class="col-xs-3">
					<input type="text" class="form-control input-sm" name="phone" value="<%= user.phone %>">
				</div>
			</div>
			<div class="form-group">
				<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>状态：</div>
				<div class="col-xs-3">
					<label class="radio-inline">
						<input type="radio" name="is_active" value="1" <%= (user.is_active == "1") ? "checked" : "" %>> 开通
					</label>
					<label class="radio-inline">
						<input type="radio" name="is_active" value="0" <%= (user.is_active == "0") ? "checked" : "" %>> 关闭
					</label>
				</div>
			</div>
			<div class="form-group">
				<div class="col-xs-2 inline-desc"><span class="required-text">*&nbsp;</span>是否管理员：</div>
				<div class="col-xs-3">
					<label class="radio-inline">
						<input type="radio" name="is_super" value="1" <%= (user.is_super == "1") ? "checked" : "" %>> 是
					</label>
					<label class="radio-inline">
						<input type="radio" name="is_super" value="0" <%= (user.is_super == "0") ? "checked" : "" %>> 否
					</label>
				</div>
			</div>
			<div class="form-group">
				<div class="col-xs-5 text-danger hint-block"></div>
				<div class="col-xs-5 clear-left">
					<button type="button" class="btn btn-default next-btn">下一步</button>
					<button type="button" class="btn btn-default cancel-btn">取消</button>
				</div>
			</div>
		</div>
		<div class="step-2" style="display: none;">
			<h3><%= editFlag ? "编辑" : "新增" %>用户 - 第二步</h3>
			<div class="form-group">
				<table class="table table-bordered table-xt">
					<thead>
						<tr>
							<th style="width: 25%;">角色</th>
							<th style="width: 55%;">模块权限说明</th>
							<th style="width: 20%;">开通</th>
						</tr>
					</thead>
					<tbody>
						<% _.each(user.group_auth_list, function(roleItem, idx) { %>
						<tr data-role-id="<%= roleItem.id %>">
							<td data-role-name="<%= roleItem.role %>"><%= roleItem.role %></td>
							<td data-role-authorities="<%= roleItem.authorities %>"><%= roleItem.authorities.replace(/；/g, "；<br/>") %></td>
							<td>
								<div class="checkbox">
									<label>
										<input type="checkbox" name="groups_ids" value="<%= roleItem.id %>" <%= roleItem.is_checked == 1 ? "checked" : "" %>>
									</label>
								</div>
							</td>
						</tr>
						<% }); %>
					</tbody>
				</table>
			</div>
			<div class="form-group">
				<div class="btn-group-left">
					<button type="button" class="btn btn-default previous-btn">上一步</button>
				</div>
				<div class="col-xs-5 text-danger hint-block"></div>
				<div class="btn-group-right">
					<button type="button" class="btn btn-default confirm-btn">确定</button>
					<button type="button" class="btn btn-default cancel-btn">取消</button>
				</div>
			</div>
		</div>
	</form>
</div>
