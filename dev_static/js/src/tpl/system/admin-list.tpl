<% _.each(list, function(user, idx) { %>
<tr>
	<td><%= user.real_name %></td>
	<td><%= user.name %></td>
	<td><%= user.email %></td>
	<td><%= user.phone ? user.phone : "---" %></td>
	<td><%= user.usergroup.replace(/,/g, "<br/>") %></td>
	<td><%= user.authorities.replace(/;/g, ";<br/>") %></td>
	<td><%= user.is_active=="1" ? "开通" : "关闭" %></td>
	<td><%= user.is_super=="1" ? "是" : "否" %></td>
	<td><a class="edit-link" href="#admin/edituser/<%= user.id %>">编辑</a>&nbsp;
        <a class="delete-link" href="javascript:;" data-user-id="<%= user.id %>">删除</a>
    </td>
</tr>
<% }); %>
