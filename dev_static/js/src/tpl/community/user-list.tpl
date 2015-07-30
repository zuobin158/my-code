<% _.each(list, function(user, idx) { %>
<tr data-user-id="<%= user.user_id %>">
	<td><%= user.user_id %></td>
	<td><%= user.nickname %></td>
	<td><%= user.date_joined %></td>
	<td><span class="prohib-status"><%= user.is_forbid=='Y'  ? '是' : '否' %></span></td>
	<td><a class="prohib-link" href="javascript:;" data-user-id="<%= user.user_id %>"><%= user.is_forbid=='Y' ? '取消禁言' : '禁言' %></a></td>
	<td><a class="delete-avatar-link" href="javascript:;" data-user-id="<%= user.id %>"><%= user.has_avatar=='Y' ? '删除头像' : '' %></a></td>
</tr>
<% }); %>
