<% _.each(list, function(comment, idx) { %>
<tr>
	<td><%= comment.post_nickname %></td>
	<td><%= comment.post_id %></td>
	<td><a href="http://www.xuetangx.com/community/post/<%= comment.post_id %>" target="_blank"><%= comment.title %></a></td>
	<td><%= comment.nickname %></td>
	<td><%= comment.id %></td>
	<td><%= comment.content %></td>
	<td><%= comment.create_time %></td>
	<td><a class="delete-link" href="javascript:;" data-comment-id="<%= comment.id %>">删除</a></td>
</tr>
<% }); %>
