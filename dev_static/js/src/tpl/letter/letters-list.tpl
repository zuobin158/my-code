<% _.each(list, function(letter, idx) { %>
<tr>
	<td><%= letter.create_time %></td>
	<td><%= letter.title %></td>
	<td><%= letter.user_ids %></td>
	<td><%= letter.update_user %></td>
	<td><a class="detail-link" href="javascript:;" data-letter-id="<%= letter.id %>">查看详情</a></td>
</tr>
<% }); %>
