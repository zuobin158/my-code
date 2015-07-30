<% _.each(list, function(post, idx) { %>
<tr data-post-id="<%= post.id %>">
	<td><%= post.author_nickname %></td>
	<td><%= post.id %></td>
	<td><a class="popup-link" href="javascript:;" data-post-id="<%= post.id %>"><%= post.title %></a></td>
	<td><%= post.createDate %></td>
	<td><span class="hide-status"><%= post.status==-1 ? '是' : '否' %></span></td>
	<td><a class="hide-link" href="javascript:;" data-post-id="<%= post.id %>" data-hide-status="<%= post.status ==-1 ? true:false %>"><%= post.status==-1 ? '取消隐藏' : '隐藏' %></a></td>
	<td class="tags">
		<% _.each(post.tags, function(tag, idx) { %>
		<div class="checkbox">
			<label>
				<input type="checkbox" class="tag-checkbox" <%= tag.isChecked==1 ? "checked" : "" %> data-tag-id="<%= tag.id %>"><%= tag.name %>
			</label>
		</div>
		<% }); %>
		&nbsp;<button class="btn btn-default btn-sm tag-submit" data-post-id="<%= post.id %>">提交</button>
	</td>
</tr>
<% }); %>
